import requests

response = requests.get('https://www.walissonsilva.com/')

print(response.status_code)
print(response.headers)

print('\n')
print(response.content)