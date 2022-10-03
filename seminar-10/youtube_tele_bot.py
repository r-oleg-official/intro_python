from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes 
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     await update.message.reply_text(f'Hello {update.effective_user.first_name}') 
     app = ApplicationBuilder().token("YOUR TOKEN HERE").build() 
     app.add_handler(CommandHandler("hello", hello)) 
     app.run_polling() 


exit()

# python-telegram-bot. doc - https://docs.python-telegram-bot.org/en/v20.0a4/
# https://python-telegram-bot.org/ ->   It's fun:
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# 
# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
# 
# app = ApplicationBuilder().token("YOUR TOKEN HERE").build()
# app.add_handler(CommandHandler("hello", hello))
# app.run_polling()

# This installs the pre-release of v20
# $ pip install python-telegram-bot --pre
# $ python bot.py
