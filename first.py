#an object of WSGI application
from flask import Flask

app = Flask(__name__)

#which url i want to access
@app.route('/')

def hello():
    return "Hello"

@app.route("/courses")
def courses():
    return "<h1>Flask basic Tutorial</h1>"

@app.route("/<name>")
def user(name):
    return f'<h1>Hello {name}! Welcome to Goeduhub Technologies!!</h1>'

from flask import render_template
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run()