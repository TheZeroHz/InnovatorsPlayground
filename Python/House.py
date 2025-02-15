from turtle import *
bgcolor('lightblue')

sides=4
angle=360/sides
pixel=200


color('brown')
begin_fill()
for i in range(sides):
  forward(pixel)
  left(angle)
end_fill()

penup()
goto(80,0)
pendown()

color('yellow')
begin_fill()
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)
end_fill()

penup()
goto(0,200)
pendown()

sides=3
angle=360/sides
pixel=200


color('green')
begin_fill()
for i in range(sides):
  forward(pixel)
  left(angle)
end_fill()

color('yellow')
penup()
goto(-200,200)
pendown()
begin_fill()
circle(50)
end_fill()



color('green')
penup()
goto(-500,0)
pendown()
begin_fill()
forward(1000)
right(90)
forward(1000)
right(90)
forward(1000)
right(90)
forward(1000)
right(90)
end_fill()






