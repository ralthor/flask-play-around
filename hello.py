from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index page'

@app.route('/hello')
def hello():
	return 'Hello World!'
	
@app.route('/user/<username>')
def profile(username):
	return 'User is %s' % username

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Subpath is %s' % subpath
	
@app.route('/projects/')
def projects():
	return 'This is the projects page<br/>{}'.format(url_for('profile', username='John Doe'))

with app.test_request_context():
	print(url_for('index'))
	print(url_for('hello'))
	print(url_for('hello', next='/'))
	print(url_for('profile', username='John Doe'))
	
#/
#/hello
#/hello?next=/
#/user/John%20Doe