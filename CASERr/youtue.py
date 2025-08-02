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
from config import YOUTUBE_COOKIES_FILE
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
        self.max_cookie_usage = 100  # حد أقصى لاستخدام الكوكيز قبل التبديل
        self.cookie_cooldown = 30  # فترة انتظار بالثواني قبل إعادة استخدام نفس الكوكيز
        
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
                    if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                        if YOUTUBE_COOKIES_FILE not in self.cookies_files:
                            if self._validate_cookie_file(YOUTUBE_COOKIES_FILE):
                                self.cookies_files.append(YOUTUBE_COOKIES_FILE)
                
                # ترتيب الملفات حسب الحجم (الأكبر أولاً - عادة أكثر صحة)
                self.cookies_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
                
                print(f"✅ تم العثور على {len(self.cookies_files)} ملف كوكيز صالح")
                
            except Exception as e:
                print(f"❌ خطأ في تحميل ملفات الكوكيز: {e}")
                # استخدام الملف الافتراضي كاحتياطي
                if YOUTUBE_COOKIES_FILE and os.path.exists(YOUTUBE_COOKIES_FILE):
                    self.cookies_files = [YOUTUBE_COOKIES_FILE]
    
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
                # تجاهل الكوكيز التي لديها أخطاء كثيرة
                if self.cookie_errors[cookie_file] > 10:
                    continue
                
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
MAX_CONCURRENT_DOWNLOADS = 50  # حد أقصى للتحميلات المتزامنة
download_semaphore = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)
user_request_count = defaultdict(lambda: {'count': 0, 'last_reset': time.time()})
search_cache = {}  # كاش للبحثات
cache_lock = threading.RLock()
MAX_CACHE_SIZE = 1000  # حد أقصى لحجم الكاش

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

