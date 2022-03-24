"""Dictionary."""

__author__ = "730484794"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value of each item in a dictionary."""
    result: dict[str, str] = {}
    for key in xs:
        for i in xs:
            if xs[i] == xs[key] and i != key:
                raise KeyError("Cannot have duplicate values!")
        result[xs[key]] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most frequent color from a dictionary of names and favorite colors."""
    color_count: dict[str, int] = {}
    most_frequent_color: str = ""
    highest_count: int = 0
    color_mentioned: bool = False
    for key in colors:
        for i in color_count:
            if colors[key] == i:
                color_mentioned = True
        if color_mentioned:
            color_count[colors[key]] += 1
        else:
            color_count[colors[key]] = 1
        color_mentioned = False
    for j in color_count:
        if color_count[j] > highest_count:
            most_frequent_color = j
            highest_count = color_count[j]
    return most_frequent_color


def count(xs: list[str]) -> dict[str, int]:
    """Given a list, returns a dict with the count of each unique value in the list."""
    count: dict[str, int] = {}
    x_mentioned: bool = False
    for key in xs:
        for i in count:
            if key == i:
                x_mentioned = True
        if x_mentioned:
            count[key] += 1
        else:
            count[key] = 1
        x_mentioned = False
    return count