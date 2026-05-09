from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from aiogram.filters import CommandStart

from keyboards.inline import start_buttons
from config import START_IMAGE
from database.users import add_user

router = Router()


START_TEXT = """
✨ Welcome To All In One Games Bot ✨

🎮 The Ultimate Group Chaos Games Bot.

Play:
💣 Bomb Battle
🕵️ Secret Spy
🎭 Fake Identity
⚡ Fastest Finger
📖 Story Mode
👻 Ghost Reply

🔥 Premium Multiplayer Experience
⚔️ Real-Time Group Games
🏆 Leaderboards & Rewards

Add Me To Your Group And Start The Chaos.
"""


HELP_TEXT = """
📚 Available Commands

/start - Start The Bot
/help - Open Help Menu

🎮 Games Commands

/bomb - Pass The Bomb
/spy - Secret Spy Game
/identity - Fake Identity
/finger - Fastest Finger
/story - One Word Story
/ghost - Ghost Reply
/lie - Lie Detector

👤 User Commands

/profile - Your Profile
/leaderboard - Global Rankings

⚡ More Games Coming Soon
"""


@router.message(CommandStart())
async def start_command(message: Message):

    await add_user(message.from_user.id)

    await message.answer_photo(
        photo=START_IMAGE,
        caption=START_TEXT,
        reply_markup=start_buttons
    )


@router.callback_query(F.data == "help_menu")
async def help_menu(callback: CallbackQuery):

    await callback.message.edit_caption(
        caption=HELP_TEXT,
        reply_markup=start_buttons
    )
