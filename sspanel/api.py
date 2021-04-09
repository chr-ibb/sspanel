# TODO header
# TODO refactor subuser to be after serverid, and give it a default value. maybe.

from . import ControlPanel

def start(username: str, password: str, subuser: bool, serverid: int):
	"""Attempts to start the server described by the credentials passed in.
	Starting an already started server seems to do nothing.

	:param username: username of an account with access to the server.
	:param password: password associated with username.
	:param subuser: whether or not the user is a subuser.
	:param serverid: Unique ID associated with the server. Visible in browser.
	:return: None

	Usage::

		>>> import sspanel
		>>> credentials = ("aUserName", "aP@ssw0rd", False)
		>>> serverid = 123456
		>>> sspanel.start(*credentials, serverid)
		Login successful
		Control Panel is ready
		Server is started
	"""
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.start()


def stop(username: str, password: str, subuser: bool, serverid: int):
	"""Attempts to stop the server described by the credentials passed in.
	Stopping an already stopped server seems to do nothing.

	:param username: username of an account with access to the server.
	:param password: password associated with username.
	:param subuser: whether or not the user is a subuser.
	:param serverid: Unique ID associated with the server. Visible in browser.
	:return: None

	Usage::

		>>> import sspanel
		>>> credentials = ("aUserName", "aP@ssw0rd", False)
		>>> serverid = 123456
		>>> sspanel.stop(*credentials, serverid)
		Login successful
		Control Panel is ready
		Server is stopped
	"""
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.stop()


def restart(username: str, password: str, subuser: bool, serverid: int):
	"""Attempts to restart the server described by the credentials passed in.
	Restarting a stopped server seems to just start the server.

	:param username: username of an account with access to the server.
	:param password: password associated with username.
	:param subuser: whether or not the user is a subuser.
	:param serverid: Unique ID associated with the server. Visible in browser.
	:return: None

	Usage::

		>>> import sspanel
		>>> credentials = ("aUserName", "aP@ssw0rd", False)
		>>> serverid = 123456
		>>> sspanel.restart(*credentials, serverid)
		Login successful
		Control Panel is ready
		Server is started
	"""
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.restart()


def info(username: str, password: str, subuser: bool, serverid: int):
	"""Attempts to retrieve info about the server described by the credentials passed in.
	Info is returned as a :class:`ServerInfo <ServerInfo>` object.

	:param username: username of an account with access to the server.
	:param password: password associated with username.
	:param subuser: whether or not the user is a subuser.
	:param serverid: Unique ID associated with the server. Visible in browser.
	:return: :class:`ServerInfo <ServerInfo>` object.
	:rtype: sspanel.ServerInfo

	Usage::

		>>> import sspanel
		>>> credentials = ("aUserName", "aP@ssw0rd", False)
		>>> serverid = 123456
		>>> info = sspanel.info(*credentials, serverid)
		Login successful
		Info gathered

		>>> print(info)
		# TODO
	"""
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.info()
