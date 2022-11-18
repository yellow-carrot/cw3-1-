import json


def load_data(filename):
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_posts(search_word=None, user_name=None):
    posts = load_data('static/data/posts.json')

    if search_word:
        posts = filter(lambda x: search_word in x['content'].lower(), posts)

    if user_name:
        posts = filter(lambda x: user_name == x['poster_name'].lower(), posts)

    return posts


def load_post(pk):
    posts = load_data('static/data/posts.json')
    for post in posts:
        if pk == post['pk']:
            return post


def load_comments(post_pk):
    all_comments = load_data('static/data/comments.json')
    comments = []
    for comment in all_comments:
        if post_pk == comment['post_id']:
            comments.append(comment)
    return comments
