from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from aiogram.filters import CommandStart

from keyboards.inline import start_buttons
from config import START_IMAGE
from database.users import add_user

router = Router()


START_TEXT = """
✨ Welcome To Vampire Games Bot ✨

🎮 Premium Multiplayer Chaos Games

💣 Bomb Battles
🕵️ Secret Spy
🎭 Fake Identity
⚡ Fastest Finger
📖 Story Mode
👻 Ghost Reply

🔥 Add Me To Your Group
And Start The Chaos 😭
"""


HELP_TEXT = """
📚 VAMPIRE GAMES HELP MENU

━━━━━━━━━━━━━━━

🎮 AVAILABLE GAMES

💣 /bomb
Pass The Bomb Before It Explodes.

🕵️ /spy
Find The Secret Spy In Group.

🎭 /identity
Copy Another User's Typing Style.

⚡ /finger
Fastest Click Wins The Round.

📖 /story
Create Funny One Word Stories.

👻 /ghost
Continue Haunted Messages.

😭 /lie
Funny Lie Detector Game.

━━━━━━━━━━━━━━━

👤 USER COMMANDS

/start - Start The Bot
/help - Open Help Menu

/profile - View Your Profile
/leaderboard - Global Rankings

━━━━━━━━━━━━━━━

📢 OWNER COMMANDS

/broadcast - Send Message To All Users

━━━━━━━━━━━━━━━

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

    await callback.answer()
