# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() and check if it returns True or not. If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.



import random

DONE_LIKELIHOOD = 0.2  # The probability of done() returning True

def done():
    # Simulate the likelihood of stopping
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print(f"\033[3mI'm going to count until 10 or until I feel like stopping, whichever comes first.\033[0m")
    
    for i in range(1, 11):
        if done():  # Check if we should stop
            return  # Stop counting if done() returns True
        print(i)

def main():
    chaotic_counting()  # Call the chaotic_counting function
    print(f"\033[94mI'm done. \033[0m🤚")  # This will print after chaotic_counting() finishes

if __name__ == '__main__':
    main()
