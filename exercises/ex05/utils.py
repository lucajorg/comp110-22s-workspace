"""Only evens, sub, and concatenation utilities."""

__author__ = "730484794"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only even values in a list."""
    new_list: list[int] = []
    for item in xs:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returns values of a list between the start and points."""
    i: int = start
    if i < 0:
        i = 0
    end_index = end
    if end_index > len(xs):
        end_index = len(xs)
    new_list: list[int] = []
    while i < end_index:
        new_list.append(xs[i])
        i += 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenates the second list immediately following the first."""
    new_list: list[int] = []
    for item in xs:
        new_list.append(item)
    for item in ys:
        new_list.append(item)
    return new_list