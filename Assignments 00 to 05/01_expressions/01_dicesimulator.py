# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

for _ in range(3):
    print(f"Rolled: {random.randint(1, 6)} and {random.randint(1, 6)}")