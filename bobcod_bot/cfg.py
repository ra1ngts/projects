from newsdataapi import NewsDataApiClient

params = {
    "access_key": "36b8f1b574f18ae0a392ba8b46006169",
    "query": "Moscow",
    "units": "metric",
    "lang": "ru"
}

api = NewsDataApiClient(apikey="pub_17234543580bd619cd57131bf6564d5aabd74")

currencies_ = {
    "доллар": "USD",
    "евро": "EUR",
    "рубль": "RUB"
}

headers = {
    "apikey": "FibfgPWm7RCCmORTtL82JpW59piiBWXD",
    "content-type": "application/x-www-form-urlencoded"
}
