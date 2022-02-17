"""Structured wordle."""

__author__ = "730427471"


def contains_char(secret: str, guess: str) -> bool:  
    """Tests to see if a letter appears in any part of the secret word. If there is a match, contains_char is True, if not then it is False."""
    assert len(guess) == 1  
    i: int = 0 
    match: bool = False
    while match is False and i < len(secret):
        if secret[i] == guess:
            match = True
        else:
            i += 1
    if match is True: 
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str: 
    """Takes two words and displays how the letters relate to each other through emojis."""
    assert len(secret) == len(guess)
    WHITE: str = " \U00002B1C"
    GREEN: str = " \U0001F7E9"
    YELLOW: str = " \U0001F7E8"
    boxes = ""
    i: int = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            boxes = boxes + str(GREEN)
            i += 1
        elif contains_char(secret, guess[i]) is False:
            boxes = boxes + str(WHITE)
            i += 1 
        else:
            boxes = boxes + str(YELLOW)
            i += 1
    return boxes


def input_guess(length: int) -> str:
    """Asks for a guess repeatedly until it is the requested length."""
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")  # keep asking for guess until you get a guess of the right length
    else: 
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i = 1
    secret: str = "salsa"
    win: bool = False
    while i <= 6 and win is False:  # Keep asking for another word until they run out of turns or guess correctly
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
            print(f"You won in {i}/6 turns!")
        else:
            i += 1
    if win is False:  # if after the loop is completed, win still hasn't been set to true, then they did not guess correctly so they lost the game
        print("X/6 - Sorry, try again tomorrow!") 
    

if __name__ == "__main__":
    main()