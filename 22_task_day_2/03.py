import requests
from parsel import Selector
import csv
#from itertools import cycle

headers = {
'Host' : 'www.gsmarena.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': "1",
'Cache-Control': 'max-age=0',
}

proxies = {
    "http": '104.248.90.255:8118', 
    "https": '104.248.90.255:8118'
}

f = open('gsdata.csv','w', newline='')
file = csv.DictWriter(f, fieldnames=["Name","Price","Storage","Network","Product_link"])
file.writeheader()
f.close()
 
url = 'https://www.gsmarena.com/'
text = requests.get(url,headers=headers,proxies=proxies).text
selector = Selector(text=text)
brand_link = selector.xpath('//*[@id="body"]/aside/div[1]/ul/li/a/@href').extract()[:5]


for i in brand_link:
    url_a = "https://www.gsmarena.com/" + i
    text = requests.get(url_a,headers=headers,proxies=proxies).text
    selector = Selector(text=text)
    url_page = (''.join(selector.xpath('//*[@id="body"]/div/div[3]/div[1]/a[1]/@href').extract()))
    my_url = url_page.replace('2.php','')
    for j in range(1,6):
        url =  'https://www.gsmarena.com/{}{}.php'.format(my_url,j)
        text = requests.get(url,headers=headers,proxies=proxies).text
        selector = Selector(text=text)
        product_link = selector.xpath('//*[@id="review-body"]/div[1]/ul/li/a/@href').extract()
        with open('gsdata.csv', 'w',newline='',encoding="utf-8") as f:
            for k in product_link:
                my_list = []
                url = "https://www.gsmarena.com/" + k
                text = requests.get(url,headers=headers,proxies=proxies).text
                selector = Selector(text=text)
                my_list.append(''.join(selector.xpath('//*[@id="body"]/div/div[1]/div/div[1]/h1/text()').extract()))
                my_list.append(''.join(selector.xpath('.//td[contains(@data-spec,"price")]/a/text()').extract()))
                my_list.append(''.join(selector.xpath('.//td[contains(@data-spec,"internalmemory")]/text()').extract()))
                my_list.append(''.join(selector.xpath('.//a[contains(@class,"link-network-detail")]/text()').extract()))
                my_list.append(url)
                writer = csv.writer(f)
                writer.writerow(my_list)

            
    



