"""
sspanel.exceptions

This module contains the set of SSPanel's exceptions
"""

class SSPanelException(Exception):
	"""There was an ambiguous exception."""


class LoginError(SSPanelException):
	"""Failed to log in."""
	def __init__(self):
		super().__init__("Failed to log in. Check credentials (username, password, subuser).")


class PanelPasswordError(SSPanelException):
	"""Failed to retrieve panel password."""
	def __init__(self):
		super().__init__("Failed to retrieve panel password.")


class ServerStartError(SSPanelException):
	"""Failed to start server."""
	def __init__(self):
		super().__init__("Failed to start server. Check server ID.")


class ServerStopError(SSPanelException):
	"""Failed to stop server."""
	def __init__(self):
		super().__init__("Failed to stop server. Check server ID.")


class ServerRestartError(SSPanelException):
	"""Failed to restart server."""
	def __init__(self):
		super().__init__("Failed to restart server. Check server ID.")


class LimitExceededError(SSPanelException):
	"""Rate limit exceeded."""
	def __init__(self, limit):
		super().__init__(f"There must be {limit} seconds between server actions.")