import random

token = "5257043486:AAEne2vsG3AXfOJ8jyO1w9INKUb2jUQFxx4"

startAnswer = 'Проклятый срущий ньюсрустер....'

f = open("dict.txt","r")
lines = f.readlines()

random_message = lambda: random.choice(lines)




