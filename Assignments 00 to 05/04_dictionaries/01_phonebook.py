# In this program we show an example of using dictionaries to keep track of information in a phonebook.


# ANSI escape codes for green text
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\033[0m"

# Initialize an empty dictionary to store the phonebook
phonebook = {}

# Loop to allow the user to add and look up contacts
while True:
    # Display a simple menu
    print("Phonebook Menu:")
    print("1. Add a contact")
    print("2. Lookup a contact")
    print("3. Exit")
    
    # Get user's choice
    choice = input("Enter your choice (1, 2, 3): ")

    if choice == '1':
        # Add a contact
        name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        phonebook[name] = phone_number
        print(f"{GREEN}Contact {name} added.{RESET}")

    elif choice == '2':
        # Lookup a contact
        name = input("Enter the contact's name to look up: ")
        if name in phonebook:
            print(f"{GREEN}{name}'s phone number is {phonebook[name]}{RESET}")
        else:
            print(f"{RED}Contact {name} not found.{RESET}")

    elif choice == '3':
        # Exit the program
        print(f"{BLUE}Exiting the phonebook. Goodbye!{RESET}")
        break

    else:
        print(f"{RED}Invalid choice. Please select 1, 2, or 3.{RESET}")
