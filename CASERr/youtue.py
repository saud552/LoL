from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
import os
import asyncio
import yt_dlp
import time 
from datetime import datetime, timedelta
import threading
import random 
from collections import defaultdict
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from config import *
from yt_dlp import YoutubeDL
from CASERr.CASERr import get_channel, johned
import aiohttp
import aiofiles
from pyrogram.types import *
import hashlib
import weakref

# إعدادات البوت ومتغيرات النظام
FORBIDDEN_WORDS_HASH = hashlib.md5(str([
    "Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل",
    "نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع",
    "خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس",
    "ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx",
    "sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك",
    "كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل",
    "ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق",
    "سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط",
    "لانجرى","لانجري","لانجيرى","مولااااعه"
]).encode()).hexdigest()

# قائمة الكلمات المحظورة (محسنة للأداء)
FORBIDDEN_WORDS = {
    "xnxx", "سكس", "اباحيه", "جنس", "اباحي", "زب", "كسمك", "كس", "شرمطه", "نيك", "لبوه", "فشخ", 
    "مهبل", "نيك خلفى", "بتتناك", "مساج", "كس ملبن", "نيك جماعى", "نيك جماعي", "نيك بنات", 
    "رقص", "قلع", "خلع ملابس", "بنات من غير هدوم", "بنات ملط", "نيك طيز", "نيك من ورا", 
    "نيك في الكس", "ارهاب", "موت", "حرب", "سياسه", "سياسي", "سكسي", "قحبه", "شواز", "ممويز", 
    "نياكه", "sex", "xxx", "born", "borno", "sesso", "احا", "خخخ", "ميتينك", "تناك", "يلعن", 
    "كسك", "عرص", "خول", "علق", "كسم", "انيك", "انيكك", "اركبك", "زبي", "شرموط", "فحل", 
    "ديوث", "سالب", "مقاطع", "ورعان", "هايج", "مشتهي", "زوبري", "طيز", "كسي", "كسى", "ساحق", 
    "سحق", "اريحها", "مقاتع", "لانجيري", "سحاق", "مقطع", "مقتع", "نودز", "ندز", "ملط", 
    "لانجرى", "لانجري", "لانجيرى", "مولااااعه"
}

# نظام إدارة الكوكيز المتقدم والآمن للـ Threading
class AdvancedCookieManager:
    def __init__(self, cookies_dir="/workspace/cookies"):
        self.cookies_dir = cookies_dir
        self.cookies_files = []
        self.cookie_usage_count = defaultdict(int)  # عدد مرات استخدام كل كوكيز
        self.cookie_last_used = defaultdict(float)  # آخر وقت استخدام
        self.cookie_errors = defaultdict(int)  # عدد الأخطاء لكل كوكيز
        self.lock = threading.RLock()  # قفل للحماية من race conditions
        self.load_cookies_files()
        self.max_cookie_usage = 10000  # تم رفع الحد إلى 10000 استخدام
        self.cookie_cooldown = 1  # تم تقليل فترة الانتظار إلى ثانية واحدة
        
    def load_cookies_files(self):
        """تحميل قائمة ملفات الكوكيز المتاحة مع فحص صحتها"""
        with self.lock:
            try:
                self.cookies_files.clear()
                
                if os.path.exists(self.cookies_dir):
                    # البحث عن ملفات الكوكيز
                    for file in os.listdir(self.cookies_dir):
                        if file.endswith('.txt') and ('cookie' in file.lower() or 'yt' in file.lower()):
                            file_path = os.path.join(self.cookies_dir, file)
                            if self._validate_cookie_file(file_path):
                                self.cookies_files.append(file_path)
                    
                                    # إضافة الملف الافتراضي إذا كان موجوداً
                try:
                    from config import YOUTUBE_COOKIES_FILE
                    if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                        if YOUTUBE_COOKIES_FILE not in self.cookies_files:
                            if self._validate_cookie_file(YOUTUBE_COOKIES_FILE):
                                self.cookies_files.append(YOUTUBE_COOKIES_FILE)
                except ImportError:
                    # لا يوجد ملف كوكيز افتراضي في الإعدادات
                    pass
                
                # ترتيب الملفات حسب الحجم (الأكبر أولاً - عادة أكثر صحة)
                self.cookies_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
                
                print(f"✅ تم العثور على {len(self.cookies_files)} ملف كوكيز صالح")
                
            except Exception as e:
                print(f"❌ خطأ في تحميل ملفات الكوكيز: {e}")
                # استخدام الملف الافتراضي كاحتياطي
                try:
                    from config import YOUTUBE_COOKIES_FILE
                    if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                        self.cookies_files = [YOUTUBE_COOKIES_FILE]
                except ImportError:
                    print("⚠️ لا توجد ملفات كوكيز متاحة")
    
    def _validate_cookie_file(self, file_path):
        """فحص صحة ملف الكوكيز"""
        try:
            if not os.path.exists(file_path):
                return False
            
            file_size = os.path.getsize(file_path)
            if file_size < 100:  # ملف صغير جداً
                return False
            
            # فحص محتوى الملف للتأكد من أنه يحتوي على كوكيز يوتيوب
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(500)  # قراءة أول 500 حرف
                if 'youtube' in content.lower() or 'google' in content.lower():
                    return True
            
            return False
            
        except Exception:
            return False
    
    def get_best_cookie(self, user_id=None):
        """الحصول على أفضل ملف كوكيز متاح باستخدام خوارزمية ذكية"""
        with self.lock:
            if not self.cookies_files:
                return None
            
            current_time = time.time()
            available_cookies = []
            
            # فحص الكوكيز المتاحة
            for cookie_file in self.cookies_files:
                # تم إلغاء حد الأخطاء - استخدام جميع الكوكيز مهما كانت الأخطاء
                
                # تجاهل الكوكيز التي استُخدمت مؤخراً
                if current_time - self.cookie_last_used[cookie_file] < self.cookie_cooldown:
                    continue
                
                # تجاهل الكوكيز التي استُخدمت كثيراً
                if self.cookie_usage_count[cookie_file] > self.max_cookie_usage:
                    continue
                
                available_cookies.append(cookie_file)
            
            # إذا لم تجد كوكيز متاحة، اختر الأفضل من كل الكوكيز
            if not available_cookies:
                available_cookies = self.cookies_files
                # إعادة تعيين العدادات للكوكيز المتعبة
                for cookie in self.cookies_files:
                    self.cookie_usage_count[cookie] = 0
            
            # اختيار أفضل كوكيز بناء على الاستخدام والأخطاء
            best_cookie = min(available_cookies, 
                            key=lambda x: (self.cookie_usage_count[x] * 2 + self.cookie_errors[x]))
            
            # تحديث إحصائيات الاستخدام
            self.cookie_usage_count[best_cookie] += 1
            self.cookie_last_used[best_cookie] = current_time
            
            # إضافة توزيع ذكي بناء على user_id
            if user_id and len(available_cookies) > 1:
                # استخدام hash للمستخدم لتوزيع الأحمال
                user_hash = hash(str(user_id)) % len(available_cookies)
                selected_cookie = available_cookies[user_hash]
                
                # تحديث الإحصائيات
                self.cookie_usage_count[selected_cookie] += 1
                self.cookie_last_used[selected_cookie] = current_time
                
                print(f"🔄 كوكيز موزع للمستخدم {user_id}: {os.path.basename(selected_cookie)}")
                return selected_cookie
            
            print(f"🎯 أفضل كوكيز: {os.path.basename(best_cookie)} (استخدام: {self.cookie_usage_count[best_cookie]})")
            return best_cookie
    
    def report_cookie_error(self, cookie_file):
        """تسجيل خطأ في ملف كوكيز معين"""
        with self.lock:
            if cookie_file:
                self.cookie_errors[cookie_file] += 1
                print(f"⚠️ خطأ في الكوكيز {os.path.basename(cookie_file)} (إجمالي الأخطاء: {self.cookie_errors[cookie_file]})")
    
    def get_cookie_stats(self):
        """الحصول على إحصائيات الكوكيز"""
        with self.lock:
            stats = {}
            for cookie_file in self.cookies_files:
                stats[os.path.basename(cookie_file)] = {
                    'usage_count': self.cookie_usage_count[cookie_file],
                    'error_count': self.cookie_errors[cookie_file],
                    'last_used': self.cookie_last_used[cookie_file]
                }
            return stats
    
    def refresh_cookies(self):
        """إعادة تحميل ملفات الكوكيز"""
        print("🔄 إعادة تحميل ملفات الكوكيز...")
        self.load_cookies_files()

