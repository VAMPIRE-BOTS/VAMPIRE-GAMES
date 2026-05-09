from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from aiogram.filters import CommandStart

from keyboards.inline import start_buttons
from config import START_IMAGE
from database.users import add_user

router = Router()


START_TEXT = """
✨ **Welcome To Vampire Games Bot** ✨

🎮 *Premium Multiplayer Chaos Games*

💣 Bomb • 🕵️ Spy • 🎭 Identity
⚡ Finger • 📖 Story • 👻 Ghost
💰 Economy • 💘 Love • 🧩 Puzzle

🔥 **Add Me To Your Group**
And Start The Chaos! ⚡
"""


HELP_TEXT = """
📚 **VAMPIRE GAMES HELP MENU**

🎮 **GAMES**
• `/bomb` - Bomb Pass Game
• `/spy` - Find the Spy
• `/identity` - Role Play
• `/finger` - Speed Click
• `/story` - One Word Story
• `/ghost` - Ghost Reply
• `/lie` - Lie Detector

💰 **ECONOMY**
• `/daily` - Get Daily Coins
• `/claim` - Claim Rewards
• `/rob` - Rob Coins (Reply)
• `/pay` - Send Coins
• `/kill` - Kill Action

💘 **LOVE & FUN**
• `/couple` - Match Maker
• `/love` - Love Meter
• `/kiss` / `/hug` - Actions
• `/brain` - IQ Level
• `/puzzle` - Solve It
• `/truth` / `/dare` - Party Game

👤 **USER**
• `/start` • `/help` • `/profile` • `/leaderboard`

📢 **OWNER**
• `/broadcast` - Global Msg

✨ *New features like Clans coming soon!*
"""

@router.message(CommandStart())
async def start_command(message: Message):

    await add_user(message.from_user.id)

    await message.answer_photo(
        photo=START_IMAGE,
        caption=START_TEXT,
        reply_markup=start_buttons,
        parse_mode="Markdown"
    )


@router.callback_query(F.data == "help_menu")
async def help_menu(callback: CallbackQuery):
    # कैप्शन को एडिट करने से पहले यह चेक करेगा कि टेक्स्ट लिमिट में है
    try:
        await callback.message.edit_caption(
            caption=HELP_TEXT,
            reply_markup=start_buttons,
            parse_mode="Markdown"
        )
    except Exception:
        # अगर फिर भी बड़ा होता है, तो यह बिना फोटो के सीधा मैसेज भेज देगा (सुरक्षा के लिए)
        await callback.message.answer(HELP_TEXT, parse_mode="Markdown")
        
    await callback.answer()
