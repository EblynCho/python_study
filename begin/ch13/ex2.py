# ex2.py

import pymysql  # pip install pymysql

con, cur = None, None
data1, data2, data3, data4 = '', '', '', ''
sql = ''
row = None

con = pymysql.connect(host='localhost', user='root', password='1234', db='mydb', charset='utf8')
cur = con.cursor()

cur.execute('SELECT * FROM tblMember2')

print('사용자ID    사용자이름   이메일    출생년도')
print('-----------------------------------------------------------')

while True :
    row = cur.fetchone()  # 레코드 한줄 읽어옴
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print('%5s    %15s     %15s    %5s' % (data1, data2, data3, data4))

con.close()