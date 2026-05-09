from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("ghost"))
async def ghost_game(message: Message):

    await message.answer(
        "👻 Ghost Reply Started!\n\n"
        "Continue The Haunted Message 😭"
    )
