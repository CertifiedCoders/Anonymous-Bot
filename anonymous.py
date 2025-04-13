import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

STICKER_ID = "CAACAgUAAx0CfL_LsAACBq1l_C1ssTP1ZZyrieOyXerC8SxliAACQw8AAj78MVeb3v2OFvEnNB4E"

WELCOME_TEXT = (
    "\U0001f337 ʜᴇʏ ᴅᴇᴀʀ, ɪ ᴀᴍ  𝙻ᴀᴡʟᴇss 𝙰ɴᴏɴʏᴍᴏᴜs Sᴇɴᴅᴇʀ Bᴏᴛ.\n\n"
    "ᴊᴜsᴛ ғᴏʀᴡᴀʀᴅ ᴍᴇ sᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴏʀ ᴍᴇᴅɪᴀ ᴀɴᴅ ɪ ᴡɪʟʟ 𝙰ɴᴏɴʏᴍᴏᴜs ᴛʜᴀᴛ!\n"
    "𝙸 ᴄᴀɴ ᴀʟsᴏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴ\udcfa\n\n"
    "\ud83d\udee0 **Server**: [Heroku](https://heroku.com)\n"
    "\ud83d\udee0 **Library**: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)\n\n"
    "𝙼ᴀᴅᴇ 𝙱ʏ » [𝙹ᴀʀᴠɪs](https://t.me/CertifiedCoder)"
)

START_KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/CertifiedCoder"),
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/CertifiedCoders")
    ],
    [
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CertifiedNetwork"),
        InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/Doraa_World")
    ]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_sticker(chat_id=update.effective_chat.id, sticker=STICKER_ID)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=START_KEYBOARD, disable_web_page_preview=True)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.caption:
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Yes", callback_data=f"yes-{update.message.message_id}"),
                InlineKeyboardButton("No", callback_data=f"no-{update.message.message_id}")
            ]
        ])
        await update.message.reply_text("Do you want to send this anonymously?", reply_markup=keyboard)
    else:
        await update.message.copy(chat_id=update.effective_chat.id)

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("✅ Received your choice.")

if __name__ == '__main__':
    logger.info("Bot is running...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, message_handler))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.run_polling()
