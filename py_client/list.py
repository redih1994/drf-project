import requests
from getpass import getpass


endpoint1 = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.post(endpoint1, json={"username": 'redi', 'password': password})
res = auth_response.json()
print(res)

if auth_response.status_code == 200:
    endpoint1 = "http://127.0.0.1:8000/api/products/"
    token = res['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(endpoint1, headers=headers)
    # print(res.headers['Content-Type'])
    print(res.json())