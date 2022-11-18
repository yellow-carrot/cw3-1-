def test_posts(client):
    response = client.get('/api/')

    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_post(client, posts_keys):
    response = client.get('/api/1')

    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == posts_keys




