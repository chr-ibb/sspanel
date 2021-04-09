# SSPanel.py

**SSPanel.py** is a simple API providing the basic functionality of the **[SurvivalServers.com](https://www.survivalservers.com/)** Control Panel to Python  
via HTTPS requests. It allows for starting, stopping, and restarting a server, as well as retrieving server info.  

```python
>>> import sspanel
>>> username, password, subuser = "aUserName", "aP@ssw0rd", False
>>> serverid = 123456
# Start the server. 
>>> sspanel.start(username, password, subuser, serverid)
'Login successful'
'Control Panel is ready'
'Server is started'
# sspanel.stop(...), sspanel.restart(...), and sspanel.info(...) are also available.

# Alternatively: create a ControlPanel object; make sequential calls with the same server. 
>>> panel = sspanel.ControlPanel(username, password, subuser, serverid)
'Login successful'
'Control Panel is ready'

>>> panel.restart()
'Login successful'
'Server is started'

>>> panel.stop()
'Login successful'
'Server is stopped'

# Retrieve basic server information.
>>> info = panel.info()
>>> print(info)
# TODO

```

Makes use of the [Requests](https://github.com/psf/requests) library.
