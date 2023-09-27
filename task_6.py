from turtle import *

def task_6():
    # speed(-1)
    left(90)
    for x in range(4):
        forward(160)
        right(150)
        forward(160)
        right(30)
    pu() #перо вниз
    for x in range(7):
        for y in range(7):
            goto(x*20, y*20)
            dot(5)
            y *= -1
            goto(x*20, y*20)
            dot(5)
    done()

task_6()