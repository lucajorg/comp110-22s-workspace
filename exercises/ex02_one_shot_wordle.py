"""Ex02 One shot Wordle."""
__author__ = "730484794"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
i: int = 0
emoji: str = ""
anywhere: bool = False
j: int = 0


while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")

while i < len(secret):
    if guess[i] == secret[i]:
        emoji += GREEN_BOX
    else:
        while not anywhere and j < len(secret):
            if guess[i] == secret[j]:
                anywhere = True
            j += 1
        if anywhere:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1
    j = 0
    anywhere = False
print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
