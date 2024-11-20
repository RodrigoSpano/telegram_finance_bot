import telebot
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./.env")

API_TOKEN = os.getenv("BOT_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# Command /start - /help handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "messages format {amount},{item},{category} \n - amount could be -3000 or 3000 \n - item could be book \n - categories are divided by letters (a,b,c,d), they are specified in the sheets")

# Command /info handler
@bot.message_handler(commands=['info'])
def send_info(message):
  bot.reply_to(message, "This is just a bot to record all my e/ingress $$🤑")

# Define a message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  # bot.reply_to(message, message.text)
  bot.reply_to(message, "que queres wachin")

# Start the bot
print("runninggg......................")
bot.polling()