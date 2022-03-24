"""Tests for the function of only_evens, sub, and concat."""

__author__ = "730484794"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_both() -> None:
    """Tests only_even function where both even and odd numbers are present."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_all_odd() -> None:
    """Tests only_even function where all values are odd."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_all_even() -> None:
    """Tests only_even function where all values are the same even number."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_sub_normal() -> None:
    """Tests sub function where endpoints are within list."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_outside_endpoints() -> None:
    """Tests sub function where endpoints are outside len of list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(xs, -5, 20) == [1, 2, 3, 4, 5, 6]


def test_sub_empty() -> None:
    """Tests sub function where list is empty."""
    xs: list[int] = []
    assert sub(xs, 0, 5) == []


def test_concat_two_lists() -> None:
    """Tests concat function where lists are same length."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 6, 7, 8]


def test_concat_empty_lists() -> None:
    """Tests concat function where lists are empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_one_empty() -> None:
    """Tests concat function where first list is empty."""
    xs: list[int] = []
    ys: list[int] = [2, 4, 6, 8]
    assert concat(xs, ys) == [2, 4, 6, 8]