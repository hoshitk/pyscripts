from turtle import *
import math
pensize(3)
pencolor('yellow')
fillcolor('orange')
r = 300
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
done()
