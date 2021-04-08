import requests
import datetime
from urls import USER_LOGIN_URL, SUBUSER_LOGIN_URL, PANEL_URL, START_URL, STOP_URL, RESTART_URL
CERT = "../certificate/survivalservers-com-chain.pem"

# TODO check if already logged in  before logging in.
# TODO replace asserts

class SSPanel:
	"""A user-created :class:`SSPanel <SSPanel>` object.

	Accepts SurvivalServer.com login credentials and server ID, attempts to login,
	and finds encrypted password for server-actions in control panel page source.

	Once constructed, provides basic Control Panel functionality via
	member methods.

	:param username: username or subusername of account with access to server.
	:param password: password which corresponds with username.
	:param subuser: whether or not the user is a "subuser"
	:param serverid: server ID of the server. If unknown, open control panel
		normally in browser, and it will be at the top of the page.
	:param limit: time, in seconds, where a second sequential server-action
		cannot be done. Intended to prevent the server from starting/stopping
		too frequently. 

	server-actions:
	start()
	stop()
	restart()

	other methods:
	info()

	Usage::
		>>> import sspanel
		>>> username = "aUserName"
		>>> password = "aP@ssw0rd"
		>>> subuser = False
		>>> serverid = 123456
		>>> panel = sspanel.SSPanel(username, password, subuser, serverid)
		Login successfull
		Panel is ready

		>>> panel.start()
		Login successfull
		Server is started

		>>> panel.stop()
		Login successfull
		Server is stopped

		>>> info = panel.info()
		Login successfull
		Info gathered
		>>> print(info)
		# TODO
	"""

	def __init__(self, username: str, password: str, subuser: bool, serverid: int, limit: int = 15):
		self.username = username
		self.password = password
		self.subuser = subuser
		self.serverid = str(serverid)
		self.panel_password = None
		self.limit = datetime.timedelta(seconds=limit)
		self.last_action = datetime.datetime.now() - self.limit
		self._login_and(self._find_password)


	def start(self):
		"""Server action for starting the server.
		Starting an already started server seems to do nothing."""
		self._check_limit()
		def start_server(sesh: requests.Session):
			print("Starting server...\r", end="")
			result = self._post_action(sesh, START_URL)
			assert result == '1', "Failed to start server."
			print("Server is started ")
		self._login_and(start_server)

	
	def stop(self):
		"""Server action for stopping the server.
		Stopping an already stopped server doesn't seem to cause harm."""
		self._check_limit()
		def stop_server(sesh: requests.Session):
			print("Stopping server...\r", end="")
			result = self._post_action(sesh, STOP_URL)
			assert result == '1', "Failed to stop server."
			print("Server is stopped ")
		self._login_and(stop_server)

	
	def restart(self):
		"""Server action for restarting the server.
		Restarting a stopped server seems to just start it without harm."""
		self._check_limit()
		def restart_server(sesh: requests.Session):
			print("Restarting server...\r", end="")
			result = self._post_action(sesh, RESTART_URL)
			assert result == '1', "Failed to restart server."
			print("Server is started   ")
		self._login_and(restart_server)

	
	def info(self):
		"""Retrieves basic server information, returns it"""
		def get_info(sesh: requests.Session):
			print("Gathering info...\r", end="")
			# TODO get the info
			print("Info gathered    ")
			return "info"
		return self._login_and(get_info)


	def _login_and(self, task):
		"""Opens a request session, attempts to log in, carries out task with the session, closes the session.
		All public api methods utilize this method; the intention is to never leave a session lingering. 

		:param task: Callback to be run with session; should accept a Session as a parameter.
		:return: typically None. get_info(sesh) returns the server information.
		"""
		url = USER_LOGIN_URL if not self.subuser else SUBUSER_LOGIN_URL
		payload = {
			'username': self.username,
			'password': self.password
		}
		with requests.Session() as sesh:
			resp = sesh.post(url, data=payload, verify=CERT)
			resp.raise_for_status()
			assert resp.text == '1', "Login failed, check username, password, and subuser."
			print("Login successfull")
			return task(sesh)


	def _find_password(self, sesh: requests.Session):
		"""Searches the Control Panel page source and finds the password needed for server-action post request forms.
		This password is a long string of letters and numbers. It might be generated from information we already have, 
		but I've no idea so we get it this way instead.
		"""
		print("Finding panel password...\r", end="")
		url = PANEL_URL + self.serverid
		resp = sesh.get(url, verify=CERT)
		resp.raise_for_status()
		# Extract these strings?
		search_phrase = "username=" + username + "&password="
		start_of_password = resp.text.find(search_phrase) + len(search_phrase)
		end_of_password = resp.text[start_of_password:].find("&") + start_of_password
		self.panel_password = resp.text[start_of_password:end_of_password]
		print("Panel is ready           ")


	def _post_action(self, sesh: requests.Session, url: str):
			payload = {
				'username': self.username,
				'password': self.panel_password,
				'gameserverid': self.serverid,
				'subuser': '1' if self.subuser else '0'
			}
			resp = sesh.post(url, data=payload, verify=CERT)
			resp.raise_for_status()
			self.last_action = datetime.datetime.now()
			return resp.text


	def _check_limit(self):
		delta = datetime.datetime.now() - self.last_action
		assert  delta > self.limit, f"There must be {self.limit.seconds} seconds between server actions."



# Mostly used for testing.
if __name__ == "__main__":
	print(">>> from login_info import username, password, subuser, serverid")
	from login_info import username, password, subuser, serverid

	print(">>> panel = SSPanel(username, password, subuser, serverid)")
	panel = SSPanel(username, password, subuser, serverid)