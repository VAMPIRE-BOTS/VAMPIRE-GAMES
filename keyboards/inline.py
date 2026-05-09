from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

# नोट: YourBotUsername की जगह अपने असली बॉट का यूज़रनेम लिखें (बिना @ के)
BOT_USERNAME = "YourBotUsername" 

# --- START MENU KEYBOARD ---
start_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            # अब यह बटन दबाते ही ग्रुप्स की लिस्ट खुलेगी
            InlineKeyboardButton(
                text="➕ Add Me To Your Group",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true&admin=post_messages+edit_messages+delete_messages"
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
            # यह बटन हेल्प से वापस स्टार्ट मेन्यू पर ले जाएगा
            InlineKeyboardButton(
                text="🔙 Back To Home",
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
