#ex2.py
# ord : 유니코드 값으로 변환

a = ord('a')
# print(a)

a = ord('A')  #65
# print(a)

mask = 0x0F  #15
# print(mask)

# %x : 16진수, %o : 8진수
print("%x & %x = %x" %(a, mask, a & mask))
print("%X & %X = %X" %(a, mask, a | mask))

mask = ord('a') - ord('A')
# print(mask)

b = a ^ mask
# %c : 글자
print("%c ^ %d = %c" % (a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))

