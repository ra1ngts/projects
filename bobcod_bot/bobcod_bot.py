from telebot import *
from cfg import TOKEN, params, api, currencies_
from extensions import CommandException, ExchangeConverter
from googletrans import Translator
import requests
import json
import datetime

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = f"Привет <b>{message.chat.username}</b> \U0001F44B! Смотри что я умею:\n\n<b>Список доступных команд</b>\
           \n/temp - Выводит показания текущей температуры \U0001F326\
           \n/news - Выводит развлекательные новости \U0001F4F0\
           \n/img - Выводит поиск изображений \U0001F5BC\
           \n/srch - Выводит поисковые системы \U0001F50D\
           \n/exrates - Выводит курсы обмена валют и инструкцию \U0001F4B1\n\
           \n<b>Другие возможности</b>\n1. Возможность отправить голосовое сообщение боту \U0001F5E3\n" \
           f"2. Возможность отправить боту изображение \U0001F5BC\n" \
           f"3. Возможность перевода c <b>Английского</b> на <b>Русский</b> \U0001F524"
    bot.reply_to(message, text)


@bot.message_handler(commands=["temp"])
def temp_info(message: telebot.types.Message):
    r = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?lat=55.75&lon=37.62&appid=",
        params)
    response = json.loads(r.content)
    weather_emoji = {800: "Ясно \U00002600",
                     801: "Небольшая облачность \U000026C5",
                     802: "Облачно \U00002601",
                     803: "Облачно с прояснениями \U0001F325",
                     804: "Пасмурно \U00002601",
                     701: "Туман \U0001F32B",
                     711: "Дымка \U0001F32B",
                     600: "Небольшой снег \U00002744",
                     601: "Снегопад \U00002744",
                     602: "Сильный снегопад \U00002744",
                     611: "Мокрый снег \U00002744",
                     612: "Мокрый снег \U00002744",
                     615: "Небольшой дождь со снегом \U00002744",
                     616: "Дождь со снегом \U00002744",
                     500: "Небольшой дождь \U0001F327",
                     501: "Дождь \U0001F327",
                     502: "Сильный дождь \U0001F327",
                     503: "Сильный дождь \U0001F327",
                     504: "Ливень \U000026C8",
                     511: "Ледяной дождь \U0001F328",
                     300: "Небольшая морось \U0001F327",
                     301: "Морось \U0001F327",
                     302: "Сильная морось \U0001F327",
                     311: "Моросящий дождь \U0001F327",
                     200: "Небольшой дождь с грозой \U000026C8",
                     201: "Дождь с грозой \U000026C8",
                     202: "Ливень с грозой \U000026C8",
                     210: "Небольшая гроза \U0001F329",
                     211: "Гроза \U0001F329",
                     212: "Сильная гроза \U0001F329"
                     }

    weather_id = response["weather"][0]["id"]
    if weather_id in weather_emoji:
        w_id = weather_emoji[weather_id]
    else:
        w_id = "Выгляни в окно, не пойму что там за погода! \U0001F937"

    city = response["name"]  # Название города.
    min_temp = response["main"]["temp_min"]  # Минимальная t.
    max_temp = response["main"]["temp_max"]  # Максимальная t.
    feels_temp = response["main"]["feels_like"]  # Ощущается как t.
    pressure = response["main"]["pressure"] * 0.75  # Давление в мм. рт/ст.
    humidity = response["main"]["humidity"]  # Влажность в %.
    wind_speed = response["wind"]["speed"]  # Скорость ветра.
    wind_gust = response["wind"]["gust"]  # Порыв ветра до:
    sunrise_timestamp = datetime.datetime.fromtimestamp(response["sys"]["sunrise"])  # Восход солнца.
    sunset_timestamp = datetime.datetime.fromtimestamp(response["sys"]["sunset"])  # Закат солнца.
    bot.reply_to(message, f"<b>Погода</b>\nВосход: <b>{sunrise_timestamp}</b> \U0001F31D\n"
                          f"Город: <b>{city}</b>\nМинимальная температура: <b>{min_temp} С°</b>\n"
                          f"Максимальная температура:"
                          f" <b>{max_temp} С°</b>\nОщущается как: <b>{feels_temp} С° {w_id}</b>\nДавление:"
                          f" <b>{pressure} мм. рт/ст.</b>\nВлажность: <b>{humidity} %</b>\nСкорость ветра:"
                          f" <b>{wind_speed} м.с.</b>\nПорывы ветра до: <b>{wind_gust} м.с.</b>\n"
                          f"Закат: <b>{sunset_timestamp}</b> \U0001F31A")


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
           "\n<b>Количество Б в А</b> - Количество первой валюты\n\n<b>Доступные валюты" \
           " \U0001F4B5 \U0001F4B6 \U000020BD</b>"
    for key in currencies_.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def send_txt(message: telebot.types.Message):
    try:
        if message.text.isalpha():
            translator = Translator()
            src = "en"
            destination = "ru"
            translated_text = translator.translate(message.text, src=src, dest=destination).text
            bot.reply_to(message, f"Перевод: <b>{translated_text}</b>")
        else:
            try:
                values = message.text.split(" ")
                if len(values) != 3:
                    raise CommandException(
                        "Что бы узнать список доступных команд введите: /help")
                quote, base, amount = values
                answer = ExchangeConverter.get_price(quote, base, amount)
            except CommandException as e:
                bot.reply_to(message, f"Ошибка ввода команды:\n{e}")
            except Exception as e:
                bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
            else:
                bot.reply_to(message, answer)
    except KeyError as e:
        bot.reply_to(message, f"Ошибка ввода:\n{e}")


@bot.message_handler(content_types=["voice"])
def voice_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"<b>{message.chat.username}</b> у тебя красивый голос!")


@bot.message_handler(content_types=["photo"])
def photo_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Очень красивая фотография <b>{message.chat.username}</b>.")


bot.polling()
