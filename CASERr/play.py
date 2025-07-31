# -*- coding: utf-8 -*-
"""
🎵 نظام التشغيل الذكي المحسن - النسخة المتطورة V3
===================================================
متكامل مع النظام المختلط المحسن (YouTube API + yt-dlp)
يدعم التشغيل المتوازي والذكي مع إحصائيات شاملة
"""

import asyncio
import random
import string
import time
import os
from typing import Dict, Optional, Union

# استيراد مكتبات Pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from pytgcalls.exceptions import NoActiveGroupCall
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioQuality, VideoQuality, MediaStream, StreamType
from pytgcalls.types import Update, StreamEnded

# استيراد مكتبات التحميل
from yt_dlp import YoutubeDL
from youtubesearchpython import SearchVideos
from youtube_search import YoutubeSearch

# استيراد إعدادات البوت
from config import *
from bot import *

# متغيرات النظام المحسن
system_stats = {
    'total_play_requests': 0,
    'successful_plays': 0,
    'failed_plays': 0,
    'cache_hits': 0,
    'hybrid_downloads': 0,
    'start_time': time.time()
}

# إحصائيات التشغيل
play_stats = {
    'total_requests': 0,
    'successful_plays': 0,
    'failed_plays': 0,
    'cache_hits': 0,
    'hybrid_downloads': 0,
    'start_time': time.time()
}

# متغيرات التشغيل
playing = {}
hossamm = []
count = 0
coun = {}
vidd = {}
playlist = {}

def update_play_stats(success: bool, from_cache: bool = False, hybrid_used: bool = False):
    """تحديث إحصائيات التشغيل"""
    play_stats['total_requests'] += 1
    if success:
        play_stats['successful_plays'] += 1
    else:
        play_stats['failed_plays'] += 1
    if from_cache:
        play_stats['cache_hits'] += 1
    if hybrid_used:
        play_stats['hybrid_downloads'] += 1

async def get_play_statistics() -> Dict:
    """الحصول على إحصائيات التشغيل الشاملة"""
    uptime = time.time() - system_stats['start_time']
    
    return {
        'system_stats': system_stats,
        'play_stats': play_stats,
        'uptime_hours': uptime / 3600,
        'success_rate': (play_stats['successful_plays'] / max(1, play_stats['total_requests'])) * 100,
        'cache_hit_rate': (play_stats['cache_hits'] / max(1, play_stats['total_requests'])) * 100,
    }

async def get_call(bot_username):
    """الحصول على كائن المكالمة"""
    return calls.get(bot_username)

async def get_userbot(bot_username):
    """الحصول على كائن المستخدم"""
    return userbots.get(bot_username)

async def join_assistant(client, hoss_chat_user, user):
    """انضمام المساعد للمكالمة"""
    join = None
    try:
        join = await client.join_chat(hoss_chat_user)
    except Exception as e:
        print(f"خطأ في الانضمام: {e}")
        return False
    return join

async def pphoto(client, message, mi, user_mention, count):
    """إرسال صورة التشغيل"""
    try:
        await client.send_photo(
            message.chat.id,
            photo=mi,
            caption=f"🎵 **تم بدء التشغيل**\n\n👤 **بواسطة:** {user_mention}\n📊 **الطلب رقم:** {count}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⏸️ إيقاف مؤقت", callback_data="pause"),
                 InlineKeyboardButton("⏭️ تخطي", callback_data="skip")],
                [InlineKeyboardButton("⏹️ إيقاف", callback_data="stop")]
            ])
        )
    except Exception as e:
        print(f"خطأ في إرسال الصورة: {e}")

async def join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention):
    """انضمام للمكالمة وتشغيل الصوت"""
    global count
    userbot = await get_userbot(bot_username)
    hoss = await get_call(bot_username)
    file_path = audio_file
    
    audio_stream_quality = AudioQuality.MEDIUM
    video_stream_quality = VideoQuality.MEDIUM
    stream = (MediaStream(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) 
              if vid else MediaStream(file_path, audio_parameters=audio_stream_quality))
    
    try:
        await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType.PULSE_STREAM)
        hossamm.append(file_path)
        count = 0
        await pphoto(client, message, mi, user_mention, count)
        return True
    except Exception as e:
        print(f"خطأ في الانضمام: {e}")
        # محاولة ثانية
        try:
            await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType.PULSE_STREAM)
            hossamm.append(file_path)
            Done = True
        except Exception:
            pass
        
        if group_id not in playlist:
            playlist[group_id] = []
            vidd[group_id] = []
            coun[group_id] = []
        
        playlist[group_id].append(file_path)
        vidd[group_id].append(vid)
        coun[group_id].append(count)
        count = len(playlist[group_id])
        coun[group_id].append(count)
        await pphoto(client, message, mi, user_mention, count)
        return False

