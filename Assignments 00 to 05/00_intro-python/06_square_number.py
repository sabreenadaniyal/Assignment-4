# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0




# Ask the user for a number
num = float(input("Type a number to see its square: "))

# Calculate the square
square = num * num

# Display the result in green bold italic
print(f"\033[3;32m\033[1m{num} squared is {square}\033[0m")