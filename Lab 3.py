# Sindre C.J Eriksen SID: 20530556 
# fireworks

import random   # module providing the randint function
import time     # time module to delay after drawing five fireworks
import turtle   # turtle module for drawing fireworks

##### Initialize variables used in the program

# The following width and height match the GIF used by the program
screen_width, screen_height = 900, 564

firework_radius = 100   # The maximum radius a firework can have
firework_count = 20     # The number of fireworks to shoot

# A list of colours to choose from for a firework
firework_colours = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]


##### Initialize the turtle module

turtle.reset()                              # Reset the turtle
turtle.setup(screen_width, screen_height)   # Set the size of the screen
turtle.bgpic("hong_kong.gif")               # Put the background image on the
                                            # screen
turtle.width(2)                             # Draw lines with a width of two


##### For loop to shoot individual firework

for i in range(firework_count):
    # Clear the sky (screen) for every five fireworks
    if i > 0 and i % 5 == 0:
        time.sleep(1)
        turtle.clear()
    
#Setting the necessary variables to draw the line before each firework
starty = -282
startx = random.randint(-450,450)
destx = random.randint(-450,450)
desty = random.randint(0,282)
turtle.speed(6)

#Drawing the line before the firework
firework_size = random.randint(firework_radius/2, firework_radius)
explosion_directions = random.randint(10,20)
number_of_firework = random.randint(firework_count/2, firework_count)
colour = firework_colours[random.randint(0,6)]
dot_size = 2
radius = 10
turtle.hideturtle()

for _ in range(number_of_firework): # Loop for going to the start poisition, shooting the firework tail, and reset the variables
    turtle.tracer(True)
    turtle.up()
    turtle.goto(startx,starty)
    turtle.down()
    turtle.color("red")
    turtle.goto(destx, desty)
    turtle.tracer(False)
    turtle.clear()
    turtle.color(firework_colours[random.randint(0,6)])
    while radius <= firework_size: #Loop which controls, and draws the size of the explosion
        turtle.up()
        turtle.forward(radius)
        turtle.left(90)
        for _ in range(explosion_directions): #Loop which controls and draws the amount of explosion directions in the firework
            turtle.down()
            turtle.dot(dot_size)
            turtle.up()
            turtle.circle(radius,360/explosion_directions)
        turtle.right(180)
        turtle.forward(3)
        turtle.left(90)
        turtle.backward(radius)
        radius = radius + 10
        if dot_size < 7:
            dot_size = dot_size + 1
    radius = 10
    explosion_directions = random.randint(10,20)
    starty = -282
    startx = random.randint(-450,450)
    destx = random.randint(-450,450)
    desty = random.randint(0,282)
    firework_size = random.randint(firework_radius/2, firework_radius)
    dot_size = 2
    turtle.update()

    
turtle.done() # Need to keep the window display up
