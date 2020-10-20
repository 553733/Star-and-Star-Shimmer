import turtle as trtl

star = trtl.Turtle()

# defining some variables for later
# don't touch this stuff
point = 18
poi = 0

# edit these equally
topstar = 27
center = 0

uplx = -10
uply = 5
uprx = 5
upry = 9

botlx = -4
botly = -10
botrx = 6
botry = -6

# the actual star 
star.speed(0)
grr = 0
star.penup()
star.pencolor("goldenrod")
star.fillcolor("gold")
star.begin_fill()
star.goto(center,topstar)
star.setheading(-72)
star.pendown()
while grr < 5:
  star.forward(20)
  star.left(72)
  star.forward(20)
  star.right(144)
  grr += 1
star.end_fill()

# I'm impatient so I sped it up
star.speed(0)
star.goto(center,center)

# the lines in the middle of the star
star.pendown()
star.pensize(1)
star.pencolor("goldenrod") 
# if we don't like it we don't have to have the lines in the middle
while poi < 5:            
  star.setheading(point)
  star.forward(25)
  star.backward(25)
  point += 72
  poi += 1
  
# hide the turtle
star.hideturtle()

def outlines():
  grr = 0
  star.goto(center,center)
  star.setheading(90)
  star.pendown()
  star.pencolor("goldenrod")
  for i in range(5):
    star.forward(25)
    star.backward(25)
    star.left(72)
  star.penup()
  star.goto(0,27)
  star.setheading(-72)
  star.pendown()
  while grr < 5:
    star.forward(20)
    star.left(72)
    star.forward(20)
    star.right(144)
    grr += 1

def sparkle():
  star.setheading(0)
  star.pendown()
  for i in range(8):
    star.pencolor("white")
    star.forward(5)
    star.backward(5)
    star.left(45)
  star.penup()

def unsparkle():
  star.setheading(0)
  star.pendown()
  for i in range(8):
    star.pencolor("gold")
    star.forward(5)
    star.backward(5)
    star.left(45)
  star.penup()

# sparkles and someone help me reduce this
pika = 0
while pika < 1:
  star.pensize(1)
  star.penup()
  star.goto(uplx,uply)
  sparkle()
  star.goto(botlx,botly)
  sparkle()
  star.goto(uplx,uply)
  unsparkle()
  star.goto(uprx,upry)
  sparkle()
  star.goto(botlx,botly)
  unsparkle()
  star.goto(botrx,botry)
  sparkle()
  star.goto(uprx,upry)
  unsparkle()
  star.goto(botrx,botry)
  unsparkle()
  star.pensize(0.75)
  outlines()

  






wn = trtl.Screen()
wn.mainloop()