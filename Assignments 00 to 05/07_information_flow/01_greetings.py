# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia

# Greetings Sophia!


def greet(name):
    print(f"\033[1mGreeting {name}!\033[0m")

def main():
    name = input("What is your name?: ")
    greet(name)

if __name__ == "__main__":
    main()