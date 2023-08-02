import requests

endpoint1 = "http://127.0.0.1:8000/api/products/1/update/"

data = {'title': 'Hello world updated', 'content': 'this is amaizing', 'price': '329.99', 'sale_price': '103.99', 'my_discount': '122'}

res = requests.patch(endpoint1, json=data)
# print(res.headers['Content-Type'])
print(res.json())