from os import getenv
from dotenv import load_dotenv

load_dotenv()

# BOT CORE
BOT_TOKEN = getenv("BOT_TOKEN", "")

# OWNER INFO
OWNER_ID = int(getenv("OWNER_ID", "0"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "yourusername")

# DATABASE
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# SUPPORT INFO
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "yourgroup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "yourchannel")

# MEDIA
START_IMAGE = getenv(
    "START_IMAGE",
    "https://i.imgur.com/yourimage.jpg"
)

# LOGGER GROUP (NEW - for your logger system)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "0"))
