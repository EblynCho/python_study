# ex1.py

import numpy as np

# print(np.__version__)

ar1 = np.array([1, 2, 3, 4, 5])
# print(ar1)  # [1 2 3 4 5]
# print(type(ar1))  # <class 'numpy.ndarray'>

ar2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(ar2)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

ar3 = np.arange(1, 11, 2)  # 1 ~ 11 까지 증가값이 2
# print(ar3)  # [1 3 5 7 9]

ar4 = np.arange(1, 31, 3)  # 자동으로 리스트 값이 됨
# print(ar4)
# [ 1  4  7 10 13 16 19 22 25 28]

ar5 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))  # 3행 2열
# print(ar5)
# [[1 2]
#  [3 4]
#  [5 6]]

ar6 = np.zeros((2, 3))  # 2행 3열, 모두 0 값 리턴
# print(ar6)
# [[0. 0. 0.]
#  [0. 0. 0.]]

ar7 = np.array([[10, 20, 30], [40, 50, 60]])
ar8 = ar7[0:2, 0:2]  # 0 : index 번호, 2 : 개수
# print(ar8)
# [[10 20]
#  [40 50]]

ar9 = ar7[0:]
# print(ar9)
# [[10 20 30]
#  [40 50 60]]

ar10 = ar7[0, :]
# print(ar10)  # [10 20 30]


ar11 = np.array(([1, 2, 3, 4, 5]))
arr12 = ar11 + 10
# print(arr12)  # [11 12 13 14 15]
ar13 = ar11 + arr12
# print(ar13)  # [12 14 16 18 20]

ar14 = ar13 * 2
print(ar14)  # [24 28 32 36 40]