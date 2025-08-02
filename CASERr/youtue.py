from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
import os
import aiohttp
import requests
import random 
import asyncio
import time
import concurrent.futures 
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
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"خطأ في حذف الملف {file_path}: {e}")

# متغير لتتبع الطلبات النشطة لمنع التكرار
active_requests = {}

# ThreadPoolExecutor للتحميل المتوازي
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

def download_with_ytdlp(url, opts):
    """دالة التحميل المتزامنة للتنفيذ في thread منفصل"""
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
        audio_file = ytdl.prepare_filename(ytdl_data)
        return ytdl_data, audio_file

# دالة التحميل المشتركة
async def download_audio(client, message, text):
    user_id = message.from_user.id if message.from_user else 0
    message_id = message.id
    request_key = f"{user_id}_{text.lower().strip()}"
    unique_key = f"{user_id}_{message_id}_{text.lower().strip()}"
    
    # فحص إذا كان هناك طلب نشط لنفس المستخدم ونفس النص بالضبط
    if request_key in active_requests:
        time_diff = time.time() - active_requests[request_key]
        if time_diff < 5:  # فقط منع التكرار في أول 5 ثوان
            print(f"🚫 تجاهل طلب مكرر: {text} (رسالة {message_id})")
            return  # تجاهل الطلب المكرر
    
    # تسجيل الطلب كنشط
    active_requests[request_key] = time.time()
    print(f"🔄 بدء معالجة طلب جديد: {text} (من المستخدم: {user_id})")
    print(f"📝 الطلبات النشطة حالياً: {len(active_requests)}")
    
    try:
        # فحص الكلمات المحظورة
        if check_forbidden_words(text):
            return await message.reply_text("لا يمكن تنزيل هذا❌")  
        
        h = await message.reply_text("جاري التحميل...")
        audio_file = None
        sedlyf = None
        
        # محاولة التحميل مع تدوير الكوكيز (أقصى 3 محاولات للسرعة)
        max_retries = min(3, len(cookie_manager.cookies_files)) if cookie_manager.cookies_files else 1
        
        download_success = False  # متغير لتتبع نجاح التحميل
        
        for attempt in range(max_retries):
            if download_success:  # إذا نجح التحميل، أوقف الحلقة
                print(f"⏹️ إيقاف المحاولات المتبقية بعد نجاح التحميل")
                break
            try:
                # الحصول على ملف الكوكيز
                cookie_file = cookie_manager.get_next_cookie()
                if not cookie_file:
                    await h.delete()
                    return await message.reply_text("لا توجد ملفات كوكيز متاحة")
                
                # البحث السريع في YouTube
                search = SearchVideos(text, offset=1, mode="dict", max_results=1)
                mi = await loop.run_in_executor(executor, search.result)
                
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
                
                # إعدادات التحميل المحسنة لتجاوز الحظر
                opts = {
                    'format': 'bestaudio[ext=m4a]/bestaudio/best[height<=720]', 
                    'outtmpl': '%(title)s.%(ext)s',
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                    },
                    'extractor_args': {
                        'youtube': {
                            'skip': ['dash', 'hls'],
                            'player_client': ['android', 'web'],
                        }
                    },
                    'no_warnings': True,
                    'ignoreerrors': True,
                }
                
                # إضافة الكوكيز فقط إذا كان الملف موجود
                if cookie_file and os.path.exists(cookie_file):
                    opts["cookiefile"] = cookie_file
                
                # تحميل متوازي لتحسين الأداء
                loop = asyncio.get_event_loop()
                ytdl_data, audio_file = await loop.run_in_executor(
                    executor, download_with_ytdlp, mo, opts
                )
                
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
                
                download_success = True  # تحديد أن التحميل نجح
                print(f"✅ تم إرسال الملف بنجاح: {title}")
                print(f"🚫 إيقاف جميع المحاولات الأخرى للطلب: {text}")
                return  # نجح التحميل، خروج من الدالة بالكامل
                
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
                
    finally:
        # تأكد من إزالة الطلب من قائمة النشطة في جميع الحالات
        if request_key in active_requests:
            del active_requests[request_key]
            print(f"تم إنهاء معالجة الطلب: {text}")

# الأوامر مع /
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل", "يوت", "بحث"], ""), group=1)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    try:
        if await johned(client, message):
            return
    except:
        pass  # تجاهل أخطاء فحص الاشتراك
    
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
    try:
        if await johned(client, message):
            return
    except:
        pass  # تجاهل أخطاء فحص الاشتراك
    
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