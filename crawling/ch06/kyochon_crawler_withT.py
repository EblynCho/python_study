# kyochon_crawler.py : 교촌 매장 정보 크롤링

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime, time
from itertools import count

import ssl  # 접속 보안 허용

def get_request_url(url, enc='utf-8') :
    req = urllib.request.Request(url)
    try :
        # [SSL: CERTIFICATE_VERIFY_FAILED] 에러 뜰때
        ssl._create_default_https_context = ssl._create_unverified_context  # 접속 보안 허용
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            try :
                rcv = response.read()
                ret = rcv.decode(enc)  # 한글로 변환
            except UnicodeDecodeError :
                ret = rcv.decode(enc, 'replace')  # replace : 에러 발생 시 ? 로 변환
            return ret

    except Exception as e :
        print(e)
        print('[%s] Error for URL : %s' % (datetime.datetime.now(), url))
        return None

def getKyochonAddress(sido1, result) :
    for sido2 in count() :  # count -> 순차적으로 값을 만들어줌 (range 와 상관없이), 나중에 break 설정
        url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (str(sido1), str(sido2))
        # print(url)
        try :
            rcv_data = get_request_url(url)
            soupData = BeautifulSoup(rcv_data, 'html.parser')
            ul_tag = soupData.find('ul', attrs={'class':'list'})
            # print(ul_tag)
            for store_data in ul_tag.find_all('a', href=True) :
                store_name = store_data.find('strong').get_text()
                # print(store_name)
                store_address = store_data.find('em').get_text().strip().split('\r')[0]
                store_sido_gu = store_address.split()[0:2]
                # print(store_address)
                result.append([store_name] + store_sido_gu + [store_address])
        except :
            break
    return

def cswin_Kyochon() :
    result = []
    print('Kyochon Address Crawling Start')
    for sido1 in range (1, 18) :
        getKyochonAddress(sido1, result)
    kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    kyochon_table.to_csv('./data/kyochon.csv', encoding='cp949', mode='w', index=True)
    del result[:]
    print('끝')

if __name__ == '__main__' :
    cswin_Kyochon()