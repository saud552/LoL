import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

# تكوين ملفات الكوكيز
COOKIES_DIR = "/workspace/cookies"
# يمكنك تغيير هذه الأسماء حسب ما تريد
YOUTUBE_COOKIES_FILE = os.path.join(COOKIES_DIR, "cookies1.txt")  # أو أي اسم تريده
# SPOTIFY_COOKIES_FILE = os.path.join(COOKIES_DIR, "cookies2.txt")  # إذا كنت تريد Spotify
# DEEZER_COOKIES_FILE = os.path.join(COOKIES_DIR, "cookies3.txt")   # إذا كنت تريد Deezer

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
