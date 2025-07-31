from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch 
import os
import aiohttp
import requests
import random 
import asyncio
import yt_dlp
from datetime import datetime, timedelta
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import pytgcalls
from pytgcalls.types import AudioQuality, VideoQuality
from typing import Union
from pyrogram import Client, filters 
from pyrogram import Client as client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType, ChatMemberStatus
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import (NoActiveGroupCall,)
from pytgcalls.types import (JoinedGroupCallParticipant,
                             LeftGroupCallParticipant, Update)
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded
import asyncio
from config import *
import numpy as np
from yt_dlp import YoutubeDL
from pytube import YouTube
from config import user, dev, call, logger, logger_mode, botname, appp, YOUTUBE_COOKIES_FILE
from bot import OWNER_ID
from CASERr.daty import get_call, get_userbot, get_dev, get_logger, del_userbot, del_call, get_devss
from pyrogram import Client
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from io import BytesIO
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
import asyncio
import aiohttp
import re
from typing import Union
from pyrogram.types import Message

playlist = {}
hossamm = []
vidd = {}
miii = {}
playing = {} 
usera = {}
user_mentio = {}
coun = {}
count = 0

async def Call(bot_username, message):
    hoss = await get_call(bot_username)
    @hoss.on_stream_end()
    async def stream_end_handler1(client, update: Update):
        if not isinstance(update, StreamAudioEnded):
            return        
        await change_stream(bot_username, update.chat_id, client, message)

async def join_assistant(client, hoss_chat_user, user):
        join = None
        hos_info = await client.get_chat(hoss_chat_user)    
        if hos_info.invite_link:
          hos_link = hos_info.invite_link
        else:
          print()
          return
        try:
          await user.join_chat(str(hos_link))
          join = True
        except Exception as e:
          pass
        return join    

