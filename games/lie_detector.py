import random

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

questions = [
    "Have You Ever Skipped School?",
    "Do You Simp In Secret?",
    "Have You Ever Lied To Your Friends?"
]


@router.message(Command("lie"))
async def lie_game(message: Message):

    question = random.choice(questions)

    lie_percent = random.randint(1, 100)

    await message.answer(
        f"🤖 Lie Detector\n\n"
        f"❓ {question}\n\n"
        f"📊 Lie Percentage: {lie_percent}% 😭"
    )
