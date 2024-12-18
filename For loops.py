#For loop programme using the turtle module
#User will be asked to insert many sides the object will have 
#Their object of choice will be drawn 
#add nested loop to draw smaller version of object inside original one.

#import turtle module
import turtle

#user input 
turns=int(input("How many side would you like you object to have?"))
colour=str(input("What colour would you like?"))

#for loop

for turn in range (turns):
    turtle.color(colour)
    turtle.forward(50)
    turtle.right(360/turns)
    for turn in range(turns):
        turtle.color("red")
        turtle.forward(10)
        turtle.right(360/turns)


    
