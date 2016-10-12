from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/')
def index():
    print('yoyoyo')
    return render_template("index.html")


@app.route('/api', methods=['POST', 'GET'])
def api():
    print(request.method)
    if request.method == 'POST':
        print('Request method: ' + request.method)
        print('First name: ' + request.form['firstName'])
        print('Last name: ' + request.form['lastName'])
        #return jsonify({'tasks': tasks})

    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/movies')
def movies():
    print('yoyoyo')
    titles = ["Godfather", "Hudson Hawk", "Die Hard"]
    return render_template("movies.html", titles=titles)


@app.route('/hello/<name>')
def hello(name):
    return render_template("hello.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

print(__name__)
if __name__ == "__main__":
    app.run(debug=True)

# =======
# import json
# from pprint import pprint

# with open('data.json') as data_file:
#    data = json.load(data_file)

# with open('dataDump.json', 'w') as f:
#    json.dump(data, f)

# pprint(data)
