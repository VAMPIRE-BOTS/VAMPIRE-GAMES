from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID", "0"))

MONGO_DB_URI = getenv("MONGO_DB_URI")

OWNER_USERNAME = "yourusername"
SUPPORT_GROUP = "yourgroup"
SUPPORT_CHANNEL = "yourchannel"

START_IMAGE = "https://i.imgur.com/yourimage.jpg"
