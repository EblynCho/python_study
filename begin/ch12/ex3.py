# python 은 오버로딩 안됨

class Car :
    color = ''
    speed = 0

    def __init__(self, var1, var2):
        self.color = var1
        self.speed = var2

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

myCar3 = Car('orange', 50)

print('자동차3의 색상은 %s이며 현재 속도는 %dkm입니다.' % (myCar3.color, myCar3.speed))