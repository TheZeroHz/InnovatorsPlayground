from turtle import *
## Draw BD Flag Using Loop
##range(start->d0,end, inc/dec->d1)
fillcolor('green')
begin_fill()
for i in range(4):
    if i==0 or i==2:
        forward(350)
        left(90)
    else:
        forward(200)
        left(90)
end_fill()

penup()
goto(175,30)
pendown()
fillcolor('red')
begin_fill()
circle(70)
end_fill()
