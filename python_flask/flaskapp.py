# http://flask.pocoo.org/
from flask import Flask, render_template
app = Flask(__name__)


posts = [
	{
		'title':'post 2',
		'content': ' lorem ipsum'
	},
	{
		'title':'post 2',
		'content': ' lorem ipsum'
	}
]

@app.route("/")
@app.route("/home")
def home(name=None):
    print("hello")


# http://flask.pocoo.org/docs/1.0/quickstart/
    return render_template('index.html', name=name, posts=posts)

@app.route("/hi")
def hi():
	return "Hi"


def calculate(x,y):
	return x+y

if __name__ == '__main__':
	app.run(debug=True) # i.e. if we run this file with python, it should launch in debug mode, e.g. python flaskapp.py



''' ''' #triple single quotes for multiline