# ex5.py

def para_func(*para) :  # 가변인수와 비슷
    result = 0
    for num in para :
        result += num
    return  result

hap = para_func(10, 20)
print('%d' % hap)
hap = para_func(10, 20, 30)
print('%d' % hap)
hap = para_func(10, 20, 30, 40)
print('%d' % hap)