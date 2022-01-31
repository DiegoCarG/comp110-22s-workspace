"""Recreating wordle program with one chance to get word right."""

__author__ = "730427471"

secret = "python"
guess = input(f"What is your {len(secret)} letter guess? ")
boxes = ""
match: bool = False 
index = 0
alt_index = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret):   # if the length of the guess is not the length of the secret word then prompt them to enter another word
    guess = input(f"That was not {len(secret)} letters! Try again: ")

while index < len(secret):
    if guess[index] == secret[index]:  # if the corresponding indexes match, then the letter is in the correct place and a green box should be printed
        boxes = boxes + GREEN_BOX
    else: 
        while match is not True and alt_index < len(secret): 
            if guess[index] == secret[alt_index]:
                match = True  # after a match is found, end the loop by declaring match true
            else:
                alt_index = alt_index + 1  # increase alternate index by 1 to repeat the loop but check the guess against the next letter of the secret
        if match is True:  # if match has been declared true, then the letter did not match the corresponding index of the secret, but it matched one of the other indexes, so print a yellow box
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    index = index + 1
    match = False  # reset match to False, so if the letter is not found in the corresponding index of the secret, the nested while loop will execute and find if the letter is present in any index of the secret.
    alt_index = 0  # to make sure the next letter is evaluated against every letter of the secret, reset the alt_index variable back to 0.

print(boxes)

if guess == secret: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
