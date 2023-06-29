from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://beans.itcarlow.ie/prices.html"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
price = soup.find('strong')
price.string