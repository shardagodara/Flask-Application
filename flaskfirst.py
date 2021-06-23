from flask import Flask, redirect, url_for,render_template
from flask import *

app = Flask(__name__) 

@app.route("/")

def goedu():

    return render_template('index.html')
@app.route("/courses")

def course():

    return "<h1>FLASK BASIC TUTORIAL</h1>"


@app.route('/submit',methods=['POST','GET'])
def submit():
    marks = 0
    if request.method =='POST':
        phy = float(request.form['physics'])
        ch = float(request.form['chemistry'])
        maths = float(request.form['maths'])
        total = (phy+ch+maths)/3
    marks=total
    return redirect(url_for('success',marks=marks))

@app.route("/user/<name>")

def user(name):

    return f"<h1>Hello {name}! Welcome to Goeduhub Technologies!</h1>"

@app.route('/results/<int:marks>')
def results(marks):
    
    return redirect(url_for('success',marks=marks))

@app.route('/success/<int:marks>')
def success(marks):
    final =""
    if marks<45:
        final ='Fail'
    else:
        final = 'Pass'
    exp = {'number':marks,'result':final}
    return render_template('result.html',result=exp)

@app.route("/about")
def about():
    return render_template('about.html')

# Asking the application to run the program

if __name__=="__main__":

    app.run(debug=True, port=8000)
