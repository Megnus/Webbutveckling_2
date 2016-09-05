from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/movies')
def movies():
    movies = ["Godfather", "Hudson Hawk", "Die Hard"]
    return render_template("movies.html", movies=movies)


@app.route('/hello/<username>')
def hello(username):
    return 'Hello there %s' % username


if __name__ == "__main__":
    app.run(debug=True)
