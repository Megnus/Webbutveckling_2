"""
    Inlämningsuppgift 6
    Magnus Sundström
    2017-01-20
"""


from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)


class Person:
    def __init__(self, name, age=None, sex=None):
        self.name, self.age, self.sex = name, age, sex

@app.route('/')
def index():
    return render_template('index.html', article=None, edit=False)


@app.route('/done', methods=['POST', 'GET'])
def done():
    if request.method == 'POST':
        add_article(request.form['author'],
                    request.form['title'],
                    request.form['article'])
        # is_edit
    return render_template('done.html')


@app.route('/edit')
def edit():
    return render_template('index.html', setter=Person('snn', 25, 6))


@app.route('/edit/<title>')
def edit_article(title):
    print(get_articlec(title))
    return render_template('index.html', article=get_articlec('title'), edit=True)


@app.route('/article/')
@app.route('/article/<ssn>')
def get_article(title):
    articles = read_articles()['articles']
    for i in range(0, len(articles)):
        if articles[i]['title'] == title:
            return jsonify({'title': articles[i]})
    return render_template('page_not_found.html'), 404


def get_articlec(title):
    articles = read_articles()['articles']
    for i in range(0, len(articles)):
        if articles[i]['title'] == title:
            return articles[i]
    return render_template('page_not_found.html'), 404


@app.route('/articles')
def get_articles():
    return render_template('articles.html', articles=read_articles()['articles'])


@app.route('/api')
def users():
    return jsonify(read_articles())


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


def read_articles():
    articles = {'articles': []}
    # noinspection PyBroadException
    try:
        file = open('articles.json', 'r')
        articles = json.loads(file.read())
        file.close()
    except:
        print("Could not read file or file is empty")
    return articles


def write_articles(articles):
    # noinspection PyBroadException
    try:
        file = open('articles.json', 'w')
        file.write(json.dumps(articles))
        file.close()
    except:
        print("Could not read file")


def add_article(author, title, article):
    articles = read_articles()
    articles['articles'].append({'author': author,
                                 'title': title,
                                 'article': article})
    # created, edited, revision, author: firstname, last name,
    write_articles(articles)


if __name__ == "__main__":
    app.run(debug=True)
