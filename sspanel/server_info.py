# TODO header

from .utils import string_between

class ServerInfo:

	def __init__(self, page_source: str):
		relevant = string_between(page_source, "GAME SERVER ID #", "FTP Details")

		self.title = get_title(relevant)
		self.status = get_status(relevant)

		if self.status == 'Stopped':
			self.players = None
			self.status_info = None
			self.version = None
		else:
			self.players = get_players(relevant)
			self.status_info = get_status_info(relevant)
			self.version = get_version(relevant)

		self.last_start = get_last_start(relevant) 
		self.ip = get_ip(relevant) 
		self.game_port = get_game_port(relevant)
		self.query_port = get_query_port(relevant)


	def __repr__(self):
		return f"<ServerInfo [{self.title}]>"

	
	def __str__(self):
		combined_status = f"{self.status}, {self.status_info}" if self.status_info else self.status
		players = self.players if self.players else "None (server is stopped)"
		version = self.version if self.version else "None (server is stopped)"
		return \
			f"title: {self.title}\n" + \
			f"status: {combined_status}\n" + \
			f"players: {players}\n" + \
			f"last start: {self.last_start}\n" + \
			f"game version: {version}\n" + \
			f"ip address: {self.ip}\n" + \
			f"game port: {self.game_port}\n" + \
			f"query port: {self.query_port}"


def get_title(s):
	s = s[s.find("panel-title bold"):]
	return string_between(s, ">", " by")


def get_status(s):
	return "Started" if "success" in s else "Stopped"


def get_players(s):
	i = s.find("players")
	return string_between(s[i - 10:], "(", " p")

def get_status_info(s):
	if "Loading.." in s: return "Loading"
	if "Ready!" in s: return "Ready"

	s = s[s.find("players"):]
	return string_between(s, ">", "<")

def get_last_start(s):
	return string_between(s, "Last Start: <em>", "<")

def get_version(s):
	return string_between(s, "label-default\">", "<")

def get_ip(s):
	return string_between(s, "IP Address: ", "<")

def get_game_port(s):
	return string_between(s, "Game Port: ", " (")

def get_query_port(s):
	return string_between(s, "Query Port: ", " (")

