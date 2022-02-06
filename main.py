import telebot
import telegram

import kolchok


bot = telebot.TeleBot(kolchok.token)


@bot.message_handler(commands=['1'])
def handle_start(messages):
    bot.send_message(messages.chat.id, kolchok.random_message())




bot.infinity_polling()
