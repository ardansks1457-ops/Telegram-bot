from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "selam":
        await update.message.reply_text("selam")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

app.run_polling()	
