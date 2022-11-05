"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_0() -> None:
    """Value at 0 of non-empty list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_1() -> None:
    """Value at 1 of non-empty list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_value_at_2() -> None:
    """Value at last of non-empty list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_value_at_full() -> None:
    """Value at of non-empty list, with index error."""
    with pytest.raises(IndexError):
        linked_list = Node(10, Node(20, Node(30, None)))
        assert value_at(linked_list, 3)


def test_max() -> None:
    """Max of non-empty list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_2() -> None:
    """Max of non-empty list with different order."""
    linked_list = Node(20, Node(30, Node(10, None)))
    assert max(linked_list) == 30


def test_max_empty() -> None:
    """Max of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify() -> None:
    """Linkify a list."""
    assert linkify([1, 2, 3]) is None


def test_scale() -> None:
    """Scale a linkify list."""
    assert scale(linkify([]), 2) is None


def test_scale_2() -> None:
    """Scale a list."""
    linked_list = Node(0, Node(1, Node(3, None)))
    assert scale(linked_list, 3) is None


