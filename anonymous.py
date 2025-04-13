import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

bot = Client("anonymous_sender_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

STICKER_ID = "CAACAgUAAx0CfL_LsAACBq1l_C1ssTP1ZZyrieOyXerC8SxliAACQw8AAj78MVeb3v2OFvEnNB4E"
WELCOME_TEXT = ("🌷 ʜᴇʏ ᴅᴇᴀʀ, ɪ ᴀᴍ 𝙻ᴀᴡʟᴇss 𝙰ɴᴏɴʏᴍᴏᴜs Sᴇɴᴅᴇʀ Bᴏᴛ.\n\n"
                "ᴊᴜsᴛ ғᴏʀᴡᴀʀᴅ ᴍᴇ sᴏᴍᴇ ᴍᴇssᴀɢᴇs ᴏʀ ᴍᴇᴅɪᴀ ᴀɴᴅ ɪ ᴡɪʟʟ 𝙰ɴᴏɴʏᴍᴏᴜs ᴛʜᴀᴛ!\n"
                "𝙸 ᴄᴀɴ ᴀʟsᴏ ᴇᴅɪᴛ ᴄᴀᴘᴛɪᴏɴ🪽\n\n"
                "🛠 **Server**: [Heroku](https://heroku.com)\n"
                "🛠 **Library**: [Pyrogram](https://github.com/pyrogram/pyrogram)\n\n"
                "𝙼ᴀᴅᴇ 𝙱ʏ » [𝙹ᴀʀᴠɪs](https://t.me/CertifiedCoder)")

START_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/CertifiedCoder"),
     InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/CertifiedCoders")],
    [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url="https://t.me/CertifiedNetwork"),
     InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/Doraa_World")]
])

@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    await message.reply_sticker(STICKER_ID)
    await message.reply_text(WELCOME_TEXT, reply_markup=START_KEYBOARD, disable_web_page_preview=True)

@bot.on_message(filters.private & filters.caption)
async def caption_handler(client: Client, message: Message):
    message_id = message.id
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes", callback_data=f"yes-{message_id}"),
         InlineKeyboardButton("No", callback_data=f"no-{message_id}")]
    ])
    await message.reply_text("Do you want to send this anonymously?", reply_markup=keyboard, quote=True)

@bot.on_message(filters.private & (filters.media | filters.text))
async def forward_handler(client: Client, message: Message):
    await message.copy(chat_id=message.chat.id)

if __name__ == "__main__":
    logger.info("Anonymous Sender Bot is up and running!")
    logger.info("Join @CertifiedNetwork for updates.")
    bot.run()
