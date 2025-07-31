from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
import time 
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from config import *
import numpy as np
from yt_dlp import YoutubeDL
from CASERr.CASERr import get_channel, johned
from io import BytesIO
import aiofiles
import wget
from pyrogram.types import *
import json
from config import YOUTUBE_COOKIES_FILE

# قائمة الكلمات المحظورة
yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]

# نظام تدوير الكوكيز
class CookieManager:
    def __init__(self, cookies_dir="/workspace/cookies"):
        self.cookies_dir = cookies_dir
        self.current_index = 0
        self.cookies_files = []
        self.load_cookies_files()
    
    def load_cookies_files(self):
        """تحميل قائمة ملفات الكوكيز المتاحة"""
        try:
            if os.path.exists(self.cookies_dir):
                # البحث عن ملفات الكوكيز
                for file in os.listdir(self.cookies_dir):
                    if file.endswith('.txt') and 'cookie' in file.lower():
                        file_path = os.path.join(self.cookies_dir, file)
                        if os.path.getsize(file_path) > 100:  # التأكد من أن الملف ليس فارغاً
                            self.cookies_files.append(file_path)
                
                # إضافة الملف الافتراضي إذا كان موجوداً
                if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                    if YOUTUBE_COOKIES_FILE not in self.cookies_files:
                        self.cookies_files.append(YOUTUBE_COOKIES_FILE)
            
            print(f"تم العثور على {len(self.cookies_files)} ملف كوكيز")
            
        except Exception as e:
            print(f"خطأ في تحميل ملفات الكوكيز: {e}")
            # استخدام الملف الافتراضي كاحتياطي
            if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                self.cookies_files = [YOUTUBE_COOKIES_FILE]
    
    def get_next_cookie(self):
        """الحصول على ملف الكوكيز التالي"""
        if not self.cookies_files:
            return None
        
        cookie_file = self.cookies_files[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.cookies_files)
        
        print(f"استخدام ملف الكوكيز: {os.path.basename(cookie_file)}")
        return cookie_file
    
    def get_random_cookie(self):
        """الحصول على ملف كوكيز عشوائي"""
        if not self.cookies_files:
            return None
        
        cookie_file = random.choice(self.cookies_files)
        print(f"استخدام ملف الكوكيز العشوائي: {os.path.basename(cookie_file)}")
        return cookie_file

# إنشاء مدير الكوكيز
cookie_manager = CookieManager()

def check_forbidden_words(text):
    """فحص النص للكلمات المحظورة"""
    text_lower = text.lower()
    for word in yoro:
        if word.lower() in text_lower:
            return True
    return False

def clean_temp_files(*files):
    """تنظيف الملفات المؤقتة"""
    for file_path in files:
        try:
            if os.path.exists(file_path):
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
    max_retries = len(cookie_manager.cookies_files) if cookie_manager.cookies_files else 1
    
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
            sedlyf = wget.download(kekme)
            
            # إعدادات التحميل مع الكوكيز الحالي
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
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل", "يوت", "بحث"], ""), group=71328934)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    if await johned(client, message):
     return
    
    # استخراج النص من الأمر
    text = message.text.split(" ", 1)
    if len(text) < 2:
        return await message.reply_text("يرجى كتابة ما تريد تحميله بعد الأمر\nمثال: /بحث هيفاء وهبي بوس الواوا")
    
    text = text[1]  # النص بعد الأمر
    await download_audio(client, message, text)

# الأوامر بدون /
@Client.on_message(filters.text, group=71328935)
async def handle_text_download(client, message):
    bot_username = client.me.username
    if await johned(client, message):
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
        return await message.reply_text("يرجى كتابة ما تريد تحميله بعد الأمر\nمثال: بحث هيفاء وهبي بوس الواوا")
    
    await download_audio(client, message, text)