from random import randint

lower_num, higher_num = 1, 10

random_number: int = randint(lower_num, higher_num)

print(f"geuss the number in the range from {lower_num} to {higher_num}. ")

while True:
    try:
        user_geuss = int(input("Enter the your number: "))
    except ValueError as err:
        print("Enter number please: ")
        continue

    if user_geuss > random_number:
        print("the number is lower: ")
    elif user_geuss < random_number:
        print("the number is higher: ")
    else:
        print("you guess the number (:")
        break
