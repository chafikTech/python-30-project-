import random


def roll_dic(amount : int) -> list[int]:
    if amount < 0:
        raise ValueError

    rolls : list[int] = []

    for i in range(amount):
        random_roller: int = random.randint(1, 6)
        rolls.append(random_roller)

    return rolls


def main():
    while True:
        try:
            user_input = input("how many dice would like to roll: ")

            if(user_input.lower() == "exit"):
                print("Thank you for playing")
                break 
            total : int = 0
            for i in roll_dic(int(user_input)):
                total += i

            print(total - 1)
            print(*roll_dic(int(user_input)), sep=", ")

        except ValueError:
            print("please Enter valide number:")



if __name__ == "__main__":
    main()
