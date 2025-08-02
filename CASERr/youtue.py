from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
import os
import aiohttp
import requests
import random 
import asyncio
import time
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
import subprocess
import json
import wget
from CASERr.CASERr import johned
import redis
import sys
from collections import defaultdict
from yt_dlp import YoutubeDL

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# قائمة الكلمات المحظورة
FORBIDDEN_WORDS = ["سكس", "porn", "xxx", "sex", "نيك", "عري"]

def check_forbidden_words(text):
    """فحص الكلمات المحظورة"""
    text_lower = text.lower()
    return any(word in text_lower for word in FORBIDDEN_WORDS)

# مدير الكوكيز البسيط
class CookieManager:
    def __init__(self):
        self.cookies_files = []
        self.current_index = 0
        self.load_cookies()
    
    def load_cookies(self):
        """تحميل ملفات الكوكيز المتاحة"""
        for i in range(1, 21):  # البحث عن ملفات من cookies1.txt إلى cookies20.txt
            cookie_file = f"cookies{i}.txt"
            if os.path.exists(cookie_file):
                self.cookies_files.append(cookie_file)
        
        print(f"تم العثور على {len(self.cookies_files)} ملف كوكيز")
    
    def get_next_cookie(self):
        """الحصول على ملف الكوكيز التالي"""
        if not self.cookies_files:
            return None
        
        cookie_file = self.cookies_files[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.cookies_files)
        return cookie_file

# إنشاء مدير الكوكيز
cookie_manager = CookieManager()

def clean_temp_files(*files):
    """تنظيف الملفات المؤقتة"""
    for file_path in files:
        try:
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"خطأ في حذف الملف {file_path}: {e}")

# دالة التحميل المشتركة
async def download_audio(client, message, text):
    # فحص الكلمات المحظورة
    if check_forbidden_words(text):
        return await message.reply_text("لا يمكن تنزيل هذا❌")  
    
    h = await message.reply_text("جاري التحميل...")
    audio_file = None
    sedlyf = None
    
    # محاولة التحميل مع تدوير الكوكيز
    max_retries = min(3, len(cookie_manager.cookies_files)) if cookie_manager.cookies_files else 1
    
    for attempt in range(max_retries):
        try:
            # الحصول على ملف الكوكيز
            cookie_file = cookie_manager.get_next_cookie()
            if not cookie_file:
                await h.delete()
                return await message.reply_text("لا توجد ملفات كوكيز متاحة")
            
            # البحث في YouTube
            search = SearchVideos(text, offset=1, mode="dict", max_results=1)
            mi = search.result()
            
            if not mi or not mi.get("search_result") or len(mi["search_result"]) == 0:
                await h.delete()
                return await message.reply_text("لم يتم العثور على نتائج للبحث المطلوب")
            
            mio = mi["search_result"]
            mo = mio[0]["link"]
            thum = mio[0]["title"]
            fridayz = mio[0]["id"]
            
            # تحميل الصورة المصغرة
            kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
            sedlyf = wget.download(kekme, bar=None)
            
            # إعدادات التحميل
            opts = {
                'format': 'bestaudio[ext=m4a]', 
                'outtmpl': '%(title)s.%(ext)s', 
                "cookiefile": cookie_file
            }
            
            with YoutubeDL(opts) as ytdl:
                ytdl_data = ytdl.extract_info(mo, download=True)
                audio_file = ytdl.prepare_filename(ytdl_data)
            
            # إعداد الرسالة
            capy = f"[{thum}]({mo})"
            duration = int(ytdl_data.get("duration", 0))
            title = str(ytdl_data.get("title", "Unknown"))
            performer = str(ytdl_data.get("uploader", "Unknown"))
            
            await h.delete()  # حذف رسالة "جاري التحميل..."
            
            # إرسال الملف الصوتي
            await client.send_audio(
                message.chat.id, 
                audio=audio_file, 
                duration=duration, 
                title=title, 
                performer=performer, 
                file_name=title, 
                thumb=sedlyf,
                caption=capy
            )
            
            # تنظيف الملفات المؤقتة
            clean_temp_files(audio_file, sedlyf)
            return  # نجح التحميل، خروج من الحلقة
            
        except Exception as e:
            print(f"محاولة {attempt + 1} فشلت مع ملف الكوكيز {os.path.basename(cookie_file) if cookie_file else 'غير محدد'}: {e}")
            
            # تنظيف الملفات في حالة الخطأ
            clean_temp_files(audio_file, sedlyf)
            
            # إذا كانت هذه المحاولة الأخيرة
            if attempt == max_retries - 1:
                try:
                    await h.delete()
                except Exception as del_error:
                    print(f"خطأ في حذف رسالة التحميل: {del_error}")
                
                return await message.reply_text("حدث خطأ أثناء التحميل، حاول مرة أخرى")
            
            # انتظار قليل قبل المحاولة التالية
            await asyncio.sleep(1)

# الأوامر مع /
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل", "يوت", "بحث"], ""), group=1)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    
    # استخراج النص من الأمر
    text = message.text.split(" ", 1)
    if len(text) < 2:
        return await message.reply_text("يرجى كتابة ما تريد تحميله بعد الأمر\nمثال: /بحث هيفاء وهبي بوس الواوا")
    
    text = text[1]  # النص بعد الأمر
    await download_audio(client, message, text)

# الأوامر بدون /
@Client.on_message(filters.text & ~filters.command([""]) & ~filters.bot, group=2)
async def handle_text_download(client, message):
    bot_username = client.me.username
    
    # تجاهل الرسائل التي تبدأ بـ / أو تحتوي على @
    if message.text.startswith('/') or '@' in message.text:
        return
    
    # تجاهل الردود على الرسائل
    if message.reply_to_message:
        return
    
    # فحص إذا كان النص يبدأ بأحد الأوامر بدون /
    commands = ["تحميل", "نزل", "تنزيل", "يوتيوب", "حمل", "تنزل", "يوت", "بحث"]
    text = message.text.strip()
    
    # فحص إذا كان النص يبدأ بأحد الأوامر
    is_command = False
    for cmd in commands:
        if text.lower().startswith(cmd.lower() + " "):
            is_command = True
            # استخراج النص بعد الأمر
            text = text[len(cmd):].strip()
            break
    
    if not is_command:
        return  # إذا لم يكن أمر، لا تفعل شيئاً
    
    if not text:  # إذا لم يكن هناك نص بعد الأمر
        return await message.reply_text("يرجى كتابة ما تريد تحميله بعد الأمر\nمثال: بحث عليكي عيون")
    
    await download_audio(client, message, text)

print("✅ تم تحميل النظام البسيط والفعال!")
print(f"📊 ملفات الكوكيز المتاحة: {len(cookie_manager.cookies_files)}")