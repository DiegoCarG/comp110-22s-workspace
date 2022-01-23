"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730427471"

chosen_word: str = input("Enter a 5-character word ")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chosen_letter: str = input("Enter a single character ")
if len(chosen_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("searching for " + chosen_letter + " in " + chosen_word)

counter: int = 0

if chosen_letter == chosen_word[0]:
    print(chosen_letter + " found in index 0")
    counter = counter + 1

if chosen_letter == chosen_word[1]:
    print(chosen_letter + " found in index 1")
    counter = counter + 1

if chosen_letter == chosen_word[2]:
    print(chosen_letter + " found in index 2")
    counter = counter + 1

if chosen_letter == chosen_word[3]:
    print(chosen_letter + " found in index 3")
    counter = counter + 1

if chosen_letter == chosen_word[4]:
    print(chosen_letter + " found in index 4")
    counter = counter + 1

if counter == 0:
    print("No instances of " + chosen_letter + " found in " + chosen_word)
else:
    print(str(counter) + " instances of " + chosen_letter + " found in " + chosen_word)