# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


numbers : list = [1, 2, 3, 4]
double_numbers = [num * 2 for num in numbers]
print(f"\033[1;3;32m{double_numbers}\033[0m")



