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

## Main Interface

### sspanel.*start*(username, password, subuser, serverid)  
- Attempts to start the server described by the credentials passed in.

### sspanel.*stop*(username, password, subuser, serverid)  
- Attempts to stop the server described by the credentials passed in.

### sspanel.*restart*(username, password, subuser, serverid)  
- Attempts to restart the server described by the credentials passed in.

### sspanel.*info*(username, password, subuser, serverid)  
- Attempts to retrieve and return info about the server described by the credentials passed in.
- **Returns:** a ServerInfo object.

## Lower-Level Classes

### sspanel.*ControlPanel*(username, password, subuser, serverid)  
- #TODO

### sspanel.*ServerInfo*  
- #TODO

## Etc

Only tested with a Valheim server; that is all I have access to. 

Makes use of the [Requests](https://github.com/psf/requests) library.
