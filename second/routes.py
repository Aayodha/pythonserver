from second import app
from flask import render_template

@app.route('/')
def index():
    return "Hello"
@app.route('/home')
def homepage():
    return render_template('homepage.html')

