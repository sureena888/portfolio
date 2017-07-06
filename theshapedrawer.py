from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.


### Write your code below:

color = input("Enter a color: ")
pencolor(color)

t.penup()
setup(500,500)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

hipposwagamus = input("Hey big fella, How many sides do you want?")

fillcolor(color)
begin_fill()
for num in range(int(hipposwagamus)):
    t.pendown()
    forward(100)
    right(360 / int(hipposwagamus))
end_fill()







# Close window on click.
exitonclick()
