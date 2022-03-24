"""Draws a classical guitar."""

__author__ = "730484794"

from turtle import Turtle, colormode, done, tracer, update

colormode(255)


def curve(a_turtle: Turtle, size: float, dir: int, angle: int) -> None:
    """Draws a circular curve with specific size, direction, and angle."""
    i: int = 0
    while (i < angle):
        a_turtle.forward(size)
        a_turtle.right(dir)
        i += 1


def move(a_turtle: Turtle, x: int, y: int) -> None:
    """Moves the turtle without drawing a line and turns it to face the right."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()


def draw_body(a_turtle: Turtle, x: int, y: int) -> None:
    """Draws the body of the guitar."""
    move(a_turtle, x, y)
    curve(a_turtle, 1, 1, 120)
    curve(a_turtle, 0.75, -1, 75)
    curve(a_turtle, 1.5, 1, 135)
    a_turtle.forward(20)
    curve(a_turtle, 1.5, 1, 135)
    curve(a_turtle, 0.75, -1, 75)
    curve(a_turtle, 1, 1, 120)
    a_turtle.forward(28)


def draw_rectangle(a_turtle: Turtle, x: int, y: int, length: int, height: int) -> None:
    """Draws a rectangle with bottom left at (x, y), with specified length and height."""
    move(a_turtle, x, y)
    i: int = 0
    while i < 2:
        a_turtle.forward(length)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)
        i += 1


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    leo: Turtle = Turtle()
    # Body of guitar, light brown.
    leo.begin_fill()
    leo.fillcolor(220, 170, 100)
    draw_body(leo, 14, 0)
    leo.end_fill()
    # Neck of guitar, dark brown.
    leo.begin_fill()
    leo.fillcolor(100, 70, 50)
    draw_rectangle(leo, -14, 0, 28, 180)
    leo.end_fill()
    # Head of guitar, dark brown
    leo.begin_fill()
    draw_rectangle(leo, -20, 180, 40, 60)
    leo.end_fill()
    # Sound hole of guitar, black
    move(leo, 0, -50)
    leo.begin_fill()
    leo.fillcolor(0, 0, 0)
    curve(leo, 0.5, 1, 360)
    leo.end_fill()
    # Bridge of guitar, black
    leo.begin_fill()
    draw_rectangle(leo, -40, -200, 80, 20)
    leo.end_fill()
    # Strings of guitar, silver.
    strings: int = 0
    leo.pencolor(240, 230, 200)
    while strings < 6:
        move(leo, -10 + strings * 4, -180)
        leo.setheading(90)
        leo.forward(360)
        strings += 1
    update()
    done()


if __name__ == "__main__":
    main()