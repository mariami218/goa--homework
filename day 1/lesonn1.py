from turtle import*


#we want to paint a house
speed(7)
width(10)
#step 1: draw a square
color("brown")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#we are making windows
penup()
goto(20,180) 
pendown()
color("white")
left(120)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(40)

#we are making second window

penup()
goto(140,180)
pendown()
forward(40)
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(40)


exitonclick()

