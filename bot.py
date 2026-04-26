import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# إعداد السجل
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 أهلاً بك! البوت يعمل بنجاح.\n\nأرسل أي رسالة وسأعيدها لك."
    )

# الرد على أي رسالة
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"📩 قلت: {text}")

# تشغيل البوت
def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN غير موجود")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
