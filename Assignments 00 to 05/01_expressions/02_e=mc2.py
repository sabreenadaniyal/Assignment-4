# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!



# Constant speed of light (m/s)
C = 299792458

while True:
        # Ask user for mass input
        mass = float(input("\nEnter kilos of mass (or type 0 to exit): "))

        if mass == 0:
            print("\033[32mExiting the program. Goodbye! 👋\033[0m\n")
            break  # Exit the loop if the user enters 0

        # Calculate energy using E = m * c^2
        energy = mass * C**2

        # Display results
        print(f"\n💡 {energy:.2e} joules of energy!\n")  # Scientific notation for large numbers