"""
sspanel.urls

This module contains static URLs (and one incomplete URL)
"""

USER_LOGIN_URL = "https://www.survivalservers.com/sspanel/includes/ajax/validate_login.php"
SUBUSER_LOGIN_URL = "https://www.survivalservers.com/sspanel/includes/ajax/validate_subuser_login.php"
LOGOUT_URL = "https://www.survivalservers.com/sspanel/user/?logout"

#PANEL_URL is incomplete; the server ID must be appended to it. 
PANEL_URL = "https://www.survivalservers.com/sspanel/user/?gameservers&gameserverid="

START_URL = "https://www.survivalservers.com/sspanel/includes/ajax/gameserver_start.php"
STOP_URL = "https://www.survivalservers.com/sspanel/includes/ajax/gameserver_stop.php"
RESTART_URL = "https://www.survivalservers.com/sspanel/includes/ajax/gameserver_restart.php"