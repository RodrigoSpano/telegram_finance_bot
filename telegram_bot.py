import telebot
from dotenv import load_dotenv
import os
from gsheets import clear_sheet,write_available_row

load_dotenv(dotenv_path="./.env")

API_TOKEN = os.getenv("BOT_API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# Command /start - /help handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "messages format {price},{item},{category} \n - amount could be -3000 or 3000 \n - item could be book \n - categories are divided by letters (a,b,c,d), they are specified in the sheets")

# Command /info handler
@bot.message_handler(commands=['info'])
def send_info(message):
  bot.reply_to(message, "This is just a bot to record all my e/ingress $$🤑")

# Define a message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  # bot.reply_to(message, message.text)
  splitted_data=message.text.split(",")
  price=float(splitted_data[0].strip())
  item=str(splitted_data[1].strip())
  category=str(splitted_data[2].strip())
  try:
    write_available_row([price,item,category])
    bot.reply_to(message, "Successfully saved!")
  except:
    bot.reply_to(message, "Oh oh, something went worng!!! try again later")

# Command /clear handler => clear paper
@bot.message_handler(commands=['clear'])
def send_info(message):
  clear_sheet()
  bot.reply_to(message, "CLear all my egress")

  
# Start the bot
print("Bot running")
bot.polling()