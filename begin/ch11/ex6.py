
inFp, outFp = None, None
inStr = ''

inFp = open('C:/temp/aaa.jpg', 'rb')  # rb : binary 로 읽어옴
outFp = open('C:/temp/bbb.jpg', 'wb')

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print('---이전 파일이 정상적으로 복사되었습니다.---')