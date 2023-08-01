import requests

endpoint1 = "http://127.0.0.1:8000/api/"

res = requests.get(endpoint1,  json={"product_id": 123})
print(res.headers['Content-Type'])
print(res.json())