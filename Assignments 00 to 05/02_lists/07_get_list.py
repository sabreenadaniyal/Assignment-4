# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']



values = []                   # Start with an empty list

while True:
    user_input = input("Enter a value: ")
    if user_input == "":
        break                  # Stop the loop if the user presses enter without typing anything
    values.append(user_input)  # Add the entered value to the list

# Print the full list in blue
print(f"Here's the list: \033[94m{values}\033[0m")

