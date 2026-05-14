import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("TELEGRAM_TOKEN bulunamadı!")
    exit()

async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        if update.message.text.lower() == "selam":
            await update.message.reply_text("selam")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

print("Bot çalışıyor...")
app.run_polling()
