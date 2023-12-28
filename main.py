import telebot
import os
from dotenv import load_dotenv
from utils.speech import ogg_to_text

load_dotenv() # reload env params from .env to environment
apikey = os.environ.get("API_KEY") # from .env file

bot = telebot.TeleBot(apikey)
workdir = os.getcwd()


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


@bot.message_handler(content_types=['voice'])
def send_text(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    ogg_file_name = 'new_file.ogg'
    ogg_file_path = os.path.join(workdir,"files",ogg_file_name)

    with open(ogg_file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
        txt = ogg_to_text(ogg_file_path)
        print(txt)
        bot.send_message(message.chat.id, txt)
        # os.remove(ogg_file_name)

bot.polling()
