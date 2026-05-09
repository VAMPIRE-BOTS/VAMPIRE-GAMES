import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("kiss"))
async def kiss_user(message: Message):

    if not message.reply_to_message:
        return await message.reply(
            "Reply To Someone."
        )

    user = message.from_user.first_name
    target = message.reply_to_message.from_user.first_name

    await message.answer(
        f"💋 {user} kissed {target} 😭"
    )


@router.message(Command("hug"))
async def hug_user(message: Message):

    if not message.reply_to_message:
        return await message.reply(
            "Reply To Someone."
        )

    user = message.from_user.first_name
    target = message.reply_to_message.from_user.first_name

    await message.answer(
        f"🤗 {user} hugged {target}"
    )


@router.message(Command("truth"))
async def truth_game(message: Message):

    truths = [
        "Who Is Your Secret Crush?",
        "Have You Ever Lied To Friends?",
        "Who Do You Stalk Most?"
    ]

    await message.answer(
        f"😈 Truth:\n\n{random.choice(truths)}"
    )


@router.message(Command("dare"))
async def dare_game(message: Message):

    dares = [
        "Spam 5 Emojis 😭",
        "Change Your DP For 1 Hour",
        "Send A Cringe Message"
    ]

    await message.answer(
        f"🔥 Dare:\n\n{random.choice(dares)}"
    )


@router.message(Command("brain"))
async def brain_game(message: Message):

    iq = random.randint(1, 200)

    await message.answer(
        f"🧠 Brain Power: {iq} IQ 😭"
    )
