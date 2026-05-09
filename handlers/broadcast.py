from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import OWNER_ID
from database.mongo import usersdb

router = Router()


@router.message(Command("broadcast"))
async def broadcast_handler(message: Message):

    # OWNER CHECK
    if message.from_user.id != OWNER_ID:
        return

    # MESSAGE CHECK
    text = message.text.split(None, 1)

    if len(text) < 2:
        return await message.reply(
            "Usage:\n/broadcast your message"
        )

    broadcast_text = text[1]

    users = usersdb.find({})

    sent = 0
    failed = 0

    # SEND TO ALL USERS
    async for user in users:

        try:
            await message.bot.send_message(
                user["user_id"],
                broadcast_text
            )

            sent += 1

        except:
            failed += 1

    # FINAL REPORT
    await message.reply(
        f"📢 Broadcast Completed\n\n"
        f"✅ Sent: {sent}\n"
        f"❌ Failed: {failed}"
    )
