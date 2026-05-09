import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

players = {}


@router.message(Command("bomb"))
async def bomb_game(message: Message):

    if not message.reply_to_message:
        return await message.reply(
            "Reply To A User."
        )

    victim = message.reply_to_message.from_user

    timer = random.randint(5, 20)

    await message.answer(
        f"💣 {victim.mention_html()} GOT THE BOMB!\n\n"
        f"⏳ Explosion In: {timer} Seconds",
        parse_mode="HTML"
    )
