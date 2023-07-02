import turtle
import random



screen = turtle.Screen()
'''
# turtle moves different directions
def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
    
screen.listen()
screen.onkey(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="A", fun=right)
screen.onkey(key="D", fun=left)
'''

# tim=turtle.Turtle
# is_race_on = True
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []


#initial the turtles

for t in range (-180, 180, 60):
    tim = turtle.Turtle(shape="turtle")
    tim.penup()
    color = random.choice(colors)
    tim.color(color)
    colors.remove(color)
    tim.goto(x=-230, y=t)
    tim.speed(random.randint(1, 10))
    all_turtle.append(tim)


# find the fastest turtle

#def find_fastest_turtle():

max_speed = 0
fastest_turtle = turtle.Turtle

for turtle in all_turtle:
    print(turtle.color(),turtle.speed())
    turtle.forward(500)
    if turtle.speed() > max_speed:
        max_speed = turtle.speed()
        fastest_turtle = turtle
winner = fastest_turtle.pencolor()
print(winner)

if user_bet == winner:
    print(f"You have won! The {winner} is the winner")
else:
    print("Sorry, You lose the game!")


screen.exitonclick()