async def pphoto(client, message, mi, user_mention, count):
    video_info = mi["search_result"][0]
    mo = video_info["link"]
    mio = mi["search_result"]
    title = video_info["title"]
    channel_name = mio[0]["channel"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    useram = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    namechat = f"{message.chat.title}"
    opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "quiet": True,
        "cookiefile": YOUTUBE_COOKIES_FILE,
        }
    url = mo
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=False)
        duration = ytdl_data.get('duration', None)
        info = ytdl.extract_info(url, download=False)
        views = info.get("view_count", "N/A")
        if duration is not None:
            duration_minutes = duration // 60
            duration_seconds = duration % 60
            video_duration = f"{duration_minutes}:{duration_seconds:02d}"
    me = await client.get_me()
    bot_username = me.username
    OWNER_ID = await get_devss(bot_username)
    usr = await client.get_chat(OWNER_ID)
    CASER = usr.username
    downloaded_photo = await client.download_media(usr.photo.big_file_id)
    im = Image.open(downloaded_photo)
    response = requests.get(useram)
    img = Image.open(BytesIO(response.content))
    image1 = img.resize((1280, 720))
    image2 = image1.convert("RGBA")
    background = image2.filter(ImageFilter.BoxBlur(10))
    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.5)
    im_square = crop_max_square(im)
    thumb_width = 500
    im_thumb = im_square.resize((thumb_width, thumb_width), Image.LANCZOS)
    im_thumb = mask_circle_transparent(im_thumb, 4)
    left_margin = 50
    top_margin = (background.height - thumb_width) // 2
    background.paste(im_thumb, (left_margin, top_margin), mask=im_thumb)
    draw = ImageDraw.Draw(background)
    center_x = left_margin + (thumb_width // 2)
    center_y = top_margin + (thumb_width // 2)
    radius = thumb_width // 2 + 13
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline=color, width=15)
    draw = ImageDraw.Draw(background)
    width, height = background.size
    border_width = 20
    border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle((0, 0, width - 1, height - 1), outline=border_color, width=border_width)
    arial = ImageFont.truetype("font2.ttf", 80)
    caesa = ImageFont.truetype("font.ttf", 40)
    caessa = ImageFont.truetype("font.ttf", 50)
    draw.text((600, 250), f"{thum}", (255, 255, 255), font=caessa)
    draw.text((600, 380), f"views : {views}", (255, 255, 255), font=caesa)
    draw.text((600, 420), f"time : {video_duration}", (255, 255, 255), font=caesa)
    draw.text((600, 460), f"channel : {channel_name}", (255, 255, 255), font=caesa)
    draw.text((600, 120), "PlaYinG EL NJUM", fill=(255, 165, 0), stroke_width=2, stroke_fill="white", font=arial)
    draw.line([(600, 220), (1050, 220)], fill=(255, 165, 0), width=7)
    background.save(f"{CASER}.png")
    photo = f"{CASER}.png"
    bot_username = client.me.username
    namechat = f"{message.chat.title}"    
    button = [[InlineKeyboardButton(text="ᎬΝᎠ", callback_data=f"stop"), InlineKeyboardButton(text="ᎡᎬՏႮᎷᎬ", callback_data=f"resume"), InlineKeyboardButton(text="ᏢᎪႮՏᎬ", callback_data=f"pause")], [InlineKeyboardButton(text="ᏟᎻᎬΝΝᎪᏞ", url=f"https://t.me/z1_xa"), InlineKeyboardButton(text="ᏀᎡΌႮᏢ", url=f"https://t.me/almhndssss")], [InlineKeyboardButton(text=f"كبير z1_xa", url=f"https://t.me/z1_xa")], [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك 🚦", url=f"https://t.me/{bot_username}?startgroup=True")]]
    if count == 0:
        await message.reply_photo(photo=photo, caption=f'🎶 𝗣𝗹𝗔𝘆𝗜𝗻𝗚 𝗡𝗼𝗪 𝗦𝘁𝗔𝗿𝗧𝗲𝗗\n\n𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : {thum}\n𝗕𝘆 : {user_mention}\n𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : <a href="https://t.me/{message.chat.username}">{namechat}</a>', reply_markup=InlineKeyboardMarkup(button))
    else:
        await message.reply_photo(photo=photo, caption=f'🎶 Add Track To Playlist » {count}\n\n𝗦𝗼𝗡𝗴 𝗡𝗮𝗠𝗲 : {thum}\n𝗕𝘆 : {user_mention}\n𝗚𝗿𝗢𝘂𝗣 𝗕𝘆 : <a href="https://t.me/{message.chat.username}">{namechat}</a>', reply_markup=InlineKeyboardMarkup(button))




async def join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention):
    global count
    userbot = await get_userbot(bot_username)
    hoss = await get_call(bot_username)
    file_path = audio_file
    audio_stream_quality = AudioQuality.MEDIUM
    video_stream_quality = VideoQuality.MEDIUM
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) 
              if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    try:
        await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType.PULSE_STREAM)
        hossamm.append(file_path)
        count = 0
        await pphoto(client, message, mi, user_mention, count)
        Done = True
    except NoActiveGroupCall:
        h = await join_assistant(client, group_id, userbot)
        if h:
            try:
                await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType.PULSE_STREAM)
                hossamm.append(file_path)
                Done = True
            except Exception:
                pass
    except :
        if group_id not in playlist:
            playlist[group_id] = []
            vidd[group_id] = []
            miii[group_id] = []
            coun[group_id] = []
            user_mentio[group_id] = []
        if group_id not in playlist[group_id]:
            playlist[group_id].append(file_path)
            vidd[group_id].append(vid)
            miii[group_id].append(mi)
            user_mentio[group_id].append(user_mention)
        if group_id in playlist:
            count = len(playlist[group_id])
            coun[group_id].append(count)
        await pphoto(client, message, mi, user_mention, count)
    except TelegramServerError:
        await client.send_message(message.chat.id, "**حدث خطأ في الخادم...**")
    except Exception as e:
        print(e)
    return False

async def _join_stream(hoss, message, stream, file_path):
    try:
        await hoss.join_group_call(message.chat.id, stream, stream_type=StreamType.PULSE_STREAM)
        hossamm.append(file_path)
        return True
    except Exception:
        return False
    