# إنشاء مدير الكوكيز المتقدم
cookie_manager = AdvancedCookieManager()

# إعدادات النظام العامة
MAX_CONCURRENT_DOWNLOADS = 10000  # تم رفع الحد إلى 10000 (عملياً لا محدود)
download_semaphore = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)
user_request_count = defaultdict(lambda: {'count': 0, 'last_reset': time.time()})
search_cache = {}  # كاش للبحثات
download_cache = {}  # كاش للملفات المحملة
active_downloads = {}  # تتبع التحميلات النشطة لمنع التكرار
request_tracking = {}  # تتبع شامل للطلبات مع إمكانية الإلغاء
cache_lock = threading.RLock()
MAX_CACHE_SIZE = 10000  # تم رفع الحد إلى 10000 عنصر
DOWNLOAD_CACHE_SIZE = 5000  # تم رفع الحد إلى 5000 ملف

def check_forbidden_words(text):
    """فحص النص للكلمات المحظورة - محسن للأداء"""
    if not text:
        return False
    
    text_lower = text.lower()
    
    # البحث السريع باستخدام set lookup
    words_in_text = set(text_lower.split())
    
    # فحص الكلمات المنفردة أولاً (أسرع)
    if words_in_text.intersection(FORBIDDEN_WORDS):
        return True
    
    # فحص الكلمات المركبة
    for forbidden_word in FORBIDDEN_WORDS:
        if len(forbidden_word) > 3 and forbidden_word in text_lower:
            return True
    
    return False

async def clean_temp_files(*files):
    """تنظيف الملفات المؤقتة بشكل غير متزامن"""
    for file_path in files:
        try:
            if file_path and os.path.exists(file_path):
                await asyncio.get_event_loop().run_in_executor(None, os.remove, file_path)
        except Exception as e:
            print(f"❌ خطأ في حذف الملف {file_path}: {e}")

async def download_thumbnail_async(url, timeout=30):
    """تحميل الصورة المصغرة بشكل غير متزامن"""
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    # إنشاء اسم ملف مؤقت فريد
                    filename = f"thumb_{int(time.time() * 1000000)}.jpg"
                    
                    async with aiofiles.open(filename, 'wb') as f:
                        await f.write(content)
                    
                    return filename
                else:
                    print(f"⚠️ فشل تحميل الصورة المصغرة: {response.status}")
                    return None
    except Exception as e:
        print(f"❌ خطأ في تحميل الصورة المصغرة: {e}")
        return None

