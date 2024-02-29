import logging, requests

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler

model = 'ruBERT2sentiment_test'
model_url = f'http://localhost:8080/predictions/{model}'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a sentiment-analyser bot, please talk to me!")

async def sentiment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sent = update.message.text
    pred = requests.post(model_url, data=sent).text
    answer = f"Model predict this message as {pred}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")



if __name__ == '__main__':
    application = ApplicationBuilder().token('7047738745:AAEw3T1g6GOQtZUF-NhQinNbLq0vOseqyMA').build()
    
    start_handler = CommandHandler('start', start)
    sentiment_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), sentiment)

    application.add_handler(start_handler)
    application.add_handler(sentiment_handler)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    application.run_polling()