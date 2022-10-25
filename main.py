import telebot
import kolchok
from telegram.ext import CommandHandler



bot = telebot.TeleBot(kolchok.token)

def start(update, context):
bot.send_message(message.chat.id, kolchok.random_message())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

 
if __name__ == '__main__': 
    bot.polling()
