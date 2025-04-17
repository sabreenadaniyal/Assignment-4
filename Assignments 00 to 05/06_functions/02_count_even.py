# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!


def count_even():
    nums = []

    while True:
        val = input("Enter an integer or press enter to stop: ")
        if val == "":
            break
        nums.append(int(val))

    # Count even numbers using list comprehension
    evens = sum(1 for n in nums if n % 2 == 0)

    print("Even numbers:", evens)

if __name__ == "__main__":
 count_even()

