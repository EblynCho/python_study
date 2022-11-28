import operator

trainDic, trainList = {}, []

trainDic = {'Thomas':'토마스', 'Edward':'에드워드', 'Henry':'헨리', 'Gothen':'고든', 'James':'제임스'}
print(trainDic)
trainList = sorted(trainDic.items(), key=operator.itemgetter(0))
print(trainList)
trainList = sorted(trainDic.items(), key=operator.itemgetter(1))
print(trainList)

print('--------------------------------------')

foods = {"떡볶이":"오뎅",
            "짜장면":"단무지",
            "라면":"김치",
            "피자":"피클",
            "맥주":"땅콩",
            "치킨":"치킨무",
            "삼겹살":"상추" }

while True :
    myFood = input(str(list(foods.keys())) + " 중 좋아하는 음식은? ")  # key 값 들만 리스트로 변환해서 출력
    if myFood in foods :
        print('<%s> 궁합 음식은 <%s> 입니다.' % (myFood, foods.get(myFood)))
    elif myFood == '끝' :
        break
    else :
        print('그런 음식이 없습니다. 확인해 보세요')