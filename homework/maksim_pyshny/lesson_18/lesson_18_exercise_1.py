import requests


def add_object():
    body = {
        "name": "Apple MacBook Pro 14",
        "data": {
            "year": 2021,
            "price": 2000,
            "CPU model": "M1",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers).json()

    return response['id']


def single_object():
    object_id = add_object()
    response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
    assert response.json()['id'] == object_id, 'No entry with this ID found'


def update_object():
    object_id = add_object()
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2021,
            "price": 3000,
            "CPU model": "M3",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{object_id}', json=body, headers=headers).json()
    assert response['name'] == 'Apple MacBook Pro 16'
    assert response['data']['price'] == 3000
    assert response['data']['CPU model'] == 'M3'


def partially_update_object():
    object_id = add_object()
    body = {
        "name": "Apple MacBook Air 16",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{object_id}', json=body, headers=headers).json()
    assert response['name'] == 'Apple MacBook Air 16'


def delete_object():
    object_id = add_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert response.status_code == 200


single_object()
update_object()
partially_update_object()
delete_object()
