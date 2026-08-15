import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --- SAFE CONFIGURATION LOADER ---
# (os.getenv("VAR") or "default") ka matlab hai agar variable khali hai, 
# toh default value use karo. Isse int() error nahi aayega.

API_ID = int(os.getenv("API_ID") or "10658015")
API_HASH = os.getenv("API_HASH") or "a0087bca748f86698c53d291c9e5b3af"
BOT_TOKEN = os.getenv("BOT_TOKEN") or "8126555519:AAElKkaaomDx0CRNIDnrgDiAHODxxvq82E0"
OWNER_ID = int(os.getenv("OWNER_ID") or "7657218453")
OWNER_USERNAME = os.getenv("OWNER_USERNAME") or "WTF_WhyMeeh"
BOT_USERNAME = os.getenv("BOT_USERNAME") or "Uchihasibot"

# Database & Logger
MONGO_DB_URI = os.getenv("MONGO_DB_URI") or "mongodb+srv://macudini67_db_user:JTByODfwRj93MXWV@cluster0.hin0kat.mongodb.net/?appName=Cluster0"
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID") or "-1002862997310")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO") or "https://github.com/NoxxOP/ShrutiMusic"
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH") or "main"
GIT_TOKEN = os.getenv("GIT_TOKEN")

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL") or "https://t.me/ShrutiBots"
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP") or "https://t.me/ShrutiBotsSupport"
INSTAGRAM = os.getenv("INSTAGRAM") or "https://instagram.com/yaduwanshi_nand"
YOUTUBE = os.getenv("YOUTUBE") or "https://youtube.com/@NandEditz"
GITHUB = os.getenv("GITHUB") or "https://github.com/NoxxOP"
DONATE = os.getenv("DONATE") or "https://t.me/ShrutiBots/91"
PRIVACY_LINK = os.getenv("PRIVACY_LINK") or "https://graph.org/Privacy-Policy-05-01-30"

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT") or "300")
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT") or "25")

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT") or "104857600")
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT") or "2145386496")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# String Sessions (Assistant)
STRING1 = os.getenv("STRING_SESSION") or "BAHvrjIAKoucFexG-a8wEEDO4bDZSp5Uci064mhze9c4d_rpdkdfuYmfWr6dqiRG90L0oQTHUmmKJymH8KnTyZNPZgbVLyPzIviJV9NQwWgj_DHg6c-MO9FxnMKuH8wRwycQKAvPxpUmkj2HOFOypygESzk-vZFz50lrXPkwwJpko6OAFXiajYzkQb1e6wB0QqnQMTfhoU520WfoDjRq-pywPOCeWpliPBERfsQrnI4pjuRxVmxP8bnNzK9J5TjRZ4v8gQ6mBzuCavk5AYGnq8euRmEEq5IAuINYCc0wMB4JN6TFPClyl6yYhAl5lF1hBnIjnN9qaQEYRG7tJRnltBEgyuVeswAAAAIJk9ZLAA"
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT") or False)

START_IMG_URL = os.getenv("START_IMG_URL") or "https://files.catbox.moe/7q8bfg.jpg"
PING_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
STATS_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/eehxb4.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ERROR_FORMAT = int("\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35")
DT_Management = "\x40\x53\x68\x72\x75\x74\x69\x53\x75\x70\x70\x6f\x72\x74\x42\x6f\x74"

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )
