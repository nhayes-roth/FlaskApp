# import statements
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# create the application?
app = Flask(__name__)
app.config.from_object(__name__)

# load default config and override config from an environment variable
app.config.update(dict(
	DATABASE	= os.path.join(app.root_path, 'FlaskApp.db'),
	DEBUG		= True,
	SECRET_KEY	= 'development key',
	USERNAME	= 'user',
	PASSWORD	= 'password'
))
app.config.from_envvar('FLASKAPP_SETTINGS', silent = True)

# connect to the database
def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

# start the server to run this file as a standalone application
if __name__ == '__main__':		# only run script if executed in Python interpreter, and not loaded as a module
	app.run()
	# app.run('0.0.0.0')		# run the server publicly

""" OLD ROUTES
# index page
@app.route('/')
def index():
	return "Index"

# about page
@app.route('/about/')
def about():
	return "About"

# user profile pages
@app.route('/users/<user_name>/')
def profile(user_name):
	return "%s's profile" % user_name

# micropost urls
@app.route('/users/<user_name>/<int:post_id>/')
def micropost(user_name, post_id):
	return "User: %s Post: %d" % (user_name, post_id)


# hello world page
@app.route('/hello/')			# what url should trigger our function
def hellow_word():
	return "Hello world!"
"""