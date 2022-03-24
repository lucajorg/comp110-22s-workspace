"""Dictionary test."""

__author__ = "730484794"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests invert function given an empty dict."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}

    
def test_invert_normal() -> None:
    """Tests invert function given a dict with all different values."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_one_value() -> None:
    """Tests invert function given a dict with only one values."""
    xs: dict[str, str] = {'michael': 'jordan'}
    assert invert(xs) == {'jordan': 'michael'}


def test_favorite_color_empty() -> None:
    """Tests favorite color function given an empty dict."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_normal() -> None:
    """Tests favorite color function given a normal dict."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_each_picked_one() -> None:
    """Tests favorite color function given a dict where each color is listed once."""
    xs: dict[str, str] = {"a": "red", "b": "orange", "c": "yellow", "d": "green", "e": "blue"}
    assert favorite_color(xs) == "red"


def test_count_empty() -> None:
    """Tests count function given an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_each_value_once() -> None:
    """Tests count function given a list where each value appears once."""
    xs: list[str] = ["a", "b", "c", "d"]
    assert count(xs) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_count_normal() -> None:
    """Tests count function given a normal list of multiple values."""
    xs: list[str] = ["red", "orange", "red", "red", "orange", "yellow"]
    assert count(xs) == {"red": 3, "orange": 2, "yellow": 1}