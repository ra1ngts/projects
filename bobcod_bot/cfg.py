from newsdataapi import NewsDataApiClient
from decouple import config

TOKEN = config("TOKEN")

params = {
    "access_key": config("access_key"),
    "query": "Moscow",
    "units": "metric",
    "lang": "ru"
}

api = NewsDataApiClient(apikey=config("apikey"))

currencies_ = {
    "доллар": "USD",
    "евро": "EUR",
    "рубль": "RUB"
}

headers = {
    "apikey": config("headers_apikey"),
    "content-type": "application/x-www-form-urlencoded"
}
