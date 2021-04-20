from parsel import Selector
text = u"<html><body><h1>hello,parsel!</h1></body></html>"
sel = Selector(text = text)
print(sel.css("h1::text").extract_first())
print(sel.xpath("body/h1/text()").extract())
