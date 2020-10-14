from turtle import *
import math
# r:=The length of one side of the star
# s:=pensize pc:=pencolor fc:=fillcolor
def draw_star(r = 300,s = 3, pc = 'yellow', fc = 'orange'):
    pensize(s)
    pencolor(pc)
    fillcolor(fc)
    penup()
    setposition(-r/2,r/2*tan(pi/10))
    pendown()
    begin_fill()
    n = 5
    for i in range(n):
        forward(r)
        right(144)
    penup()
    end_fill()
    setposition(0,0)

draw_star()
done()
