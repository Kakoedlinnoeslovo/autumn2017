from telegram.ext import Updater, CommandHandler

updater = Updater(token='344532609:AAG8LgfCK9U0UpBTgczDeEU-zaW3P4vFHno')









dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm sphere bot!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
