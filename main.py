import telebot
import kolchok


bot = telebot.TeleBot(kolchok.token)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, kolchok.random_message())


bot.infinity_polling()
