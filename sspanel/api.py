# TODO header

from . import ControlPanel

def start(username: str, password: str, subuser: bool, serverid: int):
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.start()


def stop(username: str, password: str, subuser: bool, serverid: int):
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.stop()


def restart(username: str, password: str, subuser: bool, serverid: int):
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.restart()


def info(username: str, password: str, subuser: bool, serverid: int):
	panel = ControlPanel(username, password, subuser, serverid)
	return panel.info()