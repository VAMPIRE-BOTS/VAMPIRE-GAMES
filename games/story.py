from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("story"))
async def story_game(message: Message):

    await message.answer(
        "📖 One Word Story Started!\n\n"
        "Everyone Send ONLY ONE WORD."
    )
