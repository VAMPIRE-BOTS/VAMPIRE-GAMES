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
💰 Economy System
💘 Love & Couples Games
🧩 Puzzle & Brain Games

🔥 Add Me To Your Group
And Start The Chaos 😭
"""


HELP_TEXT = """
📚 VAMPIRE GAMES HELP MENU

━━━━━━━━━━━━━━━

🎮 CORE GAMES

💣 /bomb
Pass The Bomb Before It Explodes.

🕵️ /spy
Find The Secret Spy In Group.

🎭 /identity
Fake Identity Role Game.

⚡ /finger
Fastest Click Wins The Round.

📖 /story
One Word Story Game.

👻 /ghost
Ghost Reply Challenge.

😭 /lie
Lie Detector Game.

━━━━━━━━━━━━━━━

💰 ECONOMY SYSTEM

🎁 /daily
Claim Daily Rewards.

🪙 /claim
Claim Coins Reward.

💸 /rob
Rob Coins From User (Reply Required).

💰 /pay
Send Coins To Users.

🔪 /kill
Funny Kill Action Game.

━━━━━━━━━━━━━━━

💘 LOVE & RELATIONSHIP

💞 /couple
Couple Match Percentage.

💕 /love
Love Meter Checker.

💋 /kiss @user
Kiss Someone.

🤗 /hug @user
Hug Someone.

━━━━━━━━━━━━━━━

😈 FUN / PARTY COMMANDS

🧠 /brain
Check IQ Level.

🧩 /puzzle
Solve Random Puzzle.

🔥 /truth
Truth Question Game.

😈 /dare
Dare Challenge Game.

━━━━━━━━━━━━━━━

👤 USER COMMANDS

/start - Start Bot
/help - Open Help Menu
/profile - Your Profile
/leaderboard - Global Ranking

━━━━━━━━━━━━━━━

📢 OWNER COMMANDS

/broadcast - Send Message To All Users

━━━━━━━━━━━━━━━

⚡ MORE FEATURES

- Clan System Coming Soon
- PvP Battles Coming Soon
- AI Chaos Events Coming Soon
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
