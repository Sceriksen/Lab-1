# Sindre Eriksen, SID: 20530556
import turtle
import random
turtle.speed(0)
RandomVariable = random.randint(0,101) # want numbers from 0-100, so range needs to be 0-101 since the last number will not be included
count = 1 # Start at 1 since the final, correct, guess will not be counted in the while loop
Answers = 135 #The y value for where the game will write wether answer is right or wrong

# Setting up the visual part of the game
turtle.penup()
turtle.goto(-150,200)
turtle.pendown()
turtle.write("GUESSING GAME", font=("Arial", 30, "normal"))

turtle.penup()
turtle.goto(-170,180)
turtle.pendown()

for i in range (0,2):
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.goto(-170, 150)
turtle.pendown()

GuessedNumber = int(turtle.textinput("GUESSING GAME", "guess a number between 0-100"))

#GuessedNumber = int(input("Guess a number"))
#turtle.write(RandomVariable)


#while GuessedNumber < 1 or GuessedNumber > 100:
 #   turtle.write("Please enter a number between 1 and 100")
  #  GuessedNumber = int(turtle.textinput("GUESSING GAME", "guess a number between 0-100"))

# Game mechanics code
while GuessedNumber != RandomVariable:
    if GuessedNumber < 0 or GuessedNumber > 100:
        turtle.write("Please choose a number between 0 and 100")
    elif GuessedNumber < RandomVariable:
            turtle.write("Too low!")
    else:
            turtle.write("Too high!")
    turtle.penup()
    turtle.goto(-170, Answers)
    turtle.pendown()
    Answers = Answers - 15

    GuessedNumber = int(turtle.textinput("GUESSING GAME", "guess a number between 0-100"))
    count = count + 1


if GuessedNumber == RandomVariable:
    turtle.write("You are right!")

turtle.penup()
turtle.goto(-170, Answers - 30)
turtle.write("Number of guesses:" + str(count))
turtle.penup()


turtle.done()
