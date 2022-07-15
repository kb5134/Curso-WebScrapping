import requests

response = requests.get('https://www.leonardotozoni.com/')

print(response.status_code)
print(response.headers)

print('\n')
print(response.content)