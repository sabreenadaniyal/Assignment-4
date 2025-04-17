# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5


# ANSI escape codes for bold and italic
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

# Dictionary storing the price of each fruit
fruit_prices = {
   "apple": 2.5,
   "durian": 10.0,
   "jackfruit": 5.0,
   "kiwi": 3.0,
   "rambutan": 4.0,
   "mango": 3.5
}

# Variable to store the total cost
total_cost = 0

# Loop through each fruit in the dictionary
for fruit, price in fruit_prices.items():
    
    # Ask the user how many of this fruit they want
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    
    # Calculate the cost for this fruit and add it to the total cost
    total_cost += quantity * price

# Print the total cost
print(f"{BOLD}{ITALIC}Your total is ${total_cost}{RESET}")