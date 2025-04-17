#Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

#There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.


Days_per_year = 365
Hours_in_a_day = 24
Minutes_in_an_hours = 60
Seconds_per_minutes = 60

# Calculation
seconds_in_year = Days_per_year * Hours_in_a_day * Minutes_in_an_hours * Seconds_per_minutes

# Print result
print(f"\033[32m\nThere are {seconds_in_year} seconds in a year❗\n\033[0m")