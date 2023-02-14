from cfg import currencies_, headers
import requests
import json


class APIException(Exception):
    pass


class ExchangeConverter:
    @staticmethod
    def get_price(quote, base, amount):
        try:
            quote_key = currencies_[quote.lower()]
        except KeyError:
            raise APIException(f"Нет такой валюты - {quote}")

        try:
            base_key = currencies_[base.lower()]
        except KeyError:
            raise APIException(f"Нет такой валюты - {base}")

        if base_key == quote_key:
            raise APIException(f"Невозможно перевести одинаковые валюты {base}")

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f"Невозможно обработать количество {amount}")

        r = requests.get(f"https://api.apilayer.com/fixer/latest?symbols={quote_key}&base={base_key}", headers=headers)
        response = json.loads(r.content)
        new_price = response["rates"][quote_key] * float(amount)
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {quote} = {new_price}"
        return message
