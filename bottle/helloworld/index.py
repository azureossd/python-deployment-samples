
import bottle, json
from bottle import route, response

@route('/')
def index():
    """Home page"""
    response.content_type = 'application/json'
    return json.dumps({ "msg": "Hello World from Bottle"})

if __name__ == '__main__':
	bottle.run(host='0.0.0.0', port=8080, debug=False, reloader=True)
