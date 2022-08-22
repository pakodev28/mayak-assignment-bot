import os

import pandas as pd
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.environ.get("TOKEN"))

def validate_file_format(message: telebot.types.Message, file_format: str):
    if file_format not in ("xls", "xlsx"):
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAIHeGMDlpzna-do-60_q6wwtYVqazPZAAJx9gEAAWOLRgy2C5NzsjO0bCkE",
        )
        bot.send_message(
            message.chat.id, "Загружайте только файл формата .xls или .xlsx"
        )
        raise ValueError("Формат файла не .xls или .xlsx")


@bot.message_handler(commands=["start"])
def start_callback(message: telebot.types.Message):
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAIHdmMDg_YLHITGY9_5PnLRA_92qiCvAAJ6AAPluQgavXvp8xtDHoApBA",
    )
    bot.send_message(
        message.chat.id,
        "Привет, этот бот может прочитать твой Excel документ и показать тебе его содержимое!",
    )
    bot.send_message(message.chat.id, "📎 Отправь мне файл!")


@bot.message_handler(content_types=["document"])
def document_callback(message: telebot.types.Message):
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    splited_file_name = file_name.split(".")
    file_format = splited_file_name[-1]
    validate_file_format(message, file_format)

    with open("user_xls_storage/" + file_name, "wb") as new_file:
        new_file.write(downloaded_file)

    df = pd.read_excel(downloaded_file, header=None, names=["NAME", "URL", "XPATH"])
    bot.send_message(message.chat.id, df.to_markdown())


def run_bot():
    bot.infinity_polling()


run_bot()