def generate_cache_key(text):
    """إنشاء مفتاح فريد للكاش"""
    return hashlib.md5(text.lower().encode()).hexdigest()

async def get_cached_search(text):
    """البحث في الكاش أولاً"""
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

async def cache_search_result(text, result):
    """حفظ نتيجة البحث في الكاش"""
    with cache_lock:
        # تنظيف الكاش إذا امتلأ
        if len(search_cache) >= MAX_CACHE_SIZE:
            # إزالة أقدم 100 عنصر
            oldest_keys = sorted(search_cache.keys(), 
                               key=lambda k: search_cache[k]['timestamp'])[:100]
            for key in oldest_keys:
                del search_cache[key]
        
        cache_key = generate_cache_key(text)
        search_cache[cache_key] = {
            'data': result,
            'timestamp': time.time()
        }

async def get_cached_download(video_id):
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

async def cache_download_result(video_id, audio_path, thumbnail_path, metadata):
    """حفظ الملف المحمل في الكاش"""
    with cache_lock:
        # تنظيف كاش التحميل إذا امتلأ
        if len(download_cache) >= DOWNLOAD_CACHE_SIZE:
            # إزالة أقدم 50 عنصر وحذف ملفاتهم
            oldest_items = sorted(download_cache.items(), 
                                key=lambda x: x[1]['timestamp'])[:50]
            
            for vid_id, data in oldest_items:
                try:
                    # حذف الملفات القديمة
                    if os.path.exists(data['audio_path']):
                        await asyncio.get_event_loop().run_in_executor(
                            None, os.remove, data['audio_path']
                        )
                    if data.get('thumbnail_path') and os.path.exists(data['thumbnail_path']):
                        await asyncio.get_event_loop().run_in_executor(
                            None, os.remove, data['thumbnail_path']
                        )
                except Exception as e:
                    print(f"خطأ في حذف الملف القديم: {e}")
                
                del download_cache[vid_id]
        
        # حفظ الملف الجديد في الكاش
        download_cache[video_id] = {
            'audio_path': audio_path,
            'thumbnail_path': thumbnail_path,
            'metadata': metadata,
            'timestamp': time.time()
        }
        print(f"💾 تم حفظ الملف في الكاش: {video_id}")

async def check_active_download(video_id, user_id):
    """فحص إذا كان التحميل جاري بالفعل ومنع التكرار"""
    with cache_lock:
        download_key = f"{video_id}_{user_id}"
        
        if download_key in active_downloads:
            # فحص إذا كان التحميل ما زال نشطاً (أقل من 10 دقائق)
            if time.time() - active_downloads[download_key] < 600:
                return True  # تحميل نشط
            else:
                # إزالة التحميل المنتهي الصلاحية
                del active_downloads[download_key]
        
        # تسجيل تحميل جديد
        active_downloads[download_key] = time.time()
        return False  # تحميل جديد

async def finish_download_tracking(video_id, user_id):
    """إنهاء تتبع التحميل"""
    with cache_lock:
        download_key = f"{video_id}_{user_id}"
        if download_key in active_downloads:
            del active_downloads[download_key]

class RequestTracker:
    """فئة لتتبع الطلبات ومنع التداخل"""
    
    def __init__(self, request_id, user_id, video_id=None):
        self.request_id = request_id
        self.user_id = user_id
        self.video_id = video_id
        self.is_cancelled = False
        self.is_completed = False
        self.start_time = time.time()
        self.current_stage = "initialized"
        
        # تسجيل الطلب
        with cache_lock:
            request_tracking[request_id] = self
    
    def update_stage(self, stage):
        """تحديث مرحلة الطلب"""
        if not self.is_cancelled and not self.is_completed:
            self.current_stage = stage
            print(f"🔄 طلب {self.request_id}: {stage}")
    
    def cancel(self, reason="تم الإلغاء"):
        """إلغاء الطلب"""
        self.is_cancelled = True
        self.current_stage = f"cancelled: {reason}"
        print(f"❌ طلب {self.request_id} تم إلغاؤه: {reason}")
    
    def complete(self, success=True, method="unknown"):
        """إكمال الطلب"""
        self.is_completed = True
        self.current_stage = f"completed via {method}"
        
        # إنهاء تتبع التحميل إذا كان موجوداً
        if self.video_id:
            asyncio.create_task(finish_download_tracking(self.video_id, self.user_id))
        
        # إزالة من التتبع
        with cache_lock:
            if self.request_id in request_tracking:
                del request_tracking[self.request_id]
        
        status = "✅" if success else "❌"
        print(f"{status} طلب {self.request_id} اكتمل عبر: {method}")
    
    def is_active(self):
        """فحص إذا كان الطلب نشطاً"""
        return not self.is_cancelled and not self.is_completed
    
    def __del__(self):
        """تنظيف عند حذف الكائن"""
        if hasattr(self, 'request_id'):
            with cache_lock:
                if self.request_id in request_tracking:
                    del request_tracking[self.request_id]

def generate_request_id(user_id, text):
    """إنشاء معرف فريد للطلب"""
    unique_str = f"{user_id}_{text}_{int(time.time() * 1000000)}"
    return hashlib.md5(unique_str.encode()).hexdigest()[:12]

async def check_duplicate_request(user_id, text):
    """فحص الطلبات المكررة النشطة"""
    with cache_lock:
        search_hash = hashlib.md5(f"{user_id}_{text.lower()}".encode()).hexdigest()
        
        for req_id, tracker in request_tracking.items():
            if (tracker.user_id == user_id and 
                tracker.is_active() and 
                time.time() - tracker.start_time < 300):  # 5 دقائق
                
                # فحص تشابه النص
                if search_hash in req_id or tracker.current_stage in ["searching", "downloading"]:
                    return tracker
        
        return None

