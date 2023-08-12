import telegram
from telegram.ext import Updater, MessageHandler, MessageFilter
from telegram import Update
import requests

# Ваш токен от @BotFather
TOKEN = 'TOKEN_HERE'

class PhotoFilter(MessageFilter):
    def filter(self, message):
        return bool(message.photo)

def download_image(update: Update, context):
    # Получение объекта сообщения
    message = update.message
    # Проверка на наличие фотографии в сообщении
    if message.photo:
        # Получение самой большой доступной фотографии
        photo = message.photo[-1]
        # Получение информации о файле фотографии
        file = context.bot.get_file(photo.file_id)
        # Получение прямой ссылки на файл
        direct_link = file.file_path
        message.reply_text(f"Прямая ссылка на скачивание изображения: {direct_link}")
    else:
        message.reply_text("Пожалуйста, отправьте изображение.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Обработчик для сообщений с изображениями
    dp.add_handler(MessageHandler(PhotoFilter(), download_image))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
