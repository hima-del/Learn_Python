import requests
url = '<a href="http://some-domain.com/set/cookies/headers">http://some-domain.com/set/cookies/headers</a>'
headers = {'user-agent':'your-own-user-agent/0.0.1'}
cookies = {'visit-month':'february'}
req = requests.get(url,headers=headers,cookies=cookies)