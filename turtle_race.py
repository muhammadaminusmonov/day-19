# todo make a turtle race

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win? (enter the color): ")
colors = ["blue", "green", "yellow", "brown", "red", "purple"]

num_turtles = len(colors)
turtle_y_start_position = -(num_turtles * 30 / 2)

is_game_on = False
if user_bet:
    is_game_on = True


turtles = []
for i in range(num_turtles):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].up()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=turtle_y_start_position)
    turtle_y_start_position += 30


while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winner = turtle.pencolor()
            if user_bet == str(winner):
                print(f"You've won. The {winner} turtle reached the line first!")
            else:
                print(f"You've lost. The {winner} turtle reached the line first!")
        move = randint(1, 10)
        turtle.forward(move)


screen.exitonclick()
