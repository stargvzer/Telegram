import random
from telegram.ext import Updater


token = "5257043486:AAEne2vsG3AXfOJ8jyO1w9INKUb2jUQFxx4"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


f = open("dict.txt","r")
lines = f.readlines()

random_message = lambda: random.choice(lines)




