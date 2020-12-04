from bs4 import BeautifulSoup
from urllib.request import urlopen as req

url = "http://nbg.ge/rss.php"

res = req(url)
xml = res.read()
res.close()
soup = BeautifulSoup(xml, 'xml')
items = soup.findAll('item')
print(items[0].title.text)
table = BeautifulSoup(items[0].description.text, 'html.parser')
rows = table.findAll('tr')
for row in rows:
	col = row.findAll('td')
	print(col[1].text, col[2].text)