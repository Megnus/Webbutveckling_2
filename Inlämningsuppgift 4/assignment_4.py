from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/contact')
def contact():
    return 'Hello, World!'


@app.route('/movies')
def movies():
    return 'Hello, World!'


@app.route('/hello/<username>')
def hello(username):
    return 'Hello there %s' % username


if __name__ == "__main__":
    app.run(debug=True)