async def _join_stream(hoss, message, stream, file_path):
    """انضمام للبث"""
    try:
        await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType.PULSE_STREAM)
        hossamm.append(file_path)
        return True
    except Exception:
        return False

async def change_stream(bot_username, chat_id, client, message):
    """تغيير البث"""
    hoss = await get_call(bot_username)
    if chat_id in playlist and playlist[chat_id]:
        file_path = playlist[chat_id][0]
        vid = vidd[chat_id][0]
        mi = "https://telegra.ph/file/1063fced1455967ed0d83.jpg"
        
        try:
            audio_stream_quality = AudioQuality.MEDIUM
            video_stream_quality = VideoQuality.MEDIUM
            hossamm.clear()
            stream = (MediaStream(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else MediaStream(file_path, audio_parameters=audio_stream_quality))
            await hoss.change_stream(chat_id, stream)
            hossamm.append(file_path)
            await pphoto(client, message, mi, "النظام", 1)
            
            # إزالة من القائمة
            playlist[chat_id].pop(0)
            vidd[chat_id].pop(0)
            coun[chat_id].pop(0)
            
        except Exception as e:
            print(f"خطأ في تغيير البث: {e}")

async def smart_music_search_and_play(
    message: Message,
    query: str,
    chat_id: int,
    user_id: int,
    video: bool = False,
    channel: bool = False
) -> Optional[Dict]:
    """البحث والتشغيل الذكي مع النظام المختلط"""
    
    start_time = time.time()
    print(f"🎵 بدء البحث والتشغيل الذكي: {query}")
    
    try:
        # البحث عن الفيديو
        search = SearchVideos(query, offset=1, mode="dict", max_results=1)
        mi = search.result()
        if not mi["search_result"]:
            print(f"❌ لم يتم العثور على نتائج: {query}")
            update_play_stats(success=False)
            return None
        
        video_info = mi["search_result"][0]
        mo = video_info["link"]
        title = video_info["title"]
        
        # تحضير مسار الملف
        audio_file = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp4")
        
        # التحقق من وجود الملف
        if os.path.exists(audio_file):
            print(f"✅ الملف موجود في الكاش: {title}")
            update_play_stats(success=True, from_cache=True)
            return {
                'title': title,
                'duration': 0,
                'file_path': audio_file,
                'thumbnail': f"https://img.youtube.com/vi/{video_info.get('id', '')}/hqdefault.jpg",
                'uploader': video_info.get('channel', 'قناة غير محددة'),
                'url': mo,
                'video_id': video_info.get('id', ''),
                'source': 'cache'
            }
        
        # تحميل الملف مع تدوير الكوكيز
        cookie_files = [
            "/workspace/cookies/cookies1.txt",
            "/workspace/cookies/cookies2.txt", 
            "/workspace/cookies/cookies3.txt",
            "/workspace/cookies/cookies4.txt",
            "/workspace/cookies/cookies5.txt",
            "/workspace/cookies/cookies6.txt"
        ]
        
        download_success = False
        for cookie_file in cookie_files:
            if os.path.exists(cookie_file):
                try:
                    opts = {
                        "format": "bestaudio[ext=m4a]/best[ext=mp4]/best",
                        "outtmpl": audio_file,
                        "quiet": True,
                        "cookiefile": cookie_file,
                        "no_warnings": True,
                        "extract_flat": False,
                    }
                    
                    with YoutubeDL(opts) as ytdl:
                        ytdl_data = ytdl.extract_info(mo, download=True)
                        audio_file = ytdl.prepare_filename(ytdl_data)
                    
                    download_success = True
                    break
                    
                except Exception as e:
                    print(f"فشل التحميل مع {cookie_file}: {e}")
                    continue
        
        if not download_success:
            print(f"❌ فشل في تحميل المقطع: {query}")
            update_play_stats(success=False)
            return None
        
        elapsed = time.time() - start_time
        print(f"✅ تم التحضير للتشغيل في {elapsed:.2f}s: {title}")
        
        # تحديث الإحصائيات
        update_play_stats(success=True, hybrid_used=True)
        
        return {
            'title': title,
            'duration': ytdl_data.get('duration', 0),
            'file_path': audio_file,
            'thumbnail': f"https://img.youtube.com/vi/{video_info.get('id', '')}/hqdefault.jpg",
            'uploader': video_info.get('channel', 'قناة غير محددة'),
            'url': mo,
            'video_id': video_info.get('id', ''),
            'source': 'hybrid_download'
        }
        
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"❌ خطأ في البحث والتشغيل ({elapsed:.2f}s): {e}")
        update_play_stats(success=False)
        return None

