from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

start_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Add Me",
                url="https://t.me/YourBotUsername?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 Owner",
                url=f"https://t.me/{OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text="🆘 Support",
                url=f"https://t.me/{SUPPORT_GROUP}"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Updates",
                url=f"https://t.me/{SUPPORT_CHANNEL}"
            ),
            InlineKeyboardButton(
                text="📚 Help",
                callback_data="help_menu"
            )
        ]
    ]
)
