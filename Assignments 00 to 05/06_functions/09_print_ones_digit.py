# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

def print_ones_digit(num):
    ones = num % 10
    print(f"The ones digit is {ones}")

def main():
    BLUE = "\033[94m"
    RESET = "\033[0m"
    
    num = int(input(f"{BLUE}Enter a number: {RESET}"))
    print_ones_digit(num)

if __name__ == "__main__":
    main()
  
