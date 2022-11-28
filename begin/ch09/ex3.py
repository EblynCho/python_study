# ex3.py

def func1() :
    a = 10
    print('func1()에서 a 값 %d' %a)

def func2() :
    print('func2()에서 a 값 %d' % a)

a = 20  # 전역변수 : 함수 밑에서 선언해도 ok

func1()
func2()

def func3() :
    global b  # 전역변수
    b = 10
    print('func3()에서 b 값 %d' % b)

def func4():
    print('func4()에서 b 값 %d' % b)

func3()
func4()