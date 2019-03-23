# Break_service

Windows service written in python that monitors 30 minute intervals and starts breaks
NOTE!!! Currently not - working!

## Implementation

To use this, install pywin32 using the following:

```py
pip install pywin32
```

You can then use the '`base`' class `service.py` as an import and create your own windows services. The windows service that is the subject of this repo
just reminds you every 30 minutes to take a break.

It redirects you to the following website <https://takeabreak.azurewebsites.net/> which is just a simple website with a gif on it that I created using vue.
The gifs rotated every 3 hours. (No auto reload - need to manually reload the page. I'm not using the computed field in vue).

### Service management

Note, the following commands assume that you have the same file name as me.

- if you want to install the windows service:

```python
python .\app.py install
```

- if you make changes, update the service with:

```py
python .\app.py update
```

- If you want to remove the service, use the following:

```py
python .\app.py remove
```

- If you want to debug the application, use:

```py
python .\app.py debug
```