"""Ex03 - Structured Wordle."""

__author__ = "730484794"

from mimetypes import guess_all_extensions


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
def contains_char(word: str, char: str) -> bool:
    """Returns true if single character string char is found in word"""
    assert len(char) == 1
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False
    

def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji noting the accuracy of guess"""
    assert len(guess) == len(secret)
    i: int = 0
    emoji: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected_len: int) -> str:
    """prompts user for a guess of the expected length"""
    user_input: str = input(f"enter a {expected_len} character word: ")
    while len(user_input) != expected_len:
        user_input = input(f"That wasn't {expected_len} chars! Try again: ")
    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n: int = 0
    secret_word_len: int = 5
    secret_word: str = "codes"
    my_guess: str = ""
    won: bool = False
    while not won and n < 6:
        n += 1
        print(f"=== Turn {n}/6 ===")
        my_guess = (input_guess(secret_word_len))
        print(emojified(my_guess, secret_word))
        won = secret_word == my_guess

    if won:
        print(f"You won in {n}/6 Turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()