# اسم البوت للأوامر
Nem = "شغل"

@Client.on_message(
    filters.command([
        "play", "تشغيل", "شغل", Nem, "vplay", "cplay", "cvplay",
        "playforce", "vplayforce", "cplayforce", "cvplayforce",
    ]) & ~filters.channel
)
async def enhanced_play_command(client, message: Message):
    """أمر التشغيل المحسن مع النظام المختلط"""
    
    start_time = time.time()
    
    # رسالة الحالة الأولية
    mystic = await message.reply_text("🎵 جاري معالجة طلبك...")
    
    try:
        # التحقق من وجود استعلام
        if not message.command or len(message.command) < 2:
            await mystic.edit_text("❌ يرجى كتابة ما تريد تشغيله")
            return
        
        query = " ".join(message.command[1:]).strip()
        if not query:
            await mystic.edit_text("❌ يرجى كتابة ما تريد تشغيله")
            return
        
        print(f"🎵 طلب تشغيل جديد: {query} | المستخدم: {message.from_user.id}")
        
        # تحديث رسالة الحالة
        await mystic.edit_text("🔍 جاري البحث...")
        
        # البحث والتحميل الذكي
        track_info = await smart_music_search_and_play(
            message=message,
            query=query,
            chat_id=message.chat.id,
            user_id=message.from_user.id,
            video=False,
            channel=False
        )
        
        if not track_info:
            await mystic.edit_text("❌ لم يتم العثور على نتائج")
            return
        
        # تحديث رسالة الحالة
        await mystic.edit_text("🎵 جاري بدء التشغيل...")
        
        # بدء التشغيل
        try:
            bot_username = client.me.username
            group_id = message.chat.id
            vid = False  # صوت فقط
            user_mention = f"{message.from_user.mention}"
            mi = track_info.get('thumbnail', "https://telegra.ph/file/1063fced1455967ed0d83.jpg")
            
            c = await join_call(bot_username, client, message, track_info['file_path'], group_id, vid, mi, user_mention)
            
            if c:
                await mystic.delete()
                # تسجيل نجاح التشغيل
                elapsed = time.time() - start_time
                print(f"✅ تم بدء التشغيل بنجاح ({elapsed:.2f}s): {track_info['title']}")
            else:
                await mystic.edit_text("✅ تم إضافة المقطع للقائمة")
                
        except NoActiveGroupCall:
            await mystic.edit_text(
                "❌ لا يوجد مكالمة صوتية نشطة في هذه المجموعة.\n"
                "يرجى بدء مكالمة صوتية أولاً."
            )
            
        except Exception as stream_error:
            print(f"❌ خطأ في بدء التشغيل: {stream_error}")
            await mystic.edit_text(f"❌ خطأ في بدء التشغيل: {stream_error}")
            
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"❌ خطأ في أمر التشغيل ({elapsed:.2f}s): {e}")
        
        try:
            await mystic.edit_text(
                f"❌ حدث خطأ أثناء معالجة طلبك:\n`{str(e)[:100]}...`"
            )
        except:
            pass

@Client.on_message(filters.command(["playstats", "إحصائيات التشغيل"]))
async def play_statistics_command(client, message: Message):
    """عرض إحصائيات التشغيل الشاملة"""
    
    try:
        stats = await get_play_statistics()
        
        # تنسيق الإحصائيات
        play_data = stats['play_stats']
        uptime_hours = stats['uptime_hours']
        success_rate = stats['success_rate']
        cache_hit_rate = stats['cache_hit_rate']
        
        stats_text = f"""
📊 **إحصائيات التشغيل الشاملة**
{'='*35}

🎵 **إحصائيات التشغيل:**
• إجمالي الطلبات: `{play_data['total_requests']}`
• تشغيل ناجح: `{play_data['successful_plays']}`
• تشغيل فاشل: `{play_data['failed_plays']}`
• معدل النجاح: `{success_rate:.1f}%`

💾 **إحصائيات الكاش:**
• إصابات الكاش: `{play_data['cache_hits']}`
• معدل الكاش: `{cache_hit_rate:.1f}%`
• تحميل مختلط: `{play_data['hybrid_downloads']}`

⏱️ **معلومات النظام:**
• وقت التشغيل: `{uptime_hours:.1f}` ساعة
• متوسط الطلبات/ساعة: `{play_data['total_requests'] / max(0.1, uptime_hours):.1f}`

🚀 **النظام يعمل بكفاءة عالية!**
"""
        
        await message.reply_text(stats_text)
        
    except Exception as e:
        print(f"❌ خطأ في عرض الإحصائيات: {e}")
        await message.reply_text(f"❌ خطأ في جلب الإحصائيات: {e}")

