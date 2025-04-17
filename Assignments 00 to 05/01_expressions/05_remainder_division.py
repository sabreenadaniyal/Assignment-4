# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


def main():
        # Get user input
        num1 = int(input("Please enter an integer to be divided: "))
        num2 = int(input("Please enter an integer to divide by: "))

        # Perform division and get remainder
        divident = num1 // num2  # Integer division
        remainder = num1 % num2  # Modulus (remainder)

        # Display the result
        print(f"\033[32m\nThe result of this division is {divident} with a remainder of {remainder}\033[0m")

main()

