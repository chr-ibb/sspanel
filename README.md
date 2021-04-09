# SSPanel.py

**SSPanel.py** is a simple API providing the basic functionality of the **[SurvivalServers.com](https://www.survivalservers.com/)** Control Panel to Python  
via HTTPS requests. It allows for starting, stopping, and restarting a server, as well as getting server info.  

```python
>>> import sspanel
>>> username, password, subuser = "aUserName", "aP@ssw0rd", False
>>> serverid = 123456
>>> panel = sspanel.ControlPanel(username, password, subuser, serverid)
'Login successful'
'Control Panel is ready'

>>> panel.start()
'Login successful'
'Server is started'

>>> panel.stop()
'Login successful'
'Server is stopped'
```

Makes use of the [Requests](https://github.com/psf/requests) library.
