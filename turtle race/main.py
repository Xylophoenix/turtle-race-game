from turtle import Turtle, Screen, forward
import random
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is gonna win the race? Enter a color")
color = ["red", "purple", "green", "blue", "yellow", "orange"]
y_position = [-100,-60,-20,20,60,100]
all_turtles = []
for turtle_index in range(0,6):
    turtle = Turtle("turtle")
    turtle.color(color[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle won the race.")
            else:
                print(f"You've lost. The {winning_color} turtle won the race.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()


































