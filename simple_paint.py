from turtle import *
from random import randint
from time import sleep

t1 = Turtle(shape="turtle")
t1.color("red")
t1.pensize(3)
t1.right(120)

t2 = Turtle(shape="turtle")
t2.color("green")
t2.pensize(3)
t2.left(120)


t3 = Turtle(shape="turtle")
t3.pensize(3)
t3.color("blue")

def catch1(x, y):
    t1.penup()
    t1.goto(randint(-100, 100), randint(-100, 100))
    t1.pendown()
    t1.left(randint(0, 100))
t1.onclick(catch1)

def catch2(x, y):
    t2.penup()
    t2.goto(randint(-100, 100), randint(-100, 100))
    t2.pendown()
    t2.left(randint(0, 100))
t2.onclick(catch2)

def catch3(x, y):
    t3.penup()
    t3.goto(randint(-100, 100), randint(-100, 100))
    t3.pendown()
    t3.left(randint(0, 100))
t3.onclick(catch3)

x = 200
y = 200

def game_finfshed(t1, t2, t3):
    t1_outside = abs(t1.xcor()) > x or abs(t1.ycor()) > y
    t2_outside = abs(t2.xcor()) > x or abs(t2.ycor()) > y
    t3_outside = abs(t3.xcor()) > x or abs(t3.ycor()) > y
    is_outside = t1_outside or t2_outside or t3_outside
    return is_outside

while not game_finfshed(t1, t2, t3):
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)
t2.write("Good Bye!", font=("Arial", 14, "normal"))
