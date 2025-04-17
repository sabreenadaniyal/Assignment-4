# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.



# Program to check if the user can vote in Peturksbouipo, Stanlau, or Mayengua

# ANSI escape codes for blue text
BOLD_BLUE = "\033[1;94m"
BOLD_WHITE = "\033[1;97m"
ITALIC = "\033[3m"
RESET = "\033[0m"

# Ask the user for their age
age = int(input(f"{BOLD_WHITE}Enter your age? {RESET}"))

# Print the age in blue (as part of the output)
print(f"{ITALIC}{BOLD_BLUE}Your age is: {age}{RESET}")

# Check voting eligibility in each country
if age >= 16:
    print(f"You can vote in Peturksbouipo where the voting age is: {BOLD_BLUE}16.{RESET}")
else:
    print(f"You cannot vote in Peturksbouipo where the voting age is: {BOLD_BLUE}16.{RESET}")

if age >= 25:
    print(f"You can vote in Stanlau where the voting age is: {BOLD_BLUE}25.{RESET}") 
else:
    print(f"You cannot vote in Stanlau where the voting age is: {BOLD_BLUE}25.{RESET}")

if age >= 48:
    print(f"You can vote in Mayengua where the voting age is: {BOLD_BLUE}48.{RESET}")
else:
    print(f"You cannot vote in Mayengua where the voting age is: {BOLD_BLUE}48.{RESET}") 
