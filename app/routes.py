from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Joel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/second')
def first():
    return render_template('second.html')

@app.route('/third')
def first():
    return render_template('third.html')

