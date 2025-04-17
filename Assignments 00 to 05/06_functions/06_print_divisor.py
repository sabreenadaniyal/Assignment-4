# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

def print_divisors(num):
    print(f"Here are the divisors of \033[94m{num}\033[0m")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')

def main():
    number = int(input("Enter a number: "))
    print_divisors(number)

if __name__ == "__main__":
 main()




