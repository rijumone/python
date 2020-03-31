import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.gsmarena.com/")

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

prettySoup = soup.prettify()

topList = list(soup.children)

# print([type(item) for item in topList])

html = topList[2]

# print()

print([k.get_text() for k in soup.select('div.news-item h3')])

for index in range(34, 33, -1):
	print index