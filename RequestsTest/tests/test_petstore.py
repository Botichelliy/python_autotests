import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/234134')
    assert response.status_code == 200

def test_string_name():
    response = requests.get('https://petstore.swagger.io/v2/pet/234134')
    assert response.json()['name'] == 'goga'