from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","✦ӄɛɛք ʟǟʊɢɦɨռɢ ✘ ᴹᵘᶳᶤᶜ Ᏼo͢Ꭲ ")
BOT_USERNAME = getenv("BOT_USERNAME", "keeplaughingxmusicbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Singing_music_idol_international")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))
