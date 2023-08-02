import requests

endpoint1 = "http://127.0.0.1:8000/api/products/1/"

res = requests.get(endpoint1)
# print(res.headers['Content-Type'])
print(res.json())