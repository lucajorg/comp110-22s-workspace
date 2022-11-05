import turtle as t
from random import random


def tree(x: float, y: float) -> None:
    """Paint a beautiful tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    TRUNK_LENGTH = random() * 50.0 + 50.0
    ANGLE = 90.0
    branch(TRUNK_LENGTH, ANGLE)
    t.update()


def branch(length: float, angle: float) -> None:
    """Paint a branch recursively"""
    t.setheading(angle)
    t.forward(length)

    if length < 3.0:
        ...
    else: 
        nature: float = random() * 20.0
        branch(length * 0.75, angle + 5.0 + nature)
        branch(length * 0.7, angle - (5.0 + nature))
    t.setheading(angle + 180.0)
    t.forward(length)


t.tracer(0, 0)
t.speed(0)
t.getscreen().onclick(tree)
t.done()
