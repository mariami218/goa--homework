from turtle import*

def drawMountains(pen):
  pen.penup()
  pen.goto(-200,80)
  pen.pendown()
  pen.color(5,114,3)
  pen.fillcolor(5,114,3)
  pen.begin_fill()
  for peak in range(1,11):
    pen.goto(-200+40*peak,"randint"(40,160))
  pen.goto(200,-200)
  pen.goto(-200,-200)
  pen.goto(-200,80)
  pen.end_fill()

def drawBattlements(pen,x,y,w,h):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(0,0,0)
  pen.fillcolor(150,150,150)
  pen.begin_fill()
  xEnd = x + w
  while x<xEnd:
    pen.goto(x,y)
    pen.goto(x,y+h)
    pen.goto(x+20,y+h)
    pen.goto(x+20,y)
    if x+20<xEnd:
      pen.goto(x+40,y)
    x=x+40
  pen.end_fill()  

def drawWall(pen,x,y,w,h,crenellation):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(0,0,0)
  pen.fillcolor(150,150,150)
  pen.begin_fill()
  pen.goto(x+w,y)
  pen.goto(x+w,y+h)
  pen.goto(x,y+h)
  pen.goto(x,y)
  pen.end_fill()
  pen.end_fill()
  if crenellation==True:
    drawBattlements(pen,x,y+h,w,20)
    
def drawRoof(pen,x,y,w,h):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(0,0,0)
  pen.fillcolor(200,20,20)
  pen.begin_fill()
  pen.goto(x,y)
  pen.goto(x+w//2,y+h)
  pen.goto(x+w,y)
  pen.goto(x,y)
  pen.end_fill()

def drawTower(pen,x,y,w,h,crenellation):
  drawWall(pen,x,y,w,h,False)
  if crenellation==True:
    drawWall(pen,x-20,y+h,w+40,40,True)
  else:
    drawRoof(pen,x-10,y+h,w+20,60)  

def drawDoor(pen,x,y,w,h):
  pen.penup()
  pen.goto(x-w//2,y)
  pen.pendown()
  pen.color(40,40,20)
  pen.fillcolor(40,40,20)
  pen.goto(x-w//2,y)
  pen.begin_fill()
  pen.goto(x-w//2,y+h-w//2)
  pen.goto(x+w//2,y+h-w//2)
  pen.goto(x+w//2,y)
  pen.goto(x-w//2,y)
  pen.goto(x,y+h-w)
  pen.end_fill()
  pen.begin_fill()  
  pen.circle(w//2)
  pen.end_fill()
  pen.color(0,0,0)
  pen.goto(x,y+h)
  pen.goto(x,y)
  
def drawLoophole(pen,x,y,w,h):
  pen.penup()
  pen.goto(x-w//2,y)
  pen.pendown()
  pen.color(0,0,0)
  pen.fillcolor(0,0,0)
  pen.goto(x,y)
  pen.begin_fill()
  pen.goto(x+w//2,y)
  pen.goto(x+w//2,y+h)
  pen.goto(x-w//2,y+h)
  pen.goto(x-w//2,y)
  pen.end_fill()
  
def drawFlag(pen,x,y,w,h,color):
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.color(0,0,0)
  pen.goto(x,y+h)
  pen.fillcolor(color)
  pen.begin_fill()
  pen.goto(x+w,y+h-10)
  pen.goto(x,y+h-20)
  pen.goto(x,y+h)
  pen.end_fill()

exitonclick()