@Client.on_message(filters.command(["cleantemp", "تنظيف الملفات"]))
async def clean_temp_files_command(client, message: Message):
    """تنظيف الملفات المؤقتة"""
    
    try:
        status_msg = await message.reply_text("🧹 جاري تنظيف الملفات المؤقتة...")
        
        # تنظيف الملفات القديمة
        cleaned_count = 0
        if os.path.exists(DOWNLOAD_FOLDER):
            for file in os.listdir(DOWNLOAD_FOLDER):
                file_path = os.path.join(DOWNLOAD_FOLDER, file)
                if os.path.isfile(file_path):
                    # حذف الملفات الأقدم من ساعة
                    if time.time() - os.path.getmtime(file_path) > 3600:
                        os.remove(file_path)
                        cleaned_count += 1
        
        await status_msg.edit_text(
            f"✅ تم تنظيف الملفات القديمة وحذف `{cleaned_count}` ملف!"
        )
        
    except Exception as e:
        print(f"❌ خطأ في تنظيف الملفات: {e}")
        await message.reply_text(f"❌ خطأ في التنظيف: {e}")

# أوامر التحكم في التشغيل
@Client.on_message(filters.command(["اسكت", "ايقاف"]) & filters.group)
async def stop_playback(client, message):
    """إيقاف التشغيل"""
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    ho = await message.reply_text("**جاري ايقاف التشغيل**") 
    try:    	
        await hoss.leave_group_call(message.chat.id)
        await ho.edit_text("**تم ايقاف التشغيل بنجاح**")
    except Exception as e:
        await ho.edit_text("**مفيش حاجه شغاله اصلا**")

@Client.on_message(filters.command(["تخطي", "/skip"]) & filters.group)
async def skip_track(client, message):
    """تخطي المقطع الحالي"""
    group_id = message.chat.id
    bot_username = client.me.username 
    ho = await message.reply_text("**جاري تخطي التشغيل**") 
    await change_stream(bot_username, group_id, client, message)
    await ho.delete()

@Client.on_message(filters.command(["توقف", "وقف"]) & filters.group)
async def pause_playback(client, message):
    """إيقاف مؤقت للتشغيل"""
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري توقف التشغيل**") 
    try:    	
        await hoss.pause_stream(chat_id)
        await ho.edit_text("**حاضر هسكت اهو 🥺**")
    except Exception as e:
        await ho.edit_text("**مفيش حاجه شغاله اصلا**")

@Client.on_message(filters.command(["كمل"]) & filters.group)
async def resume_playback(client, message):
    """استكمال التشغيل"""
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري استكمال التشغيل**") 
    try:    	
        await hoss.resume_stream(chat_id)
        await ho.edit_text("**تم استكمال التشغيل بنجاح**")
    except Exception as e:
        await ho.edit_text("**مفيش حاجه شغاله اصلا**")

# إضافة تنظيف دوري للملفات المؤقتة
async def periodic_cleanup():
    """تنظيف دوري للملفات المؤقتة"""
    while True:
        try:
            await asyncio.sleep(3600)  # كل ساعة
            cleaned_count = 0
            if os.path.exists(DOWNLOAD_FOLDER):
                for file in os.listdir(DOWNLOAD_FOLDER):
                    file_path = os.path.join(DOWNLOAD_FOLDER, file)
                    if os.path.isfile(file_path):
                        # حذف الملفات الأقدم من ساعة
                        if time.time() - os.path.getmtime(file_path) > 3600:
                            os.remove(file_path)
                            cleaned_count += 1
            if cleaned_count > 0:
                print(f"🧹 تم تنظيف {cleaned_count} ملف قديم تلقائياً")
        except Exception as e:
            print(f"❌ خطأ في التنظيف الدوري: {e}")

