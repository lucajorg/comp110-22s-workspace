"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730484794"

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + single_char + " in " + five_char_word)
count: int = 0
if five_char_word[0] == single_char:
    print(single_char + " found at index 0")
    count = count + 1
if five_char_word[1] == single_char:
    print(single_char + " found at index 1")
    count = count + 1
if five_char_word[2] == single_char:
    print(single_char + " found at index 2")
    count = count + 1
if five_char_word[3] == single_char:
    print(single_char + " found at index 3")
    count = count + 1
if five_char_word[4] == single_char:
    print(single_char + " found at index 4")
    count = count + 1
if count == 0:
    print("No instances of " + single_char + " found in " + five_char_word)
else:
    if count == 1:
        print("1 instance of " + single_char + " found in " + five_char_word)
    if count > 1:
        print(str(count) + " instances of " + single_char + " found in " + five_char_word)
