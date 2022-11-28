import turtle
import random

# 전역변수 선언
myTurtle, tx, ty, tColor, tSize, tShape = [None] * 6
# print(myTurtle)  #None
shapeList = []
playerTurtle = []
swidth, sheight = 500, 500

# 메인 코드
if __name__ == '__main__' :
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)

    shapeList = turtle.getshapes()
    # print(shapeList)  #['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
    for i in range(1, 100) :
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle(shapeList[0])
        tx = random.randrange(-swidth / 2, swidth / 2)
        ty = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random();
        tSize = random.randrange(1, 3)
        playerTurtle.append([myTurtle, tx, ty, tSize, r, g, b])  # List append


    # print(playerTurtle)

    for tList in playerTurtle :
        myTurtle = tList[0]
        myTurtle.color(tList[4], tList[5], tList[6])
        myTurtle.pencolor(tList[4], tList[5], tList[6])
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])

    turtle.done()