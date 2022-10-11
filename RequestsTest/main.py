import requests

response = requests.post('https://petstore.swagger.io/v2/pet', json={
  "id": 234134,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "frank",
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


response = requests.put('https://petstore.swagger.io/v2/pet', json={
  "id": 234134,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "goga",
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


response = requests.get('https://petstore.swagger.io/v2/pet/234134')

print(response.text)