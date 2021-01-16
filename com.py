import turtle


##from playsound import playsound
##playsound('l.mp3')
import pygame

pygame.mixer.init()
pygame.mixer.music.load('l.mp3')
pygame.mixer.music.play(1)

s=turtle.getscreen() #used for screen
t=turtle.Turtle() #used for turtle
t1=turtle.Turtle()
turtle.title("My First turtle program")
import time
s.bgcolor("white")
t.penup()
t.goto(-300,-100)
t.pendown()
t.pencolor("pink")
t.fillcolor("blue4")
t.begin_fill()
t.right(45)
t.forward(70)
t.right(135)
t.forward(100)
t.right(135)
t.forward(72)

t.hideturtle()

t.right(45)
t.forward(130)
t.right(45)
t.forward(60)
t.right(45)
t.forward(59)
t.right(90)

t.forward(225)
t.right(90)

t.forward(52)
t.right(91)
t.penup()
t.forward(100)
t.pendown()
t.right(90)
t.forward(54)
t.end_fill()
t.penup()
t.right(90)
t.forward(40)
t.right(90)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.penup()
t.end_fill()
t.begin_fill()
t.left(135)
t.forward(30)
t.end_fill()
t.pendown()
t.pencolor("yellow")
t.dot(5)
t.end_fill()

import random

t = turtle.Turtle()
t.speed(0)

#firework color
def pen(color):
    t.color(color)

pen('red')

def movement():
    t.pu()
    x = random.randint(-300,300)
    y = random.randint(0,300)
    t.goto(x,y)
    t.pd()



def fire(size):
    for num in range (20):
         t.fd(size)
         t.rt(180-(360/20))
s.bgpic("night.png")
fire(50)
movement()
pen('gold')
fire(75)
movement()

pen('orange')
fire(199)   
fire(50)
movement()

pen('blue')
fire(75)
movement()

pen('pink')
fire(199)
fire(50)
movement()

pen('yellow')
fire(75)
movement()

pen('orange')
fire(199)   
fire(50)
movement()

pen('blue')
fire(75)
movement()

pen('gray')
fire(199)
fire(50)
movement()

pen('yellow')
fire(75)
movement()

pen('orange')
fire(170)   
fire(80)
movement()
pen('blue')
fire(75)
movement()

pen('HotPink')
fire(199)
fire(40)
movement()

pen('yellow')
fire(75)
movement()

pen('coral2')
fire(199)   
fire(50)
movement()

pen('blue')
fire(75)
movement()

pen('pink')
fire(199)  
movement()
t.pencolor("cyan")
t.pensize(7)
t.penup()
t.right(90)
t.goto(-200,-350)
t.pendown()
t.write("Happy Diwali",font=("Script",98,"bold"))

for i in range(900):
    print()


pygame.mixer.music.stop()
