#ex7.py

ch = ""
a, b = 0, 0

while True :
    a = int(input("계산할 첫 번째 수를 입력하세요 : "))
    b = int(input("계산할 두 번째 수를 입력하세요 : "))
    ch = input("계산할 연산자를 입력하세요(+ - * / % // **)")

    if ch == "+" :
        result = a + b
    elif ch == "-" :
        result = a - b
    elif ch == "*" :
        result = a * b
    elif ch == "/" :
        result = a / b
    elif ch == "%" :
        result = a % b
    elif ch == "//" :
        result = a // b
    elif ch == "**" :
        result = a ** b

    print("%d %s %d = %d" %(a, ch, b, result))