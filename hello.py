from flask import Flask, url_for, render_template
app = Flask(__name__)

posts = [
	{
		'author': 'Rand Althor',
		'title': 'My first blog post',
		'content': 'It is the very start of my blog',
		'date_posted': '3 December 2018'
	},
	{
		'author': 'John Doe',
		'title': 'My another blog post',
		'content': 'I am professional in writing blogs',
		'date_posted': '2 December 2018'
	},
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}
]

@app.route('/')
def index():
	return 'Index page'

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name, title='test')
	
@app.route('/user/<username>')
def profile(username):
	return 'User is %s' % username

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Subpath is %s' % subpath
	
@app.route('/posts')
def blog():
	return render_template('blog.html', posts=posts)
	
@app.route('/projects/')
def projects():
	return 'This is the projects page<br/>{}'.format(url_for('profile', username='John Doe'))

with app.test_request_context():
	print(url_for('index'))
	print(url_for('hello'))
	print(url_for('hello', next='/'))
	print(url_for('profile', username='John Doe'))
