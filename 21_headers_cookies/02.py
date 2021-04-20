import requests
response = requests.get('https://api.github.com')
#response.encoding = 'utf-8'
#print(response.json()) #return value will be dictionary
print(response.headers)