import math
import turtle
t = turtle.Turtle()
t.left(90)
t.penup()
t.setpos(0,-70)
t.pendown()
#the print statements and junk var with input are to step through the code and understand whats going on
#you can delete them or just skip through them
def tree(trunk_length, height):
    t.forward(trunk_length)
    #base case
    if height < 1:
        print(height)
        return None

    if height > 1:
        t.left(45)
        print(height)
        junk = input("left")
        tree(trunk_length * .5, height -1)
        t.right(90)
        print(height)
        junk = input("right")
        tree(trunk_length *.5, height - 1)
        t.left(45)
    t.backward(trunk_length)
    print(height)
    junk = input('end')




    #have one turtle create the trunk
  #have the same turtle create a branch on either side
  #have a seperate turtle begin at where the trunk ends so it can create the second branch
  #at the end, the turtles will continue to branch off and make smaller branches until it is ordered to stop
  #maybe have more turtles grow? not sure if that would be too much

