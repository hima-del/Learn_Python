import requests
from parsel import Selector
url = 'http://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'
text = requests.get(url).text
selector = Selector(text=text)
print(selector.xpath('//title/text()'))           