from newsdataapi import NewsDataApiClient

TOKEN = ""

params = {
    "access_key": "",
    "query": "Moscow",
    "units": "metric",
    "lang": "ru"
}

api = NewsDataApiClient(apikey="")

currencies_ = {
    "доллар": "USD",
    "евро": "EUR",
    "рубль": "RUB"
}

headers = {
    "apikey": "",
    "content-type": "application/x-www-form-urlencoded"
}
