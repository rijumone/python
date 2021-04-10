from conftest import client


def make_encode_request(client):
    return client.post(
        '/encode', json={'url': 'https://codesubmit.io/library/react'})


def make_decode_request(client, short_url):
    return client.post(
        '/decode', json={'short_url': short_url})


def test_json_return(client):
    encode_res = make_encode_request(client)
    encode_json = encode_res.get_json()
    short_url = encode_json['data']

    decode_res = make_decode_request(client, short_url=short_url)

    try:
        decode_res.get_json()
    except TypeError:
        assert False
    assert True


def test_response_structure(client):
    encode_res = make_encode_request(client)
    encode_json = encode_res.get_json()
    short_url = encode_json['data']

    decode_res = make_decode_request(client, short_url=short_url)

    json_data = decode_res.get_json()

    assert 'message' in json_data
    assert 'data' in json_data


def test_response_success(client):
    encode_res = make_encode_request(client)
    encode_json = encode_res.get_json()
    short_url = encode_json['data']

    decode_res = make_decode_request(client, short_url=short_url)

    json_data = decode_res.get_json()

    assert json_data['message'] == 'success'


def test_decode_functionality(client):
    encode_res = make_encode_request(client)
    encode_json = encode_res.get_json()
    short_url = encode_json['data']

    decode_res = make_decode_request(client, short_url=short_url)

    json_data = decode_res.get_json()
    assert json_data['data'] == 'https://codesubmit.io/library/react'


def test_invalid_request(client):
    response = client.post('/decode', json={})
    json_data = response.get_json()
    assert 'error' in json_data


def test_non_existent_url(client):
    # add functionality to add 404 code
    response = client.post('/decode', json={'short_url': 'foobarqux'})
    json_data = response.get_json()
    assert 'error' in json_data


def test_other_request_verbs_failing(client):
    assert False
