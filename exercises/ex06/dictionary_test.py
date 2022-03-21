"""Testing dictionary functions."""

__author__ = "730427471"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_normal() -> None:
    """Tests if invert function is working."""
    original = {"Name": "Diego", "Kris": "Professor"}
    assert invert(original) == {"Diego": "Name", "Professor": "Kris"}


def test_invert_only1() -> None:
    """Tests invert function when there is only one key/value in the dictionary."""
    original = {"1": "2"}
    assert invert(original) == {"2": "1"}


def test_invert_list() -> None:
    """Tests invert function when keys/values are lists."""
    original = {("Kris", "Jordan"): ("Professor", "UNC")}
    assert invert(original) == dict({("Professor", "UNC"): ("Kris", "Jordan")})


def test_favorite_color_normal() -> None:
    """Tests to see if favorite color function is working."""
    favs = {"Diego": "Grey", "Max": "Blue", "Jose": "Yellow", "Declan": "Yellow"}
    assert favorite_color(favs) == "Yellow"


def test_favorite_color_same() -> None:
    """Tests to see if favorite color function works when all the favorite colors are the same."""
    favs = {"Diego": "Grey", "Max": "Grey", "Bartholomew": "Grey"}
    assert favorite_color(favs) == "Grey"


def test_favorite_color_tie() -> None:
    """Tests to see if when there is a tie for favorite color, it returns the first one in the dictionary."""
    favs = {"Diego": "Grey", "Declan": "Blue"}
    assert favorite_color(favs) == "Grey"


def test_favorite_color_only1() -> None:
    """Tests to see if the function works when all colors are the same but one."""
    favs = {"Diego": "Grey", "Declan": "Grey", "Adrian": "Grey", "Max": "Yellow"}
    assert favorite_color(favs) == "Grey"


def test_count_normal() -> None:
    """Checks to see if count function works."""
    list = ["yes", "no", "yes"]
    assert count(list) == {"yes": 2, "no": 1}


def test_count_only1() -> None: 
    """Checks to see if count function works when there's only 1 item in list."""
    list = ["yes"]
    assert count(list) == {"yes": 1}


def test_count_all_the_same() -> None:
    """Checks to see if count function works when there's only 1 item in list."""
    list = ["yes"]
    assert count(list) == {"yes": 1}