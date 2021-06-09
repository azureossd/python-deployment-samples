import json

import falcon

from wsgiref import simple_server

class MyApplication:

    def on_get(self, req, resp):
        

        
        resp.text = "Falcon is working!"

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
        
app = application = falcon.App()

app.add_route('/', MyApplication())

if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()