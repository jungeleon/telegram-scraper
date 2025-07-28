import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Hole Token und Ziel-Chat-ID aus Umgebungsvariablen
BOT_TOKEN = os.environ["7549886594:AAE5XnkoYuQVqopELJekyGGgLheDMNuJilY"]
NOTIFY_CHAT_ID = os.environ["7115694132"]

# Liste der Schlüsselwörter für Filter
KEYWORDS = ["dringend", "alarm", "kritisch", "wichtig"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        message_text = update.message.text.lower()
        if any(keyword in message_text for keyword in KEYWORDS):
            await context.bot.send_message(
                chat_id=NOTIFY_CHAT_ID,
                text=f"🔔 Neue gefilterte Nachricht:\n\n{update.message.text}"
            )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot läuft...")
    app.run_polling()
