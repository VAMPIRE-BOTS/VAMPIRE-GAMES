from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("finger"))
async def finger_game(message: Message):

    await message.answer(
        "⚡ FASTEST FINGER ROUND STARTED!\n\n"
        "PRESS FAST 😭"
    )
