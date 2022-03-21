"""."""

__author__ = "730427471"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_normal() -> None:
    """Test only evens function in a normal case."""
    xs: list[int] = [1, 2, 3, 4, 5] 
    assert only_evens(xs) == [2, 4]


def test_only_evens_only_odds() -> None:
    """Test only evens function when the input is a list of only odd numbers."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == list()


def test_only_evens_only_evens() -> None:
    """Test only evens function when the input is a list of only even numbers."""
    xs: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_only_zeroes() -> None:
    """Test only evens function when the input is a list of zeroes."""
    xs: list[int] = [0, 0, 0, 0, 0]  # is 0 even tho
    assert only_evens(xs) == list()  # think about it 


def test_only_evens_negatives() -> None:
    """Test only evens function when the input is a list of negative numbers."""
    xs: list[int] = [-1, -2, -3, -4, -5]
    assert only_evens(xs) == [-2, -4]


def test_sub_normal() -> None:
    """Test sub function in a normal case."""
    xs: list[int] = [1, 2, 3, 4, 5]
    start = 1
    end = 3
    assert sub(xs, start, end) == [2, 3]


def test_sub_neg_start() -> None:
    """Tests sub function when the start value is negative."""
    xs: list[int] = [1, 2, 3, 4, 5]
    start = -1
    end = 3
    assert sub(xs, start, end) == [1, 2, 3]


def test_sub_big_end() -> None:
    """Tests sub function when end value is greater than the length of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    start = 1
    end = 6
    assert sub(xs, start, end) == [2, 3, 4, 5]


def test_concat_normal() -> None:
    """Tests concatination function in a normal case."""
    first: list[int] = [1, 2, 3, 4, 5]
    second: list[int] = [6, 7, 8, 9, 10]
    assert concat(first, second) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_empty_first() -> None:
    """Tests concatination function when the first list is empty."""
    first: list[int] = list()
    second: list[int] = [1, 2, 3, 4, 5]
    assert concat(first, second) == [1, 2, 3, 4, 5]


def test_concat_empty_second() -> None:
    """Tests concatincation function when the second list is empty."""
    first: list[int] = [1, 2, 3, 4, 5]
    second: list[int] = list()
    assert concat(first, second) == [1, 2, 3, 4, 5]