"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_non_empty() -> None:
    """Value at of index 3 should return the data of the 3rd data value."""
    linked_list = Node(1, Node(2, Node(3, Node(4, None))))
    assert value_at(linked_list, 3) == 3


def test_value_at_index_0() -> None:
    """When the index is 0, the function should return the first value."""
    linked_list = Node(1, Node(2, Node(3, Node(4, None))))
    assert value_at(linked_list, 0) == 1


def test_value_at_out_of_range() -> None:
    """When the index is greater than the amount of objects in linked list, return IndexError."""
    linked_list = Node(1, Node(2, Node(3, Node(4, None))))
    # with pytest.raises(IndexError) as e:
    #     value_at(linked_list, 8)
    with pytest.raises(IndexError) as exc_info:
        value_at(linked_list, 6)
    exception_raised = exc_info.value
    assert str(exception_raised) == "Index is out of bounds on the list."

