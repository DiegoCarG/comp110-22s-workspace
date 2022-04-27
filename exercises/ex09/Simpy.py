"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730427471"


class Simpy:
    """Useful class for numerical operations."""
    values: list[float]

    def __init__(self, x: list[float]):
        """Constructor to initalize values."""
        self.values = x  

    def __str__(self) -> str:
        """Represents Simpy objects as strings."""
        return f"Simpy({self.values})"

    def fill(self, f: float, amount: int) -> None:
        """Fills values list with the same number."""
        new: list[float] = []
        for i in range(amount):
            new.append(f)
        self.values = new

    def arange(self, start: float, stop: float, step: float = 1) -> None:
        """Create a list that spans the start-stop values and increases by an increment of step by each value."""
        new: list[float] = []
        assert step != 0.0
        if step > 0.0:
            while start < stop:
                new.append(start)
                start += step
        else:
            while start > stop:
                new.append(start)
                start += step
        self.values = new

    def sum(self) -> float:
        """Return sum of all values."""
        items_sum: float = sum(self.values)
        return items_sum

    def __add__(self, left: Union[float, Simpy]) -> Simpy:
        """Allows usage of addition operator with respect to Simpy objects."""
        new: list[float] = []
        if isinstance(left, float):
            for i in self.values:
                new.append(i + left)
        else:
            assert len(left.values) == len(self.values)
            for i in range(len(left.values)):
                new.append(self.values[i] + left.values[i])

        ret: Simpy = Simpy(new)
        return ret

    def __pow__(self, x: Union[float, Simpy]) -> Simpy: 
        """Allows usage of power operator with Simpy objects."""
        new: list[float] = []
        if isinstance(x, float):
            for i in self.values:
                new.append(i ** x)
        else:
            assert len(x.values) == len(self.values)
            for i in range(len(x.values)):
                new.append(self.values[i] ** x.values[i])
        ret: Simpy = Simpy(new)
        return ret

    def __eq__(self, x: Union[float, Simpy]) -> list[bool]:
        """Allows for mask creation of each item in values."""
        final: list[bool] = []
        if isinstance(x, float):
            for i in self.values:
                final.append(i == x)
        else:
            assert len(x.values) == len(self.values)
            for i in range(len(x.values)):
                final.append(self.values[i] == x.values[i])
        return final

    def __gt__(self, x: Union[float, Simpy]) -> list[bool]:
        """Allows for mask creation using > relation between each item."""
        final: list[bool] = []
        if isinstance(x, float):
            for i in self.values:
                final.append(i > x)
        else:
            assert len(x.values) == len(self.values)
            for i in range(len(x.values)):
                final.append(self.values[i] > x.values[i])
        return final

    def __getitem__(self, x: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds ability to use the subscription operator with Simpy objects."""
        final: list[bool] = []
        if isinstance(x, int):
            return self.values[x]
        else:
            assert len(x) == len(self.values)
            for i in range(len(x)):
                if x[i]:  # checks to see if current val in list[bool] is true
                    final.append(self.values[i])
        results: Simpy = Simpy(final)
        return results
