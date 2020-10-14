from turtle import *

def tree(n):
    if n <= 1:
        forward(5)
    else:
        forward(5*(1.1**n))
        xx = pos()
        h = heading()
        left(30)

        tree(n-2)

        penup()
        setpos(xx)
        setheading(h)
        pendown()
        right(15)

        tree(n-1)

        penup()
        setpos(xx)
        setheading(h)
        pendown()

speed(0)

tree(12)
