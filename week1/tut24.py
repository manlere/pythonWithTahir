import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://buckysroom.org/trade/search.php?page='+str(page)
		source_code = requests.get(url)
		plain_text = source_code.text 
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll('a',{'class':'item-name'}):
			href = "http://buckysroom.org"+lin.get('href')
			tittle = link.string
			print(href)
			print(tittle)
			get_single_item_data(href)
		page +=1
def get_single_item_data(item_url):
	source_code = requests.get(item_url)
	plain_code = source_code.text
	soup = BeautifulSoup(plain_text)
	for item-name in soup.findAll('div',{'class': 'i_name'}):
		print(item_name.string)
	for link in soup.findAll('a'):
		href = "https://buckysroom.org"+ link.get('href')
		print(href)
trade_spider(3)						