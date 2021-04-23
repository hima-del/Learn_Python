import requests
from parsel import Selector
import csv

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

csvfile=open('mydata.csv','w', newline='')
file = csv.DictWriter(csvfile, fieldnames=["Product_link","Name","Price"])
file.writeheader()
csvfile.close()

url = ' https://scrapeme.live/shop/'
text = requests.get(url,headers=headers).text
selector = Selector(text=text)
path = selector.xpath('//*[@id="main"]/ul/li')
with open('mydata.csv', 'a',newline='') as f:
    for item in path:
        my_list = []
        my_list.append((''.join(item.xpath('.//a[contains(@class,"product__link")]/@href').extract())))
        my_list.append(''.join(item.xpath('.//h2/text()').extract()))
        my_list.append((''.join(item.xpath('.//span[contains(@class,"Price-amount")]/text()').extract())))
        writer = csv.writer(f)
        writer.writerow(my_list)

