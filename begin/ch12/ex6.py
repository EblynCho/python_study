
class Line :

    length = 0

    def __init__(self, length):
        self.length = length
        print(self.length, '길이의 선이 생성 되었습니다.')

    def __del__(self):  # 삭제하면 호출되는 메서드
        print(self.length, '길이의 선이 제거 되었습니다.')

    def __repr__(self):  # print 호출 시
        return '선의 길이 : ' + str(self.length)

    def __add__(self, other):
        return  self.length + other.length

    def __lt__(self, other):
        return self.length < other.length

    def __eq__(self, other):
        return self.length == other.length


myLine1 = Line(100)
myLine2 = Line(200)

print(myLine1)

print('두 선의 길이 합 : ', myLine1 + myLine2)

if myLine1 < myLine2 :
    print('myLine2가 더 기네요')
elif myLine1 == myLine2 :
    print(' 두개의 선이 같네요')
else:
    print('모르겠습니다.')

del (myLine1)