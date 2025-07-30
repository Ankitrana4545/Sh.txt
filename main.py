from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    chat_id = update.message.chat.id
    msg = "Hello! I am your sh to txt file converter bot."
    context.bot.send_message(chat_id=chat_id, text=msg)

def echo(update, context):
    chat_id = update.message.chat.id
    msg = update.message.text
    context.bot.send_message(chat_id=chat_id, text=f"You said: {msg}")

def main():
    updater = Updater(token='7644490207:AAFu28rVCBZhwyHmU1Xg8nKk24Hmdj0s9lM', use_context=True)
    
    dp = updater.dispatcher
    
    # Start command handler
    dp.add_handler(CommandHandler('start', start))
    
    # Echo message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    # Start polling updates
    updater.start_polling()

if __name__ == '__main__':
    main()
