# import the Flask class
from flask import Flask

app = Flask(__name__)	# instance of Flask class
						# __name__ is name of the application's module

@app.route('/hello')			# what url should trigger our function
def hellow_word():
	return "Hello world!"

if __name__ == '__main__':		# only run script if executed in Python interpreter, and not loaded as a module
	app.run()
	# app.run('0.0.0.0')		# run the server publicly