async def cancel_related_requests(video_id, exclude_request_id=None):
    """إلغاء جميع الطلبات المتعلقة بنفس الفيديو"""
    with cache_lock:
        to_cancel = []
        
        for req_id, tracker in request_tracking.items():
            if (tracker.video_id == video_id and 
                tracker.is_active() and 
                req_id != exclude_request_id):
                to_cancel.append(tracker)
        
        for tracker in to_cancel:
            tracker.cancel("ملف متوفر من طلب آخر")
        
        if to_cancel:
            print(f"🚫 تم إلغاء {len(to_cancel)} طلب متعلق بالفيديو {video_id}")

def check_rate_limit(user_id):
    """فحص حد المعدل للمستخدم"""
    current_time = time.time()
    user_data = user_request_count[user_id]
    
    # إعادة تعيين العداد كل دقيقة
    if current_time - user_data['last_reset'] > 60:
        user_data['count'] = 0
        user_data['last_reset'] = current_time
    
    # السماح بـ 5 طلبات كحد أقصى في الدقيقة
    if user_data['count'] >= 5:
        return False
    
    user_data['count'] += 1
    return True

# دالة التحميل المحسنة والآمنة مع تتبع شامل
async def download_audio(client, message, text):
    user_id = message.from_user.id if message.from_user else 0
    
    # تم إلغاء فحص حد المعدل للمستخدم - استخدام حر بلا قيود
    
    # فحص الكلمات المحظورة
    if check_forbidden_words(text):
        return await message.reply_text("❌ لا يمكن تنزيل هذا المحتوى")
    
    # فحص الطلبات المكررة النشطة
    duplicate_tracker = await check_duplicate_request(user_id, text)
    if duplicate_tracker:
        return await message.reply_text(f"⏳ طلب مشابه قيد المعالجة ({duplicate_tracker.current_stage}). انتظر قليلاً...")
    
    # إنشاء معرف فريد للطلب وبدء التتبع
    request_id = generate_request_id(user_id, text)
    tracker = RequestTracker(request_id, user_id)
    
    # تم إلغاء حد التحميلات المتزامنة - تحميل حر بلا قيود
    status_message = await message.reply_text(f"🔍 جاري البحث... (ID: {request_id[:6]})")
    audio_file = None
    thumbnail_file = None
    cookie_file = None
        
        try:
            # تحديث مرحلة البحث
            tracker.update_stage("searching_cache")
            
            # فحص إلغاء الطلب
            if not tracker.is_active():
                await status_message.delete()
                return
            
            # البحث في الكاش أولاً
            cached_result = await get_cached_search(text)
            if cached_result:
                search_result = cached_result
                tracker.update_stage("found_in_search_cache")
            else:
                # البحث الجديد
                tracker.update_stage("searching_youtube")
                await status_message.edit_text(f"🔍 البحث في يوتيوب... (ID: {request_id[:6]})")
                
                search = await asyncio.get_event_loop().run_in_executor(
                    None, lambda: SearchVideos(text, offset=1, mode="dict", max_results=1)
                )
                search_result = await asyncio.get_event_loop().run_in_executor(
                    None, search.result
                )
                
                # فحص إلغاء الطلب بعد البحث
                if not tracker.is_active():
                    await status_message.delete()
                    return
                
                if not search_result or not search_result.get("search_result") or len(search_result["search_result"]) == 0:
                    tracker.complete(False, "no_results")
                    await status_message.delete()
                    return await message.reply_text("❌ لم يتم العثور على نتائج للبحث المطلوب")
                
                # حفظ في الكاش
                await cache_search_result(text, search_result)
                tracker.update_stage("search_completed")
            
            video_data = search_result["search_result"][0]
            video_url = video_data["link"]
            video_title = video_data["title"]
            video_id = video_data["id"]
            
            # تحديث معرف الفيديو في التتبع
            tracker.video_id = video_id
            
            # إلغاء الطلبات المتعلقة بنفس الفيديو
            await cancel_related_requests(video_id, exclude_request_id=request_id)
            
            # فحص إذا كان التحميل جاري بالفعل لمنع التكرار
            is_active = await check_active_download(video_id, user_id)
            if is_active:
                tracker.complete(False, "duplicate_download")
                await status_message.delete()
                return await message.reply_text("⏳ هذا الملف قيد التحميل بالفعل، انتظر قليلاً...")
            
            # فحص إلغاء الطلب
            if not tracker.is_active():
                await status_message.delete()
                return
            
            # البحث عن الملف في كاش التحميلات أولاً
            tracker.update_stage("checking_download_cache")
            cached_download = await get_cached_download(video_id)
            if cached_download:
                tracker.update_stage("sending_from_cache")
                await status_message.edit_text(f"📁 إرسال الملف من الكاش... (ID: {request_id[:6]})")
                
                # إلغاء جميع الطلبات المتعلقة بنفس الفيديو
                await cancel_related_requests(video_id, exclude_request_id=request_id)
                
                # إرسال الملف المحفوظ مباشرة
                await client.send_audio(
                    chat_id=message.chat.id,
                    audio=cached_download['audio_path'],
                    duration=cached_download['metadata']['duration'],
                    title=cached_download['metadata']['title'],
                    performer=cached_download['metadata']['performer'],
                    thumb=cached_download['thumbnail_path'],
                    caption=cached_download['metadata']['caption'],
                    reply_to_message_id=message.id
                )
                
                await status_message.delete()
                tracker.complete(True, "download_cache")
                print(f"✅ تم إرسال ملف محفوظ: {video_title} للمستخدم {user_id}")
                return  # توقف هنا - تم الإرسال من الكاش
            
            # إذا لم يوجد في الكاش، ابدأ التحميل الجديد
            tracker.update_stage("preparing_download")
            await status_message.edit_text(f"📊 فحص معلومات الفيديو... (ID: {request_id[:6]})")
            
            # فحص إلغاء الطلب
            if not tracker.is_active():
                await status_message.delete()
                return
            
            # الحصول على أفضل ملف كوكيز
            cookie_file = cookie_manager.get_best_cookie(user_id)
            if not cookie_file:
                tracker.complete(False, "no_cookies")
                await status_message.delete()
                return await message.reply_text("❌ لا توجد ملفات كوكيز متاحة")
            
            # فحص إلغاء الطلب
            if not tracker.is_active():
                await status_message.delete()
                return
            
            # تحميل الصورة المصغرة بشكل غير متزامن
            tracker.update_stage("downloading_thumbnail")
            await status_message.edit_text(f"🖼️ تحميل الصورة المصغرة... (ID: {request_id[:6]})")
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            thumbnail_file = await download_thumbnail_async(thumbnail_url)
            
            # فحص إلغاء الطلب
            if not tracker.is_active():
                await clean_temp_files(thumbnail_file)
                await status_message.delete()
                return
            
            # إعدادات التحميل المحسنة
            tracker.update_stage("downloading_audio")
            await status_message.edit_text(f"⬇️ تحميل الملف الصوتي... (ID: {request_id[:6]})")
            
            opts = {
                'format': 'bestaudio/best',  # تم إلغاء حد الحجم - تحميل بأي حجم
                'outtmpl': f'audio_{int(time.time() * 1000000)}_{video_id}_%(title)s.%(ext)s',
                'cookiefile': cookie_file,
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                'writethumbnail': False,
                'writeinfojson': False,
                'ignoreerrors': True,
                'retries': 3,
                'fragment_retries': 3,
                'socket_timeout': 300,  # تم رفع timeout إلى 5 دقائق
            }
            
            # تحميل الملف في thread منفصل لعدم حجب البوت
            def download_with_ytdl():
                with YoutubeDL(opts) as ytdl:
                    info = ytdl.extract_info(video_url, download=True)
                    filename = ytdl.prepare_filename(info)
                    return info, filename
            
            ytdl_data, audio_file = await asyncio.get_event_loop().run_in_executor(
                None, download_with_ytdl
            )
            
            # فحص إلغاء الطلب بعد التحميل
            if not tracker.is_active():
                await clean_temp_files(audio_file, thumbnail_file)
                await status_message.delete()
                return
            
            # إلغاء جميع الطلبات المتعلقة بنفس الفيديو بعد نجاح التحميل
            await cancel_related_requests(video_id, exclude_request_id=request_id)
            
            # تم إلغاء فحص حجم الملف - قبول أي حجم
            
            # إعداد معلومات الملف
            tracker.update_stage("preparing_send")
            duration = int(ytdl_data.get("duration", 0))
            title = str(ytdl_data.get("title", "Unknown"))[:100]  # تحديد طول العنوان
            performer = str(ytdl_data.get("uploader", "Unknown"))[:50]
            caption = f"🎵 [{title}]({video_url})\n👤 {performer}"
            
            await status_message.edit_text(f"📤 إرسال الملف... (ID: {request_id[:6]})")
            
            # فحص إلغاء الطلب قبل الإرسال
            if not tracker.is_active():
                await clean_temp_files(audio_file, thumbnail_file)
                await status_message.delete()
                return
            
            # إرسال الملف الصوتي
            await client.send_audio(
                chat_id=message.chat.id,
                audio=audio_file,
                duration=duration,
                title=title,
                performer=performer,
                thumb=thumbnail_file,
                caption=caption,
                reply_to_message_id=message.id
            )
            
            # حفظ الملف في كاش التحميل للاستخدام المستقبلي
            tracker.update_stage("caching_result")
            metadata = {
                'duration': duration,
                'title': title,
                'performer': performer,
                'caption': caption
            }
            await cache_download_result(video_id, audio_file, thumbnail_file, metadata)
            
            await status_message.delete()
            tracker.complete(True, "full_download")
            print(f"✅ تم تحميل وحفظ بنجاح: {title} للمستخدم {user_id}")
            
            # لا تحذف الملفات هنا - سيتم حذفها تلقائياً عند تنظيف الكاش
            return
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ خطأ في التحميل للمستخدم {user_id}: {error_msg}")
            
            # تسجيل خطأ الكوكيز
            if cookie_file:
                cookie_manager.report_cookie_error(cookie_file)
            
            # إنهاء تتبع الطلب في حالة الخطأ
            tracker.complete(False, f"error: {error_msg[:50]}")
            
            try:
                await status_message.delete()
            except:
                pass
            
            # رسائل خطأ مفصلة
            if "Sign in to confirm your age" in error_msg:
                error_response = "❌ هذا الفيديو يتطلب تسجيل دخول للتأكد من العمر"
            elif "Video unavailable" in error_msg:
                error_response = "❌ هذا الفيديو غير متاح أو محذوف"
            elif "Private video" in error_msg:
                error_response = "❌ هذا فيديو خاص"
            elif "blocked" in error_msg.lower():
                error_response = "❌ هذا الفيديو محجوب في منطقتك"
            else:
                error_response = "❌ حدث خطأ أثناء التحميل، حاول مرة أخرى"
            
            await message.reply_text(error_response)
            
        finally:
            # تنظيف الملفات المؤقتة فقط إذا لم يتم حفظها في الكاش أو كان الطلب ملغى
            should_clean = True
            
            try:
                # فحص إذا تم حفظ الملف في الكاش
                if 'video_id' in locals() and video_id and video_id in download_cache:
                    should_clean = False
                elif tracker and tracker.is_completed and tracker.current_stage.startswith("completed"):
                    should_clean = False
                
                if should_clean:
                    # تنظيف آمن للملفات المؤقتة
                    files_to_clean = []
                    if 'audio_file' in locals() and audio_file:
                        files_to_clean.append(audio_file)
                    if 'thumbnail_file' in locals() and thumbnail_file:
                        files_to_clean.append(thumbnail_file)
                    
                    if files_to_clean:
                        await clean_temp_files(*files_to_clean)
                
            except Exception as cleanup_error:
                print(f"❌ خطأ في تنظيف الملفات: {cleanup_error}")
            
            # التأكد من تنظيف التتبع
            try:
                if 'tracker' in locals() and tracker and not tracker.is_completed:
                    tracker.complete(False, "cleanup")
            except Exception as tracker_error:
                print(f"❌ خطأ في تنظيف التتبع: {tracker_error}")