async def change_stream(bot_username, chat_id, client, message):
    hoss = await get_call(bot_username)
    if chat_id in playlist and playlist[chat_id] and vidd and vidd[chat_id] and miii and miii[chat_id] and coun and coun[chat_id] and user_mentio and user_mentio[chat_id]:
        next_song = playlist[chat_id].pop(0)
        vid = vidd[chat_id].pop(0)
        mi = miii[chat_id].pop(0)
        count = coun[chat_id].pop(0)
        user_mention = user_mentio[chat_id].pop(0)    
        user_mention = user_mention   
        count = count   
        file_path = next_song 
        vid = vid      
        mi = mi      
        try:
            audio_stream_quality = AudioQuality.MEDIUM
            video_stream_quality = VideoQuality.MEDIUM
            hossamm.clear()
            stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
            await hoss.change_stream(chat_id, stream)
            hossamm.append(file_path)
            await pphoto(client, message, mi, user_mention, count)
        except Exception as e:
            pass
    else:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception as e:
            await message.reply_text("يعم فوق مفيش حاجه شغاله اصلا 😂")

DOWNLOAD_FOLDER = "/root/downloads"

mamno = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]
@Client.on_message(filters.command(["تشغيل", "شغل", "فيد", "فيديو", "video", "play"], ""), group=57655580)
async def play_audio(client, message):
    group_id = message.chat.id
    text = None
    if message.reply_to_message:
        if "v" in message.command[0] or "ف" in message.command[0]:
            vid = True
        else:
            vid = None
    else:
        try:
            text = message.text.split(None, 1)[1]
        except IndexError:
            name = await client.ask(
                chat_id=message.chat.id,
                text="ارسل اسم او رابط الي تريد تشغيله.",
                reply_to_message_id=message.id,
                filters=filters.user(message.from_user.id),
                timeout=200
            )
            text = name.text
    if text is None:
        return
    if "v" in message.command[0] or "ف" in message.command[0]:
        vid = True
    else:
        vid = None
    try:
        mm = await message.reply_text("جاري التشغيل انتظر")
        playing.setdefault(group_id, []).clear()
        playing[group_id].append(message.from_user.id)
    except Exception as e:
        playing[group_id].append(5993309733)
    hos_info = await client.get_chat(group_id)
    hos_link = hos_info.invite_link or await message.reply("لا يمكن العثور على رابط الدعوة لهذه المجموعة/القناة\n قم برفعي مشرف في الجروب أولاً")
    if not hos_info.invite_link:
        return
    try:
        await user.join_chat(str(hos_link))
    except Exception as e:
        pass
    try:
        user_mention = f"{message.from_user.mention}"
    except Exception as e:
        user_mention = "ᏟᎻᎬΝΝᎪᏞ"
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    if not mi["search_result"]:
        return await message.reply("لم يتم العثور على نتائج.")
    video_info = mi["search_result"][0]
    mo = video_info["link"]
    mio = mi["search_result"]
    title = video_info["title"]
    audio_file = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp4")
    if os.path.exists(audio_file):
        await mm.delete()
        bot_username = client.me.username
        c = await join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention)
        if not c:
            return
        return 
    opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": audio_file,
        "quiet": True,
        "cookiefile": "/root/zombie/zombie.txt",
    }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(mo, download=True)
        audio_file = ytdl.prepare_filename(ytdl_data)
    await mm.delete()
    bot_username = client.me.username
    c = await join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention)
    if not c:
        return

@Client.on_message(filters.command(["مين شغل","م شغل","مين مشغل"], ""), group=5880)
async def playingy(client, message):
        chat_id = message.chat.id
        bot_username = client.me.username
        for hos in playing[chat_id]:
          user = await client.get_users(hos)
          user_mention = user.mention()
          await message.reply_text(f" هذا الشخص من قام بالتشغيل 🌿♥️ {user_mention}")


def crop_max_square(pil_img):
    """Crop a PIL image to the largest possible square."""
    width, height = pil_img.size
    size = min(width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    right = (width + size) // 2
    bottom = (height + size) // 2
    return pil_img.crop((left, top, right, bottom))

def mask_circle_transparent(pil_img, offset=0):
    """Apply a circular mask to a PIL image with transparent background."""
    width, height = pil_img.size
    mask = Image.new('L', pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, width - offset, height - offset), fill=255)
    pil_img.putalpha(mask)
    return pil_img

 
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


#..................................................بحث يوتيوب.................................................................

@Client.on_message(filters.command("بحث",prefixes=""),group=592231800844)
async def ytsearch(_, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text("/search needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text(" searching")
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"Song: {results[i]['title']}\n"
            text += f"Duration: {results[i]['duration']}\n"
            text += f"Views: {results[i]['views']}\n"
            text += f"Channel: {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
