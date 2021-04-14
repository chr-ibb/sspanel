"""
sspanel.control_panel

This module contains the ControlPanel class, the primary object powering SSPanel.
"""

import requests
import datetime
from .urls import USER_LOGIN_URL, SUBUSER_LOGIN_URL, PANEL_URL, START_URL, STOP_URL, RESTART_URL
from .server_info import ServerInfo
from .utils import string_between
from .exceptions import (
	LoginError, PanelPasswordError, ServerStartError, ServerStopError, ServerRestartError, LimitExceededError)
from importlib.resources import path


class ControlPanel:
	"""A user-created :class:`ControlPanel <ControlPanel>` object.

	Accepts SurvivalServer.com login credentials and server ID, attempts to login,
	and finds encrypted password for server-actions in control panel page source.

	Once constructed, provides basic Control Panel functionality via
	member methods.

	:param username: username of an account with access to the server.
	:param password: password associated with username.
	:param subuser: whether or not the user is a subuser.
	:param serverid: Unique ID associated with the server. Visible in browser.
	:param limit: (default) Time, in seconds, where a second sequential server-action
		cannot be done. Intended to prevent the server from starting/stopping
		too frequently. (does not affect info() method)

	methods:
		start()
		stop()
		restart()
		info()

	Usage::
		>>> import sspanel
		>>> username, password, subuser = "aUserName", "aP@ssw0rd", False
		>>> serverid = 123456
		>>> panel = sspanel.ControlPanel(username, password, subuser, serverid)
		>>> panel.start()
		Server is started

		>>> panel.stop()
		Server is stopped

		>>> info = panel.info()
		Info gathered

		>>> print(info)
		title: ServerTitle
		status: Started, Ready
		players: 3/22
		last start: 04/1/2021 04:20:00
		game version: v0.123.4
		ip address: 111.111.11.11
		game port: 9876
		query port: 9877

	"""

	def __init__(self, username: str, password: str, subuser: bool, serverid: int, limit: int = 15):
		self.username = username
		self.password = password
		self.subuser = subuser
		self.serverid = str(serverid)
		self.limit = datetime.timedelta(seconds=limit)
		self.last_action = datetime.datetime.now() - datetime.timedelta(seconds=limit+1)
		self.panel_password = None # found and assigned the first time it is needed


	def start(self):
		"""Server-action for starting the server.
		Starting an already started server seems to do nothing."""
		self.__check_limit()
		if not self.panel_password:
			self.__login_and(self.__find_password)

		def start_server(sesh: requests.Session):
			print("Starting server...       \r", end="")
			result = self.__post_action(sesh, START_URL)
			if result != '1':
				raise ServerStartError()
			print("Server is started        ")

		self.__login_and(start_server)

	
	def stop(self):
		"""Server-action for stopping the server.
		Stopping an already stopped server seems to do nothing."""
		self.__check_limit()
		if not self.panel_password:
			self.__login_and(self.__find_password)

		def stop_server(sesh: requests.Session):
			print("Stopping server...       \r", end="")
			result = self.__post_action(sesh, STOP_URL)
			if result != '1':
				raise ServerStopError()
			print("Server is stopped        ")

		self.__login_and(stop_server)

	
	def restart(self):
		"""Server-action for restarting the server.
		Restarting a stopped server seems to just start it."""
		self.__check_limit()
		if not self.panel_password:
			self.__login_and(self.__find_password)

		def restart_server(sesh: requests.Session):
			print("Restarting server...     \r", end="")
			result = self.__post_action(sesh, RESTART_URL)
			if result != '1':
				raise ServerRestartError()
			print("Server is started        ")

		self.__login_and(restart_server)

	
	def info(self):
		"""Retrieves basic server information, returns it"""
		def get_info(sesh: requests.Session):
			print("Gathering info...        \r", end="")
			url = PANEL_URL + self.serverid
			with cert_path() as cert:
				resp = sesh.get(url, verify=cert)
			resp.raise_for_status()
			s_info = ServerInfo(resp.text)
			print("Info gathered            ")
			return s_info
		return self.__login_and(get_info)


	def get_password(self):
		"""Finds and saves the panel password. This password is usually found automatically
		the first time it is needed. Use this to find it earlier than necessary, to save time later."""
		self.__login_and(self.__find_password)


	# "Private" Methods #
	
	def __login_and(self, task):
		"""Opens a request session, attempts to log in, carries out TASK with the session, closes the session.
		All api methods utilize this method; the intention is to never leave a session lingering. 

		:param task: Callback to be run with session; should accept a Session as a parameter.
		:return: typically None. get_info(sesh) returns a ServerInfo instance.
		"""
		url = USER_LOGIN_URL if not self.subuser else SUBUSER_LOGIN_URL
		payload = {
			'username': self.username,
			'password': self.password
		}
		with requests.Session() as sesh:
			with cert_path() as cert:
				resp = sesh.post(url, data=payload, verify=cert)
			resp.raise_for_status()
			if resp.text != '1':
				raise LoginError()
			print("Login successful         \r", end="")
			return task(sesh)


	def __find_password(self, sesh: requests.Session):
		"""Searches the Control Panel page source and finds the password needed for server-action post request forms.
		This password is a long string of letters and numbers. It might be generated from information we already have, 
		but I've no idea so we get it this way instead.
		"""
		print("Finding panel password...\r", end="")
		url = PANEL_URL + self.serverid
		with cert_path() as cert:
			resp = sesh.get(url, verify=cert)
		resp.raise_for_status()
		search_phrase = "username=" + self.username + "&password="
		p = string_between(resp.text, search_phrase, "&")
		if p: 
			self.panel_password = p
		else:
			raise PanelPasswordError()


	def __post_action(self, sesh: requests.Session, url: str):
		"""Consolidates code between start, stop, and restart methods.
		Creates a post request using the session and url passed in. 
		"""
		payload = {
			'username': self.username,
			'password': self.panel_password,
			'gameserverid': self.serverid,
			'subuser': '1' if self.subuser else '0'
		}
		with cert_path() as cert:
			resp = sesh.post(url, data=payload, verify=cert)
		resp.raise_for_status()
		self.last_action = datetime.datetime.now()
		return resp.text


	def __check_limit(self):
		"""Checks whether the rate limit has been exceeded."""
		delta = datetime.datetime.now() - self.last_action
		if  delta < self.limit:
			raise LimitExceededError(self.limit.seconds)


	# For testing
	def __panel_text(self):
		"""Returns the page source text of the server's Control Panel"""
		def get_panel_text(sesh):
			url = PANEL_URL + self.serverid
			with cert_path() as cert:
				resp = sesh.get(url, verify=cert)
			resp.raise_for_status()
			return resp.text
		return self.__login_and(get_panel_text)


def cert_path():
	"""Returns context manager which provides a pathlib.Path object
	for the sspanel/data/survivalservers-com-chain.pem file path."""
	return path('sspanel.data', 'survivalservers-com-chain.pem')