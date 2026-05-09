import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

puzzles = [
    "What Has Keys But Can't Open Locks?\n\nAnswer: Keyboard",
    "What Runs But Never Walks?\n\nAnswer: Water",
    "What Has Hands But Cannot Clap?\n\nAnswer: Clock"
]


@router.message(Command("puzzle"))
async def puzzle_game(message: Message):

    await message.answer(
        f"🧩 Puzzle Time\n\n{random.choice(puzzles)}"
    )