# دالة مساعدة للتحقق من صحة النص المطلوب تحميله
def validate_search_text(text):
    """التحقق من صحة النص المطلوب للبحث - تم تخفيف القيود"""
    if not text or len(text.strip()) < 1:
        return False, "النص فارغ"
    
    # تم إلغاء حد طول النص - قبول أي طول
    # تم إلغاء فحص الأحرف - قبول أي نوع أحرف
    
    return True, "صالح"

# تشغيل التنظيف الدوري عند بدء البوت
async def initialize_cleanup_task():
    """تشغيل مهمة التنظيف الدوري"""
    try:
        asyncio.create_task(periodic_cleanup())
        print("✅ تم تشغيل التنظيف الدوري بنجاح")
    except Exception as e:
        print(f"❌ خطأ في تشغيل التنظيف الدوري: {e}")

# معالج الأوامر المحسن
async def handle_download_command(client, message, search_text):
    """معالج مشترك للأوامر"""
    try:
        # التحقق من الانضمام للقنوات المطلوبة
        if await johned(client, message):
            return
        
        # التحقق من صحة النص
        is_valid, validation_msg = validate_search_text(search_text)
        if not is_valid:
            return await message.reply_text(f"❌ {validation_msg}")
        
        # تنظيف النص
        clean_text = search_text.strip()
        
        # بدء عملية التحميل
        await download_audio(client, message, clean_text)
        
    except Exception as e:
        print(f"❌ خطأ في معالج الأوامر: {e}")
        await message.reply_text("❌ حدث خطأ في معالجة الطلب")

