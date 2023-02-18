from telebot import *
from cfg import TOKEN, params, api, currencies_
from extensions import CommandException, ExchangeConverter
import requests
import json

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = f"Привет <b>{message.chat.username}</b>! Смотри что я умею:\n\n<b>Список доступных команд</b>\
           \n/temp - Выводит показания текущей температуры\
           \n/news - Выводит развлекательные новости\
           \n/img - Выводит кнопку для поиска изображений\
           \n/srch - Выводит поисковые системы\
           \n/exrates - Выводит курсы обмена валют и инструкцию\n\
           \n<b>Другие возможности</b>\n1. Возможность отправить голосовое сообщение боту\n2. Возможность отправить боту" \
           f" изображение"
    bot.reply_to(message, text)


@bot.message_handler(commands=["temp"])
def temp_info(message: telebot.types.Message):
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?lat=55.75&lon=37.62&appid=40fa44cfcc6aaed1838bc7454a27556f",
        params)
    response = json.loads(r.content)
    city = response["name"]  # Название города.
    min_temp = response["main"]["temp_min"]  # Минимальная t.
    max_temp = response["main"]["temp_max"]  # Максимальная t.
    feels_temp = response["main"]["feels_like"]  # Ощущается как t.
    weather_cond = response["weather"][0]["description"]  # Состояние погоды.
    pressure = response["main"]["pressure"] * 0.75  # Давление в мм. рт/ст.
    symbol = "C\u00B0"
    bot.reply_to(message, f"<b>Погода</b>\n"
                          f"Город: <b>{city} ({weather_cond})</b>\nМинимальная температура: <b>{min_temp} {symbol}</b>\n"
                          f"Максимальная температура:"
                          f" <b>{max_temp} {symbol}</b>\nОщущается как: <b>{feels_temp} {symbol}</b>\nДавление:"
                          f" <b>{pressure} мм. рт/ст.</b>")


@bot.message_handler(commands=["news"])
def news_info(message: telebot.types.Message):
    response = api.news_api(category="entertainment", country="us", language="en")
    news_title_0 = response["results"][0]["title"]
    news_link_0 = response["results"][0]["link"]
    news_title_1 = response["results"][1]["title"]
    news_link_1 = response["results"][1]["link"]
    news_title_2 = response["results"][3]["title"]
    news_link_2 = response["results"][3]["link"]
    news_title_3 = response["results"][4]["title"]
    news_link_3 = response["results"][4]["link"]
    news_title_4 = response["results"][5]["title"]
    news_link_4 = response["results"][5]["link"]
    news_title_5 = response["results"][6]["title"]
    news_link_5 = response["results"][6]["link"]
    news_title_6 = response["results"][7]["title"]
    news_link_6 = response["results"][7]["link"]
    news_title_7 = response["results"][8]["title"]
    news_link_7 = response["results"][8]["link"]
    news_title_8 = response["results"][9]["title"]
    news_link_8 = response["results"][9]["link"]
    bot.reply_to(message, f"<b>Новости развлечений</b>\n{news_title_0}\n{news_link_0}\n\n{news_title_1}"
                          f"\n{news_link_1}\n\n{news_title_2}\n{news_link_2}\n\n{news_title_3}\n{news_link_3}\n\n"
                          f"{news_title_4}\n{news_link_4}\n\n{news_title_5}\n{news_link_5}\n\n"
                          f"{news_title_6}\n{news_link_6}\n\n{news_title_7}\n{news_link_7}\n\n"
                          f"{news_title_8}\n{news_link_8}")


@bot.message_handler(commands=["img"])
def search_images(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Изображения", url="https://www.google.ru/imghp?hl=ru&ogbl")
    markup.add(button1)
    button2 = types.InlineKeyboardButton("Изображения кошек", url="https://is.gd/XavY8R")
    markup.add(button2)
    button3 = types.InlineKeyboardButton("Изображения собак", url="https://is.gd/XZaE8G")
    markup.add(button3)
    button4 = types.InlineKeyboardButton("Изображения автомобилей", url="https://is.gd/1i53b7")
    markup.add(button4)
    button5 = types.InlineKeyboardButton("Изображения природы", url="https://is.gd/aDJyIJ")
    markup.add(button5)
    button6 = types.InlineKeyboardButton("Изображения космоса", url="https://is.gd/Jh3meO")
    markup.add(button6)
    button7 = types.InlineKeyboardButton("Изображения моря", url="https://is.gd/VVEHa0")
    markup.add(button7)
    button8 = types.InlineKeyboardButton("Изображения цветов", url="https://is.gd/N42BXs")
    markup.add(button8)
    button9 = types.InlineKeyboardButton("Изображения городов", url="https://is.gd/j977KX")
    markup.add(button9)
    bot.send_message(message.chat.id, f"<b>Изображения</b>",
                     reply_markup=markup)


@bot.message_handler(commands=["srch"])
def search(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Google поиск", url="https://www.google.com/")
    markup.add(button1)
    button2 = types.InlineKeyboardButton("Yandex поиск", url="https://ya.ru/")
    markup.add(button2)
    button3 = types.InlineKeyboardButton("Wikipedia поиск", url="https://is.gd/VHZ4M6")
    markup.add(button3)
    bot.send_message(message.chat.id, f"<b>Поисковые системы</b>",
                     reply_markup=markup)


@bot.message_handler(commands=["exrates"])
def currencies(message: telebot.types.Message):
    text = "Что бы начать работу, введите команду в формате:\n\n( <b>Валюта А</b> )\
           ( <b>Валюта Б</b> )\
           ( <b>Количество Б в А</b> )\n\n<b>Валюта А</b> - Название валюты, цену которой хотите узнать" \
           "\n<b>Валюта Б</b> - Название валюты, в которой надо узнать цену первой валюты" \
           "\n<b>Количество Б в А</b> - Количество первой валюты\n\n<b>Доступная валюта</b>"
    for key in currencies_.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def converter(message: telebot.types.Message):
    greetings = "Привет! привет! Приветик! приветик! Приветствую! Привет привет Приветик приветик Приветствую" \
                "приветствую прива Добрый день добрый день" \
                "Доброе утро доброе утро Hi hi Hello hello".split(" ")
    if message.text in greetings:
        bot.reply_to(message, f"Привет <b>{message.chat.username}</b>, меня зовут <b>BobCod</b> и я умный бот.")
    else:
        try:
            values = message.text.split(" ")
            if len(values) != 3:
                raise CommandException(f"Я не знаю пока такой команды :(")
            quote, base, amount = values
            answer = ExchangeConverter.get_price(quote, base, amount)
        except CommandException as e:
            bot.reply_to(message, f"Ошибка ввода команды:\n{e}")
        except Exception as e:
            bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
        else:
            bot.reply_to(message, answer)


@bot.message_handler(content_types=["voice"])
def voice_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"<b>{message.chat.username}</b> у тебя красивый голос!")


@bot.message_handler(content_types=["photo"])
def photo_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Очень красивая фотография <b>{message.chat.username}</b>")


bot.polling()
