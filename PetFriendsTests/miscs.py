import requests

url = f'https://petfriends.skillfactory.ru/'
res = requests.get(url, headers = {'accept': 'application/json'}, params={'status': 'available'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))