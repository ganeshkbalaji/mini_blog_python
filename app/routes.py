
from flask import render_template
from app import app


@app.route('/')
@app.route('/helloWorld')
def helloWorld():
    user = {'username': 'ganeshkb'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Oakland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Cant wait to climb a mountain!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
