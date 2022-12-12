# ex3.py : chromedriver.exe을 지정한 위치에 저장

from selenium import webdriver

wd = webdriver.Chrome('./WebDriver/chromedriver.exe')

wd.get('https://www.hanbit.co.kr/')  # 켰다가 꺼짐 -> 정상 실행
