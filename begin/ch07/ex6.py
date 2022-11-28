tt1 = (10, 20, 30, 40)
print(tt1[0])
print(tt1[1])
print(tt1[2])
print(tt1[3])

print(tt1[1:3])
print(tt1[1:])
print(tt1[:3])

tt2 = ('A', 'B')
print(tt1 + tt2)
print(tt2 * 3)

print()

tt3 = ((1, 2, 3),
       (4, 5, 6),
       (7, 8, 9))
for i in tt3 :
    print(i)

print()

# 튜플 -> 리스트
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
for i in myList :
    print(i)

myTuple = tuple(myList)
for i in myTuple :
    print(i)