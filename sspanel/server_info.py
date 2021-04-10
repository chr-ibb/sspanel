# TODO header

from .utils import search_between, get_between

class ServerInfo:

	def __init__(self, page_source: str):
		relevant = get_between(page_source, "GAME SERVER ID #", "FTP Details")

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
		s = \
		f"title: {self.title}\nstatus: {self.status}\nplayers: {self.players}\nstatus info: {self.status_info}\n" + \
		f"last start: {self.last_start}\nversion: {self.version}\nip address: {self.ip}\n" + \
		f"game port: {self.game_port}\nquery port: {self.query_port}"
		return s


def get_title(s):
	s = s[s.find("panel-title bold"):]
	return get_between(s, ">", " by")


def get_status(s):
	return "Started" if "success" in s else "Stopped"


def get_players(s):
	i = s.find("players")
	return get_between(s[i - 10:], "(", " p")

def get_status_info(s):
	if "Loading.." in s: return "Loading"
	if "Ready!" in s: return "Ready"

	s = s[s.find("players"):]
	return get_between(s, ">", "<")

def get_last_start(s):
	return get_between(s, "Last Start: <em>", "<")

def get_version(s):
	return get_between(s, "label-default\">", "<")

def get_ip(s):
	return get_between(s, "IP Address: ", "<")

def get_game_port(s):
	return get_between(s, "Game Port: ", " (")

def get_query_port(s):
	return get_between(s, "Query Port: ", " (")

