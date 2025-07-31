import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

# تكوين ملفات الكوكيز
COOKIES_DIR = getenv("COOKIES_DIR", "/workspace/cookies")
# يمكنك تغيير هذه الأسماء حسب ما تريد
YOUTUBE_COOKIES_FILE = os.path.join(COOKIES_DIR, "cookies1.txt")  # أو أي اسم تريده
# SPOTIFY_COOKIES_FILE = os.path.join(COOKIES_DIR, "cookies2.txt")  # إذا كنت تريد Spotify
# DEEZER_COOKIES_FILE = os.path.join(COOKIES_DIR, "cookies3.txt")   # إذا كنت تريد Deezer

# إنشاء مجلد الكوكيز إذا لم يكن موجوداً
os.makedirs(COOKIES_DIR, exist_ok=True)

# متغيرات البيئة للبوت
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
OWNER_ID = getenv("OWNER_ID")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AAAKP")

# متغيرات Redis
REDIS_URL = getenv("REDIS_URL", "redis://localhost:6379")

# متغيرات أخرى
DOWNLOAD_FOLDER = getenv("DOWNLOAD_FOLDER", "/workspace/downloads")

admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}
