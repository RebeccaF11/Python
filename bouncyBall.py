import turtle
import time
import random
width=400
gravity = -1
window = turtle.Screen()
window.setup(400,400)
window.colormode(255)
window.tracer(0)
ball = turtle.Turtle()
ball.goto(0,0)
ball.hideturtle()
print(float(str(-100.33)[1:]))
ball.verspeed = -5
hight = 400
horizontalspeed = 3
wall = turtle.Turtle()
wall.penup()
wall.back(width/2)
wall.right(90)
wall.forward(hight/2+30)
wall.right(-90)
wall.pendown()
wall.forward(width+30)
ball.shape("circle")
def left():
    global horizontalspeed
    horizontalspeed = horizontalspeed + 1
def right():
    global horizontalspeed
    horizontalspeed = horizontalspeed - 1
def up():

    ball.verspeed = ball.verspeed -2
for i in range(2000):
    ball.sety(ball.ycor()-ball.verspeed)

    ball.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball.clear()
    ball.begin_fill()



    for side in range(5):
        ball.forward(40)
        ball.right(144)


    ball.end_fill()
    verspeed = verspeed-gravity
    if ball.ycor() < -hight/2:
        verspeed *= -0.2


    ball.setx(ball.xcor() + horizontalspeed)
    if ball.xcor()> width/2 or ball.xcor() < -width/2:
        horizontalspeed *= -0.2
    window.onkey(left,'Right')
    window.onkey(right,'Left')
    window.onkey(up, 'Up')
    window.listen()
    window.update()
    time.sleep(0.1)
turtle.done()