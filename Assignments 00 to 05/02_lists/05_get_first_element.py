# Fill out the function get_first_element(l2st) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst):
    # Print the first element of the list
    print(lst[0])

# Prompt the user to input elements for the list
n = int(input("How many elements do you want to enter? "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

# Call the function
get_first_element(user_list)
