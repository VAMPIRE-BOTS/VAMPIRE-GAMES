from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("identity"))
async def identity_game(message: Message):

    await message.answer(
        "🎭 Fake Identity Started!\n\n"
        "Copy Someone's Typing Style 😭"
    )
