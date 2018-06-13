
from flask import render_template
from app import app


@app.route('/')
@app.route('/helloWorld')
def helloWorld():
    user = {'username': 'ganeshkb'}
    return render_template('index.html', title ='Home', user=user)
