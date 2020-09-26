from flask import Flask
import os
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


@app.route('/')
def index():
    return 'Index Page'

#@app.route('/hello')
#def hello():
#    return 'Hello, World'

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
	app.run()
