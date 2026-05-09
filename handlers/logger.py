from aiogram import Router, F
from aiogram.types import Message

from config import LOG_GROUP_ID  # 👈 add this in config.py

router = Router()


# 👤 NEW USER START LOG
@router.message(F.text == "/start")
async def log_start(message: Message):

    user = message.from_user

    text = (
        f"📥 NEW USER STARTED BOT\n\n"
        f"👤 Name: {user.full_name}\n"
        f"🆔 ID: {user.id}\n"
        f"🔗 Username: @{user.username if user.username else 'None'}"
    )

    try:
        await message.bot.send_message(LOG_GROUP_ID, text)
    except:
        pass


# ➕ BOT ADDED TO GROUP LOG
@router.message(F.new_chat_members)
async def bot_added_to_group(message: Message):

    for member in message.new_chat_members:

        if member.id == (await message.bot.get_me()).id:

            chat = message.chat
            user = message.from_user

            text = (
                f"➕ BOT ADDED TO GROUP\n\n"
                f"👥 Group Name: {chat.title}\n"
                f"🆔 Group ID: {chat.id}\n\n"
                f"👤 Added By:\n"
                f"Name: {user.full_name}\n"
                f"ID: {user.id}\n"
                f"Username: @{user.username if user.username else 'None'}"
            )

            try:
                await message.bot.send_message(LOG_GROUP_ID, text)
            except:
                pass
