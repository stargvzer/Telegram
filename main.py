import telebot
import kolchok


bot = telebot.TeleBot(kolchok.token)


@bot.message_handler(commands=['Колчок'])
def handle_start(messages):
    bot.send_message(messages.chat.id, kolchok.startAnswer)
 
if __name__ == '__main__': 
    bot.polling()
