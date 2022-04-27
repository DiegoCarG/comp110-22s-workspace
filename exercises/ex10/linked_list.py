"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "Your PID"


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
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the nth value in a linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    elif index - 1 == 0:
        return head.data
    else:
        index -= 1
        return value_at(head.next, index)


def max(head: Node) -> int:
    """Returns the largest value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    
    elif head.next is None:
        return head.data
    
    else:
        val = max(head.next)
        if head.data > val:
            return head.data
        return val


def linkify(list: list[int]) -> Node:
    """Turns list into linked list."""
    head = Node(list[0], None)
    tail = head

    i = 1
    while i < len(list):
        tail.next = Node(list[i], None)
        tail = tail.next
        i += 1
    return head


def scale

print(linkify([1, 2, 3, 4]))

