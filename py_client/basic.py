import requests

endpoint1 = "http://127.0.0.1:8000/api/"

res = requests.post(endpoint1,  json={"title": "abc", "content": "Hello world", "price": 123})
# print(res.headers['Content-Type'])
print(res.json())