# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.



# ANSI escape codes for text
BLUE = "\033[94m"
RESET = "\033[0m"

# Dictionary to store the counts of each number
count_dict = {}

# Loop that repeatedly asks the user to enter a number
while True:
    user_input = input("Enter a number: ")

    # Stop if the user presses enter without typing anything (empty input)
    if user_input == "":
        break

    # Convert the input to an integer
    number = int(user_input)

    # Update the count in the dictionary
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# Print the count of each number
for number, count in count_dict.items():
    print(f"{BLUE}{number} appears {count} times.{RESET}")
