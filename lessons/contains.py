"""Example of a function that searches through a list."""


# Define a function named contains
# Two paramaters:
#   1. needle - the string we're searching for
#   2. haystack - the list we're searching through


def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False