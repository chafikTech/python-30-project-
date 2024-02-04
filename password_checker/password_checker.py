def check_password(password: str):
    with open("password.txt", "r") as file:
        common_password = file.read().splitlines()

    for i, common_password in enumerate(common_password, start=1):
        if password == common_password:
            print(f"{password}: X (#{i})")
            return
    print(f"{password}: (Unique)")


def main():
    user_password = input("Enter your password for checking: >> ")
    check_password(user_password)


if __name__ == "__main__":
    main()
