# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random

def Guess_number():
    # Pick a random number between 0 and 99
    secret_number = random.randint(0, 99)

    print("🔢 Welcome to the Guess My Number Game!")
    print("I am thinking of a number between 0 and 99...🤔")

    while True:
            guess = int(input("💬 Enter a guess: "))

            if guess < secret_number:
                print("📉 Your guess is too Low!") 
            elif guess > secret_number:
                print("📈 Your guess is too High!")
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                break
       
# Correct main function call
if __name__ == '__main__':
    Guess_number()
