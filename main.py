import telebot
import os
from dotenv import load_dotenv

load_dotenv() # reload env params from .env to environment
apikey = os.environ.get("API_KEY") # from .env file

bot = telebot.TeleBot(apikey)

@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'Hello my friend',parse_mode='Markdown')


@bot.message_handler(commands=['end'])
def end_message(message):
    bot.send_message(message.chat.id, 'Возвращайся...')
    # bot.send_message(message.chat.id, 'Возвращайся...', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'Хорошо')

@bot.message_handler(content_types=['sticker'])
def send_text(message):
    bot.send_message(message.chat.id, 'стикер')

bot.polling()
