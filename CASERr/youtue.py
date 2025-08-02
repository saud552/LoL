from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
import time 
import hashlib
import threading
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
from collections import defaultdict

# ========== إعدادات النظام بدون قيود ==========
print("🚀 نظام التحميل المطور - بدون قيود أو حدود!")
print("📊 الإعدادات:")
print("   ✅ التحميلات المتزامنة: غير محدودة")
print("   ✅ حجم الملفات: غير محدود") 
print("   ✅ طول النصوص: غير محدود")
print("   ✅ معدل الطلبات: غير محدود")
print("   ✅ استخدام الكوكيز: غير محدود")
print("   ✅ مهلة العمليات: غير محدودة")
print("   ✅ حجم الكاش: غير محدود")
print("=" * 50)

# قائمة الكلمات المحظورة
yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]

# ========== نظام منع التكرار وتتبع الطلبات ==========
active_downloads = {}  # تتبع التحميلات النشطة
request_tracking = {}  # تتبع جميع الطلبات
cache_lock = threading.RLock()  # حماية من race conditions

class RequestTracker:
    """فئة لتتبع الطلبات ومنع التكرار"""
    def __init__(self, request_id, user_id, search_text):
        self.request_id = request_id
        self.user_id = user_id
        self.search_text = search_text.lower().strip()
        self.video_id = None
        self.is_completed = False
        self.is_cancelled = False
        self.start_time = time.time()
        self.stage = "initialized"
        
        # تسجيل الطلب
        with cache_lock:
            request_tracking[request_id] = self
    
    def update_stage(self, stage):
        """تحديث مرحلة الطلب"""
        if not self.is_cancelled:
            self.stage = stage
            print(f"🔄 طلب {self.request_id[:8]}: {stage}")
    
    def complete(self, success=True):
        """إكمال الطلب"""
        self.is_completed = True
        status = "✅" if success else "❌"
        print(f"{status} طلب {self.request_id[:8]} اكتمل")
        
        # إزالة من التتبع
        with cache_lock:
            if self.request_id in request_tracking:
                del request_tracking[self.request_id]
    
    def cancel(self, reason="تم الإلغاء"):
        """إلغاء الطلب"""
        self.is_cancelled = True
        self.stage = f"cancelled: {reason}"
        print(f"🚫 طلب {self.request_id[:8]} تم إلغاؤه: {reason}")

def generate_request_id(user_id, text):
    """إنشاء معرف فريد للطلب"""
    unique_str = f"{user_id}_{text.lower().strip()}_{int(time.time() * 1000)}"
    return hashlib.md5(unique_str.encode()).hexdigest()

def check_duplicate_request(user_id, text):
    """فحص الطلبات المكررة النشطة"""
    with cache_lock:
        search_hash = text.lower().strip()
        current_time = time.time()
        
        for req_id, tracker in request_tracking.items():
            if (tracker.user_id == user_id and 
                tracker.search_text == search_hash and
                not tracker.is_completed and
                not tracker.is_cancelled and
                current_time - tracker.start_time < 300):  # 5 دقائق
                return tracker
        
        return None

def cancel_related_requests(video_id, exclude_request_id=None):
    """إلغاء جميع الطلبات المتعلقة بنفس الفيديو"""
    with cache_lock:
        cancelled_count = 0
        for req_id, tracker in list(request_tracking.items()):
            if (tracker.video_id == video_id and 
                not tracker.is_completed and
                not tracker.is_cancelled and
                req_id != exclude_request_id):
                tracker.cancel("ملف متوفر من طلب آخر")
                cancelled_count += 1
        
        if cancelled_count > 0:
            print(f"🚫 تم إلغاء {cancelled_count} طلب متكرر للفيديو {video_id}")

# ========== نظام الكاش المتقدم ==========
search_cache = {}  # كاش البحثات
download_cache = {}  # كاش الملفات المحملة

def generate_cache_key(text):
    """إنشاء مفتاح فريد للكاش"""
    return hashlib.md5(text.lower().strip().encode()).hexdigest()

def get_cached_search(text):
    """البحث في كاش البحثات"""
    with cache_lock:
        cache_key = generate_cache_key(text)
        if cache_key in search_cache:
            cached_result = search_cache[cache_key]
            # فحص انتهاء صلاحية الكاش (30 دقيقة)
            if time.time() - cached_result['timestamp'] < 1800:
                print(f"📋 استخدام نتيجة محفوظة للبحث: {text[:30]}...")
                return cached_result['data']
            else:
                # إزالة النتيجة منتهية الصلاحية
                del search_cache[cache_key]
        return None

