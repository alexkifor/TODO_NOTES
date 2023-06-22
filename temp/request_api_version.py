import requests

response = requests.post('http://localhost:8000/api-token-auth/',
                         data={
                             'username': 'admin',
                             'password': 'admin'
                         })
token = f'Token {response.json()["token"]}'
print(response.json())
response = requests.get('http://localhost:8000/api/users/40/',
                        headers={'Accept': 'application/json', 'Authorization': token})
# {'id': 2, 'username': 'admin', 'first_name': 'admin', 'last_name': 'admin', 'email': 'admin@email.ru'}
print(response.json())
response = requests.get('http://localhost:8000/api/users/40/',
                        headers={'Accept': 'application/json; version=0.2', 'Authorization': token})
# {'id': 2, 'username': 'admin', 'first_name': 'admin', 'last_name': 'admin', 'email': 'admin@email.ru',
# 'is_superuser': True, 'is_staff': True}
print(response.json())