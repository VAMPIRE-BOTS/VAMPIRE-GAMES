import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("couple"))
async def couple_game(message: Message):

    percentages = random.randint(1, 100)

    await message.answer(
        f"💘 Perfect Couple Match\n\n❤️ Love Percentage: {percentages}%"
    )


@router.message(Command("love"))
async def love_game(message: Message):

    love = random.randint(1, 100)

    await message.answer(
        f"💕 Love Meter: {love}% 😭"
    )
