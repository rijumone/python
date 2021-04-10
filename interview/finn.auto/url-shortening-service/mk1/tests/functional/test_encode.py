from conftest import client


def make_request(client):
    return client.post(
        '/encode', json={'url': 'https://codesubmit.io/library/react'})


def test_json_return(client):
    response = make_request(client)
    try:
        response.get_json()
    except TypeError:
        assert False
    assert True


def test_len_shorturl(client):

    response = make_request(client)

    json_data = response.get_json()
    short_url_suffix = json_data['data'].split('/')[-1]
    assert len(short_url_suffix) == 5


def test_response_structure(client):
    response = make_request(client)

    json_data = response.get_json()

    assert 'message' in json_data
    assert 'data' in json_data


def test_response_success(client):
    response = make_request(client)

    json_data = response.get_json()

    assert json_data['message'] == 'success'


def test_other_request_verbs_failing(client):
    response = client.get('/encode', json={})
    assert response.status_code == 405


def test_invalid_request(client):
    response = client.post(
        '/encode', json={'url1': 'https://codesubmit.io/library/react'})
    json_data = response.get_json()
    assert 'errors' in json_data
    assert response.status_code == 400

# test_json_return(client)
