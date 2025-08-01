import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Hole Token und Ziel-Chat-ID aus Umgebungsvariablen
BOT_TOKEN = os.environ["BOT_TOKEN"]
NOTIFY_CHAT_ID = os.environ["NOTIFY_CHAT_ID"]

# Liste der Schlüsselwörter für Filter
KEYWORDS = ["Wipkingen", "8037", "8057", "8005", "Kreis 10", "Kreis 6", "Kreis 5", "K10", "K6", "K5"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Nachricht empfangen:", update.message.text)
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
