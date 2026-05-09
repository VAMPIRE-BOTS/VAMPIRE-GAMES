from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

# --- START MENU KEYBOARD ---
start_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Add Me To Group",
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
                text="📚 Help Menu",
                callback_data="help_menu"
            )
        ]
    ]
)

# --- HELP MENU KEYBOARD (With Back Button) ---
help_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Back to Home",
                callback_data="back_to_start"
            )
        ],
        [
            InlineKeyboardButton(
                text="🆘 Support Group",
                url=f"https://t.me/{SUPPORT_GROUP}"
            )
        ]
    ]
)