def cache_search_result(text, result):
    """حفظ نتيجة البحث في الكاش"""
    with cache_lock:
        cache_key = generate_cache_key(text)
        search_cache[cache_key] = {
            'data': result,
            'timestamp': time.time()
        }
        print(f"💾 تم حفظ نتيجة البحث في الكاش: {text[:30]}...")

def get_cached_download(video_id):
    """البحث عن ملف محمل في الكاش"""
    with cache_lock:
        if video_id in download_cache:
            cached_download = download_cache[video_id]
            # فحص انتهاء صلاحية الكاش (2 ساعة للملفات)
            if time.time() - cached_download['timestamp'] < 7200:
                # فحص وجود الملف فعلياً
                if os.path.exists(cached_download['audio_path']):
                    print(f"📁 استخدام ملف محمل مسبقاً: {video_id}")
                    return cached_download
                else:
                    # إزالة الملف المفقود من الكاش
                    del download_cache[video_id]
        return None

def cache_download_result(video_id, audio_path, thumbnail_path, metadata):
    """حفظ الملف المحمل في الكاش"""
    with cache_lock:
        download_cache[video_id] = {
            'audio_path': audio_path,
            'thumbnail_path': thumbnail_path,
            'metadata': metadata,
            'timestamp': time.time()
        }
        print(f"💾 تم حفظ الملف في الكاش: {video_id}")

# ========== نظام تدوير الكوكيز الذكي ==========
class AdvancedCookieManager:
    def __init__(self, cookies_dir="/workspace/cookies"):
        self.cookies_dir = cookies_dir
        self.current_index = 0
        self.cookies_files = []
        self.cookie_usage = defaultdict(int)  # عداد الاستخدام
        self.cookie_errors = defaultdict(int)  # عداد الأخطاء
        self.lock = threading.RLock()
        self.load_cookies_files()
    
    def load_cookies_files(self):
        """تحميل قائمة ملفات الكوكيز المتاحة"""
        with self.lock:
            try:
                self.cookies_files.clear()
                
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
                
                # ترتيب الملفات حسب الحجم (الأكبر أولاً)
                self.cookies_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
                
                print(f"✅ تم العثور على {len(self.cookies_files)} ملف كوكيز")
                
            except Exception as e:
                print(f"❌ خطأ في تحميل ملفات الكوكيز: {e}")
                if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                    self.cookies_files = [YOUTUBE_COOKIES_FILE]
    
    def get_best_cookie(self, user_id=None):
        """الحصول على أفضل ملف كوكيز متاح مع التدوير الذكي"""
        with self.lock:
            if not self.cookies_files:
                return None
            
            # اختيار الكوكيز الأقل استخداماً والأقل أخطاءً
            best_cookie = min(self.cookies_files, 
                            key=lambda x: self.cookie_usage[x] + (self.cookie_errors[x] * 5))
            
            # تدوير ذكي بناء على معرف المستخدم
            if user_id and len(self.cookies_files) > 1:
                user_hash = hash(str(user_id)) % len(self.cookies_files)
                selected_cookie = self.cookies_files[user_hash]
                
                # إذا كان الكوكيز المختار لم يتم استخدامه كثيراً
                if (self.cookie_usage[selected_cookie] < 
                    min(self.cookie_usage[c] for c in self.cookies_files) + 10):
                    best_cookie = selected_cookie
            
            # تحديث إحصائيات الاستخدام
            self.cookie_usage[best_cookie] += 1
            
            print(f"🎯 استخدام كوكيز: {os.path.basename(best_cookie)} (استخدام: {self.cookie_usage[best_cookie]})")
            return best_cookie
    
    def report_error(self, cookie_file):
        """تسجيل خطأ في ملف كوكيز"""
        if cookie_file:
            with self.lock:
                self.cookie_errors[cookie_file] += 1
                print(f"⚠️ خطأ في كوكيز {os.path.basename(cookie_file)} (أخطاء: {self.cookie_errors[cookie_file]})")
    
    def get_stats(self):
        """الحصول على إحصائيات الكوكيز"""
        with self.lock:
            stats = {}
            for cookie_file in self.cookies_files:
                stats[os.path.basename(cookie_file)] = {
                    'usage': self.cookie_usage[cookie_file],
                    'errors': self.cookie_errors[cookie_file]
                }
            return stats

