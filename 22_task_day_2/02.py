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

csvfile=open('gsmarinadata.csv','w', newline='')
file = csv.DictWriter(csvfile, fieldnames=["Product_link","Storage","Network","Price","Name"])
file.writeheader()
csvfile.close()
 
url = 'https://www.gsmarena.com/'
text = requests.get(url,headers=headers).text
selector = Selector(text=text) 
product_link = selector.xpath('.//a[contains(@class,"block-link")]/@href').extract()
with open('gsmarinadata.csv', 'a',newline='',encoding="utf-8") as f:
    for i in product_link:
        my_list = []
        url = "https://www.gsmarena.com/" + i
        my_list.append(url)
        text = requests.get(url,headers=headers).text
        selector = Selector(text=text)
        my_list.append(''.join(selector.xpath('//*[@id="review-body"]/ul/li[4]/text()').extract()))
        network_link = selector.xpath('//*[@id="body"]/div/div[1]/div/div/div[3]/ul/li[3]/a/@href').extract()
        url_string = ''.join(network_link)
        url = "https://www.gsmarena.com/" + url_string
        text = requests.get(url,headers=headers).text
        selector = Selector(text=text)
        my_list.append(''.join(selector.xpath('.//a[contains(@class,"link-network-detail")]/text()').extract()))
        my_list.append(''.join(selector.xpath('.//td[contains(@data-spec,"price")]/a/text()').extract()))
        my_list.append(''.join(selector.xpath('//*[@id="body"]/div/div[1]/div/div[1]/h1/text()').extract()))
        writer = csv.writer(f)
        writer.writerow(my_list)
    
    
    
