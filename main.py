#!/bin/python3
######################################################
# Project: Project 2
# UIN: 654135206
# repl.it URL: https://trinket.io/library/trinkets/62eeab4a0d
######################################################

#imports
import turtle 
import random
import math

#all the turtles
net = turtle.Turtle()
z = turtle.Turtle()
rock = turtle.Turtle()
rock_1 = turtle.Turtle()
fish_1 = turtle.Turtle()
fish_2 = turtle.Turtle()
crab = turtle.Turtle()


#adding turtles to screen 
a = turtle.Screen()
a = net.getscreen()
a = z.getscreen()
a = rock.getscreen()
a = rock_1.getscreen()
a = fish_1.getscreen()
a = fish_2.getscreen()
a = crab.getscreen()

#screen
a_width = 500
a_height = 500
a.setup(width = a_width, height = a_height)
a.bgpic('Background.jpg')


 #adding images to turtles
a.addshape("net.png")
a.addshape("Rock.png")
a.addshape("Fish_1.png")
a.addshape("Fish_2.png")
a.addshape("Background.jpg")
a.addshape("Crab.png")


#hiding all turtles as well as penup
net.hideturtle()
net.penup()

z.hideturtle()
z.penup()

rock.hideturtle()
rock.penup()

rock_1.hideturtle()
rock_1.penup()


fish_1.hideturtle()
fish_1.penup()

fish_2.hideturtle()
fish_2.penup()

crab.hideturtle()
crab.penup()


r = 20 
y =  -(a_width/2 - r)


#assign all images to turtles
z.color("yellow")

net.goto(y,0)
net.tracer(0)
net.showturtle()
net.shape("net.png")

r_2 = 20
rock.showturtle()
rock.left(90)
rock.shape("Rock.png")
rock.goto(-90,100)

rock_1.showturtle()
rock_1.left(90)
rock_1.shape("Rock.png")
rock_1.goto(190,-100)

fish_1.showturtle()
fish_1.left(90)
fish_1.shape("Fish_1.png")
fish_1.goto(0,48)

fish_2.showturtle()
fish_2.left(90)
fish_2.shape("Fish_2.png")
fish_2.goto(-170,200)

crab.showturtle()
crab.left(90)
crab.shape("Crab.png")
crab.goto(90,-243)



#function that moves turtle up
def up():
  #print("starting up")
  net.clear()
  current_y = net.ycor()
  new_y = current_y + 10 
  net.sety(new_y)
  #net.dot(r)
  net.update()


#function that moves turtle down
def down():
  #print("starting up")
  net.clear()
  current_y = net.ycor()
  new_y = current_y - 10
  net.sety(new_y)
  #net.dot(r)
  net.update()
  
  
#function to check if turtles collide
def are_colliding(obj_1, obj_2,radius1,radius2):
  
  #TODO: implement collision detection 
  # https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection 
  X = obj_1.xcor() - obj_2.xcor()
  Y = obj_1.ycor() - obj_2.ycor()
  distance = math.sqrt(X*X + Y*Y)
  #print(distance)
  #print (radius1 + radius2)
  if distance < radius1 + radius2:
   collision_detected = True
   obj_2.setx(a_height/2 +(r_2/2))
   obj_2.sety(random.randint(-a_height/2, a_height/2))
   
  else:
    collision_detected = False
    
  return collision_detected


#main part of the code
def main():
  
  #assigning keys to the functions
  a.onkey(up,"up")
  a.onkey(down,"down") 
  a.listen()
  
  
  #main game function
  lives = 3
  score = 0
  while lives != 0:
    
    z.clear()
    z.goto(170,220)
    z.write(("Score",score), move=False, align='centre', font=('Arial', 10, 'normal'))
    z.goto(-220,220)
    z.write(("Lives",lives), move=False, align='centre', font=('Arial', 10, 'normal'))
    
    rock.clear()
    rock_1.clear()
    fish_1.clear()
    fish_2.clear()
    crab.clear()
    
  
    #value 
    rock.setx(rock.xcor() - 3) 
    
    rock_1.setx(rock_1.xcor() - 3)
    
    fish_1.setx(fish_1.xcor() - 2) 
    
    fish_2.setx(fish_2.xcor() - 2) 
    
    crab.setx(crab.xcor() - 2) 
  
    
    #conditiom
    if ((-rock.xcor()-(r_2) ) >= a_width/2):
      rock.setx(a_height/2 +(r_2/2))
      rock.sety(random.randint(-a_height/2, a_height/2))
      
    if ((-fish_1.xcor()-(r_2) ) >= a_width/2):
      fish_1.setx(a_height/2 +(r_2/2))
      fish_1.sety(random.randint(-a_height/2, a_height/2))  
      
    if ((-rock_1.xcor()-(r_2) ) >= a_width/2):
      rock_1.setx(a_height/2 +(r_2/2))
      rock_1.sety(random.randint(-a_height/2, a_height/2))
      
    if ((-fish_2.xcor()-(r_2) ) >= a_width/2):
      fish_2.setx(a_height/2 +(r_2/2))
      fish_2.sety(random.randint(-a_height/2, a_height/2))  
    
    if ((-crab.xcor()-(r_2) ) >= a_width/2):
      crab.setx(a_height/2 +(r_2/2))
      crab.sety(random.randint(-a_height/2, a_height/2))    
    
   
   
    harm = are_colliding(net,rock,r/2,r_2/2)
    harm_1 = are_colliding(net,rock_1,r/2,r_2/2)
    
    
    add = are_colliding(net,fish_1,r/2,r_2/2)
    add_1 = are_colliding(net,fish_2,r/2,r_2/2)
    add_2 = are_colliding(net,crab,r/2,r_2/2)
    
    if harm or harm_1:
      lives = lives - 1
    
    if add or add_1 or add_2:
      score = score + 10
    
      
    rock.update()
    rock_1.update()
    fish_1.update()
    fish_2.update()
    crab.update()
    
  
  z.clear()
  
  
  z.color("red")
  z.goto(-200,0)
  z.write(" Game Over",move=True, align='centre', font=('Arial', 50, 'bold'))
  z.goto(-150,-70)
  z.color("yellow")
  z.write(("Lives " + str(lives) + " Score " + str(score)),move=True, align='centre', font=('Arial', 25, 'bold'))
  
  rock.update()
  rock_1.update()
  fish_1.update()
  fish_2.update()
  crab.update()
  
  
main()