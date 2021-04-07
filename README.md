# SSPanel.py

**SSPanel.py** is an API providing basic functinality of the **[Survival Servers](https://www.survivalservers.com/ "survivalservers.com") Control Panel** to Python via HTTP requests.  
Allows for starting, stopping, and restarting a server, as well as getting server info.  

```python
>>> import sspanel
>>> username, password = "aUserName", "aP@ssw0rd"
>>> subuser = false
>>> serverid = 123456
>>> panel = sspanel.SSPanel(username, password, subuser, serverid)
'Login successfull'
'Finding panel password...'
'Panel password found'

>>> panel.start()
'Login successfull'
'Starting server...'
'Server started successfully'

>>> panel.stop()
'Login successfull'
'Stopping server...'
'Server stopped successfully'
```

Makes use of the [Requests](https://github.com/psf/requests) library.
