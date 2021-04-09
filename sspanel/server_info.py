# TODO header

from .utils import get_between

class ServerInfo:

	def __init__(self, page_source: str):
		self.success, index = get_between(page_source, "label-success\">", "</")
		page_source = page_source[index:]

		self.players, index = get_between(page_source, "(", ")")
		page_source = page_source[index:]

		self.info, index = get_between(page_source, "label-info\">", "</")
		page_source = page_source[index:]

		self.last_start, index = get_between(page_source, "em>", "</em")
		page_source = page_source[index:]

		self.version, index = get_between(page_source, "default\">", "</")
		page_source =  page_source[index:]

		self.ip_address, index = get_between(page_source, "IP Address: ", "<")
		page_source = page_source[index:]

		self.game_port, index = get_between(page_source, "Game Port: ", " (")
		page_source = page_source[index:]

		self.query_port, index = get_between(page_source, "Query Port: ", " (")


	def __repr__(self):
		s = f"success: {self.success}\nplayers: {self.players}\ninfo: {self.info}\n" + \
		f"last start: {self.last_start}\nversion: {self.version}\nip address: {self.ip_address}\n" + \
		f"game port: {self.game_port}\nquery port: {self.query_port}"
		return s


