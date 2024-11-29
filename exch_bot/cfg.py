from decouple import config

TOKEN = config("TOKEN")

currencies_ = {
    "доллар": "USD",
    "евро": "EUR",
    "рубль": "RUB"
}

headers = {
    "apikey": config("headers_apikey")
}
