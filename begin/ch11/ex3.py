
outFp = None
outStr = ''

outFp = open('C:/temp/data1.txt', 'w')  # 파일 w 이기 때문에 만들어짐

while True :
    outStr = input('내용입력 : ')
    if outStr != '' :
        outFp.write(outStr + '\n')
    else :
        break

outFp.close()
print('---파일에 정상적으로 써졌음---')