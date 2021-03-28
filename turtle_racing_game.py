import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not a number... Try again!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number is not in range 2-10... Try again!')

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)  # pixels
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
            # returns the winner racer whose number is the index number

def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    # We add 1 so the first turtle does not start at the edge of the screen.
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        # 20 is a random number to space the turtles not at the bottom of the screen
        # WIDTH and HEIGHT // 2 because the normal starting position is 0 like in a x and y coordinate
        # -WIDTH and -HEIGHT will give -250 to reach the bottom of the screen
        racer.pendown()
        turtles.append(racer)
    return turtles

racers = get_number_of_racers()
print(racers)
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print('The winner is the turtle with the color:', winner)
time.sleep(5)
