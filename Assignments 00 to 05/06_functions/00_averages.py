# Write a function that takes two numbers and finds the average between the two.

def Average(num1, num2):
    # calculate the average
    average = (num1 + num2) / 2
    return average

# Take user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the average
result = Average(num1, num2)

# Display the result
print(f"The average of {num1} and {num2} is {result}")

# No need to call Average() again, the function has already been called.
if __name__ == '__main__':
    pass  # This is optional; the function is already called above.



