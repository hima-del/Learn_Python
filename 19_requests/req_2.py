import requests

response = requests.get("https://api.github.com/")
print(response.headers['Content-Type'])
print(response.raise_for_status)