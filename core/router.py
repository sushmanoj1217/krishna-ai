import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Direct values डाल दिए ताकि बिना .env के भी काम करे
BOT_TOKEN = "7987248090:AAGMOE56FV3H_eHFBbVF1PNCUPS_GMwmaeA"
USER_ID = 1266551700

# Telegram Bot instance बनाएं
app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("✅ Krishna AI Connected & Running!")
    else:
        await update.message.reply_text("❌ Access Denied.")

def handle_telegram():
    app.add_handler(CommandHandler("start", start))
    # Non-blocking run
    app.run_polling(stop_signals=None)
