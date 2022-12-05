# ex3.py

import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'http://quotes.toscrape.com/'

html = ur.urlopen(url)
# print(html.read()[:100])
soup = bs(html.read(), 'html.parser')

quote = soup.find_all('span', {'class':'text'})  # 자동으로 리스트
by = soup.find_all('span', {'class':''})
tag = soup.find_all('a', class_='tag')
# print(quote[0])
# print('------------------')
# print(quote[1])

for i in quote :
    print(i.text)

print('---------------------------')
for i in by :
    print(i.text)

print('---------------------------')
for i in tag :
    print(i.text)

