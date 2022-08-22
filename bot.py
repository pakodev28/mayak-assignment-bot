import os

import pandas as pd
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ.get("TOKEN"))


@bot.message_handler(commands=["start"])
def start_callback(message):
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAIHdmMDg_YLHITGY9_5PnLRA_92qiCvAAJ6AAPluQgavXvp8xtDHoApBA",
    )
    bot.send_message(
        message.chat.id,
        "Привет, этот бот может прочитать твой Excel документ и показать тебе его содержимое!",
    )
    bot.send_message(message.chat.id, "📎 Отправь мне файл!")
