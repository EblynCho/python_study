#ex3.py

# 1~100 사이의 값들 중 짝수는 aa, 홀수는 bb에 저장

aa = []
bb = []

for i in range(0, 101, 2) :
    aa.append(i)
for i in range(1, 100, 2) :
    bb.append(i)

print(aa)
print(bb)