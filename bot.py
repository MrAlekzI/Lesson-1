import logging
import settings
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(rf"Hello {user.mention_html()}!") #User greetings

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: #echo reply
    await update.message.reply_text(update.message.text)    

def main():
    mybot = ApplicationBuilder().token(settings.TOKEN.build()
    mybot.add_handler(CommandHandler('start',start))
    logging.info("The bot has started")
    mybot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    mybot.run_polling()

if __name__ == "__main__":
    main()
