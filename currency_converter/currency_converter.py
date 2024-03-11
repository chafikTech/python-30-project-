import json
from typing import Final

import requests

BASE_URL: Final[str] = ""
API_KEY: Final[str] = ""


def get_rates(mock: bool = False) -> dict:
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    with open("rates.json", "w") as file:
        json.dump(data, file)

    return data


def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else: 
        raise ValueError(f"{currency} is not a valid currency")


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate : float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)