# متغير لتتبع تشغيل التنظيف الدوري
cleanup_initialized = False

# الأوامر مع / - محسنة
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل", "يوت", "بحث"], ""), group=71328934)
async def command_download_handler(client, message):
    """معالج الأوامر مع العلامة /"""
    global cleanup_initialized
    
    # تشغيل التنظيف الدوري مرة واحدة
    if not cleanup_initialized:
        await initialize_cleanup_task()
        cleanup_initialized = True
    
    try:
        # استخراج النص من الأمر
        command_parts = message.text.split(" ", 1)
        if len(command_parts) < 2:
            help_text = (
                "📝 **كيفية الاستخدام:**\n\n"
                "🔸 `/بحث اسم الأغنية أو الفنان`\n"
                "🔸 `/تحميل اسم المقطع`\n"
                "🔸 `/يوتيوب رابط أو عنوان`\n\n"
                "**مثال:** `/بحث عمرو دياب أهواك`"
            )
            return await message.reply_text(help_text)
        
        search_text = command_parts[1]
        await handle_download_command(client, message, search_text)
        
    except Exception as e:
        print(f"❌ خطأ في معالج الأوامر مع /: {e}")
        await message.reply_text("❌ حدث خطأ في معالجة الأمر")

# الأوامر بدون / - محسنة ومحدودة أكثر
@Client.on_message(filters.text & ~filters.command([""]), group=71328935)
async def text_download_handler(client, message):
    """معالج الأوامر النصية بدون /"""
    try:
        # تم إلغاء حد طول الرسائل - قبول أي طول
        # تم إلغاء تجاهل الروابط - قبول جميع أنواع النصوص
        
        commands = ["تحميل", "نزل", "تنزيل", "يوتيوب", "حمل", "تنزل", "يوت", "بحث"]
        text = message.text.strip()
        
        # البحث عن الأمر في النص
        found_command = None
        search_text = None
        
        for cmd in commands:
            cmd_patterns = [
                f"{cmd} ",           # أمر + مسافة
                f"{cmd.lower()} ",   # أمر صغير + مسافة
            ]
            
            for pattern in cmd_patterns:
                if text.lower().startswith(pattern):
                    found_command = cmd
                    search_text = text[len(pattern):].strip()
                    break
            
            if found_command:
                break
        
        # إذا لم يجد أمر، تجاهل الرسالة
        if not found_command or not search_text:
            return
        
        await handle_download_command(client, message, search_text)
        
    except Exception as e:
        print(f"❌ خطأ في معالج النصوص: {e}")

