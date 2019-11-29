import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://buckysroom.org/trade/search.php?page='+ str(page)
		source_code = requests.get(url)
		plain_text = source_code.plain_text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a',{'class': 'item-name'}):
			href = "https://buckysroom.org"+link.get('href')
			tittle = link.string
			print(href)
			print(tittle)
		page += 1
trade_spider(1)			