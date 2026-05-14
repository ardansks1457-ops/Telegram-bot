from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import json

# =========================
# CONFIG OKUMA (JSON)
# =========================
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["TELEGRAM_TOKEN"]

# =========================
# BOT LOGIC
# =========================
async def cevap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "selam":
        await update.message.reply_text("selam")

# =========================
# BOT START
# =========================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevap))

print("Bot çalışıyor...")
app.run_polling()
