
import bottle, json
from bottle import route, run, response

@route('/')
def index():
    """Home page"""
    response.content_type = 'application/json'
    return json.dumps({ "msg": "Hello World from Bottle with different module name"})

if __name__ == '__main__':
	run(host='0.0.0.0', port=8080, debug=True, reloader=True)

#app = bottle.default_app()
#using gunicorn, this will need to match with file:PATH or python:MODULE_NAME example: gunicorn index:myserver
myserver = bottle.default_app()