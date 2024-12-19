#programe based on while loops 
#user gets prompted to specify the line length,colour and angle 
#Use the turtle module to draw the line 
#Allow user to specify new lines until they enter length of zero
#When user enters line length of 0, stop programme

#import module 
import turtle

#initialize variable 
line_length=0
colour= ""
angle=0
#user input
colour= str(input("What colour would like your line to be? ")) 
line_length=int(input("What length would you like your line to be? "))
angle=int(input("What angle would like to see (e.g. 360/4=90 degerees, so 4=90 degrees)? "))

#while loop

while line_length != 0:

    turtle.color(colour)
    turtle.forward(line_length)
    turtle.right(360/angle)
