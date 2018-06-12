from app import app


@app.route('/')
@app.route('/helloWorld')
def helloWorld():
    return "Hello World!"
