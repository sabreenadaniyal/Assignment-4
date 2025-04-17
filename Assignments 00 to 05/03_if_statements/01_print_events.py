# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38


def evenNumbers():
# Program to print the first 20 even numbers

 for i in range(20):          # Loop 20 times
    print(i * 2, end=" ")     # Print the even number (i * 2), and keep (end=> print on the same line)
   
# Call the function when "run", no need to edit anything below!
evenNumbers()