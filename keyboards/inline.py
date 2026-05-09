from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

# अपने बॉट का यूज़रनेम यहाँ लिखें (बिना @ के)
BOT_USERNAME = "AllGameProBot" 

# मुख्य स्टार्ट मेन्यू
start_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Add Me To Your Group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
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

# हेल्प मेन्यू के लिए कीबोर्ड (इसमें Back Button और Updates दोनों रखें)
help_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Back To Home",
                callback_data="back_to_start"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Updates",
                url=f"https://t.me/{SUPPORT_CHANNEL}"
            ),
            InlineKeyboardButton(
                text="🆘 Support",
                url=f"https://t.me/{SUPPORT_GROUP}"
            )
        ]
    ]
)
