import requests
import pytest


@pytest.fixture()
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
    object_id = response['id']

    yield object_id
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.fixture(scope='session')
def testing_stage():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def test_progress():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
def test_single_object(add_object, testing_stage, test_progress):
    response = requests.get(f'https://api.restful-api.dev/objects/{add_object}')
    assert response.json()['id'] == add_object, 'No entry with this ID found'


@pytest.mark.medium
def test_update_object(add_object, test_progress):
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
    response = requests.put(f'https://api.restful-api.dev/objects/{add_object}', json=body, headers=headers).json()
    assert response['name'] == 'Apple MacBook Pro 16'
    assert response['data']['price'] == 3000
    assert response['data']['CPU model'] == 'M3'


def test_partially_update_object(add_object, test_progress):
    body = {
        "name": "Apple MacBook Air 16",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{add_object}', json=body, headers=headers).json()
    assert response['name'] == 'Apple MacBook Air 16'


@pytest.mark.parametrize('body', [{"name": "Apple MacBook Pro 16",
                                   "date": {"year": 2021, "price": 2500, "CPU model": "M2", "Hard disk size": "1 TB"}},
                                  {"name": "Apple MacBook Air",
                                   "date": {"year": 2019, "price": 900, "CPU model": "M1", "Hard disk size": "128 GB"}},
                                  {"name": "Apple MacBook Pro 16",
                                   "date": {"year": 2023, "price": 3500, "CPU model": "M3", "Hard disk size": "1 TB"}}
                                  ])
def test_add_object(test_progress, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code == 200

