from turtle import *

t = Turtle(shape="circle")
t.color("blue")
t.pensize(3)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()

def set_red():
    t.color("red")
def set_green():
    t.color("green")
def set_blue():
    t.color('blue')
def set_white():
    t.color('white')
#------------------
def pen_size_50():
    t.pensize(50)
def pen_size_10():
    t.pensize(10)
def pen_size_3():
    t.pensize(3)
speed = 10
def step_up():
    t.goto(t.xcor(), t.ycor() + speed)
def step_down():
    t.goto(t.xcor(), t.ycor() - speed)
def step_left():
    t.goto(t.xcor() - speed, t.ycor())
def step_right():
    t.goto(t.xcor() + speed, t.ycor())

def begin():
    t.begin_fill()
def end():
    t.end_fill()
t.ondrag(draw)

scr = t.getscreen()
scr.listen()
scr.onkey(step_up, 'w')
scr.onkey(step_down, 's')
scr.onkey(step_left, 'a')
scr.onkey(step_right, 'd')

scr.onkey(begin, 'z')
scr.onkey(end, 'x')

scr.onkey(set_red, '1')
scr.onkey(set_green, '2')
scr.onkey(set_blue, '3')
scr.onkey(set_white, '4')
scr.onkey(pen_size_50, 'u')
scr.onkey(pen_size_10, 'i')
scr.onkey(pen_size_3, 'p')

scr.onscreenclick(move)
