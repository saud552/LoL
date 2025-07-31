import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

# تكوين ملفات الكوكيز
COOKIES_DIR = "/workspace/cookies"
YOUTUBE_COOKIES_FILE = os.path.join(COOKIES_DIR, "youtube_cookies.txt")
SPOTIFY_COOKIES_FILE = os.path.join(COOKIES_DIR, "spotify_cookies.txt")
DEEZER_COOKIES_FILE = os.path.join(COOKIES_DIR, "deezer_cookies.txt")

# إنشاء مجلد الكوكيز إذا لم يكن موجوداً
os.makedirs(COOKIES_DIR, exist_ok=True)

admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}
