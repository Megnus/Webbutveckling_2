"""
    Inlämningsuppgift 4
    Magnus Sundström
    2016-09-06
"""


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/hello/<name>')
def hello(name):
    return render_template("hello.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
