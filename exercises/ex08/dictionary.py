"""Figuring out dictionary functions."""

__author__ = "730427471"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Inverts the order of the key and the value in dictionary."""
    inverted = {}
    for key, value in original.items():
        inverted[value] = key
    if len(inverted) != len(original):
        raise KeyError("Error: Duplicate Keys")
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns for most common value in dictionary."""
    tracker = {}
    for key, value in colors.items():
        if value not in tracker:  # creates a key in the dictionary for each color and sets its value to 0
            tracker[value] = 0
        else:
            tracker[value] += 1  # Looks to see if the key for the color has been created, if it has, then there is a duplicate and it will add 1 to the value for that key
    return max(tracker, key=tracker.get)

  
def count(mylist: list[str]) -> dict[str, int]:
    """Counts the amount of time each item in the list appears in the list."""
    counter = {}
    for thing in mylist:
        if thing not in counter:
            counter[thing] = 1
        else:
            counter[thing] += 1
    return counter
