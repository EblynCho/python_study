# ex5.py

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

article1 = 'https://news.v.daum.net/v/20200427090630709'
html = ur.urlopen(article1)
soup = bs(html.read(), 'html.parser')

f = open('./data/links.txt', 'w', encoding='utf-8')

# 헤드라인 출력
headLine = soup.find_all('h3', {'class':'tit_view'})[0].text
print(headLine)  # 당정, 농산물꾸러미 초중고 학생 364만명에 지원..5월 8개 시도부터(종합)

# 특정기사 본문 저장하기
for i in soup.find_all('p') :
    f.write(i.text+'\n')
f.close()