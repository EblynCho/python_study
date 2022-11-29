
# python 특징 : 변수 타입이 없고 중괄호 대신 : 사용

class Car :
    color = ''
    speed = 0

    ###################### 생성자
    def __init__(self):
        self.color = 'white'
        self.speed = 10

    # error : Python 은 오버로딩 안됨
    # def __init__(self, var1, var2):
    #     self.speed = var1
    #     self.color = var2

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0 :
            self.speed = 0

###################### Class 생성

myCar1 = Car()
myCar1.color = 'red'
# myCar1.speed = 0

myCar2 = Car()
myCar2.color = 'blue'
# myCar2.speed = 0
myCar2.upSpeed(30)

# myCar3 = Car('orange', 50)

print('자동차1의 색상은 %s이며 현재 속도는 %dkm입니다.' % (myCar1.color, myCar1.speed))
print('자동차2의 색상은 %s이며 현재 속도는 %dkm입니다.' % (myCar2.color, myCar2.speed))
# print('자동차3의 색상은 %s이며 현재 속도는 %dkm입니다.' % (myCar3.color, myCar3.speed))