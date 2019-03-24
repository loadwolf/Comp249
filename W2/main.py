__author__ = 'loadwolf'

from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    return "Test"

if __name__ == '__main__':
    app.run()