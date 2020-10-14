from turtle import *
import math
# x,y:=coordinate
# r:=The length of one side of the star
# s:=pensize pc:=pencolor fc:=fillcolor
def draw_star(x = 0, y = 0, r = 300,s = 3, pc = 'yellow', fc = 'orange'):
    pensize(s)
    pencolor(pc)
    fillcolor(fc)
    speed(8)
    bgcolor('black')
    penup()
    setposition(-r/2 + x, r/2*tan(pi/10) + y)
    pendown()
    begin_fill()
    n = 5
    for i in range(n):
        forward(r)
        right(144)
    penup()
    end_fill()
    setposition(0,0)

draw_star(-300,300,100)
draw_star(400,200,150)
draw_star(200,-300,180)
draw_star()
done()
