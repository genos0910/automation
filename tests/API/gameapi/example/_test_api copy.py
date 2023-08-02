import requests

platform_id = ""
uuid = ""
username=""
credit=""
transaction_id=""
key=""

def test_get_request():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_post_request():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', data = {'key':'value'})
    assert response.status_code == 201
    json_response = response.json()
    assert json_response['id'] == 101
