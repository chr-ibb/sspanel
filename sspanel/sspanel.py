import requests

from urls import USER_LOGIN_URL, SUBUSER_LOGIN_URL, PANEL_URL, START_URL, STOP_URL, RESTART_URL

CERT = "../certificate/survivalservers-com-chain.pem"


class SSPanel:
	"""A user-created :class:`SSPanel <SSPanel>` object.

	Accepts login credentials and server ID, attempts to login,
	finds encrypted password for server actions in panel page source.

	Usage::
		>>> import sspanel
		>>> username = "aUserName"
		>>> password = "aP@ssw0rd"
		>>> subuser = false
		>>> serverid = 123456
		>>> panel = sspanel.SSPanel(username, password, subuser, serverid)
		Login successfull
		Finding panel password...
		Panel password found

		>>> panel.start()
		Login successfull
		Starting server...
		Server started successfully

		>>> panel.start()
		Login successfull
		Server is already started # TODO

		>>> panel.stop()
		Login successfull
		Stopping server...
		Server stopped successfully

		>>> panel.info()
		Login successfull
		# TODO

	"""


	def __init__(self, username: str, password: str, subuser: bool, serverid: int):
		self.username = username
		self.password = password
		self.subuser = subuser
		self.serverid = str(serverid)
		self.panel_password = None
		self._login_and(self._find_password)


	def info(self):
		def get_info(sesh: requests.Session):
			print("TODO")

		self._login_and(get_info)


	def start(self):
		def start_server(sesh: requests.Session):
			# TODO: check if server is already started. Does this matter? I'm affraid to try it. 
			# Maybe just call self.info() to check status? Maybe just let it error and let user handle that. 
			url = START_URL
			payload = {
				'username': self.username,
				'password': self.panel_password,
				'gameserverid': self.serverid,
				'subuser': '1' if self.subuser else '0'
			}
			print("Starting server...")
			resp = sesh.post(url, data=payload, verify=CERT)
			assert resp.text == '1', "Failed to start server."
			print("Server started successfully")


		self._login_and(start_server)


	def stop(self):
		def stop_server(sesh: requests.Session):
			# TODO: check if server is already stopped. 
			url = STOP_URL
			payload = {
				'username': self.username,
				'password': self.panel_password,
				'gameserverid': self.serverid,
				'subuser': '1' if self.subuser else '0'
			}
			print("Stopping server...")
			resp = sesh.post(url, data=payload, verify=CERT)
			assert resp.text == '1', "Failed to stop server."
			print("Server stopped successfully")

		self._login_and(stop_server)



	def restart(self):
		def restart_server(sesh: requests.Session):
			# TODO: check if server is already started. Suggest start if it is. 
			url = RESTART_URL
			payload = {
				'username': self.username,
				'password': self.panel_password,
				'gameserverid': self.serverid,
				'subuser': '1' if self.subuser else '0'
			}
			print("Restarting server...")
			resp = sesh.post(url, data=payload, verify=CERT)
			assert resp.text == '1', "Failed to restart server."
			print("Server restarted successfully")

		self._login_and(restart_server)



	# "Private" Methods:

	def _login_and(self, task):
		"""Opens a request session, attempts to log in, carries out task with the session, closes the session.
		All api methods use this method; the intention is to never leave a session lingering. 
		:param task: Callback to be run with session
		:type task: (requests.Session) -> None
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

			task(sesh)



	def _find_password(self, sesh: requests.Session):
		"""Opens the server's control panel in order to find the special password needed for start, stop, and restart forms.
		This password is a long string of letters and numbers. It might be generated from information we already have, 
		like the user password, but I've no idea so we get it this way instead.
		"""
		print("Finding panel password")
		url = PANEL_URL + self.serverid
		resp = sesh.get(url, verify=CERT)
		resp.raise_for_status()
		# Extract these strings?
		search_phrase = "username=" + username + "&password="
		start_of_password = resp.text.find(search_phrase) + len(search_phrase)
		end_of_password = resp.text[start_of_password:].find("&") + start_of_password
		self.panel_password = resp.text[start_of_password:end_of_password]
		print("Panel password found")


if __name__ == "__main__":
	print(">>> from login_info import username, password, subuser, serverid")
	from login_info import username, password, subuser, serverid
	print(">>> panel = SSPanel(username, password, subuser, serverid)")
	panel = SSPanel(username, password, subuser, serverid)