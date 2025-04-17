# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

# Here's a sample run of the program (user input is in blue):

# Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!


def make_sentence(word, part_of_speech):

    GREEN = "\033[92m"
    RESET = "\033[0m"

    if part_of_speech == 0:
        print(f"{GREEN}I am excited to add this {word} to my vast collection of them! {RESET}") 
    elif part_of_speech == 1:
        print(f"{GREEN}It's so nice outside today it makes me want to {word}! {RESET}")
    elif part_of_speech == 2:
        print(f"{GREEN}Looking out my window, the sky is big and {word}! {RESET}")
    else:
        print("❗ Invalid part of speech!! ")

def main():
    BLUE = "\033[94m"
    RESET = "\033[0m"

    word = input(f"{BLUE}Please enter a noun, verb or adjective! {RESET}") 
    part = int(input(f"{BLUE}Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: {RESET}"))
    make_sentence(word, part)

if __name__ == "__main__":
    main()