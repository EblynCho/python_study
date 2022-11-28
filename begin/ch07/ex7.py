# 딕셔너리 : key 와 value 쌍으로 구성

dic1 = {1 : 'a', 2 : 'b', 3 : 'c'}
print(dic1)

student1 = {'학번' : 1000, '이름' : '홍길동', '학과' : '컴퓨터학과'} # 타입이 일치하지 않아도 됨(숫자형, 문자형)
print(student1)
student1['연락처'] = '010-8888-9999'
print(student1)
student1['학과'] = '파이썬학과'  #수정
print(student1)
del(student1['학과'])  # 삭제
print(student1)

print(student1.get('학과'))  # 값 찾을때 get()
print(student1.get('연락처'))
print(student1.keys())  # key 값 리턴