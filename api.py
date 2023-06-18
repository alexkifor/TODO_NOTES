import requests
import time

DOMAIN = 'http://127.0.0.1:8004'


def timeout():
    time.sleep(2)


def get_url(url):
    return f'{DOMAIN}{url}'


timeout()

# не авторизован
response = requests.get(get_url('/api/projects/'))
assert response.status_code == 401

timeout()
# базовая авторизация
response = requests.get(get_url('/api/projects/'), auth=('user0', 'user'))
assert response.status_code == 200

timeout()
# авторизация по токену
TOKEN = 'ca4078efde49ecb14d754ba3b0f3b27b5a7a4c69'
# response = requests.get(get_url('/api/projects/'), headers={'Authorization': f'Token {TOKEN}'})
headers = {'Authorization': f'Token {TOKEN}'}
response = requests.get(get_url('/api/projects/'), headers=headers)
assert response.status_code == 200

timeout()

# авторизация по jwt
# Получаем токен
response = requests.post(get_url('/api/token/'), data={'username': 'user0', 'password': 'user'})
result = response.json()
# это наш токен
access = result['access']
print('Первый токен',access,end=f'\n{150*"*"}\n')
# это для рефреша
refresh = result['refresh']
print('refresh',refresh,end=f'\n{150*"*"}\n')
timeout()
# Авторизуемся с ним
headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/projects/'), headers=headers)
assert response.status_code == 200

timeout()
# Рефрешим токен ( ДЛЯ ОБНОВЛЕНИЯ)
response = requests.post(get_url('/api/token/refresh/'), data={'refresh': refresh})
# print(response.status_code)
# print(response.text)
result = response.json()
# это наш токен
access = result['access']
print('Обновленный токен',access,end=f'\n{150*"*"}\n')
print('refresh',refresh,end=f'\n{150*"*"}\n')
timeout()
# Авторизуемся с ним
headers = {'Authorization': f'Bearer {access}'}
response = requests.get(get_url('/api/projects/'), headers=headers)
assert response.status_code == 200