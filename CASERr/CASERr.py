import asyncio
import requests
import random
import re
import os
import time
import datetime
import redis, re
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client as client
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from bot import OWNER_USERNAME
from unidecode import unidecode
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram.errors import FloodWait
from os import remove
from asyncio import sleep
from pyrogram.types import *
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from bot import OWNER
from pyrogram.types import Chat, User
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from unidecode import unidecode
from io import BytesIO
import aiofiles
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

##مطور السورس
caes = ["z1_xa"]
casery = "z1_xa"
##ايدي مطور السورس
caserid = 1457243602
##قناه السورس
source = "https://t.me/z1_1ax" 
ch = "z1_1ax" 
##جروب السورس
group = "https://t.me/z1_1ax" 
##لوجو السورس
photosource = "https://imgg.io/image/0hzyK"
##اسمك&الميوزك
muusiic = "ABBAS" 
##اسم السورس ع صوره التشغيل
suorce = "SoUrCe ABBAS" 


name = f"{OWNER}"

r = redis.Redis(
    host="127.0.0.1",
    port=6379,)


Keyard = ReplyKeyboardMarkup(
  [
    [("• السورس •")], 
    [("• مطور البوت •"),("• مطور السورس •")], 
    [("• صراحه •"),("• تويت •")],
    [("• حروف •"),("• امثله •")],
    [("• نكته •"),("• احكام •")],
    [("• قران •"),("• ازكار •")],
    [("• لو خيروك •")],
    [("• صور شباب •"),("• صور بنات •")],
    [("• انمي •"),("• استوري •")],
    [("• اغاني •")],
    [("• ممثلين •"),("• مغنين •")],
    [("• مشاهير •"),("• لاعبين •")],
    [("• اعلام •"),("• افلام •")],
    [("• لغز •"),("• مختلف •")],  
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Keyboard = ReplyKeyboardMarkup(
  [
    [("قسم البوت"), ("قسم المساعد")],   
    [("قسم الاذاعه"), ("قسم الترويج")],   
    [("قسم الاشتراك"), ("قسم الاحتياطي")],     
    [("《الاحصائيات》")],
    [("قسم التشغيل")],    
    [("قسم الحظر")],    
    [("قسم التفعيل والتعطيل")],
    [("قسم الحذف والاستخراج")],
    [("كيب الاعضاء")],
    [("مطور السورس"), ("مطور البوت")],
    [("سورس")],
  ],
  resize_keyboard=True,  
  placeholder=f"{name}"
)

Keybcasoard = ReplyKeyboardMarkup(
  [
    [("قسم البوت"), ("قسم المساعد")],   
    [("قسم الاذاعه"), ("قسم الترويج")],   
    [("قسم الاشتراك"), ("قسم الاحتياطي")],     
    [("《الاحصائيات》")],
    [("قسم التشغيل")],    
    [("قسم الحظر")],    
    [("قسم التفعيل والتعطيل")],
    [("قسم الحذف والاستخراج")],
    [("كيب الاعضاء")],
    [("تفعيل الصلاحيات المدفوعه"),("تعطيل الصلاحيات المدفوعه")],
    [("مطور السورس"), ("مطور البوت")],
    [("سورس")],
  ],
  resize_keyboard=True,  
  placeholder=f"{name}"
)


Keyboazard = ReplyKeyboardMarkup(
  [
    [("《اذاعة》")],
    [("《اذاعة بالمجموعات》")], 
    [("《اذاعة بالتوجيه》")], 
    [("《اذاعة بالتثبيت》")],  
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True,  
  placeholder=f"{name}"
)

Keyttd = ReplyKeyboardMarkup(
  [
    [("ترويج للحمايه")],
    [("ترويج للميوزك")],   
    [("《الغاء》")],
    [("رجوع")],
  ],
  resize_keyboard=True,  
  placeholder=f"{name}"
)

Kealrdyttd = ReplyKeyboardMarkup(
  [
    [("تعيين اسم البوت")],
    [("تعيين جروب السورس"), ("تعيين قناه السورس")],   
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Keal56rdyttd = ReplyKeyboardMarkup(
  [
    [("اضف قناه اشتراك")],  
    [("حذف قناه اشتراك")],   
    [("قنوات الاشتراك")],     
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Keal16rdyttd = ReplyKeyboardMarkup(
  [
    [("الجروبات"), ("المستخدمين")],
    [("رفع نسخه الجروبات"), ("رفع نسخه الاشخاص")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Keal36rdyttd = ReplyKeyboardMarkup(
  [
    [("《تعطيل التواصل》"), ("《تفعيل التواصل》")],
    [("تعطيل البوت بالصوره"),("تفعيل البوت بالصوره")],
    [("قفل الردود"),("فتح الردود")],
    [("قفل الميوزك"),("فتح الميوزك")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Keal66rdyttd = ReplyKeyboardMarkup(
  [
    [("حظر مستخدم")],
    [("الغاء الحظر")],   
    [("المحظورين")],    
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Key282ard = ReplyKeyboardMarkup(
  [
    [("• استخرج جلسه •")],    
    [("• استخراج api •")],    
    [("• حذف حساب •")],    
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

Keal360rdyttd = ReplyKeyboardMarkup(
  [
    [("شغل"), ("فيد")],
    [("كمل"), ("وقف")],
    [("ايقاف"), ("تخطي")],
    [("رجوع")],
  ],
  resize_keyboard=True, 
  placeholder=f"{name}"
)

caes = caes
casery = casery
source = source
group = group
caserid = caserid
photosource = photosource
muusiic = muusiic
suorce = suorce
names = {} 
devuser = {} 
devchannel = {} 
devgroup = {} 
devphots = {} 
devess = {} 

@Client.on_message(filters.regex("حظر مستخدم") & filters.private, group=71513)
async def maadd_CASER(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    ask = await client.ask(message.chat.id, f"ارسل ايدي الشخص", timeout=300)
    channel = int(ask.text)
    oo = [channel]
    add_CASER(oo, bot_username)
    await client.send_message(message.chat.id, "تم الحظر بنجاح")
            
@Client.on_message(filters.command("المحظورين", "") & filters.private, group=71513089)
async def botzbjbbojCASER(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    o = 0
    text = "المحظورين\n"
    for x in get_CASER(bot_username):
        o += 1
        channel = x[0]
        text += f"{o}- {channel}\n"
    if o == 0:
        return await message.reply_text("لا يوجد محظورين")
    await message.reply_text(text)
  
@Client.on_message(filters.command(["فك الحظر","الغاء الحظر"], "") & filters.private, group=715138608)
async def deletehombie(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.id == OWNER_ID:
    try:
        bot = await client.ask(message.chat.id, "هات ايدي المستخدم", timeout=200)
    except:
        return
    channel = int(bot.text)
    for x in get_CASER(bot_username):
        if x[0] == channel:
            del_CASER(x, bot_username)
    await message.reply_text("تم الغاء حظر المستخدم")
 
def add_CASER(bots, bot_username):
    if is_CASER(bots, bot_username):
        return
    r.sadd(f"CASER{bot_username}", str(bots))

def is_CASER(bots, bot_username):
    try:
        a = get_CASER(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_CASER(bots, bot_username):
    if not is_CASER(bots, bot_username):
        return False
    r.srem(f"CASER{bot_username}", str(bots))

def get_CASER(bot_username):
    try:
        lst = []
        for a in r.smembers(f"CASER{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def johCASER(client, message):
    CASER = []  
    bot_username = client.me.username
    for x in get_CASER(bot_username):
        ch = x[0]
        CASER.append(ch)
    if message.from_user.id in CASER:
        return True     
    return False
   
@Client.on_message(filters.command(["تفعيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def for_5s(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  usr1 = await client.get_chat(OWNER_ID)
  wenru = usr1.username
  if message.from_user.username in caes:
    try: 
     devess[bot_username] = wenru
     await message.reply_text(f"تم تفعيل الصلاحيات المدفوعة للبوت بنجاح، عزيزي المبرمج 🎧")
    except:
     return await message.reply_text("تم التفعيل من قبل")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
     
@Client.on_message(filters.command(["تعطيل الصلاحيات المدفوعه"], "") & filters.private, group=667563)
async def disabl(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
    if message.from_user.username in caes:
        if devess[bot_username] == wenru:
            del devess[bot_username]
            await message.reply_text("تم تعطيل الصلاحيات المدفوعة للبوت وحذفها من التخزين بنجاح 🎧")
        else:
            await message.reply_text("الصلاحيات غير مفعلة من قبل")
    else:
        await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
    
@Client.on_message(filters.regex("تعيين اسم البوت") & filters.private, group=757113)
async def bot_name(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.id == OWNER_ID or message.from_user.username in caes:
   try:
    bot = await client.ask(message.chat.id, "هات اسم البوت", timeout=200)
   except:
    return
   bot_name = bot.text
   names[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين اسم البوت بنجاح 🎧**")
   
@Client.on_message(filters.regex("تعيين قناه السورس") & filters.private, group=716713)
async def dev_channel(client, message):
  bot_username = client.me.username
  bot_id = client.me.id
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
   try:
    bot = await client.ask(message.chat.id, "هات رابط القناه", timeout=200)
   except:
    return
   bot_name = bot.text
   devchannel[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين قناه السورس بنجاح 🎧**")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
   
@Client.on_message(filters.regex("تعيين جروب السورس") & filters.private, group=711513)
async def dev_group(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
   try:
    bot = await client.ask(message.chat.id, "هات رابط الجروب", timeout=200)
   except:
    return
   bot_name = bot.text
   devgroup[bot_username] = bot_name
   await client.send_message(message.chat.id, "**تم تعيين جروب السورس بنجاح 🎧**")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
   
@Client.on_message(filters.regex("اضف قناه اشتراك") & filters.private, group=7113)
async def maadd_channel(client, message):
  bot_username = client.me.username
  makr = f"@{bot_username}"
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    ask = await client.ask(message.chat.id, f"لتفعيل الاشتراك الاجباري \n قم باضافه هذا البوت {makr} الي قناتك\nلو ضفته ارسل `تم`", timeout=300)
    me = ask.text
    if me == "تم":
     try:
      bot = await client.ask(message.chat.id, "هات رابط القناه", timeout=200)
     except:
      return
     channel = bot.text.replace("https://t.me/", "")  
     oo = [channel]
     add_channel(oo, bot_username)
     await client.send_message(message.chat.id, "تم حفظ القناه بنجاح")
  else:
    await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
            
@Client.on_message(filters.command("قنوات الاشتراك", "") & filters.private)
async def botzbjbbojfchhmbie(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    o = 0
    text = "قائمة القنوات\n"
    for x in get_channel(bot_username):
        o += 1
        channel = x[0]
        text += f"{o}- @{channel}\n"
    if o == 0:
        return await message.reply_text("لا يوجد قنوات")
    await message.reply_text(text)
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
  
@Client.on_message(filters.command("حذف قناه اشتراك", "") & filters.private)
async def delete_bot_zchombie(client, message):
  bot_username = client.me.username
  dev = devess.get(bot_username) if devess.get(bot_username) else f"{caes}"
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.username in caes or message.from_user.username == dev:
    try:
        bot = await client.ask(message.chat.id, "هات رابط القناه", timeout=200)
    except:
        return
    channel = bot.text.replace("https://t.me/", "")
    for x in get_channel(bot_username):
        if x[0] == channel:
            del_channel(x, bot_username)
    await message.reply_text("تم حذف القناه بنجاح")
  else:
   await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر في الوضع المدفوع، تواصل مع مطور السورس")
 
def add_channel(bots, bot_username):
    if is_channel(bots, bot_username):
        return
    r.sadd(f"channel{bot_username}", str(bots))

def is_channel(bots, bot_username):
    try:
        a = get_channel(bot_username)
        if bots in a:
            return True
        return False
    except:
        return False

def del_channel(bots, bot_username):
    if not is_channel(bots, bot_username):
        return False
    r.srem(f"channel{bot_username}", str(bots))

def get_channel(bot_username):
    try:
        lst = []
        for a in r.smembers(f"channel{bot_username}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def johned(client, message):
   try:
       bot_username = client.me.username
       channels = get_channel(bot_username)
       
       # إذا لم توجد قنوات، لا نفرض الاشتراك
       if not channels:
           return False
           
       for x in channels:
           try:
               ch = x[0] if isinstance(x, (list, tuple)) else str(x)
               if not ch:
                   continue
                   
               keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(" اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{ch}")]])
               
               # فحص العضوية مع معالجة شاملة للأخطاء
               try:
                   get = await client.get_chat_member(ch, message.from_user.id)
                   # إذا وصلنا هنا، المستخدم مشترك في هذه القناة
               except Exception as member_error:
                   # المستخدم غير مشترك أو خطأ في الوصول للقناة
                   try:
                       await message.reply_text(
                           f"🚦عذرا عزيزي {message.from_user.mention} يجب عليك الاشترك في القناة اولا..\n\n    قنـاة الـبـوت :\n ⤹ https://t.me/{ch} ⤸", 
                           disable_web_page_preview=True, 
                           reply_markup=keyboard
                       )
                   except:
                       pass  # تجاهل أخطاء الإرسال
                   return True  # المستخدم غير مشترك
           except Exception as channel_error:
               print(f"خطأ في فحص القناة {x}: {channel_error}")
               continue  # تجاهل هذه القناة والمتابعة
               
       return False  # المستخدم مشترك في جميع القنوات
   except Exception as e:
       print(f"خطأ في دالة johned: {e}")
       return False  # في حالة أي خطأ، السماح بالاستخدام

@Client.on_message(filters.command(["تفعيل الاشتراك"], "") & filters.group, group=7530844)
async def retthd(client: Client, message: Message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    a = await client.get_chat_member(message.chat.id, message.from_user.id)    
    if a.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention}، هذا الأمر لا يخصك.")    
    chat_id = message.chat.id
    try:
        text = message.text.split(None, 2)[2]
    except Exception as e: 
        return await message.reply_text("يرجى كتابة الأمر بصيغة: تفعيل الاشتراك + الرابط \nمثلا \nتعطيل الاشتراك https://t.me/z1_xa")
    channel = text.replace("https://t.me/", "")
    try:
        channel_member = await client.get_chat_member(channel, client.me.id)        
    except Exception as e: 
        return await message.reply_text("يرجى رفع البوت مشرفًا في القناة أولاً.")
    oo = [channel]
    add_channelll(oo, bot_username, chat_id)
    await message.reply_text("تم حفظ القناة بنجاح.")
    
    
@Client.on_message(filters.command(["تعطيل الاشتراك"], "") & filters.group, group=7534)
async def rett645hd(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    a = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
    chat_id = message.chat.id
    try:
       text = message.text.split(None, 2)[2]
    except:
       await message.reply_text("تعطيل الاشتراك + الرابط \nمثلا \nتعطيل الاشتراك https://t.me/z1_1ax")
    channel = text.replace("https://t.me/", "")
    for x in get_channelll(bot_username, chat_id):
      if x[0] == channel:
        del_channelll(x, bot_username, chat_id)
    await message.reply_text("تم حذف القناه بنجاح")

@Client.on_message(filters.command(["قنوات الاشتراك"], "") & filters.group, group=7508834)
async def rett54645hd(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    a = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} هذا الأمر لا يخصك")
    chat_id = message.chat.id
    o = 0
    text = "قائمة القنوات\n"
    for x in get_channelll(bot_username, chat_id):
       o += 1
       channel = x[0]
       text += f"{o}- @{channel}\n"
    if o == 0:
       return await message.reply_text("لا يوجد قنوات")
    await message.reply_text(text)
 
def add_channelll(bots, bot_username, chat_id):
    if is_channelll(bots, bot_username, chat_id):
        return
    r.sadd(f"channel{bot_username}h{chat_id}", str(bots))

def is_channelll(bots, bot_username, chat_id):
    try:
        a = get_channelll(bot_username, chat_id)
        if bots in a:
            return True
        return False
    except:
        return False

def del_channelll(bots, bot_username, chat_id):
    if not is_channelll(bots, bot_username, chat_id):
        return False
    r.srem(f"channel{bot_username}h{chat_id}", str(bots))

def get_channelll(bot_username, chat_id):
    try:
        lst = []
        for a in r.smembers(f"channel{bot_username}h{chat_id}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

async def johnd(client, message, chat_id):
   bot_username = client.me.username
   for x in get_channelll(bot_username, chat_id):
    ch = x[0]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(" اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{ch}")]])
    try:
      get = await client.get_chat_member(ch, message.from_user.id)
    except Exception as e:    
      await message.delete()	
      return await message.reply_text(f"🚦عذرا عزيزي {message.from_user.mention} يجب عليك الاشترك في القناة اولا..\n\n    قنـاة الـبـوت :\n ⤹ https://t.me/{ch} ⤸", disable_web_page_preview=True, reply_markup=keyboard)

@Client.on_message(filters.text & filters.group, group=715053135)
async def johnd546(client, message):
    bot_username = client.me.username
    chat_id = message.chat.id
    if await johnd(client, message, chat_id):
      return
 
caesar_responses = [
    "معاك يا قلبى",
    "بحبك يعم قول عايز ايه",
    "يبني هتقول عايز ايه ولا اسيبك وامشي",
    "قلب {name} من جوه",
    "نعم يا قلب {name} ",
    "قرفتني والله بس بحبك بقى اعمل ايه",
    "خلاص هزرنا وضحكنا انطق بقا عايز ايه؟",
    "قوول يا قلبو ",
    "نبض قلب {name} يولا🌚🤍", 
    "روح قلب {name} من جوا 👀♥",  
]
  
bot_responses = [
    "اسمي {name} يا صحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "نعم يا حب ",
    "قول يا قلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يا عم والله بحبك بس ناديلي بـ {name}",
    "تعرف بالله هحبك اكتر لو ناديتلي {name}",
    "ايه يا معلم مين مزعلك",
    "ما تصلي على النبي كدا ",
    "مش فاضيلك نصايه وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "انجز عايزني اشقطلك مين؟",
    "شكلها منكده عليك وجاي تطلعهم علينا "
]

cff = []
sc = []

photo_responses = {}

@Client.on_message(filters.regex("تعطيل البوت بالصوره") & filters.private, group=57981)
async def disable_photo_reply(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.id == OWNER_ID:
    if bot_username not in photo_responses:
        photo_responses[bot_username] = False
    if photo_responses[bot_username]:
        photo_responses[bot_username] = False
        return await message.reply_text("تم تعطيل رد البوت بالصورة✅🥰")
    else:
        return await message.reply_text("رد البوت بالصورة معطل بالفعل✅🥰")

@Client.on_message(filters.regex("تفعيل البوت بالصوره") & filters.private, group=246588)
async def enable_photo_reply(client, message):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  if message.from_user.id == OWNER_ID :
    if bot_username not in photo_responses:
        photo_responses[bot_username] = False
    if not photo_responses[bot_username]:
        photo_responses[bot_username] = True
        return await message.reply_text("تم تفعيل رد البوت بالصورة✅🥰")
    else:
        return await message.reply_text("رد البوت بالصورة مفعل بالفعل✅🥰")

@Client.on_message(filters.command(["بوت", "البوت"], ""), group=71198535)
async def caesa57648r_bot(client, message):
    bot_username = client.me.username
    bot_id = client.me.id
    me = names.get(bot_username) if names.get(bot_username) else f"{name}"
    if not photo_responses[bot_username]:
        bar = random.choice(bot_responses).format(name=me)
        bot_username = client.me.username
        await message.reply_text(text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
    else:
        async for photo in client.get_chat_photos(client.me.id, limit=1):
            bar = random.choice(bot_responses).format(name=me)
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🚦", url=f"https://t.me/{bot_username}?startgroup=True")]
            ])
            await message.reply_photo(
                photo.file_id,
                caption=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
                reply_markup=keyboard
            )

@Client.on_message(filters.text & filters.group, group=715135)
async def respond_to_caesar(client, message):
    bot_username = client.me.username
    bot_id = client.me.id
    me = names.get(bot_username) if names.get(bot_username) else f"{name}"
    if me in message.text:     
        if not photo_responses[bot_username]:
            bar = random.choice(caesar_responses).format(name=me)
            await message.reply_text(text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**", disable_web_page_preview=True)
        else:
            async for photo in client.get_chat_photos(bot_id, limit=1):
                bar = random.choice(caesar_responses).format(name=me)
                keyboard = InlineKeyboardMarkup([
                    [InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🚦", url=f"https://t.me/{bot_username}?startgroup=True")]
                ])
                await message.reply_photo(
                    photo.file_id,
                    caption=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
                    reply_markup=keyboard
                )     

async def gen_ot(app, CASER, message, bot_id):
    caesar = await app.get_chat(bot_id)
    CASR = caesar.username
    name = caesar.first_name
    try:
        user_chat = await app.get_chat(bot_id)
        if user_chat.photo:
            photo_id = user_chat.photo.big_file_id
            downloaded_photo = await app.download_media(photo_id)
            youtube = Image.open(downloaded_photo)
            image1 = youtube.resize((1280, 720))
            image2 = image1.convert("RGBA")
            background = image2.filter(ImageFilter.BoxBlur(10))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.5)
            draw = ImageDraw.Draw(background)
            arial = ImageFont.truetype("font2.ttf", 80)
            caesa = ImageFont.truetype("font.ttf", 50)
            box_size = (500, 500)
            box_position = (40, 100)
            box_image = Image.new("RGBA", box_size, (255, 255, 255, 0))
            box_draw = ImageDraw.Draw(box_image)
            box_draw.ellipse([(0, 0), box_size], outline="white", width=5)
            user_chat_2 = await app.get_chat(message.from_user.id)
            inner_image = Image.open(downloaded_photo)
            inner_image = inner_image.resize((480, 480))
            box_image.paste(inner_image, (10, 10))
            background.paste(box_image, box_position)
            draw.text((580, 220), f"USER: @{CASR}", (255, 255, 255), font=caesa)
            draw.text((580, 120), f"MUSIC PLAYER BOT", fill="white", stroke_width=2, stroke_fill="white", font=arial)
            draw.text((580, 290), f"ID: {bot_id}", (255, 255, 255), font=caesa)
            draw.text((580, 360), f"DeV: {casery}", (255, 255, 255), font=caesa)
            draw.text((580, 430), f"users: {len(get_user(bot_id))}", (255, 255, 255), font=caesa)
            draw.text((580, 500), f"groups: {len(get_groups(bot_id))}", (255, 255, 255), font=caesa)
            photo_path = f"/root/ddd/{bot_id}.png"
            background.save(photo_path)
            return photo_path
    except Exception as e:
        print(f"An error occurred: {e}")

@Client.on_message(filters.command(["start"]) & filters.private, group=1267686)
async def fousers(client, message):
    if await johCASER(client, message):
        return
    if await johned(client, message):
        return
    bot = client.me
    bot_id, bot_username = bot.id, bot.username
    OWNER_ID = await get_dev(bot_username)
    usr1 = await client.get_chat(OWNER_ID)

    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk"),
         InlineKeyboardButton("English 🏴", callback_data="english")],
        [InlineKeyboardButton(usr1.first_name, url=f"https://t.me/{usr1.username}")]
    ])

    photo_path = f"/root/ddd/{bot_id}.png"

    if os.path.exists(photo_path):
        await message.reply_photo(photo=photo_path, caption="", reply_markup=button)
    else:
        await message.reply("⚠️ تعذر إرسال الصورة - لم يتم العثور على الملف.")

    if not is_user(message.from_user.id, bot_id):
        add_user(message.from_user.id, bot_id)
        text = (
            f"🙍 شخص جديد دخل الى البوت !\n\n"
            f"🎯 الأسم: {message.from_user.first_name}\n"
            f"♻️ الايدي: {message.from_user.id}\n\n"
            f"🌐 اصبح عدد المستخدمين: {len(get_user(bot_id))}"
        )
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(message.from_user.first_name, user_id=message.from_user.id)]
        ])
        admins = get_admins(bot_id) + [OWNER_ID]
        for admin in admins:
            await client.send_message(int(admin), text, reply_markup=reply_markup)

@Client.on_callback_query(filters.regex(pattern=r"^(arbk|english)$"))
async def admin_r98hts(client: Client, CallbackQuery):
    bot_username = client.me.username
    bot_id = client.me.id
    name = client.me.first_name
    botmention = client.me.mention
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    OWNER_ID = await get_dev(bot_username)
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
    namew = usr1.first_name    
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id 
    if command == "arbk":
     button = [[InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{bot_username}?startgroup=new")],[InlineKeyboardButton("القناه", url=f"{soesh}"), InlineKeyboardButton("الجروب", url=f"{gr}")], [InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")]]
     await CallbackQuery.answer("مرحبا بك في قسم اللغه العربيه 🎧", show_alert=True)	
     await CallbackQuery.edit_message_text(f"انا بوت تشغيل موسيقى صوتية ومرئية .⚡️\nقم بإضافة البوت إلي مجموعتك او قناتك .⚡️\nسيتم تفعيل البوت وانضمام المساعد تلقائياً\nفي حال مواجهت مشاكل تواصل مع المطور \nاستخدم الازرار لمعرفه اوامر الاستخدام .⚡️", reply_markup=InlineKeyboardMarkup(button))
    if command == "english":
     button = [[InlineKeyboardButton(text="اضف البوت الي مجموعتك 🚦", url=f"https://t.me/{bot_username}?startgroup=True")], [InlineKeyboardButton(text=f"Channel ⚡", url=f"{soesh}"), InlineKeyboardButton(text=f"Group ⚡", url=f"{gr}")], [InlineKeyboardButton(text=f"{namew}", url=f"https://t.me/{wenru}")],]
     await CallbackQuery.answer("مرحبا بك في قسم اللغه الانجليزيه 🎧", show_alert=True)	
     await CallbackQuery.edit_message_text(f"A Telegram Music Bot\\nPlayed Music and Video in VC\\nBot Online Now ......🖱️❤️\\nAdd Me To Your Chat\\Powered By [{namew}]", reply_markup=InlineKeyboardMarkup(button))
  
@Client.on_message(filters.command(["/start","رجوع","رجوع للتحكم الكامل"], "") & filters.private, group=67875563)
async def for_users(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
      return
    if await johCASER(client, message):
      return      
    if message.from_user.id == OWNER_ID:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyboard)
    elif message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keybcasoard)        
    else:
        await message.reply_text(f"صلي على النبي وتبسم 🌺♥", reply_markup=Keyard)
        
@Client.on_message(filters.command(["الالعاب","العاب"], ""), group=56783)
async def gammmes(client, message):
    await message.reply_text(
        """
✏ اوامر الالعاب.
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• صراحه » اسئلة صراحه
• تويت » اسئله ترفيهيه
• اعلام » معرفة الاعلام من الصور
• لغز » الغاز مشهوره
• مشاهير » معرفة المشاهير من الصور
• ممثلين » معرفه الممثلين من الصور
• مغنين » معرفه المغنين من الصور
• لاعبين » معرفه اللاعبين من الصور
• لو خيروك » اختار حاجه من اتنين
• تحدي » تحديات مسليه 
• مختلف » معرفه الرمز المختلف
• امثله » امثله معروفه 
• تفكيك » تركب الكلمه المفككه
• فزوره » فزوره مشهوره وتحلها
• اسئله » اسئله متنوعه
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
        """.strip()
    )
   
        
@Client.on_message(filters.command(["قسم الاذاعه"], "") & filters.private, group=67563)
async def for_5useers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyboazard)

@Client.on_message(filters.command(["قسم الحذف والاستخراج"], "") & filters.private, group=675693033)
async def for_5use382ers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Key282ard)

@Client.on_message(filters.command(["قسم الحظر"], "") & filters.private, group=697533)
async def for_5usee36rs(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keal66rdyttd)
 
@Client.on_message(filters.command(["قسم الاشتراك"], "") & filters.private, group=62357563)
async def for_5u72seers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keal56rdyttd)

@Client.on_message(filters.command(["قسم الاحتياطي"], "") & filters.private, group=620973)
async def for_5use57ers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keal16rdyttd)

@Client.on_message(filters.command(["قسم البوت"], "") & filters.private, group=67582963)
async def for_5usehwgwers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Kealrdyttd)

@Client.on_message(filters.command(["قسم التفعيل والتعطيل"], "") & filters.private, group=853263)
async def for_5u5sehwg6wers(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keal36rdyttd)
     
@Client.on_message(filters.command(["قسم الترويج"], "") & filters.private, group=67563)
async def for_5usersKeyttd(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyttd)

@Client.on_message(filters.command(["قسم التشغيل"], "") & filters.private, group=677438563)
async def for_5us4ersKey97ttd(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keal360rdyttd)
        
@Client.on_message(filters.command(["كيب الاعضاء"], "") & filters.private, group=63467563)
async def for_5usaersKeyard(client, message):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    if await johned(client, message):
     return
    if message.from_user.id == OWNER_ID or message.from_user.username in caes:
        return await message.reply_text(f"مرحبا عزيزي {message.from_user.mention} اليك كيب الاعضاء", reply_markup= Keyard)

@Client.on_message(filters.command(["قسم المساعد", "عوده لقسم المساعد"], "") & filters.private, group=67563)
async def foassrsKeyttd(client, message):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   if await johned(client, message):
     return
   me = userbot.me
   i = f"@{me.username} : {me.id}" if me.username else me.id
   b = await client.get_chat(me.id)
   b = b.bio if b.bio else "لا يوجد بايو"
   if message.from_user.id == OWNER_ID or message.from_user.username in caes:
    kep = ReplyKeyboardMarkup([["فحص المساعد"], ["تغير الاسم الاول", "تغير اسم المستخدم"], ["تغير البايو", "اضافه صوره"], ["ازاله صوره"], ["توجيه عام بالمساعد", "اذاعه عام بالمساعد"], ["دعوه المساعد الي الانضمام"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text(f"**أهلا بك عزيزي المطور **\n**هنا قسم الحساب المساعد**\n**{me.mention}**\n**{i}**\n**{b}**", reply_markup=kep)

    
admins_commands = [
   '《الاحصائيات》', '《تفعيل التواصل》',
   '《تعطيل التواصل》', '《اذاعة بالتثبيت》', '《اذاعة》',
   '《اذاعة بالتوجيه》', '《تفعيل الاشتراك》', '《تعطيل الاشتراك》',
   '《ضع قناة الاشتراك》', '《حذف قناة الاشتراك》', '《قناة الاشتراك》','قائمه الأدمنيه',
   'المستخدمين', 'الأدمنية', 'الجروبات',
   '《اذاعة بالمجموعات》','《اذاعة بالتثبيت بالمجموعات》', 'اخفاء الكيبورد'
   ]
   
owner_commands = [
   'نقل ملكية البوت', 'رفع ادمن', 'تنزيل ادمن'
]

@Client.on_message(filters.text & filters.private, group=2)
async def keyboardforadmins(client, m):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  bot_id = client.me.id
  if m.text in admins_commands:
    if not await check(m.from_user.id, bot_username, bot_id):
      return await m.reply('🌀 هذا الأمر لا يخصك', quote=True)
    else:    
      if m.text == '《الاحصائيات》':
        text = f'**👤 عدد المستخدمين: {len(get_user(bot_id))}\n'
        text += f'📊 عدد المجموعات: {len(get_groups(bot_id))}\n'
        text += f'🌀 عدد المشرفين: {len(get_admins(bot_id))}**'
        await m.reply(text, quote=True)        
      if m.text == '《تفعيل التواصل》':
        if r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تفعيل التواصل مسبقاً", quote=True)          
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل التواصل بنجاح**', quote=True)
        r.set(f'enable_twasol{bot_id}', 1)      
      if m.text == '《تعطيل التواصل》':
        if not r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تعطيل التواصل مسبقاً", quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل التواصل بنجاح**', quote=True)
        r.delete(f'enable_twasol{bot_id}')      
      if m.text == 'المستخدمين':
        await m.reply_document(get_users_backup(bot_id), quote=True)      
      if m.text == 'الأدمنية':
        await m.reply_document(get_admins_backup(bot_id), quote=True)      
      if m.text == 'الجروبات':
        await m.reply_document(get_groups_backup(bot_id), quote=True)      
      if m.text == '《تفعيل الاشتراك》':
        if r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تفعيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل الاشتراك بنجاح**', quote=True) 
        r.set(f"enable_force_subscribe{bot_id}", 1)      
      if m.text == '《تعطيل الاشتراك》':
        if not r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تعطيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل الاشتراك بنجاح**', quote=True) 
        r.delete(f"enable_force_subscribe{bot_id}")      
      if m.text == '《ضع قناة الاشتراك》':
        await m.reply("• ارسل معرف القناة العام مثال @z1_xa", quote=True)
        r.set(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")      
      if m.text == '《حذف قناة الاشتراك》':
        if not r.get(f'force_channel{bot_id}'):
          return await m.reply("• لا توجد قناة اشتراك معينة", quote=True)
        await m.reply("• تم حذف قناة الاشتراك بنجاح", quote=True)
        r.delete(f'force_channel{bot_id}')      
      if m.text == '《قناة الاشتراك》':
        if not r.get(f'force_channel{bot_id}'):
          await m.reply('• لاتوجد قناة مضافة', quote=True)
        else:
          channel = r.get(f'force_channel{bot_id}').decode('utf-8')
          await m.reply(f"https://t.me/{channel}", quote=True)      
      if m.text == 'قائمه الأدمنيه':
        if len(get_admins(bot_id)) == 0:
          await m.reply("• لايوجد آدمنية", quote=True)
        else:
          text = '• قائمة الأدمنية\n'
          for admin in get_admins(bot_id):
            try:
              get = await client.get_chat(int(admin))
              text += f'• [{get.first_name}](tg://user?id={admin})\n'
            except:
              text += f'• [@z1_xa](tg://user?id={admin})\n'
          await m.reply(text, quote=True)         
      if m.text == '《اذاعة》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == '《اذاعة بالتثبيت》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")        
      if m.text == '《اذاعة بالتوجيه》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == '《اذاعة بالمجموعات》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == '《اذاعة بالتثبيت بالمجموعات》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")      
      if m.text == 'اخفاء الكيبورد':
        await m.reply("• تم اخفاء لوحة التحكم لاظهارها مجدداً ارسل /start",
        quote=True, reply_markup=ReplyKeyboardRemove (selective=True))


@Client.on_message(filters.text & filters.private, group=3)
async def for_owner(client,m):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  bot_id = client.me.id
  text = m.text
  if text in owner_commands:
   if not m.from_user.id == int(OWNER_ID):
      return await m.reply("• هذا الأمر يخص المطور الأساسي فقط", quote=True)   
   if text == 'نقل ملكية البوت':
     await m.reply("• ارسل ايدي المالك الجديد الآن", quote=True)
     r.set(f"{m.from_user.id}transfer{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   if text == 'رفع ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")   
   if text == 'تنزيل ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}", 1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")

@Client.on_message(filters.text & filters.private, group=4)
async def response_for_commands(client, m):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   bot_id = client.me.id
   text = m.text   
   if text in admins_commands:
     return
   if text in owner_commands:
     return      
   if await check(m.from_user.id, bot_username, bot_id):
     if text == '《الغاء》':
       await m.reply("• تم الغاء كل شيء", quote=True)
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")     
     if r.get(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}"):
       try:
         get = await client.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)         
       if is_admin(int(text), bot_id):
         r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
         return await m.reply(f"• المستخدم [{get.first_name}]({get.id}) ادمن من قبل")
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       txt = '• تم رفع المستخدم ادمن بنجاح :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       add_admin(int(text), bot_id)
       await m.reply(txt, quote=True)
       return      
     if r.get(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}"):
      try: 
       if not is_admin(int(text), bot_id):
         r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
         return await m.reply("• المستخدم مو ادمن من قبل")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       del_admin(int(text), bot_id)
       await m.reply("• تم تنزيل المستخدم ادمن بنجاح", quote=True)
       return 
      except:
       return await m.reply("• الآيدي خطأ")     
     if r.get(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}"):
       channel = text.replace("@","")
       r.set(f"force_channel{bot_id}", channel)
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       await m.reply("• تم تعيين القناة بنجاح ", quote=True)


@Client.on_message(filters.group, group=1586024)
async def cfsaer(client, m):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    bot_id = client.me.id
    if not is_group(m.chat.id, bot_id): 
        add_group(m.chat.id, bot_id) 
        text = '• تم تفعيل البوت في مجموعة جديدة\n'
        text += f'• اسم المجموعة: {m.chat.title}\n'
        if m.chat.username:
            text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الذي قام بتفعيلي:\n'
        text += f'• اسمهم: {m.from_user.mention}\n'
        text += f'• الايدي: {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups(bot_id))}'
        if len(get_admins(bot_id)) > 0:
            admins = get_admins(bot_id) 
            for admin in admins:
                await client.send_message(int(admin), text, disable_web_page_preview=True)
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)
        else:
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)   

@Client.on_message(filters.channel, group=1586024)
async def cf54er(client, m):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    bot_id = client.me.id
    if not is_group(m.chat.id, bot_id): 
        add_group(m.chat.id, bot_id)
                
@Client.on_message(filters.group, group=1586024)
async def cfsa54er(client, m):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    bot_id = client.me.id
    photo = await gen_bot(client, bot_username, bot_id)        
    if not is_group(m.chat.id, bot_id):
        add_group(m.chat.id, bot_id)
        text = '• تم تفعيل البوت في مجموعة جديدة\n'
        text += f'• اسم المجموعة: {m.chat.title}\n'
        if m.chat.username:
            text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الذي قام بتفعيلي:\n'
        text += f'• اسمهم: {m.from_user.mention}\n'
        text += f'• الايدي: {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups(bot_id))}'
        if len(get_admins(bot_id)) > 0:
            admins = get_admins(bot_id)
            for admin in admins:
                await client.send_message(int(admin), text, disable_web_page_preview=True)
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)
        else:
            owner_id = int(OWNER_ID)
            if owner_id:
                await client.send_message(int(owner_id), text, disable_web_page_preview=True)
        await m.reply_photo(
            photo=photo,
            caption=f"""⋖⊶◎⊷⌯[ᏟᎻᎬΝΝᎪᏞ]({soesh})⌯⊶◎⊷⋗

تم تفعيل الجروب بنجاح 🥰✅
وتم تفعيل منع التصفيه تلقائي 🥰✅
تم رفع المالك والمشرفين 🥰✅
لمعرفه كل الاوامر اضغط علي (الاوامر بالاسفل) 🥰✅

⋖⊶◎⊷⌯[ᏟᎻᎬΝΝᎪᏞ]({soesh})⌯⊶◎⊷⋗""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "الاوامـر✅", callback_data="backkkkk"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "ᏟᎻᎬΝΝᎪᏞ", url=f"{soesh}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اضف البوت الي مجموعتك او قناتك 🚦", url=f"https://t.me/{bot_username}?startgroup=new"
                        ),
                    ],
                ]
            ),
        )

async def gen_bot(client, CASR, bot_id):
    try:
        user_chat = await client.get_chat(bot_id)
        if user_chat.photo:
            photo_id = user_chat.photo.big_file_id
            downloaded_photo = await client.download_media(photo_id)
            return downloaded_photo
    except Exception as e:
        print(f"An error occurred: {e}")

        
@Client.on_message(filters.new_chat_members, group=6)
async def add_group(client, m):
  bot_username = client.me.username
  OWNER_ID = await get_dev(bot_username)
  devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
  soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
  gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
  bot_id = client.me.id
  photo = await gen_bot(client, bot_username, bot_id)        
  for mm in m.new_chat_members:
    if mm.id == bot_id:
      if not is_group(m.chat.id, bot_id):
        add_group(m.chat.id, bot_id)
        text = '• تم اضافة البوت الى مجموعة جديدة\n'
        text += f'• اسم المجموعه: {m.chat.title}\n'
        if m.chat.username:
          text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الي ضافني :\n'
        text += f'• اسمه : {m.from_user.mention}\n'
        text += f'• الايدي : {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups(bot_id))}'
        if len(get_admins(bot_id)) > 0:
          list = get_admins(bot_id)
          for admin in list:
            await client.send_message(int(admin), text,
            disable_web_page_preview=True)
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
        else:
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
        await m.reply_photo(
            photo=photo,
            caption=f"مرحبا عزيزي : [ {m.from_user.mention} ] \nشكرا لاضافتي الي هذي المجموعه : [ {m.chat.title} ]⚡♥\n اقوم ايضا بحمايه جروبك من التصفيه والاباحي ⚡♥\n لمعرفه الاوامر : اضغط علي زر الاوامر بالاسفل 👇⚡♥",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "الاوامـر✅", callback_data="backkkkk"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "ᏟᎻᎬΝΝᎪᏞ", url=f"{soesh}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اضف البوت الي مجموعتك او قناتك 🚦", url=f"https://t.me/{bot_username}?startgroup=new"
                        ),
                    ],
                ]
            ),
        )
 
@Client.on_raw_update(group=7)
async def kick_from_group(client: Client, m: Update, _, __):
   bot_username = client.me.username   
   OWNER_ID = await get_dev(bot_username)
   bot_id = client.me.id
   try:
     name = re.search(r"first_name='([^']+)'", str(_)).group(1)
     title = re.search(r"title='([^']+)'", str(__)).group(1)
     if m.new_participant:
      get = await client.get_me()
      if m.new_participant.peer.user_id == get.id:
        print("🌀")
      else:  return 
      if m.new_participant.kicked_by:
        print("🌀")
      del_group(int(f'-100{m.channel_id}'))
      text = '• تم طرد البوت من مجموعة:\n\n'
      text += f'• اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'• ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n• معلومات المجموعة: \n'
      text += f'\n• ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n• اسم المجموعه: {title}'
      text += '\n• تم مسح جميع بيانات الجروب'
      if len(get_admins(bot_id)) > 0:
          list = get_admins(bot_id)
          for admin in list:
            await client.send_message(int(admin), text,
            disable_web_page_preview=True)
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
      else:
          await client.send_message(int(OWNER_ID), text,
          disable_web_page_preview=True)
   except:
     pass

@Client.on_message(filters.private, group=8)
async def forbroacasts(client, m):
   bot_username = client.me.username
   OWNER_ID = await get_dev(bot_username)
   bot_id = client.me.id
   if m.text:
      if m.text in admins_commands:  return
      if m.text in owner_commands:  return 
   if m.from_user:
     if r.get(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_user(bot_id):
          try:
            await m.copy(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_user(bot_id):
          try:
            a = await m.copy(int(user))
            await a.pin(disable_notification=False,both_sides=True)
          except PeerIdInvalid:
            del_user(int(user), bot_id)
            pass
          except Exception as e:
            print(e)
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_user(bot_id):
          try:
            await m.forward(int(user))
          except PeerIdInvalid:
            del_user(int(user), bot_id)
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups(bot_id):
          try:
            await m.copy(int(group))
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
     
     if r.get(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups(bot_id):
          try:
            a = await m.copy(int(group))
            await a.pin(disable_notification=False)
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
@Client.on_message(filters.private, group=9)
async def twasol2(client, m):
    bot_username = client.me.username 
    OWNER_ID = await get_dev(bot_username)
    bot_id = client.me.id
    if not await check(m.from_user.id, bot_username, bot_id):
        if r.get(f'enable_twasol{bot_id}'):
            if not m.from_user.is_bot:
                await m.forward(OWNER_ID)
    if m.from_user.id == OWNER_ID:
        if m.reply_to_message:
            if m.reply_to_message.forward_from:
                await m.reply(f"• تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
                try:
                    await m.copy(m.reply_to_message.forward_from.id)
                except:
                    pass
                    

def add_user(user_id, bot_id: int):
	if is_user(user_id, bot_id):
		return
	r.sadd(f"botusers{bot_id}", user_id)
	
def is_user(user_id, bot_id: int):
  try:
    a= get_user(bot_id)
    if user_id in a:
      return True
    return False
  except:
    return False

def del_user(user_id, bot_id: int):
	if not is_user(user_id, bot_id):
		return False
	r.srem(f"botusers{bot_id}", user_id)
	return True

def get_user(bot_id):
   try:
     list = []
     for a in r.smembers(f"botusers{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_users_backup(bot_id) -> str:
	text = ''
	for user in r.smembers(f"botusers{bot_id}"):
		text += user.decode('utf-8')+'\n'
	with open('users.txt', 'w+') as f:
		f.write(text)
	return 'users.txt'
	
def add_admin(user_id, bot_id: int):
    if is_admin(user_id, bot_id):  return 
    r.sadd(f"botadmins{bot_id}", user_id)

def is_admin(user_id, bot_id: int):
  try:
    a = get_admins(bot_id)
    if user_id in a:
      return True
    return False
  except:
    return False

def del_admin(user_id, bot_id: int):
	if not is_admin(user_id, bot_id):
		return False
	r.srem(f"botadmins{bot_id}", user_id)
	
def get_admins(bot_id):
   try:
     list = []
     for a in r.smembers(f"botadmins{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_admins_backup(bot_id) -> str:
	text = ''
	for admin in r.smembers(f"botadmins{bot_id}"):
		text += admin.decode('utf-8')+'\n'
	with open('admins.txt', 'w+') as f:
		f.write(text)
	return 'admins.txt'
	

async def check(id, bot_username, bot_id):
    if is_admin(id, bot_id):
      return True
    OWNER_ID = await get_dev(bot_username)
    if id == OWNER_ID:
      return True
    else:
      return False

async def check_sub(c,m,bot_id):
    if not r.get(f"enable_force_subscribe{bot_id}"):
      return
    else:
      if not r.get(f"force_channel{bot_id}"):
        return 
      else:
        channel = r.get(f"force_channel{bot_id}").decode('utf-8')
        text = f'✖️ عذراً عليك الاشتراك بقناة البوت أولاً لتتمكن من استخدامه !\n\nhttps://t.me/{channel}\n- /start'
        try:
           get = await c.get_chat_member(r.get(f"force_channel{bot_id}").decode('utf-8'), m.from_user.id)
           if get.status in [enums.ChatMemberStatus.LEFT, enums.ChatMemberStatus.BANNED]:
             return await m.reply(text, quote=True, disable_web_page_preview=True)
        except:
           return await m.reply(text, quote=True, disable_web_page_preview=True)

def add_group(chat_id, bot_id: int):
    if is_group(chat_id, bot_id):  return 
    r.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id, bot_id: int):
  try:
    a = get_groups(bot_id)
    if chat_id in a:
      return True 
    return False 
  except:
    return False

def del_group(chat_id, bot_id: int):
	if not is_group(chat_id, bot_id):
		return False
	r.srem(f"botgroups{bot_id}", chat_id)

def get_groups(bot_id):
   try:
     list = []
     for a in r.smembers(f"botgroups{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_groups_backup(bot_id) -> str:
	text = ''
	for group in r.smembers(f"botgroups{bot_id}"):
		text += group.decode('utf-8')+'\n'
	with open('groups.txt', 'w+') as f:
		f.write(text)
	return 'groups.txt'

#الحمايه

@Client.on_message(filters.command(["ترويج للحمايه", "ترويج الحمايه"], ""), group=1588024)
async def casrty(client, message):
   bot_username = client.me.username
   bot_id = client.me.id
   name = client.me.first_name
   botmention = client.me.mention
   OWNER_ID = await get_dev(bot_username)
   user = await client.get_chat(OWNER_ID)
   name = user.first_name
   username = user.username     
   button = [[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك 🎧", url=f"https://t.me/{bot_username}?startgroup=True")]]
   mm = f"**- البوت ده من افضل بوتات التليجرام الموجوده في تشغيل الاغاني 🎸 🎵\n\nمعرف البوت 🎸 [ @{bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{bot_username}\n\n-𝙳𝙴𝚅 ➤ @{username}**"
   await message.reply_text(f"**- البوت ده من افضل بوتات التليجرام الموجوده في تشغيل الاغاني 🎸 🎵\n\nمعرف البوت 🎸 [ @{bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{bot_username}\n\n-𝙳𝙴𝚅 ➤ @{username}**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎧", url=f"https://t.me/{bot_username}?startgroup=tru")]]))        
   for user in get_user(bot_id):
    hogs = int(user)
    try:
     m = await client.send_message(hogs, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   for group in get_groups(bot_id):
    hog = int(group)
    try:
     m = await client.send_message(hog, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   await message.reply_text("**تم الانتهاء من الترويج🎧**")         

@Client.on_message(filters.command(["ترويج للميوزك", "ترويج الميوزك"], ""), group=1588024)
async def casrt54y(client, message):
   bot_username = client.me.username
   bot_id = client.me.id
   name = client.me.first_name
   botmention = client.me.mention
   OWNER_ID = await get_dev(bot_username)
   user = await client.get_chat(OWNER_ID)
   name = user.first_name
   username = user.username     
   button = [[InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك 🎧", url=f"https://t.me/{bot_username}?startgroup=True")]]
   mm = f"**- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه\n\nوبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.\n\nارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️\n\nمعرف البوت 🎸 [ @{bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{bot_username}\n\n-𝙳𝙴𝚅 ➤ @{username}**"
   await message.reply_text(mm, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎧", url=f"https://t.me/{bot_username}?startgroup=new")]]))        
   for user in get_user(bot_id):
    hogs = int(user)
    try:
     m = await client.send_message(hogs, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   for group in get_groups(bot_id):
    hog = int(group)
    try:
     m = await client.send_message(hog, mm, reply_markup=InlineKeyboardMarkup(button))
    except Exception as es:
     print(es)
   await message.reply_text("**تم الانتهاء من الترويج🎧**")         
#..........................................   الاوامر     ................................................................
@Client.on_message(filters.command(["الاوامر","اوامر السورس","اوامر البوت","الاعدادات"], ""), group=73)
async def kggalid(client, message):
    bot_username = client.me.username
    bot_id = client.me.id
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    ff = devphots.get(bot_username) if devphots.get(bot_username) else f"{photosource}"   
    photo = await gen_bot(client, bot_username, bot_id)        
    if await johned(client, message):
     return
    await message.reply_photo(photo=photo, caption=f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• اوامــر البــوت الرئيسيـة\n\n• ( م1 ) ← اوامر الميوزك\n\n• ( م2 ) ← اوامر التحميل\n\n• ( م3 ) ← الحمايه\n\n• ( م4 ) ← منع التصفيه\n\n• ( م5 ) ← الاشتراك الاجبارى\n\n• ( م6 ) ← اوامر التسليه\n\n• ( م7 ) ← اوامر الرفع\n\n• ( م8 ) ← العاب\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("م1", callback_data="muusiiczombie"), InlineKeyboardButton("م2", callback_data="tahelalrady")],[InlineKeyboardButton("م3", callback_data="hemayazombie"), InlineKeyboardButton("م4", callback_data="mnatsfaalrady")],[InlineKeyboardButton("م5", callback_data="ashtrakalrady"), InlineKeyboardButton("م6", callback_data="tasliazombie")],[InlineKeyboardButton("م7", callback_data="auameralrdy"), InlineKeyboardButton("م8", callback_data="alabbalrady")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")],[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{bot_username}?startgroup=tru")]]))     

@Client.on_callback_query(filters.regex("muusiiczombie")) #زرار الموسيقى 
async def maui1sic(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\nاوامر الميوزك 🎶:\n\n🎵 `شغل` او `تشغيل` + اسم الاغنيه\n 📽 `فيد` او `فيديو` + اسم الفيديو\n 🔇 `وقف` او `ايقاف موقت` ← يقاف  موقت للتشغيل\n 🎶 `كمل` او `استكمال` ← لاستكمال الاغاني\n 🔂 `تخطي` ←لتشغيل الاغنيه القادمه\n 🚫 `ايقاف` او `اسكت` ← لايقاف التشغيل\n ❓ `مين شغل` ← لتعرف مين اخر شخص شغل\n ↙️ `انضم` ← لانضمام الحساب المساعد\n⚕️ `تحكم` ← للتحكم ف التشغيل \n ♻️ `تحديث` ← لتحديث الميوزك \n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("tahelalrady")) #زورار التحميل
async def tah11elalrady(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n اوامر التحميل ⏬: \n `تحميل` او `تنزيل` ← \n اختار تحميل صوت او تحميل فيديو ←\n ارسل اسم المطلوب تحميله\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("hemayazombie")) #زورو الحمايه
async def hemaya11zombie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• الـحـمـايـه 🛡:\n\n• ( م1 ) ← كـتـم\n\n• ( م2 ) ← تـقـيـد\n\n• ( م3 ) ← حـظـر\n\n• ( م4 ) ← الـحـذف\n\n• ( م5 ) ← حمايه الجروبات\n\n• ( م6 ) ← حمايه القنوات\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("م1", callback_data="katmalrdy"), InlineKeyboardButton("م2", callback_data="taqidalrdy")],[InlineKeyboardButton("م3", callback_data="tardalrady"), InlineKeyboardButton("م4", callback_data="auamralmsh")],[InlineKeyboardButton("م5", callback_data="hegmayrazobmbie")],[InlineKeyboardButton("م6", callback_data="hekmayanzotmbie")],[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))
       
@Client.on_callback_query(filters.regex("katmalrdy")) #زورار الكتم
async def k6atm1alrdy(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• `كتم` ←لحذف اى رساله يتم ارسلها الشخص\n\n1_ `كتم ` + معرف الشخص (اليوزر)\n\n2_ `كتم ` + ايدي الشخص\n\n3_ `كتم` ← بتحديد رساله من رسائل الشخص\n\n• `الغاء كتم` ←الغاء حذف اى رساله يتم ارسلها الشخص\n\n• `المكتومين` ← لعرض قائمه الاعضاء المكتومين ف الجروب\n\n• `مسح المكتومين` ←لحذف كل المكتومين وعدم حذف رسيلهم\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkalradykkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))
       
@Client.on_callback_query(filters.regex("taqidalrdy")) #زورار التقيد
async def ta5qid1alrdy(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•         ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• `تقيد` ← منع الشخص من ارسال اى رساله ف الجروب\n\n1_ `تقيد ` + معرف الشخص (اليوزر)\n\n2_ `تقيد ` + ايدي الشخص\n\n3_ `تقيد` ← بتحديد رساله من رسائل الشخص\n\n• `الغاء تقيد` ← الغاء منع الشخص من الارسال\n\n• `المقيدين` ←لعرض قائمه الممنوعين من الارسال\n\n• `مسح المقيدين` ←الغاء منع جميع الاشخص من الارسال\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkalradykkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))
       
@Client.on_callback_query(filters.regex("tardalrady")) #زورار الحظر
async def tard1alr9ady(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• `طرد` او `حظر` ←لطرد الشخص من الجروب\n\n1_ `طرد ` او `حظر ` + معرف الشخص (اليوزر)\n\n2_ `طرد ` او `حظر ` + ايدي الشخص\n\n3_ `طرد` او `حظر` ← بتحديد رساله من رسائل الشخص\n\n• `الغاء طرد` او `الغاء حظر` ← لمسح الشخص من قائمه المحظورين\n\n• `المحظورين` ←لعرض قائمه المحظورين\n\n• `مسح المحظورين` ←مسح كل المحظورين من قائمه مستخدمين تمت ازالتهم\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkalradykkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))
       
@Client.on_callback_query(filters.regex("auamralmsh")) #المسح
async def hema1yaalrdy(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• `مسح` او `حذف` ←بتحديد الرساله لحذف الرسالة فقط\n\n• `مسح رسايله` ←بتحديد رساله للشخص لحذف كل رسائل الشخص من الجروب\n\n• `مسح ` او `حذف ` + عدد الرسائل المطلوب حذفها ←لحذف العدد المطلوب من الرسائل\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkalradykkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("hegmayrazobmbie")) #حمايه الجروبات
async def hegmayra1zobmbie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• حمايه الجروبات 👥: \n\n ♻️ `قفل الكل` _ `فتح الكل` ← لقفل وفتح جميع اوامر الحمايه \n 🌀 `قفل المنشن` _ `فتح المنشن` ← لمنع المنشن @\n 🈂️ `قفل الشراحه` _ `فتح المنشن` ←لمنع الشراحه  €\n 📽 `قفل الفيديو` _ `فتح الفيديو` ←لمنع الفيديوهات \n 🖼 `قفل الصور` _ `فتح الصور` ←لمنع الصور\n 🔁 `قفل التوجيه` _ `فتح التوجيه` ←لمنع التوجيهات او التحويلات\n 🎆 `قفل الملصقات` _ `فتح الملصقات` ←لمنع الملصقات\n 🌐 `قفل الروابط` _ `فتح الروابط` ←لمنع الروابط\n 🔞 `قفل السب` _ `فتح السب` ←لمنع السب\n 🎞 `قفل المتحركات` _ `فتح المتحركات` ←لمنع المتحركات\n\n ⚠️ `قفل الدردشه` _ `فتح الدردشه` ←لمنع  ارسال اى رساله\n `close` 🚮 ← اغلاق الرساله\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkalradykkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]])) 

@Client.on_callback_query(filters.regex("hekmayanzotmbie")) #حمايه القنوات
async def hekma1yanzotmbie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• حمايه القنوات 📣: \n\n ♻️ `قفل الكل` _ `فتح الكل` ← لقفل وفتح جميع اوامر الحمايه\n 📽 `قفل الفيديو` _ `فتح الفيديو` ←لمنع الفيديوهات \n 🖼 `قفل الصور` _ `فتح الصور` ←لمنع الصور\n 🔁 `قفل التوجيه` _ `فتح التوجيه` ←لمنع التوجيهات او التحويلات\n 🎆 `قفل الملصقات` _ `فتح الملصقات` ←لمنع الملصقات\n 🎞 `قفل المتحركات` _ `فتح المتحركات` ←لمنع المتحركات\n`close` 🚮 ← اغلاق الرساله\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="backkalradykkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]])) 
        
@Client.on_callback_query(filters.regex("backkalradykkk")) #رجوع الحمايه
async def backkal1radykkk(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• الـحـمـايـه 🛡:\n\n• ( م1 ) ← كـتـم\n\n• ( م2 ) ← تـقـيـد\n\n• ( م3 ) ← حـظـر\n\n• ( م4 ) ← الـحـذف\n\n• ( م5 ) ← حمايه الجروبات\n\n• ( م6 ) ← حمايه القنوات\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("م1", callback_data="katmalrdy"), InlineKeyboardButton("م2", callback_data="taqidalrdy")],[InlineKeyboardButton("م3", callback_data="tardalrady"), InlineKeyboardButton("م4", callback_data="auamralmsh")],[InlineKeyboardButton("م5", callback_data="hegmayrazobmbie")],[InlineKeyboardButton("م6", callback_data="hekmayanzotmbie")],[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("mnatsfaalrady")) #زورار منع التصفيه
async def mnats1faalrady(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• طريقه استخدام منع التصفيه ✋:\n\nبتنزل كل المشرفين من الجروب / القناه وترفعهم عن طريق البوت او ترفع حساب واحد من البوت وترفع به كل المشرفين\n\n• `رفع مشرف` ف الجروبات ←لرفع العضو مشرف ف الجروبات\n1_ `رفع مشرف ` + لقب ← بتحديد رساله من رسائل الشخص لرفعو مشرف بلقب\n2_ `رفع مشرف` ← بتحديد رساله من رسائل الشخص لرفعو مشرف\n3_ `رفع مشرف ` + معرف الشخص (اليوزر)\n4_ `رفع مشرف ` + ايدي الشخص\n\n`رفع مشرف` ف القنوات ← لرفع العضو مشرف ف قناه\n←ارسل `رفع مشرف` ←ثم ارسل ايدي الشخص المطلوب رفعو مشرف\n\n• تنزيل مشرف ←لتنزيل المشرف لعضو عادى\n\n1_ تنزيل مشرف  + معرف الشخص (اليوزر)\n2_ تنزيل مشرف  + ايدي الشخص\n3_ تنزيل مشرف ← بتحديد رساله من رسائل الشخص لتنزيله من مشرف\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("ashtrakalrady")) #زورار الاشتراك الاجبارى
async def ash1trak6alrady(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• الاشتراك الاجبار ✋← لا يمكن لاى شخص ان يكتب اى رساله دون ان يشترك ف القناه او الجروب المضافه ف الاشتراك الاجبار \n\n• ل `تفعيل الاشتراك `←يجب رفع البوت مشرف ف القناه او الجروب المطوب وضعه ف الاشتراك \n\n←ثم ارسال `تفعيل الاشتراك ` + رابط القناه او الجروب \n\n←مثلا: \n`تفعيل الاشتراك` {soesh}\n\n• لحذف قناه او جروب من الاشتراك\n\n←ارسل `تعطيل الاشتراك ` + رابط القناه او الجروب \n\n← مثلا: \n`تعطيل الاشتراك` {soesh}\n\nلعرض الاشتركات المضافه \n←ارسل `قنوات الاشتراك`\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("tasliazombie")) #زورار الترفيه
async def tas1liazombie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• `قفل التسليه` او `تعطيل التسليه` ← لتعطيل اوامر التسليه \n• `فتح التسليه` او `تعطيل التسليه` ← لتفعيل اوامر التسليه\n\nاوامر التسليه🥸:\n←`زخرفه`\n←`صراحه` ، `انصحني` ، `لو خيروك` ، `حروف` ، `امثله` ، `نكته` ، `احكام` ، `ازكار`\n← `صور` ، `صور شباب` ، `صور بنات` ، `انمي` ، `استوري`\n← `اغاني` ، `قران`\n\n• `الساعه` ← لعرض الساعه والتاريخ \n• `بوسه` او `مح` ← بتحديد رساله للشخص المطلوب تقبيله 😘\n• `تف` ←بتحديد رساله للشخص المطلوب البصق عليه 🤤\n• `تخ` ← بتحديد رساله للشخص المطلوب قتله 😵\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("auameralrdy")) #زورار اوامر الرفع
async def auam1eralrdy(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•    ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• اوامر الرفع🤪:\n\nالرفع: \n←`رفع اخ` ، `رفع اخت` ، `رفع بنتي` ، `رفع مراتي` ، `رفع زوجي` ، `رفع جدع` ، `رفع ابني` ، `رفع غبي` ، `رفع اهبل` \n← `رفع نمله`  ، `رفع صرصار` ، `رفع قرد` ، `رفع حمار` ، `رفع خنزير` ، `رفع عجل` ، `رفع كلب` ، `رفع خروف` ، `رفع جاموسه`\n← `رفع خول` ، `رفع متناك` ، `رفع عرص` ، `رفع نجس` ، `رفع ديوث` ،  `رفع شاذ`\n\nاو ارسل كلمه `الرفع` \n\nالتنزيل: \n←`تنزيل اخ` ، `تنزيل اخت` ، `تنزيل بنتي` ، `تنزيل مراتي` ، `تنزيل زوجي` ، `تنزيل جدع` ، `تنزيل ابني` ، `تنزيل غبي` ، `تنزيل اهبل` \n← `تنزيل نمله`  ، `تنزيل صرصار` ، `تنزيل قرد` ، `تنزيل حمار` ، `تنزيل خنزير` ، `تنزيل عجل` ، `تنزيل كلب` ، `تنزيل خروف` ، `تنزيل جاموسه` \n← `تنزيل خول` ، `تنزيل متناك` ، `تنزيل عرص` ، `تنزيل نجس` ، `تنزيل ديوث` ،  `تنزيل شاذ`\n\nاو ارسل كلمه `التنزيل` \n\nلمرفوعين: \n←`اخواتي` ، `اخوتي` ، `بناتي` ، `مراتاتي` ، `ازواجي` ، `ابنائي` ، `اغبياء` ، `الهبل` \n← `النمل` ، `الصارصير` ، `القرود` ، `الحمير` ، `الخنازير` ، `العجول` ، `الكلاب` ، `الخرفان` ، `الجواميس` \n← `الخولات` ، `المتناكين` ، `المعرصين` ، `النجسين` ، `الديوثين` ، `الشاذين`\n\n او ارسل كلمه `المرفوعين`\n\n•    ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("alabbalrady")) #زورار الالعاب 
async def alabb1alrady(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n الالعاب 🕹: \n\n• لعبه `البنك`← لعرض اوامر لعبه البنك ارسل `البنك`\n\n• لعبه `اكس او` ←لبدا اللعبه ارسل `اكس او`\n\n• لعبه `حجرة` `ورقة` `مقص` ← لبدا العبه ارسل `حجرة` او `ورقه` او `مقص`\n\nلعبه `الجاسوس` ← لبدا العبه ارسل `الجاسوس`\n\nالغاز 🤔: \n← `ممثلين` ،  `مغنين` ،  `لاعبين` ،  `مشاهير` ،  `اعلام` ،  `افلام`\n← `مختلف` ،  `لغز`\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع", callback_data="backkkkk")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")]]))

@Client.on_callback_query(filters.regex("backkkkk")) #رجوع كامل
async def enzom54ddbie(client, callback_query: CallbackQuery):
    bot_username = client.me.username
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    await callback_query.edit_message_text(f"""•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗\n\n• اوامــر البــوت الرئيسيـة\n\n• ( م1 ) ← اوامر الميوزك\n\n• ( م2 ) ← اوامر التحميل\n\n• ( م3 ) ← الحمايه\n\n• ( م4 ) ← منع التصفيه\n\n• ( م5 ) ← الاشتراك الاجبارى\n\n• ( م6 ) ← اوامر التسليه\n\n• ( م7 ) ← اوامر الرفع\n\n• ( م8 ) ← العاب\n\n•        ⋖⊶◎⊷⌯[ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ]({soesh})⌯⊶◎⊷⋗""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("م1", callback_data="muusiiczombie"), InlineKeyboardButton("م2", callback_data="tahelalrady")],[InlineKeyboardButton("م3", callback_data="hemayazombie"), InlineKeyboardButton("م4", callback_data="mnatsfaalrady")],[InlineKeyboardButton("م5", callback_data="ashtrakalrady"), InlineKeyboardButton("م6", callback_data="tasliazombie")],[InlineKeyboardButton("م7", callback_data="auameralrdy"), InlineKeyboardButton("م8", callback_data="alabbalrady")],[InlineKeyboardButton("ᥴ𝗁ᥲ️ꪀꪀᥱᥣ ᥉᥆υᖇᥴᥱ", url=f"{soesh}")],[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{bot_username}?startgroup=tru")]]))     
#..........................................   الاوامر     ................................................................

@Client.on_message(filters.command(["سورس","السورس","• السورس •"], ""))
async def caesar_bot(client, message):
    bot_username = client.me.username
    devus = devuser.get(bot_username) if devuser.get(bot_username) else f"{casery}"
    soesh = devchannel.get(bot_username) if devchannel.get(bot_username) else f"{source}"
    gr = devgroup.get(bot_username) if devgroup.get(bot_username) else f"{group}"
    if await johned(client, message):
     return
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᏟᎻᎬΝΝᎪᏞ", url=f"https://t.me/z1_xa"),
                InlineKeyboardButton("ᏀᎡΌႮᏢ", url=f"https://t.me/almhndssss"),
            ],
            [
                 InlineKeyboardButton("كبير ABBAS", url=f"https://t.me/z1_xa")
            ],
            [ 
                 InlineKeyboardButton("اضف البوت الي مجموعتك ♥️", url=f"https://t.me/{bot_username}?startgroup=tru")
            ]
        ]
    )

    await message.reply_video(
        caption=f"**⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼**", 
        video="https://t.me/ii_T_a/623",
        reply_markup=keyboard
    )


@Client.on_message(filters.command(["المطور","• مطور البوت •", "مطور البوت"], ""))
async def deev(client, message):
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    user = await client.get_chat(OWNER_ID)
    name = user.first_name
    username = user.username 
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    link = f"https://t.me/{message.chat.username}"
    title = message.chat.title if message.chat.title else message.chat.first_name
    chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
    if await johned(client, message):
     return
    try:
     await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
    except:
      pass
    await message.reply_photo(
    photo=photo,
    caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
    try:
      os.remove(photo)
    except:
       pass    

@Client.on_message(filters.command(["مطور السورس","البوب","• مطور السورس •","《مطور السورس》"], ""))
async def dsaev(client, message):
    bot_username = client.me.username
    if await johned(client, message):
     return
    user = await client.get_chat(chat_id=f"z1_xa")
    name = user.first_name
    username = user.username 
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    link = f"https://t.me/{message.chat.username}"
    title = message.chat.title if message.chat.title else message.chat.first_name
    chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
    try:
     await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
    except:
      pass
    await message.reply_photo(
    photo=photo,
    caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
    try:
      os.remove(photo)
    except:
       pass   
       
                     
       
@Client.on_message(filters.regex("رفع نسخه الجروبات") & filters.private)
async def upper_back5up(client, msg):
    bot_id = client.me.id
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if msg.from_user.id == OWNER_ID or msg.from_user.id == 5993309733:
        if msg.reply_to_message:
            if msg.reply_to_message.document.file_name.endswith("txt"):
                wait = await msg.reply("• انتظر قليلا ..", quote=True)
                await msg.reply_to_message.download("./groups.txt")                
                try:
                    file = open("groups.txt", "r").readlines()
                except FileNotFoundError:
                    await msg.reply("حدث خطأ أثناء فتح الملف.", quote=True)
                    return                    
                for line in file:
                    chat_id = int(line)
                    add_group(chat_id, bot_id)                    
                await msg.reply("تم رفع نسخه الجروبات بنجاح 🎧")
 
@Client.on_message(filters.regex("رفع نسخه الاشخاص") & filters.private)
async def upper_backup(client, msg):
    bot_id = client.me.id
    bot_username = client.me.username
    OWNER_ID = await get_dev(bot_username)
    if msg.from_user.id == OWNER_ID or msg.from_user.id == 5993309733:
        if msg.reply_to_message:
            if msg.reply_to_message.document.file_name.endswith("txt"):
                wait = await msg.reply("• انتظر قليلا ..", quote=True)
                await msg.reply_to_message.download("./users.txt")                
                try:
                    file = open("users.txt", "r").readlines()
                except FileNotFoundError:
                    await msg.reply("حدث خطأ أثناء فتح الملف.", quote=True)
                    return                    
                for line in file:
                    chat_id = int(line)
                    add_user(chat_id, bot_id)                    
                await msg.reply("تم رفع نسخه الاشخاص بنجاح 🎧")

@Client.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""),group=59075096875)
async def gak_owne(client: Client, message: Message):
    if len(message.command) > 1:
        return
    
    chat_id = message.chat.id

    async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            id = member.user.id
            key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
            m = await client.get_chat(id)
            if m.photo:
                photo = await client.download_media(m.photo.big_file_id)
                return await message.reply_photo(photo, caption=f"𝅄 𓏺 𝖭𝖺𝗆𝖾:{m.first_name}\n𝅄 𓏺 𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾 : @{m.username}\n𝅄 𓏺 𝗂𝖽 :{m.id}\n𝅄 𓏺 𝙱𝙸𝙾 : {m.bio}\n𝅄 𓏺 𝖦𝗋𝗈𝗎𝗉 : {message.chat.title}\n𝅄 𓏺 𝖦𝗋𝗈𝗎𝗉 𝗂𝖽 : {message.chat.id}`", reply_markup=key)
            else:
                return await message.reply("• " + member.user.mention)
            
@Client.on_chat_member_updated(filters.group)
async def chat_member_updated(client, chat_member_update):
    if chat_member_update.new_chat_member:
        user = chat_member_update.new_chat_member.user
        user_id = user.id
        chat_id=chat_member_update.chat.id
        user_mentio = user.mention
        me = await client.get_me()
        bot_username = me.username
        OWNER_ID = await get_dev(bot_username)
        if user_id == OWNER_ID:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=True,
                    can_manage_video_chats=True,
                    can_pin_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, "مطور البوت")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مالك البوت الي هنا")
        elif user_id == 7962801242:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=True,
                    can_manage_video_chats=True,
                    can_pin_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج البوب")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")
        elif user_id == 7055185:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=True,
                    can_manage_video_chats=True,
                    can_pin_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج ليدر")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")
        elif user_id == 555801:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=True,
                    can_manage_video_chats=True,
                    can_pin_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج زومبي")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")
        elif user_id == 129434:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=True,
                    can_manage_video_chats=True,
                    can_pin_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج ستيتش")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")
@Client.on_chat_member_updated(filters.channel)
async def chat_memr_updated(client, chat_member_update):
    if chat_member_update.new_chat_member:
        user = chat_member_update.new_chat_member.user
        user_id = user.id
        chat_id=chat_member_update.chat.id
        user_mentio = user.mention
        me = await client.get_me()
        bot_username = me.username
        OWNER_ID = await get_dev(bot_username)
        if user_id == OWNER_ID:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=False,
                    can_manage_video_chats=True,
                    can_post_messages=True,
                    can_invite_users=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id,  "مطور البوت")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مالك البوت الي هنا ")
        elif user_id == 5999733:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=False,
                    can_manage_video_chats=True,
                    can_post_messages=True,
                    can_invite_users=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج ايطالي")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")
        elif user_id == 707385:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=False,
                    can_manage_video_chats=True,
                    can_post_messages=True,
                    can_invite_users=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id,  " المبرمج ليدر")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس ليدر هنا")
        elif user_id == 5677801:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=False,
                    can_manage_video_chats=True,
                    can_post_messages=True,
                    can_invite_users=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج زومبي")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")  
        elif user_id == 121434:
            await client.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(
                    can_promote_members=False,
                    can_manage_video_chats=True,
                    can_post_messages=True,
                    can_invite_users=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_change_info=False
                )
            )
            await client.set_administrator_title(chat_id, user_id, " المبرمج ستيتش")
            await client.send_message(chat_id=chat_member_update.chat.id,text=f"♪ {user_mentio} ♥️ انضم مبرمج السورس الي هنا")

@Client.on_message(filters.command(["لقبي"], ""), group=72726566)
async def tsssaitle(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"**لقبك هو  : {title}**")

@Client.on_message(filters.command(["لقبه"], ""), group=7727866)
async def titssle(client, message):
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"**لقبه هو  : {title}**")