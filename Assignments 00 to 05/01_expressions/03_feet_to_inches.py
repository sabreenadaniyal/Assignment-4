# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Simple feet to inches converter
def main():
    feet_to_inch = float(input("Enter feet🦶: "))  # Get user input
    inches = feet_to_inch * 12  # Convert to inches

     # Print result
    print(f"\033[31m{feet_to_inch} feet is {inches} inches\033[0m")

main()