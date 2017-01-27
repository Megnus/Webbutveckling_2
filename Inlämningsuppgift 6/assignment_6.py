"""
    Inlämningsuppgift 6
    Magnus Sundström
    2017-01-20
"""

import datetime
from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)


@app.route('/')
def index():
    return articles()


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/edit/<title>')
def edit(title):
    return render_template('edit.html', article=get_article(title))


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=read_articles()['articles'])


@app.route('/article/<title>')
def article(title):
    return render_template('read.html', article=get_article(title))


@app.route('/api')
def get_api():
    return jsonify(read_articles())


@app.route('/api/<title>')
def get_api_title(title):
    return jsonify(get_article(title))


@app.route('/added', methods=['POST', 'GET'])
def added():
    if request.method == 'POST':
        add_article(request.form['author'],
                    request.form['title'],
                    request.form['text'])
    return render_template('done.html', message='Article was successfully added')


@app.route('/edited', methods=['POST', 'GET'])
def edited():
    if request.method == 'POST':
        edit_article(request.form['author'],
                     request.form['title'],
                     request.form['text'])
    return render_template('done.html', message='Article was successfully edited')


@app.route('/delete/<title>')
def delete(title):
    content = read_articles()
    idx = get_index(content, title)
    if idx >= 0:
        content['articles'].pop(idx)
    write_articles(content)
    return render_template('done.html', message='Article was successfully deleted')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def get_index(content, title):
    for i in range(0, len(content['articles'])):
        if content['articles'][i]['title'] == title:
            return i
    return -1


def get_json_article(title):
    content = read_articles()
    idx = get_index(content, title)
    if idx >= 0:
        return jsonify({'title': content['articles'][idx]})
    return render_template('page_not_found.html'), 404


def get_article(title):
    content = read_articles()['articles']
    for i in range(0, len(content)):
        if content[i]['title'] == title:
            return content[i]
    return render_template('page_not_found.html'), 404


def read_articles():
    content = {'articles': []}
    # noinspection PyBroadException
    try:
        file = open('articles.json', 'r')
        content = json.loads(file.read())
        file.close()
    except:
        print("Could not read file or file is empty")
    return content


def write_articles(content):
    # noinspection PyBroadException
    try:
        file = open('articles.json', 'w')
        file.write(json.dumps(content))
        file.close()
    except:
        print("Could not read file")


def add_article(author, title, text):
    content = read_articles()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    content['articles'].append({'author': author,
                                'title': title,
                                'text': text,
                                'created': date,
                                'edited': date,
                                'revision': 1})
    write_articles(content)


def edit_article(author, title, text):
    content = read_articles()
    idx = get_index(content, title)
    if idx >= 0:
        content['articles'][idx]['author'] = author
        content['articles'][idx]['text'] = text
        content['articles'][idx]['edited'] = datetime.datetime.now().strftime("%Y-%m-%d")
        content['articles'][idx]['revision'] = int(content['articles'][idx]['revision']) + 1
    write_articles(content)


if __name__ == "__main__":
    app.run(debug=True)
