# SSPanel

**SSPanel** is a simple API providing the basic functionality of the **[SurvivalServers.com](https://www.survivalservers.com/)** Control Panel to Python  
via HTTPS requests. It allows for starting, stopping, and restarting a server, as well as retrieving server info.  

```python
>>> import sspanel
>>> username, password, subuser = "aUserName", "aP@ssw0rd", False
>>> serverid = 123456

# Start the server. 
>>> sspanel.start(username, password, subuser, serverid)
'Server is started'

# Retrieve basic server information.
>>> info = sspanel.info(username, password, subuser, serverid)
'Info gathered'
>>> print(info)
'title: ServerTitle'
'status: Started, Ready'
'players: 3/22'
'last start: 04/1/2021 04:20:00'
'game version: v0.123.4'
'ip address: 111.111.11.11'
'game port: 9876'
'query port: 9877'

# Alternatively: create a ControlPanel object; make sequential calls with the same server. 
>>> panel = sspanel.ControlPanel(username, password, subuser, serverid)
>>> panel.restart()
'Server is started'

>>> panel.stop()
'Server is stopped'

```

## Main Interface

- sspanel.**start**(username, password, subuser, serverid)  
    - Attempts to start the server described by the credentials passed in.

- sspanel.**stop**(username, password, subuser, serverid)  
    - Attempts to stop the server described by the credentials passed in.

- sspanel.**restart**(username, password, subuser, serverid)  
    - Attempts to restart the server described by the credentials passed in.

- sspanel.**info**(username, password, subuser, serverid)  
    - Attempts to retrieve and return info about the server described by the credentials passed in.
    - **Returns:** a ServerInfo object.

## Classes

- sspanel.**ControlPanel**(username, password, subuser, serverid, limit=15)  
    - ControlPanel object which stores login credentials and serverid, allowing for sequential actions on the same server. 
    - *limit* parameter is the minimum time (in seconds) between sequential server actions (aside from .info(), which is not limited).

- sspanel.**ServerInfo**  
    - ServerInfo object which stores all of the information retrieved from a ControlPanel.info() call.


## Installing SSPanel

SSPanel is available on PyPI:

```console
$ python -m pip install sspanel
```

## Etc

Only tested with a Valheim server; that is all I have access to. 

Makes use of the [Requests](https://github.com/psf/requests) library.
