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
    "доллар".lower(): "USD",
    "евро".lower(): "EUR",
    "рубль".lower(): "RUB"
}

headers = {
    "apikey": "",
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "translo.p.rapidapi.com"
}
