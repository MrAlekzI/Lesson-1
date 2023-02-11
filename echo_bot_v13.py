import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO) #запись логов уровня INFO в файл

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text #запрос текста
    print(user_text)
    update.message.reply_text(user_text) #ответ бота    

def main():
    mybot = Updater(settings.TOKEN, use_context=True)
    dp = mybot.dispatcher #обработка события
    dp.add_handler(CommandHandler("start", greet_user)) #вызов комманды пр нажатии
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) #hреагирует только на текст
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()