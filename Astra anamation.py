import turtle
import math
import time
import random
window = turtle.Screen()
window.bgcolor("black")
window.tracer(0)
pen = turtle.Turtle()
pen.color("gold")

def star():
    pen.begin_fill()
    for side in range(5):
        pen.forward(10)
        pen.right(144)
    pen.end_fill()
for starr in range(100):
    pen.penup()
    pen.goto(random.randint(-400,400),random.randint(-400,400))
    pen.pendown()
    star()

sun = turtle.Turtle()
sun.color("yellow")
sun.dot(60)
def animateSun(x,y,step,Dot, size):
    Dot.penup()
    suncor=[sun.xcor(),sun.ycor()]
    sunfuturecor=[x,y]
    step=step
    xgo = 0
    ygo = 0

    xgo = sunfuturecor[0] - suncor[0]
    xgo = xgo/step
    print(xgo)
    ygo = sunfuturecor[1] - suncor[1]
    ygo = ygo/step
    print(ygo)
    for frame in range(step):
        Dot.clear()
        Dot.sety(Dot.ycor()+ygo)

        Dot.setx(Dot.xcor()+xgo)
        Dot.dot(size)
        window.update()
        time.sleep(0.1)
posesforsun = [[20,0,2],[-20,0,2],[20,0,2],[-20,0,2],[20,0,2],[-20,0,2],[20,0,2],[-20,0,2],[20,0,2],[400,400,10],[-400,400,10],[390,390,7],[-280,-280,6],[270,270,5],[-260,-260,4],[250,250,4],[-240,-240,4],[200,200,6],[-160,-160,6],[140,140,6],[-120,-120,6],[-80,-80,8],[40,40,10],[-20,-20,12],[0,0,7]]
for i in range(len(posesforsun)):
    animateSun(posesforsun[i][0],posesforsun[i][1],posesforsun[i][2],sun,60)

window.update()
turtle.done()