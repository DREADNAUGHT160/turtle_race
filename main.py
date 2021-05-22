from turtle import Turtle, Screen
import random


def end_line():
    end = Turtle()
    end.penup()
    end.goto(230, 200)
    end.pendown()
    end.setheading(270)
    end.goto(230, -200)


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("bet chooser", "place the bet on the color: ")
name = ["cat", "de", "da", "adda", "dopa"]
color = ["red", "yellow", "orange", "blue", "purple"]
turtle = []
x = -230
y = -100
end_line()
for x, tur in enumerate(name):
    tur = Turtle()
    tur.penup()
    tur.goto(-230, y)
    tur.color(color[x])
    tur.shape("turtle")
    y += 50
    turtle.append(tur)

if bet:
    race_on = True

while race_on:
    for rur in turtle:
        if rur.xcor() > 230:
            win_color = rur.pencolor()
            race_on = False
            if win_color == bet:
                print("you w0n the bet")
            else:
                print("you lost")

        space = random.randint(0, 10)
        rur.forward(space)

screen.exitonclick()
