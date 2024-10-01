import telebot
import kol


bot = telebot.TeleBot(kol.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, kol.startAnswer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, kol.random_message())


if __name__ == '__main__':
    bot.polling(none_stop=True)
