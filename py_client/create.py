import requests

endpoint1 = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 32.99
}


res = requests.post(endpoint1, json=data)
# print(res.headers['Content-Type'])
print(res.json())