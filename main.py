import telebot
import kolchok


bot = telebot.TeleBot(kolchok.token)


@bot.message_handler(commands=['start'])
def handle_start(messages):
    bot.send_message(messages.chat.id, kolchok.startAnswer)


@bot.message_handler(content_types=['text'])
def handle_text(messages):
    bot.send_message(messages.chat.id, kolchok.random_message())


bot.infinity_polling(none_stop = True)
