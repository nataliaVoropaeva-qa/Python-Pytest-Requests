from pytest import param
import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 777,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print(response.text)

response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 777,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "vasya",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/777")

print(response.text)