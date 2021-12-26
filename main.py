import os
import telebot

bot = telebot.TeleBot("API KEY HERE")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I'm Gimhan Geek Chat Bot")

@bot.message_handler(commands=["How"])    
def send_message(message):
    bot.send_message(message,"https://youtube.com/c/GimhanGeek")

bot.polling()