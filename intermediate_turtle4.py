from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=1000, height=800)
tim = Turtle()
tim.penup()
tim.goto(488, 300)
tim.right(90)
tim.color('red')
tim.pendown()
tim.forward(500)
y_positions = [0, 50, 100, -50, -100, -150]
all_turtles = []
colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_input = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.shapesize(2, 3, 1)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-485, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
is_race_on = False

if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 430:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                screen.textinput('Final Score', 'YOU WON! The ' + winning_color + ' turtle is the winner!')
            else:
                screen.textinput('Final Score', 'YOU LOST! The ' + winning_color + ' turtle is the winner!')
                    
                    
        random_distance = random.randint(0, 15)
        turtle.forward(random_distance)


screen.exitonclick()