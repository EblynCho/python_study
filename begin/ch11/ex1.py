
inFp = None
inStr = ''

inFp = open('C:/temp/data1.txt', 'r', encoding='utf-8')

# inStr = inFp.readline()
# print(inStr, end='')
#
# inStr = inFp.readline()
# print(inStr, end='')
#
# inStr = inFp.readline()
# print(inStr, end='')

# while True :
#     inStr = inFp.readline()
#     if inStr == '' :
#         break
#     print(inStr, end='')

inList = ''

inList = inFp.readlines()
# print(inList)

for str in inList :
    print(str, end='')

inFp.close()