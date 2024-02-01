from random import choice


def run_game():
    word: str = choice(["apple", "secret", "banana"])

    username: str = input("What is your name: >>")
    print(f"Welcome to hangman {username}")

    # setup
    guessed: str = ""
    tries: int = 3

    while tries > 0:
        blanks: int = 0

        print("Word: ", end="")
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print("_", end="")
                blanks += 1
        print()

        if blanks == 0:
            print("you got it ")
            break

        guess: str = input("Enter leter >> ")

        if guess in guessed:
            print(f"You already use: '{guess}' Please try with another letter")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"sorry that was wrong.. {tries} tries remaining")

            if tries == 0:
                print("you lose. sorry next time")
                break


if __name__ == "__main__":
    run_game()
