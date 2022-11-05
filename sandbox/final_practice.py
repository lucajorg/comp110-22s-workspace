from itertools import count
from re import I

from pygame import CONTROLLER_BUTTON_LEFTSHOULDER


def reverse_multiply(items: list[int]) -> list[int]:
    i: int = 0
    new_list: list[int] = []
    while i < len(items):
        new_list.append((items[len(items) - 1] - i) * 2)
        i += 1
    return new_list


def free_biscuits(teams: dict[str, list[int]]) -> dict[str, bool]:
    new_dict: dict[str, bool] = {}
    for items in teams:
        i: int = 0
        for points in teams[items]:
            i += points
        if i >= 100:
            new_dict[items] = True
        else:
            new_dict[items] = False
        
    return new_dict


def multiples(items: list[int]) -> list[bool]:
    i: int = 1
    new_list: list[bool] = []
    new_list.append(items[0] % items[len(items) - 1] == 0)
    while i < len(items):
        new_list.append(items[i] % items[i - 1] == 0)
        i += 1
    return new_list


def merge_lists(strs: list[str], ints: list[int]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    if len(strs) == len(ints):
        for items in range(len(strs)):
            new_dict[strs[items]] = ints[items]
    return new_dict


class HotCocoa:
    has_whip: bool
    flavor: bool
    marshmallow_count: int
    sweetness: int

    def __init__(self, has_whip: bool, flavor: bool, marshmallow_count: int, sweetness: int):
        """Docstring."""
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness
    
    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows 
        self.sweetness += mallows * 2
    
    def calorie_count(self) -> float:
        calories: float = 0.0
        if self.flavor == "vanilla" or self.flavor == "peppermint":
            calories += 30
        else:
            calories += 20
        if self.has_whip:
            calories += 100
        calories += self.marshmallow_count / 2
        return calories


print(reverse_multiply([1, 2, 3]))
print(free_biscuits({"UNCvsDuke": [38, 20, 42], "UNCvsState": [9, 51, 16, 23]}))
print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))
print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))


word: str = "aabbeeeeb"

I
count
max_count
cur_letter
max_letter

while i< len(word):
    while