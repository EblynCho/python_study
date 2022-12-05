# ex3.py

import os, re
import usecsv as uc

os.chdir(r'.\data')

apt = uc.switch(uc.opencsv('apt_202211.csv'))

new_list = []
for i in apt :
    try :
        # 부산에 크기는 150 넘거나 5억 이상 리스트 저장
        if (i[5] >= 150 or i[-7] >= 50000) and re.match('부산', i[0]):
            # print(i[0], i[4], i[-4], i[-7])
            new_list.append([i[0], i[4], i[-4]])
    except :
        pass

print(len(new_list))
uc.writecsv('over150+high50000.csv', new_list)