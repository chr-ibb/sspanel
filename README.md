# SSPanel.py

**SSPanel.py** is an API providing basic functinality of the **[Survival Servers](https://www.survivalservers.com/ "survivalservers.com")** *Control Panel* to Python via HTTPS requests.  
Allows for starting, stopping, and restarting a server, as well as getting server info.  

```python
>>> import sspanel
>>> username, password = "aUserName", "aP@ssw0rd"
>>> subuser = False
>>> serverid = 123456
>>> panel = sspanel.SSPanel(username, password, subuser, serverid)
'Login successfull'
'Panel is ready'

>>> panel.start()
'Login successfull'
'Server is started'

>>> panel.stop()
'Login successfull'
'Server is stopped'
```

Makes use of the [Requests](https://github.com/psf/requests) library.
