import requests

endpoint1 = "http://127.0.0.1:8000/api/products/8/delete/"

res = requests.delete(endpoint1)
# print(res.headers['Content-Type'])
print(res.status_code)
