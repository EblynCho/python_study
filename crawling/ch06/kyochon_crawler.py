# kyochon_crawler.py : 교촌 매장 정보 크롤링

from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime, time

from selenium import webdriver


def kyochon_store(result) :

    for option1 in range(1, 18) :
        for option2 in range(1, 45) :
            kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (option1, option2)
            wd = webdriver.Chrome('./WebDriver/chromedriver.exe')
            try :
                # print(kyochon_url)
                # html = urllib.request.urlopen(kyochon_url)
                wd.get(kyochon_url)
                # time.sleep(1)

                html = wd.page_source
                soupKyochon = bs(html, 'html.parser')

                ul_tag = soupKyochon.find('ul')
                store_list = soupKyochon.select('div.shopSchList > ul > li > a > span')

                for i in store_list :
                    store_name = i.find('strong').get_text()
                    store_address = i.find('em').get_text().strip().split('\r')[0]
                    store_sido_gu = store_address.split()[:2]
                    # print('%s %s %s' % (store_name, store_address, store_sido_gu))
                    result.append([store_name] + [store_sido_gu] + [store_address])
                    # print('%s' % store_name)
            except :
                break
    return


def main() :
    result = []
    print('Kyochon store')
    kyochon_store(result)
    kc_tbl = pd.DataFrame(result, columns=('store', 'sido_gu', 'address'))
    kc_tbl.to_csv('./data/kyochon_store.csv', encoding='cp949', mode='w', index=True)
    print('완료')


if __name__ == '__main__':
    main()