# دالة التحميل المحسنة والآمنة
async def download_audio(client, message, text):
    user_id = message.from_user.id if message.from_user else 0
    
    # فحص حد المعدل للمستخدم
    if not check_rate_limit(user_id):
        return await message.reply_text("⏳ تم تجاوز الحد المسموح من الطلبات. حاول مرة أخرى بعد دقيقة.")
    
    # فحص الكلمات المحظورة
    if check_forbidden_words(text):
        return await message.reply_text("❌ لا يمكن تنزيل هذا المحتوى")  
    
    # استخدام Semaphore لتحديد عدد التحميلات المتزامنة
    async with download_semaphore:
        status_message = await message.reply_text("🔍 جاري البحث...")
        audio_file = None
        thumbnail_file = None
        cookie_file = None
        
        try:
            # البحث في الكاش أولاً
            cached_result = await get_cached_search(text)
            if cached_result:
                search_result = cached_result
            else:
                # البحث الجديد
                await status_message.edit_text("🔍 البحث في يوتيوب...")
                search = await asyncio.get_event_loop().run_in_executor(
                    None, lambda: SearchVideos(text, offset=1, mode="dict", max_results=1)
                )
                search_result = await asyncio.get_event_loop().run_in_executor(
                    None, search.result
                )
                
                if not search_result or not search_result.get("search_result") or len(search_result["search_result"]) == 0:
                    await status_message.delete()
                    return await message.reply_text("❌ لم يتم العثور على نتائج للبحث المطلوب")
                
                # حفظ في الكاش
                await cache_search_result(text, search_result)
            
            video_data = search_result["search_result"][0]
            video_url = video_data["link"]
            video_title = video_data["title"]
            video_id = video_data["id"]
            
            # فحص مدة الفيديو لتجنب الملفات الطويلة جداً
            await status_message.edit_text("📊 فحص معلومات الفيديو...")
            
            # الحصول على أفضل ملف كوكيز
            cookie_file = cookie_manager.get_best_cookie(user_id)
            if not cookie_file:
                await status_message.delete()
                return await message.reply_text("❌ لا توجد ملفات كوكيز متاحة")
            
            # تحميل الصورة المصغرة بشكل غير متزامن
            await status_message.edit_text("🖼️ تحميل الصورة المصغرة...")
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            thumbnail_file = await download_thumbnail_async(thumbnail_url)
            
            # إعدادات التحميل المحسنة
            await status_message.edit_text("⬇️ تحميل الملف الصوتي...")
            
            opts = {
                'format': 'bestaudio[filesize<50M]/bestaudio',  # تحديد حجم أقصى
                'outtmpl': f'audio_{int(time.time() * 1000000)}_%(title)s.%(ext)s',
                'cookiefile': cookie_file,
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                'writethumbnail': False,
                'writeinfojson': False,
                'ignoreerrors': True,
                'retries': 3,
                'fragment_retries': 3,
                'socket_timeout': 30,
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
            
            # فحص حجم الملف
            if audio_file and os.path.exists(audio_file):
                file_size = os.path.getsize(audio_file)
                if file_size > 50 * 1024 * 1024:  # 50 MB
                    await clean_temp_files(audio_file, thumbnail_file)
                    await status_message.delete()
                    return await message.reply_text("❌ حجم الملف كبير جداً (أكثر من 50 ميجا)")
            
            # إعداد معلومات الملف
            duration = int(ytdl_data.get("duration", 0))
            title = str(ytdl_data.get("title", "Unknown"))[:100]  # تحديد طول العنوان
            performer = str(ytdl_data.get("uploader", "Unknown"))[:50]
            caption = f"🎵 [{title}]({video_url})\n👤 {performer}"
            
            await status_message.edit_text("📤 إرسال الملف...")
            
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
            
            await status_message.delete()
            print(f"✅ تم تحميل بنجاح: {title} للمستخدم {user_id}")
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ خطأ في التحميل للمستخدم {user_id}: {error_msg}")
            
            # تسجيل خطأ الكوكيز
            if cookie_file:
                cookie_manager.report_cookie_error(cookie_file)
            
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
            # تنظيف الملفات المؤقتة
            await clean_temp_files(audio_file, thumbnail_file)

# دالة مساعدة للتحقق من صحة النص المطلوب تحميله
def validate_search_text(text):
    """التحقق من صحة النص المطلوب للبحث"""
    if not text or len(text.strip()) < 2:
        return False, "النص قصير جداً"
    
    if len(text) > 200:
        return False, "النص طويل جداً (أكثر من 200 حرف)"
    
    # فحص الأحرف المسموحة
    if not any(c.isalnum() or c.isspace() for c in text):
        return False, "النص يحتوي على أحرف غير صالحة"
    
    return True, "صالح"

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

# الأوامر مع / - محسنة
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل", "يوت", "بحث"], ""), group=71328934)
async def command_download_handler(client, message):
    """معالج الأوامر مع العلامة /"""
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
        # تجاهل الرسائل الطويلة جداً لتوفير الموارد
        if len(message.text) > 300:
            return
        
        # تجاهل الرسائل التي تحتوي على روابط أو mentions
        if any(x in message.text.lower() for x in ['http', 'www.', '@', '#']):
            return
        
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
        cache_size = len(search_cache)
        
        # إحصائيات Rate Limiting
        active_users = len(user_request_count)
        
        stats_text = f"""
📊 **إحصائيات البوت:**

🍪 **ملفات الكوكيز:** {len(cookie_manager.cookies_files)}
📋 **حجم الكاش:** {cache_size}/{MAX_CACHE_SIZE}
👥 **المستخدمين النشطين:** {active_users}
⬇️ **التحميلات النشطة:** {MAX_CONCURRENT_DOWNLOADS - download_semaphore._value}

🔍 **تفاصيل الكوكيز:**
"""
        
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
            old_size = len(search_cache)
            search_cache.clear()
        
        await message.reply_text(f"✅ تم تنظيف الكاش ({old_size} عنصر محذوف)")
        
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

# إضافة تنظيف دوري للذاكرة والكاش
async def periodic_cleanup():
    """تنظيف دوري للنظام كل ساعة"""
    while True:
        try:
            await asyncio.sleep(3600)  # ساعة واحدة
            
            # تنظيف الكاش من العناصر منتهية الصلاحية
            with cache_lock:
                current_time = time.time()
                expired_keys = [
                    key for key, data in search_cache.items() 
                    if current_time - data['timestamp'] > 1800  # 30 دقيقة
                ]
                
                for key in expired_keys:
                    del search_cache[key]
                
                if expired_keys:
                    print(f"🧹 تم تنظيف {len(expired_keys)} عنصر منتهي الصلاحية من الكاش")
            
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

# بدء التنظيف الدوري عند تشغيل البوت
asyncio.create_task(periodic_cleanup())

print("🚀 تم تحميل مدير تحميل يوتيوب المطور بنجاح!")
print(f"📊 الإعدادات الحالية:")
print(f"   🍪 ملفات الكوكيز: {len(cookie_manager.cookies_files)}")
print(f"   ⬇️ الحد الأقصى للتحميلات المتزامنة: {MAX_CONCURRENT_DOWNLOADS}")
print(f"   📋 الحد الأقصى لحجم الكاش: {MAX_CACHE_SIZE}")
print(f"   ⏱️ معدل الطلبات: 5 طلبات/دقيقة لكل مستخدم")
print(f"   🔐 نظام الحماية: مفعل")
print("=" * 50)