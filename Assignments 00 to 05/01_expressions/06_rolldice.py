# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"🎲 You rolled: {die1} and {die2}")
print(f"➡️ Total: \033[31m{die1 + die2}\033[0m")