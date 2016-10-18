"""
    Inlämningsuppgift 5
    Magnus Sundström
    2016-10-17
"""


from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/done', methods=['POST', 'GET'])
def done():
    if request.method == 'POST':
        add_users(request.form['firstname'],
                  request.form['lastname'],
                  request.form['ssn'],
                  request.form['email'],
                  request.form['address'])
    return render_template('done.html')


@app.route('/users/')
@app.route('/users/<ssn>')
def user(ssn):
    users = read_users()['users']
    for i in range(0, len(users)):
        if users[i]['ssn'] == ssn:
            return jsonify({'user': users[i]})
    return render_template('page_not_found.html'), 404


@app.route('/users')
def users():
    return jsonify(read_users())


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def read_users():
    users = {'users': []}
    # noinspection PyBroadException
    try:
        file = open('users.json', 'r')
        users = json.loads(file.read())
        file.close()
    except:
        print("Could not read file or file is empty")
    return users


def write_users(users):
    # noinspection PyBroadException
    try:
        file = open('users.json', 'w')
        file.write(json.dumps(users))
        file.close()
    except:
        print("Could not read file")


def add_users(firstname, lastname, ssn, email, address):
    persons = read_users()
    persons['users'].append({'firstname': firstname,
                             'lastname': lastname,
                             'ssn': ssn,
                             'email': email,
                             'address': address})
    write_users(persons)


if __name__ == "__main__":
    app.run(debug=True)