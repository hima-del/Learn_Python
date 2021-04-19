import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'http error occured:{http_err}')
    except Exception as err:
        print(f'other error occured:{err}')
    else:
        print("success!")                    