
class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        print('현재 속도(슈퍼클래스) : %d' % self.speed)

# 오버라이딩
class Sedan(Car) :
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
        print('현재 속도(서브 클래스) : %d' % self.speed)

# 오버라이딩 할 필요 없다면 pass
class Truck(Car) :
    pass

sedan1, truck1 = None, None

sedan1 = Sedan()
truck1 = Truck()

sedan1.upSpeed(200)
truck1.upSpeed(200)