import requests
import pytest

def test_statuscode():
    response = requests.get("https://petstore.swagger.io/v2/pet/777")
    assert response.status_code == 200
    
def test_name():
    response = requests.get("https://petstore.swagger.io/v2/pet/777")
    assert response.json()["name"] == "vasya"

