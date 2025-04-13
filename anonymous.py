import os
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from telegram.error import RetryAfter, BadRequest

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.WARNING,
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_TEXT = (
    "\U0001f337 <b>ʜᴇʏ ᴅᴇᴀʀ, ɪ ᴀᴍ  𝙻ᴀᴡʟᴇss 𝙰ɴᴏɴʏᴍᴏᴜs Sᴇɴᴅᴇʀ Bᴏᴛ.</b>\n\n"
    "ᴊᴜsᴛ ғᴏʀᴡᴀʀᴅ ᴍᴇ sᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴏʀ ᴍᴇᴅɪᴀ ᴀɴᴅ ɪ ᴡɪʟʟ 𝙰ɴᴏɴʏᴍᴏᴜs ᴛʜᴀᴛ!\n"
    "𝙸 ᴄᴀɴ ᴀʟsᴏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴ 🪽\n\n"
    "🔧 <b>Server</b>: <a href='https://heroku.com'>Heroku</a>\n"
    "🔧 <b>Library</b>: <a href='https://github.com/python-telegram-bot/python-telegram-bot'>python-telegram-bot</a>\n\n"
    "<b>𝙼ᴀᴅᴇ 𝙱ʏ »</b> <a href='https://t.me/CertifiedCoder'>𝙹ᴀʀᴠɪs</a>"
)

START_KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/CertifiedCoder"),
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/CertifiedCoders")
    ],
    [
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CertifiedNetwork"),
        InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/CertifiedCoders/Anonymous-Bot")
    ]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != "private":
        return
    try:
        await update.message.reply_text(WELCOME_TEXT, reply_markup=START_KEYBOARD, disable_web_page_preview=True, parse_mode="HTML")
    except UnicodeEncodeError as ue:
        logger.error(f"UnicodeEncodeError in welcome text: {ue}")
        await update.message.reply_text("👋 Welcome! Forward me a message to send anonymously.")

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != "private":
        return
    try:
        message = update.message
        await message.copy(chat_id=message.chat.id)
        logger.info(f"Message from {update.effective_user.id} sent anonymously.")
    except RetryAfter as e:
        await asyncio.sleep(e.retry_after + 1)
        logger.warning(f"Rate limit hit. Retrying after {e.retry_after} seconds.")
    except BadRequest as e:
        logger.warning(f"BadRequest: {e.message}")
    except Exception as e:
        logger.error(f"Error handling message: {e}")

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text("✅ Received your choice.")
        logger.info(f"Callback received: {update.callback_query.data}")
    except Exception as e:
        logger.error(f"Callback error: {e}")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update caused error: {context.error}")

if __name__ == '__main__':
    logger.warning("Bot is starting...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_error_handler(error_handler)
    app.run_polling()