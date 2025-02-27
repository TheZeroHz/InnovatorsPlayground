from turtle import *
## Draw Ukrane Flag Using Loop // Ctrl+C=Copy   Ctrl+V=Paste 
##range(start->d0,end, inc/dec->d1)
fillcolor('yellow')
begin_fill()
for i in range(4):
    if i==0 or i==2:
        forward(350)
        left(90)
    else:
        forward(100)
        left(90)
end_fill()

penup()
goto(0,100)
pendown()

fillcolor('blue')
begin_fill()
for i in range(4):
    if i==0 or i==2:
        forward(350)
        left(90)
    else:
        forward(100)
        left(90)
end_fill()

