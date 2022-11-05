"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730484794"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)
        

def value_at(head: Optional[Node], index: int) -> int:
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index > 0:
            return value_at(head.next, index - 1)
        else:
            return head.data


def max(head: Optional[Node], value: int = 0) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next is not None: 
            if head.data > value:
                return max(head.next, head.data)
            else:
                return max(head.next, value)
        else:
            if head.data > value:
                value = head.data
            return value


def linkify(items: list[int], index: int = 0) -> Optional[Node]:
    """Linkify function."""
    if len(items) >= index:
        return None
    else:
        head: Node = Node(items[index], None)
        head.next = linkify(items[index:], index + 1)
        return head


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    if head is None:
        return None