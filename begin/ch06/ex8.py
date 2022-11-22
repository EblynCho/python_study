ch = ""
a, b = 0, 0
mathE = 0

while True :
    a = input("계산할 첫 번째 수를 입력하세요 : ")
    b = input("계산할 두 번째 수를 입력하세요 : ")
    ch = input("계산할 연산자를 입력하세요(+ - * / % // **)")

    mathE = eval(a+ch+b)
    print(mathE)