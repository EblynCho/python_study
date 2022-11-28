aa = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

for i in range (0, 3) :
    for j in range (0, 3) :
        print(aa[i][j], end=" ") # print 기본으로 한줄 띄움, end=" " : 한줄 띄우지 않고 한칸 띄우기
    print()

print()

list1 = []
list2 = []
value = 1
for i in range (0, 3) :
    for j in range (0, 4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []  # 초기화해서 다시 값 넣을 수 있음

for i in range (0, 3) :
    for j in range (0, 4) :
        print("%3d" % list2[i][j], end=" ")
    print()