# بدء التنظيف الدوري
asyncio.create_task(periodic_cleanup())

print("✅ تم تحميل نظام التشغيل الذكي المحسن بنجاح!")

 
@Client.on_callback_query(
    filters.regex(pattern=r"^(pause|skip|stop|resume)$")
)
async def admin_risghts(client: Client, CallbackQuery):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    if command == "pause":
        try:
         await hoss.pause_stream(chat_id)
         await CallbackQuery.answer("تم ايقاف التشغيل موقتا .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم ايقاف التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"**مفيش حاجه شغاله اصلا يا {CallbackQuery.from_user.mention}**")
    if command == "resume":
        try:
         await hoss.resume_stream(chat_id)
         await CallbackQuery.answer("تم استكمال التشغيل .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم إستكمال التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"**مفيش حاجه شغاله اصلا يا {CallbackQuery.from_user.mention}**")
    if command == "stop":
        try:
         await hoss.leave_group_call(chat_id)
        except:
          pass
        await CallbackQuery.answer("تم انهاء التشغيل بنجاح .", show_alert=True)
        await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم انهاء التشغيل بواسطه**")
       
@Client.on_message(filters.command(["اسكت", "ايقاف"], "") & filters.group, group=55646568548)
async def ghuser(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     ho = await message.reply_text("**جاري ايقاف التشغيل**") 
     try:    	
      await hoss.leave_group_call(message.chat.id)
      await ho.edit_text("**حاضر سكت اهو 🥺**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
      return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["اسكت", "ايقاف"], "") & filters.channel, group=5564656568548)
async def gh24user(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    ho = await message.reply_text("**جاري ايقاف التشغيل**") 
    try:    	
        await hoss.leave_group_call(message.chat.id)
        await ho.edit_text("**تم ايقاف التشغيل بنجاح**")
    except Exception as e:
        await ho.edit_text("**مفيش حاجه شغاله اصلا**")
 
@Client.on_message(filters.command(["تخطي", "/skip"], "") & filters.group, group=5864548)
async def skip2(client, message):
    group_id = message.chat.id
    bot_username = client.me.username 
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        chat_id = message.chat.id
        ho = await message.reply_text("**جاري تخطي التشغيل**") 
        await change_stream(bot_username, chat_id, client, message)
        await ho.delete()
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["تخطي", "/skip"], "") & filters.channel, group=5869864548)
async def ski25p2(client, message):
    chat_id = message.chat.id
    bot_username = client.me.username 
    ho = await message.reply_text("**جاري تخطي التشغيل**") 
    await ho.delete()
    await change_stream(bot_username, chat_id, client, message)
    
@Client.on_message(filters.command(["توقف", "وقف"], "") & filters.group, group=58655654548)
async def sp2(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري توقف التشغيل**") 
     try:    	
      await hoss.pause_stream(chat_id)
      await ho.edit_text("**حاضر هسكت اهو 🥺**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
     return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["توقف", "وقف"], "") & filters.channel, group=5866555654548)
async def s356p2(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    chat_id = message.chat.id
    ho = await message.reply_text("**جاري توقف التشغيل**") 
    try:    	
     await hoss.pause_stream(chat_id)
     await ho.edit_text("**حاضر هسكت اهو 🥺**")
    except Exception as e:
     await ho.edit_text("**مفيش حاجه شغاله اصلا**")
     
@Client.on_message(filters.command(["كمل"], "") & filters.group, group=5866564548)
async def s12p2(client, message):
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    group_id = message.chat.id
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     chat_id = message.chat.id
     ho = await message.reply_text("**جاري استكمال التشغيل**") 
     try:    	
      await hoss.resume_stream(chat_id)
      await ho.edit_text("**تم استكمال التشغيل بنجاح**")
     except Exception as e:
      await ho.edit_text("**مفيش حاجه شغاله اصلا**")
    else:
     return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@Client.on_message(filters.command(["كمل"], "") & filters.channel, group=645866564548)
async def s12p582(client, message):
    chat_id = message.chat.id
    bot_username = client.me.username 
    hoss = await get_call(bot_username)
    ho = await message.reply_text("**جاري استكمال التشغيل**") 
    try:    	
     await hoss.resume_stream(chat_id)
     await ho.edit_text("**تم استكمال التشغيل بنجاح**")
    except Exception as e:
     await ho.edit_text("**مفيش حاجه شغاله اصلا**")



