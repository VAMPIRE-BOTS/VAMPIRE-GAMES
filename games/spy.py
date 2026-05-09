import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

topics = [
    "Pizza",
    "Anime",
    "Football",
    "Movies",
    "Cats"
]


@router.message(Command("spy"))
async def spy_game(message: Message):

    topic = random.choice(topics)

    await message.answer(
        f"🕵️ Secret Spy Game Started!\n\n"
        f"📌 Topic: {topic}\n\n"
        f"Find The Spy 😭"
    )
