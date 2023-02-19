import telebot
from cfg import keys, TOKEN
from extensions import ConversionException, CryptoConverter

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = "Что бы начать работу, введите команду в формате:\n\n( <b>Валюта А</b> )\
           ( <b>Валюта Б</b> )\
           ( <b>Количество Б в А</b> )\n\n<b>Валюта А</b> - Название валюты, цену которой хотите узнать" \
           "\n<b>Валюта Б</b> - Название валюты, в которой надо узнать цену первой валюты" \
           "\n<b>Количество Б в А</b> - Количество первой валюты\n\n<b>Увидеть список всех доступных валют:" \
           " /exrates</b>"
    bot.reply_to(message, text)


@bot.message_handler(commands=["exrates"])
def currencies(message: telebot.types.Message):
    text = "<b>Доступные валюты</b>"
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def conversion(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConversionException("Количество параметров должно быть = 3")
        current, exchange, amount = values
        total_amount = CryptoConverter.conversion(current, exchange, amount)

    except ConversionException as e:
        bot.reply_to(message, f"Ошибка пользователя:\n{e}!")

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду:\n{e}!")

    else:
        text = f"Цена {amount} {current} в {exchange} = {total_amount * float(amount)}"
        bot.send_message(message.chat.id, text)


bot.polling()
