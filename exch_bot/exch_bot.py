import telebot
from cfg import TOKEN, currencies_
from extensions import APIException, ExchangeConverter

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = "Что бы начать работу, введите команду в формате:\n\n< *Валюта А* >\
           < *Валюта Б* >\
           < *Количество Б в А* >\n\n*Валюта А* - Название валюты, цену которой хотите узнать" \
           "\n*Валюта Б* - Название валюты, в которой надо узнать цену первой валюты" \
           "\n*Количество Б в А* - Количество первой валюты\n\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def currencies(message: telebot.types.Message):
    text = "Доступные валюты:\n"
    for key in currencies_.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise APIException(f"Количество параметров должно быть = 3")
        quote, base, amount = values
        answer = ExchangeConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка ввода команды:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling()
