"""Recreating wordle program with one chance to get word right."""
___author___ = 730427471

secret = "python"
guess = input(f"What is your {len(secret)} letter guess? ")

WHITE_BOX: str = " \U00002B1C"
GREEN_BOX: str = " \U0001F7E9"
YELLOW_BOX: str = " \U0001F7E8"

index = 0
boxes = ""
match: bool = False 
alt_index = 0
while len(guess) != len(secret):   # if the length of the guess is not the length of the secret word then prompt them to enter another word
    guess = input(f"That was not {len(secret)} letters! Try again: ")

while index < len(secret):
    if guess[index] == secret[index]:  # if the corresponding indexes match, then the letter is in the correct place and a green box should be printed
        boxes = boxes + GREEN_BOX
    else: 
        while match is False and alt_index < len(secret): 
            if guess[index] == secret[alt_index]:
                boxes = boxes + YELLOW_BOX
                match = True  # after a match is found and a yellow box is added to the boxes string, end the loop by declaring match true
            else:
                alt_index = alt_index + 1  # increase alternate index by 1 to repeat the loop but check the next letter
    if guess[index] != secret[index] and match is False:  # the first condition for a white box is that the corresponding indexes don't match, but also that there has been no match found in the whole word aka that the match bool has not been declared true and there is no yellow box added to the box string
        boxes = boxes + WHITE_BOX
    index = index + 1
    match = False
    alt_index = 0

print(boxes)

if guess == secret: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
