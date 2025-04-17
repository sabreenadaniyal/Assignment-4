# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.


MAX_LENGTH = 3  # You can change this value for testing

def shorten(lst):
    # Keep removing and printing the last item until the list is MAX_LENGTH long
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Remove the last item
        print(removed)       # Print the removed item

def main():
    # Ask the user to enter items for the list
    items = []
    while True:
        value = input("Enter a value (press Enter to stop): ")
        if value == "":
            break
        items.append(value)

    print("Original list:", items)
    shorten(items)
    print("Shortened list:", items)

main()
