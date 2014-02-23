# import the Flask class
from flask import Flask

app = Flask(__name__)	# instance of Flask class
						# __name__ is name of the application's module

# index page
@app.route('/')
def index():
	return "Index"

# about page
@app.route('/about/')
def about():
	return "About"

# user profile pages
@app.route('/users/<user_name>')
def profile(user_name):
	return "%s's profile" % user_name


# hello world page
@app.route('/hello/')			# what url should trigger our function
def hellow_word():
	return "Hello world!"

if __name__ == '__main__':		# only run script if executed in Python interpreter, and not loaded as a module
	app.debug = True			# enable debug mode
	app.run()
	# app.run('0.0.0.0')		# run the server publicly