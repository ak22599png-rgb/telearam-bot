from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN =8892069929:AAEYBI0X0vhwFsxjScgCotCmJCt_2mN-if4

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to Solo Leveling Cards!\n\n"
        "Use /spawn to spawn a card."
    )

async def spawn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎴 Card Spawned!\n\n"
        "👤 Sung Jinwoo\n"
        "⭐ Mythic\n\n"
        "Type /catch to claim!"
    )

async def catch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 You caught Sung Jinwoo ⭐ Mythic!"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("spawn", spawn))
    app.add_handler(CommandHandler("catch", catch))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
