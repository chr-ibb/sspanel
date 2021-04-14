"""
SSPanel

Simple API for the SurvivalServers.com Control Panel using HTTP requests.

:copyright: (c) 2021 by Christopher Ibbotson.
:license: MIT, see LICENSE for more details.
"""

# TODO Check compatibility

from .control_panel import ControlPanel
from .server_info import ServerInfo
from .api import start, stop, restart, info

