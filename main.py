import telebot
import stulchmoha

bot = telebot.TeleBot(stulchmoha.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
     bot.send_message(message.chat.id, stulchmoha.startAnswer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
         bot.send_message(message.chat.id, stulchmoha.random_message())

if __name__ == '__main__':
     bot.polling(none_stop=True)
     
     

bot.infinity_polling()
