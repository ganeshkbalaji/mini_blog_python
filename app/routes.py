from app import app


@app.route('/')
@app.route('/helloWorld')
def helloWorld():
    user = {'username': 'ganeshkb'}
    return '''
    <html>
        <head>
            <title>Microblog</title>
        </head>
        <body>
            <h1>Hi, ''' + user['username'] + '''</h1>
        </body>
    </html>'''
