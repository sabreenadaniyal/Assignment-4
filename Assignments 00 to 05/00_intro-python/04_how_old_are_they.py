# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):



def main():
  Anton : int = 21           # Anton's age is given as 21 years old.
  Beth : int = 6 + Anton     # Beth is 6 years older than Anton.
  Chen : int = 20 + Beth     # Chen is 20 years older than Beth
  Drew : int = Chen + Anton  # Drew is as old as Chen's age plus Anton's age.
  Ethan : int = Chen         # Ethan is the same age as Chen.

# display the result
  print(f"Anton is {Anton} years old.")
  print(f"Beth is {Beth} years old.")
  print(f"Chen is {Chen} years old.")
  print(f"Drew is {Drew} years old.")
  print(f"Ethan is {Ethan} years old.")

main()