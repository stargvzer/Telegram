import telebot
import kolchok


bot = telebot.TeleBot(kolchok.token)

def start(update, context):
bot.send_message(message.chat.id, kolchok.random_message())
 
if __name__ == '__main__': 
    bot.polling()
