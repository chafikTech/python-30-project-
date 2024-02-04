import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_website(csv_path: str) -> list[str]:
    website: list[str] = []
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if "https://" not in row[1] :
                website.append(f"https://{row[1]}")
            else:
                website.append(row[1])

        return website
    

def get_use_agent() -> str:
    ua = UserAgent()
    return ua.firefox

def get_use_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code :
            description: str = f"({value} {value.name}) {value.description}"
            return description

    return "(???) Unknown status code ..."


def check_website(website: str, user_agent):
    try:
        code: int = requests.get(website, headers={"User-Agent": user_agent}).status_code
        print(website, get_use_description(code))
    except Exception:
        print(f"could not get intformation about website, {website}")
    

def main():
    sites: list[str] = get_website("websites.csv")
    user_agent:str = get_use_agent()

    for site in sites:
        check_website(site, user_agent)


if __name__ == "__main__":
    main()