# إضافة أمر للإحصائيات (للمطورين فقط)
@Client.on_message(filters.command(["احصائيات", "stats"], ""))
async def stats_handler(client, message):
    """عرض إحصائيات استخدام البوت"""
    try:
        # فحص إذا كان المستخدم مطور
        if message.from_user.id not in [6221604842]:  # ضع ID المطورين هنا
            return
        
        # إحصائيات الكوكيز
        cookie_stats = cookie_manager.get_cookie_stats()
        
        # إحصائيات الكاش
        search_cache_size = len(search_cache)
        download_cache_size = len(download_cache)
        active_downloads_count = len(active_downloads)
        active_requests_count = len(request_tracking)
        
        # إحصائيات Rate Limiting
        active_users = len(user_request_count)
        
        # إحصائيات مراحل الطلبات
        stages_count = {}
        for tracker in request_tracking.values():
            stage = tracker.current_stage
            stages_count[stage] = stages_count.get(stage, 0) + 1
        
        stats_text = f"""
📊 **إحصائيات البوت:**

🍪 **ملفات الكوكيز:** {len(cookie_manager.cookies_files)}
🔍 **كاش البحث:** {search_cache_size}/{MAX_CACHE_SIZE}
💾 **كاش التحميل:** {download_cache_size}/{DOWNLOAD_CACHE_SIZE}
👥 **المستخدمين النشطين:** {active_users}
⬇️ **التحميلات النشطة:** {MAX_CONCURRENT_DOWNLOADS - download_semaphore._value}
🔄 **التحميلات قيد المعالجة:** {active_downloads_count}
📋 **الطلبات المتتبعة:** {active_requests_count}

📈 **مراحل الطلبات النشطة:**
"""
        
        for stage, count in stages_count.items():
            stats_text += f"• {stage}: {count}\n"
        
        stats_text += "\n🔍 **تفاصيل الكوكيز:**\n"
        
        for cookie_name, stats in cookie_stats.items():
            stats_text += f"• {cookie_name}: {stats['usage_count']} استخدام، {stats['error_count']} أخطاء\n"
        
                 await message.reply_text(stats_text)
         
     except Exception as e:
         print(f"❌ خطأ في عرض الإحصائيات: {e}")

# أوامر إدارية إضافية
@Client.on_message(filters.command(["تنظيف_كاش", "clear_cache"], ""))
async def clear_cache_handler(client, message):
    """تنظيف الكاش (للمطورين فقط)"""
    try:
        if message.from_user.id not in [6221604842]:  # ضع ID المطورين هنا
            return
        
        with cache_lock:
            # تنظيف كاش البحث
            search_old_size = len(search_cache)
            search_cache.clear()
            
            # تنظيف كاش التحميل وحذف الملفات
            download_old_size = len(download_cache)
            for vid_id, data in download_cache.items():
                try:
                    if os.path.exists(data['audio_path']):
                        await asyncio.get_event_loop().run_in_executor(
                            None, os.remove, data['audio_path']
                        )
                    if data.get('thumbnail_path') and os.path.exists(data['thumbnail_path']):
                        await asyncio.get_event_loop().run_in_executor(
                            None, os.remove, data['thumbnail_path']
                        )
                except Exception as e:
                    print(f"خطأ في حذف ملف {vid_id}: {e}")
            
            download_cache.clear()
            
            # تنظيف التحميلات النشطة
            active_old_size = len(active_downloads)
            active_downloads.clear()
        
        result_text = f"""✅ تم تنظيف الكاش بالكامل:
🔍 كاش البحث: {search_old_size} عنصر
💾 كاش التحميل: {download_old_size} ملف
🔄 التحميلات النشطة: {active_old_size} عملية"""
        
        await message.reply_text(result_text)
        
    except Exception as e:
        print(f"❌ خطأ في تنظيف الكاش: {e}")

@Client.on_message(filters.command(["اعادة_تحميل_كوكيز", "reload_cookies"], ""))
async def reload_cookies_handler(client, message):
    """إعادة تحميل ملفات الكوكيز (للمطورين فقط)"""
    try:
        if message.from_user.id not in [6221604842]:  # ضع ID المطورين هنا
            return
        
        old_count = len(cookie_manager.cookies_files)
        cookie_manager.refresh_cookies()
        new_count = len(cookie_manager.cookies_files)
        
        await message.reply_text(f"🔄 تم إعادة تحميل الكوكيز\n🔸 السابق: {old_count}\n🔸 الحالي: {new_count}")
        
    except Exception as e:
        print(f"❌ خطأ في إعادة تحميل الكوكيز: {e}")

@Client.on_message(filters.command(["الطلبات", "requests"], ""))
async def active_requests_handler(client, message):
    """عرض الطلبات النشطة (للمطورين فقط)"""
    try:
        if message.from_user.id not in [6221604842]:  # ضع ID المطورين هنا
            return
        
        with cache_lock:
            if not request_tracking:
                return await message.reply_text("لا توجد طلبات نشطة حالياً")
            
            requests_text = "📋 **الطلبات النشطة:**\n\n"
            current_time = time.time()
            
            for req_id, tracker in list(request_tracking.items())[:10]:  # أول 10 طلبات
                elapsed = int(current_time - tracker.start_time)
                status = "🟢" if tracker.is_active() else "🔴"
                
                requests_text += (
                    f"{status} **ID:** `{req_id}`\n"
                    f"👤 المستخدم: {tracker.user_id}\n"
                    f"📹 الفيديو: {tracker.video_id or 'غير محدد'}\n"
                    f"📊 المرحلة: {tracker.current_stage}\n"
                    f"⏱️ المدة: {elapsed}ث\n\n"
                )
            
            if len(request_tracking) > 10:
                requests_text += f"... و {len(request_tracking) - 10} طلب آخر"
        
        await message.reply_text(requests_text)
        
    except Exception as e:
        print(f"❌ خطأ في عرض الطلبات: {e}")

