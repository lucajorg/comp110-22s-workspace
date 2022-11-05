from __future__ import annotations
from typing import Optional


class Node:

    data: int = -1
    next: Optional[Node] = None


def linkify(start: int, end: int) -> Optional[Node]:
    """Linkify function."""
    if start >= end:
        return None
    else:
        head: Node = Node()
        head.data = start
        head.next = linkify(start + 1, end)
        return head


head: Optional[Node] = linkify(0, 2)