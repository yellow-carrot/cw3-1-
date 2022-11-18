from utils import *


def test_utils_load_data():
    response = load_data('static/data/posts.json')
    assert isinstance(response, list)


def test_utils_load_posts():
    response = load_posts()
    assert isinstance(response, list)


def test_utils_load_post(posts_keys):
    response = load_post(1)
    assert isinstance(response, dict)
    assert set(response.keys()) == posts_keys


def test_utils_load_comments(comments_keys):
    response = load_comments(1)
    assert isinstance(response, list)
    assert set(response[0].keys()) == comments_keys
