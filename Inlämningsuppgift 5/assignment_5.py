from flask import Flask, request, render_template, jsonify, json
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def index():
    print('index')
    return render_template('index.html')


@app.route('/add', methods=['POST', 'GET'])
def api():
    # print(request.method)
    if request.method == 'POST':
        add_persons(request.form['firstname'],
                    request.form['lastname'],
                    request.form['snn'],
                    request.form['email'],
                    request.form['address'])
        # return jsonify({'persons': persons})
        print_persons()
        return redirect('/')

    return render_template('index.html')


@app.route('/done')
def contact():
    return render_template('done.html')


@app.route('/render')
def render():
    return render_template("contact.html")


@app.route('/users')
def users():
    print('users')
    # titles = ["Godfather", "Hudson Hawk", "Die Hard"]
    print(read_persons())
    return render_template('users.html', users=read_persons()['persons'])


@app.route('/hello/<name>')
def hello(name):
    return render_template("users.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def read_persons():
    persons = {'persons': []}
    # noinspection PyBroadException
    try:
        file = open('persons.json', 'r')
        persons = json.loads(file.read())
        file.close()
    except:
        print("Could not read file or file is empty")
    # return players
    return persons


def write_persons(persons):
    # noinspection PyBroadException
    try:
        file = open('persons.json', 'w')
        file.write(json.dumps(persons))
        file.close()
    except:
        print("Could not read file")


def add_persons(firstname, lastname, snn, email, address):
    persons = read_persons()
    persons['persons'].append({'firstname': firstname,
                    'lastname': lastname,
                    'snn': snn,
                    'email': email,
                    'address': address})
    write_persons(persons)


def print_persons():
    persons = read_persons()
    for i in range(1, len(persons)):
        print(", ".join([persons['persons'][i]["firstname"],
                         persons['persons'][i]["lastname"],
                         persons['persons'][i]["snn"],
                         persons['persons'][i]["email"],
                         persons['persons'][i]["address"]]))


# print(__name__)
if __name__ == "__main__":
    app.run(debug=True)

# set FLASK_APP=assignment_5.py
# flask run

# =======
# import json
# from pprint import pprint

# with open('data.json') as data_file:
#    data = json.load(data_file)

# with open('dataDump.json', 'w') as f:
#    json.dump(data, f)

# pprint(data)


# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]
