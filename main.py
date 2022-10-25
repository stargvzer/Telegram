import telebot
import kolchok


bot = telebot.TeleBot(kolchok.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, kolchok.startAnswer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, kolchok.random_message())


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
