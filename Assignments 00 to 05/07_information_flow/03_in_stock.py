# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.


def num_in_stock(fruit):
    Inventory = {
        "pear": 1000,
        "apple": 500,
        "banana": 300,
        "orange": 200,
        "grape": 0                  # Example of a fruit with 0 in stock
    }
    return Inventory.get(fruit, 0)  # Returns 0 if fruit is not found in inventory

def main():
    fruit = input(f"\033[1mEnter a fruit: \033[0m").lower()    # Prompt user to input a fruit, and convert it to lowercase
    stock = num_in_stock(fruit)     # Get the number of that fruit in stock
    
    if stock > 0:
     print("This fruit is in stock! Here is how many: ") 
     print(stock)
    else:
       print("This fruit is not in stock")

if __name__ == "__main__":
   main()