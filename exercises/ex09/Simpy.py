"""Utility class for numberical operations."""

from __future__ import annotations
# from re import S

from typing import Union

__author__ = "730484794"


class Simpy:
    """Utility class for numerical operations."""

    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, vals: list[float]):
        """Initialize Simpy class."""
        self.values = vals

    def __str__(self) -> str:
        """Return string of Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num: int) -> None:
        """Fill Simpy list with num items with value value."""
        self.values = []
        i: int = 0
        while i < num:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill simpy list with a range from start to stop incremented by step."""
        self.values = []
        assert step != 0.0
        while step > 0.0 and start < stop or step < 0.0 and start > stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Sums all items in values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds each item with an item in rhs with the same index."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])        

        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the power (**) operator."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])        

        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Use the equal to (==) operator."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])        

        return result
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Use the greater than (>) operator."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])        

        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use the subscription operator."""
        if isinstance(rhs, int):
            result: float = self.values[rhs]
            return result
        else:
            result_list: list[float] = []
            for index in range(len(rhs)):
                if rhs[index]:
                    result_list.append(self.values[index])
            return Simpy(result_list)