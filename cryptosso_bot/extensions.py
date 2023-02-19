import requests
import json
from cfg import keys


class ConversionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def conversion(current: str, exchange: str, amount: float):
        if current == exchange:
            raise ConversionException(f"Невозможно перевести одинаковые валюты '{exchange}'!")

        try:
            current_ticker = keys[current]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту '{current}'")

        try:
            exchange_ticker = keys[exchange]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту '{exchange}'")

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Не удалось обработать количество '{amount}'")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={current_ticker}&tsyms={exchange_ticker}")
        total_amount = json.loads(r.content)[keys[exchange]]

        return total_amount
