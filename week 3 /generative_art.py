# File: week3/generative_art.py
# Generative Art - Random Sun Pattern
# Reference inspiration:
# https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Sun_symbol.svg/1024px-Sun_symbol.svg.png

import turtle
import random

# -----------------------------
# Screen Setup
# -----------------------------
screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.setup(width=800, height=800)

sun = turtle.Turtle()
sun.speed(0)
sun.width(2)
sun.hideturtle()

# -----------------------------
# Color Lists for Randomness
# -----------------------------
sun_colors = [
    "gold",
    "orange",
    "yellow",
    "red",
    "white"
]

background_dots = [
    "lightblue",
    "purple",
    "pink",
    "cyan"
]

# -----------------------------
# Draw Random Background Stars
# -----------------------------
sun.penup()

for i in range(80):
    x = random.randint(-390, 390)
    y = random.randint(-390, 390)

    sun.goto(x, y)

    # Conditional statement
    if i % 2 == 0:
        size = random.randint(2, 5)
    else:
        size = random.randint(5, 8)

    sun.dot(size, random.choice(background_dots))

# -----------------------------
# Draw Sun Center
# -----------------------------
sun.goto(0, -60)
sun.color("yellow")
sun.begin_fill()
sun.pendown()
sun.circle(60)
sun.end_fill()
sun.penup()

# -----------------------------
# Draw Generative Sun Rays
# -----------------------------
sun.goto(0, 0)

# Outer loop
for layer in range(36):

    sun.color(random.choice(sun_colors))

    # Conditional statement changes ray length
    if layer % 3 == 0:
        ray_length = random.randint(120, 180)
    else:
        ray_length = random.randint(80, 140)

    # Nested loop
    for repeat in range(3):
        sun.forward(ray_length)
        sun.dot(random.randint(10, 20),
                random.choice(sun_colors))
        sun.backward(ray_length)
        sun.right(3)

    sun.right(10)

# -----------------------------
# Finish
# -----------------------------
turtle.done()

