# Falcon



Empty Python Falcon **WSGI** app ready to be deployed to Azure
> The application will be listening by default on **0.0.0.0:8000**
  
## Linux App Service

Can be run by Oryx with gunicorn, as it's identical to [Flask or other WSGI's](https://docs.microsoft.com/en-us/azure/app-service/configure-language-python#flask-app)(it will look for app:app)

Or you can add the following startup command(in case that the main .py file and Falcon app have different names):

```sh
gunicorn app:app
```

## Locally 

Locally, if you don't have gunicorn or other WSGI server you can start it directly through the wsgiref.simple_Server class:

```sh
if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()
```
execute:

```sh
python app.py
```


