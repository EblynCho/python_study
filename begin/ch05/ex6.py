select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

## 메인 코드 부분 ##
select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if select == 1 :
    cal = input("*** 수식을 입력하세요 : ")
    result = eval(cal)
    print("%s 결과는 %.1f" %(cal, result))
# elif select == 2 :
#     a = int(input("*** 첫 번째 숫자를 입력하세요 : "))
#     b = int(input("*** 두 번째 숫자를 입력하세요 : "))
#     if a >= b :
#         result = (a-b+1) * (a+b)/2
#         print("%d +...+ %d 는 %d 입니다" %(b, a, result))
#
#     else :
#         result = (b - a + 1) * (a + b) / 2
#         print("%d +...+ %d 는 %d 입니다" % (a, b, result))

elif select == 2 :
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))
    for i in range (num1, num2 + 1) :
        answer = answer + 1
    print("%d +...+ %d 는 %d 입니다" % (num1, num2, answer))
else :
    print("1또는 2만 입력해야 합니다.")