# إنشاء مدير الكوكيز المتقدم
cookie_manager = AdvancedCookieManager()

def check_forbidden_words(text):
    """فحص النص للكلمات المحظورة"""
    if not text:
        return False
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

# ========== دالة التحميل المطورة بدون قيود ==========
async def download_audio(client, message, text):
    user_id = message.from_user.id if message.from_user else 0
    
    # فحص الكلمات المحظورة
    if check_forbidden_words(text):
        return await message.reply_text("لا يمكن تنزيل هذا❌")
    
    # فحص الطلبات المكررة
    duplicate_tracker = check_duplicate_request(user_id, text)
    if duplicate_tracker:
        return await message.reply_text(f"⏳ طلب مشابه قيد المعالجة ({duplicate_tracker.stage})")
    
    # إنشاء معرف فريد للطلب
    request_id = generate_request_id(user_id, text)
    tracker = RequestTracker(request_id, user_id, text)
    
    h = await message.reply_text(f"🔍 جاري البحث... (ID: {request_id[:6]})")
    audio_file = None
    sedlyf = None
    
    try:
        # البحث في الكاش أولاً
        tracker.update_stage("checking_cache")
        cached_result = get_cached_search(text)
        
        if cached_result:
            search_result = cached_result
            tracker.update_stage("found_in_cache")
        else:
            # البحث الجديد
            tracker.update_stage("searching_youtube")
            await h.edit_text(f"🔍 البحث في YouTube... (ID: {request_id[:6]})")
            
            search = SearchVideos(text, offset=1, mode="dict", max_results=1)
            search_result = search.result()
            
            if not search_result or not search_result.get("search_result") or len(search_result["search_result"]) == 0:
                tracker.complete(False)
                await h.delete()
                return await message.reply_text("❌ لم يتم العثور على نتائج للبحث المطلوب")
            
            # حفظ في الكاش
            cache_search_result(text, search_result)
            tracker.update_stage("search_completed")
        
        # استخراج معلومات الفيديو
        video_data = search_result["search_result"][0]
        mo = video_data["link"]
        thum = video_data["title"]
        fridayz = video_data["id"]
        
        # تحديث معرف الفيديو في التتبع
        tracker.video_id = fridayz
        
        # إلغاء الطلبات المتعلقة بنفس الفيديو
        cancel_related_requests(fridayz, exclude_request_id=request_id)
        
        # فحص كاش التحميل
        tracker.update_stage("checking_download_cache")
        cached_download = get_cached_download(fridayz)
        
        if cached_download:
            tracker.update_stage("sending_from_cache")
            await h.edit_text(f"📁 إرسال من الكاش... (ID: {request_id[:6]})")
            
            # إرسال الملف المحفوظ
            await client.send_audio(
                message.chat.id,
                audio=cached_download['audio_path'],
                duration=cached_download['metadata']['duration'],
                title=cached_download['metadata']['title'],
                performer=cached_download['metadata']['performer'],
                thumb=cached_download['thumbnail_path'],
                caption=cached_download['metadata']['caption'],
                reply_to_message_id=message.id
            )
            
            await h.delete()
            tracker.complete(True)
            return
        
        # التحميل الجديد
        tracker.update_stage("downloading")
        await h.edit_text(f"⬇️ جاري التحميل... (ID: {request_id[:6]})")
        
        # تحميل الصورة المصغرة
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        sedlyf = wget.download(kekme, bar=None)
        
        # الحصول على أفضل ملف كوكيز
        cookie_file = cookie_manager.get_best_cookie(user_id)
        if not cookie_file:
            tracker.complete(False)
            await h.delete()
            return await message.reply_text("❌ لا توجد ملفات كوكيز متاحة")
        
        # إعدادات التحميل بدون قيود
        opts = {
            'format': 'bestaudio/best',  # أفضل جودة متاحة - بدون حد حجم
            'outtmpl': f'audio_{int(time.time() * 1000000)}_{fridayz}_%(title)s.%(ext)s',
            'cookiefile': cookie_file,
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'writethumbnail': False,
            'writeinfojson': False,
            'ignoreerrors': True,
            'retries': 10,  # محاولات كثيرة
            'fragment_retries': 10,
            'socket_timeout': 600,  # 10 دقائق timeout
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        
        # التحميل
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
        
        # إلغاء الطلبات المتعلقة بنفس الفيديو بعد نجاح التحميل
        cancel_related_requests(fridayz, exclude_request_id=request_id)
        
        # إعداد معلومات الملف (بدون حد طول)
        tracker.update_stage("preparing_send")
        duration = int(ytdl_data.get("duration", 0))
        title = str(ytdl_data.get("title", "Unknown"))
        performer = str(ytdl_data.get("uploader", "Unknown"))
        capy = f"[{title}]({mo})"
        
        await h.edit_text(f"📤 إرسال الملف... (ID: {request_id[:6]})")
        
        # إرسال الملف الصوتي (بدون حد حجم)
        await client.send_audio(
            message.chat.id,
            audio=audio_file,
            duration=duration,
            title=title,
            performer=performer,
            file_name=title,
            thumb=sedlyf,
            caption=capy,
            reply_to_message_id=message.id
        )
        
        # حفظ في كاش التحميل
        tracker.update_stage("caching")
        metadata = {
            'duration': duration,
            'title': title,
            'performer': performer,
            'caption': capy
        }
        cache_download_result(fridayz, audio_file, sedlyf, metadata)
        
        await h.delete()
        tracker.complete(True)
        print(f"✅ تم تحميل وحفظ: {title} للمستخدم {user_id}")
        
        # لا تحذف الملفات - محفوظة في الكاش
        return
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ خطأ في التحميل للمستخدم {user_id}: {error_msg}")
        
        # تسجيل خطأ الكوكيز
        if 'cookie_file' in locals() and cookie_file:
            cookie_manager.report_error(cookie_file)
        
        tracker.complete(False)
        
        try:
            await h.delete()
        except:
            pass
        
        # تنظيف الملفات في حالة الخطأ
        clean_temp_files(audio_file, sedlyf)
        
        # رسائل خطأ محسنة
        if "Sign in to confirm your age" in error_msg or "confirm you're not a bot" in error_msg:
            error_response = "❌ هذا الفيديو يتطلب تأكيد إضافي من YouTube"
        elif "Video unavailable" in error_msg:
            error_response = "❌ هذا الفيديو غير متاح أو محذوف"
        elif "Private video" in error_msg:
            error_response = "❌ هذا فيديو خاص"
        elif "blocked" in error_msg.lower():
            error_response = "❌ هذا الفيديو محجوب في منطقتك"
        else:
            error_response = "❌ حدث خطأ أثناء التحميل، حاول مرة أخرى"
        
        await message.reply_text(error_response)

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
        return await message.reply_text("يرجى كتابة ما تريد تحميله بعد الأمر\nمثال: بحث عليكي عيون")
    
    await download_audio(client, message, text)

# أمر الإحصائيات للمطورين
@Client.on_message(filters.command(["احصائيات", "stats"], ""))
async def stats_handler(client, message):
    """عرض إحصائيات النظام"""
    try:
        if message.from_user.id not in [6221604842, 985612253]:  # المطورين
            return
        
        with cache_lock:
            search_cache_size = len(search_cache)
            download_cache_size = len(download_cache)
            active_requests = len(request_tracking)
            
            # إحصائيات الكوكيز
            cookie_stats = cookie_manager.get_stats()
            
            stats_text = f"""📊 **إحصائيات النظام بدون قيود:**

🔍 **كاش البحث:** {search_cache_size} عنصر
💾 **كاش التحميل:** {download_cache_size} ملف  
🔄 **الطلبات النشطة:** {active_requests}
🍪 **ملفات الكوكيز:** {len(cookie_manager.cookies_files)}

🎯 **إحصائيات الكوكيز:**"""
            
            for cookie_name, stats in cookie_stats.items():
                stats_text += f"\n• {cookie_name}: {stats['usage']} استخدام، {stats['errors']} أخطاء"
        
        await message.reply_text(stats_text)
        
    except Exception as e:
        print(f"❌ خطأ في الإحصائيات: {e}")

print("🎉 تم تحميل النظام المطور بنجاح!")
print("✅ جميع الميزات مفعلة: منع التكرار، كاش ذكي، تدوير الكوكيز، بدون قيود!")