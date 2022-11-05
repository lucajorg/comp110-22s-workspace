"""Some demonstrations of randomness."""

__author__ = "Kris Jordan"

import numpy as np
from random import random, randint
import pandas as pd

# The random function produces a random float
# between 0.0 and 1.0, not inclusive of 1.0
random_float: float = random()
print("A random_float: " + str(random_float))

# The randint function produces a random int
# between the given arguments, inclusive of 
# the second argument.
random_int: int = randint(0, 100)
print("A random int: " + str(random_int))


x = np.arange(1, 5)
print(x.std())

titanic = pd.read_csv("data/titanic.csv")


print(titanic[titanic["Age"] > 35].shape)