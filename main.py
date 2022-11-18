from flask import Flask, render_template, jsonify, request

import logger
from utils import *


app = Flask(__name__)


@app.route('/')
def page_index():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:pk>')
def page_post(pk):
    post = load_post(pk)
    comments = load_comments(pk)
    return render_template('post.html', post=post, comments=comments)


log = logger.get_logger('main')


@app.route('/api/posts')
def api_index():
    posts = load_posts()
    log.info('Запрос /api/posts')
    return jsonify(posts)


@app.route('/api/posts/<int:pk>')
def api_post(pk):
    post = load_post(pk)
    log.info(f'Запрос api/posts/{pk}')
    return jsonify(post)


@app.route('/search/')
def page_search():
    s = request.args.get('s', '').lower()  # request.args.get('s', '') '' - default value.
    posts = load_posts(search_word=s)
    return render_template('search.html', posts=posts)


@app.route('/user/<user_name>')
def page_search_by_user(user_name):
    posts = load_posts(user_name=user_name)
    return render_template('user-feed.html', posts=posts)

# Несуществующие страницы
@app.errorhandler(404)
def not_found(e):
    return 'Ошибка 404, запрашиваемая страница не существует.'

# Ошибки на стороне сервера
@app.errorhandler(500)
def server_error(e):
    return 'ошибка 500, Internal Server Error'






if __name__ == '__main__':
    app.run(debug=True)
