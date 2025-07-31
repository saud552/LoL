from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
import time 
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from pyrogram import Client as client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
import asyncio
from config import *
import numpy as np
from yt_dlp import YoutubeDL
from pyrogram import Client
from youtubesearchpython import SearchVideos
from CASERr.CASERr import get_channel, johned
from io import BytesIO
import aiofiles
import wget
from pyrogram.types import *
import os, json, requests
from config import YOUTUBE_COOKIES_FILE

yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]
    
@Client.on_message(filters.command(["تحميل", "نزل", "تنزيل", "يوتيوب","حمل","تنزل"], ""), group=71328934)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    if await johned(client, message):
     return
    
    # طلب النص من المستخدم مباشرة
    try:
        name = await client.ask(message.chat.id, text="عاوز تنزل ايه..🚦", filters=filters.user(message.from_user.id), timeout=200)
        text = name.text
    except:
        return await message.reply_text("انتهت مهلة الطلب، حاول مرة أخرى")
    
    if text in yoro:
        return await message.reply_text("لا يمكن تنزيل هذا❌")  
    
    h = await message.reply_text(f"جاري البحث انتظر قليلا 🚦")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {'format': 'bestaudio[ext=m4a]', 'outtmpl': '%(title)s.%(ext)s', "cookiefile": YOUTUBE_COOKIES_FILE}
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"خطأ في التحميل : {e}")
        await h.delete()
        return await message.reply_text("حدث خطأ أثناء التحميل، حاول مرة أخرى")
    
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await h.delete()
    try:
        await client.send_audio(message.chat.id, audio=audio_file, duration=int(ytdl_data["duration"]), title=str(ytdl_data["title"]), performer=str(ytdl_data["uploader"]), file_name=str(ytdl_data["title"]), thumb=sedlyf,caption=capy)
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f"خطأ في الإرسال\n{e}")
        await message.reply_text("حدث خطأ أثناء إرسال الملف")