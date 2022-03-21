"""Create functions to be tested."""

__author__ = "730427471"


def only_evens(xs: list[int]) -> list[int]:
    """Input is a list of integers and output is a list of only the even numbers in the input list."""
    evens = list()
    for x in xs:
        if x % 2 == 0 and x != 0:
            evens.append(x)
    return evens


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Input is a list and start and end values which refer to indexes. Starts at start index and returns up to the last item before the end index."""
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)
    if start > len(xs) or end <= 0 or len(xs) == 0:
        return list()
    else:
        subset = list()
        subset = xs[start:end]
        return subset


def concat(first: list[int], second: list[int]) -> list[int]:
    """Takes two lists and concatinates the second list onto the first list without modifying the elements of either."""
    i = 0
    while i < len(second):
        first.append(second[i])
        i += 1
    return first