import itertools
import string
import time


def commom_guess(word: str) -> str | None:
    with open("words.txt", "r") as words:
        words_list: list[str] = words.read().splitlines()

    for i, match in enumerate(words_list, start=1):
        if match == word:
            return f"Common match: {match} (#{i})"


def brute_force(word: str, length: int, digits: bool = False, symbole: bool = False) -> str | None :
    chars: str = string.ascii_lowercase 

    if digits:
        chars += string.digits

    if symbole:
        chars += string.punctuation

    attemps: int = 0 

    for geuss in itertools.product(chars, repeat =length):
        attemps +=1
        guess: str = "".join(geuss)

        if guess == word:
            return f"{word} was check in {attemps:,} guesses,/"

    print(guess, attemps)



def main():
    print("Searching...")
    password: str = "xbc1"
    start_time: float = time.perf_counter()

    if common_match := commom_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=4,  digits=True, symbole=False):
            print(cracked)
        else:
            print("there was no match ....")

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2) , "s")




if __name__ == "__main__":
    main()


