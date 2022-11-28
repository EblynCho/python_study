'''
파일명 : ex2.py
개발자 : EblynCho
'''

# ss = input('입력 문자열 ==> ')
# print('출력 문자열 ==> ', end='')
#
# if ss.startswith('(') == False :  # ss 시작에 (없으면 추가됨
#     print('(', end='')
#
# print(ss, end='')
#
# if ss.endswith(')') == False :
#     print(')', end='')

inStr = '       한글 Python 프로그래밍    '
outStr = ''  # inStr에 공백문자를 제거하고 리턴

# outStr = inStr.replace(" ", "")

for i in range(0, len(inStr)) :
    if inStr[i] != ' ' :
        outStr += inStr[i]

print("원래 문자열 ==> " + '[' + inStr + ']')
print("공백 삭제 문자열 ==> " + '[' + outStr + ']')

inStr = 'Live as if you will die today.'

print(inStr.replace('i', '$'))  # L$ve as $f you w$ll d$e today.