# إضافة تنظيف دوري للذاكرة والكاش
async def periodic_cleanup():
    """تنظيف دوري للنظام كل ساعة"""
    while True:
        try:
            await asyncio.sleep(3600)  # ساعة واحدة
            
            # تنظيف كاش البحث من العناصر منتهية الصلاحية
            with cache_lock:
                current_time = time.time()
                expired_keys = [
                    key for key, data in search_cache.items() 
                    if current_time - data['timestamp'] > 1800  # 30 دقيقة
                ]
                
                for key in expired_keys:
                    del search_cache[key]
                
                if expired_keys:
                    print(f"🧹 تم تنظيف {len(expired_keys)} عنصر منتهي الصلاحية من كاش البحث")
            
            # تنظيف كاش التحميل من الملفات منتهية الصلاحية
            with cache_lock:
                current_time = time.time()
                expired_downloads = [
                    vid_id for vid_id, data in download_cache.items()
                    if current_time - data['timestamp'] > 7200  # 2 ساعة
                ]
                
                for vid_id in expired_downloads:
                    try:
                        data = download_cache[vid_id]
                        # حذف الملفات منتهية الصلاحية
                        if os.path.exists(data['audio_path']):
                            await asyncio.get_event_loop().run_in_executor(
                                None, os.remove, data['audio_path']
                            )
                        if data.get('thumbnail_path') and os.path.exists(data['thumbnail_path']):
                            await asyncio.get_event_loop().run_in_executor(
                                None, os.remove, data['thumbnail_path']
                            )
                        del download_cache[vid_id]
                    except Exception as e:
                        print(f"خطأ في تنظيف الملف {vid_id}: {e}")
                
                if expired_downloads:
                    print(f"🧹 تم تنظيف {len(expired_downloads)} ملف منتهي الصلاحية من كاش التحميل")
            
            # تنظيف التحميلات النشطة المنتهية الصلاحية
            with cache_lock:
                current_time = time.time()
                expired_active = [
                    key for key, timestamp in active_downloads.items()
                    if current_time - timestamp > 600  # 10 دقائق
                ]
                
                for key in expired_active:
                    del active_downloads[key]
                
                if expired_active:
                    print(f"🧹 تم تنظيف {len(expired_active)} تحميل نشط منتهي الصلاحية")
            
            # تنظيف تتبع الطلبات المنتهية الصلاحية
            with cache_lock:
                current_time = time.time()
                expired_requests = [
                    req_id for req_id, tracker in request_tracking.items()
                    if current_time - tracker.start_time > 1800  # 30 دقيقة
                ]
                
                for req_id in expired_requests:
                    try:
                        tracker = request_tracking[req_id]
                        if not tracker.is_completed:
                            tracker.complete(False, "expired")
                        del request_tracking[req_id]
                    except Exception as e:
                        print(f"خطأ في تنظيف تتبع الطلب {req_id}: {e}")
                
                if expired_requests:
                    print(f"🧹 تم تنظيف {len(expired_requests)} طلب منتهي الصلاحية")
            
            # تنظيف إحصائيات المستخدمين القديمة
            current_time = time.time()
            old_users = [
                user_id for user_id, data in user_request_count.items()
                if current_time - data['last_reset'] > 3600  # ساعة واحدة
            ]
            
            for user_id in old_users:
                del user_request_count[user_id]
            
            if old_users:
                print(f"🧹 تم تنظيف إحصائيات {len(old_users)} مستخدم قديم")
            
            # إعادة تحميل الكوكيز كل 4 ساعات
            if int(time.time()) % 14400 == 0:  # 4 ساعات
                cookie_manager.refresh_cookies()
                print("🔄 تم إعادة تحميل ملفات الكوكيز")
            
        except Exception as e:
            print(f"❌ خطأ في التنظيف الدوري: {e}")

# دالة لتشغيل التنظيف الدوري
def start_periodic_cleanup():
    """تشغيل التنظيف الدوري في event loop"""
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(periodic_cleanup())
        else:
            asyncio.create_task(periodic_cleanup())
    except RuntimeError:
        # سيتم تشغيله لاحقاً عند بدء البوت
        print("⏳ سيتم تشغيل التنظيف الدوري عند بدء البوت")

# محاولة تشغيل التنظيف الدوري
start_periodic_cleanup()

print("🚀 تم تحميل مدير تحميل يوتيوب المطور بنجاح!")
print(f"📊 الإعدادات الحالية:")
print(f"   🍪 ملفات الكوكيز: {len(cookie_manager.cookies_files)}")
print(f"   ⬇️ التحميلات المتزامنة: {MAX_CONCURRENT_DOWNLOADS} (لا محدود عملياً)")
print(f"   🔍 كاش البحث: {MAX_CACHE_SIZE} عنصر")
print(f"   💾 كاش التحميل: {DOWNLOAD_CACHE_SIZE} ملف") 
print(f"   ⏱️ معدل الطلبات: بلا حدود")
print(f"   📏 حجم الملفات: بلا حدود")
print(f"   📝 طول النصوص: بلا حدود")
print(f"   🔐 نظام منع التكرار المتقدم: مفعل")
print(f"   📋 تتبع الطلبات الذكي: مفعل")
print(f"   📁 نظام الكاش المتقدم: مفعل")
print(f"   🚫 إلغاء الطلبات المتداخلة: مفعل")
print(f"   🔄 التنظيف التلقائي: كل ساعة")
print(f"   🚀 وضع الأداء العالي: مفعل (بلا قيود)")
print("=" * 50)