
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('helloWorld'))
    return render_template('login.html', title='Sign In', form=form)
