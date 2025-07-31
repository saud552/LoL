import asyncio
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from datetime import datetime
from pyrogram import enums
from typing import Union, List, Iterable
from pyrogram import Client as client
from pyrogram.errors import FloodWait
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned
#............................................ المساعد  ...........................................................................    
@Client.on_message(filters.command("فحص المساعد", ""), group=5865)
async def userrrrr(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in caes:
    client = await get_userbot(bot_username)
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = client.me
    usere = Meh.mention
    async for dialog in client.get_dialogs():
        type = dialog.chat.type
        if enums.ChatType.PRIVATE == type:
            u += 1
        elif enums.ChatType.BOT == type:
            b += 1
        elif enums.ChatType.GROUP == type:
            g += 1
        elif enums.ChatType.SUPERGROUP == type:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status == enums.ChatMemberStatus.ADMINISTRATOR or user_s.status == enums.ChatMemberStatus.OWNER:
                a_chat += 1
        elif enums.ChatType.CHANNEL == type:
            c += 1
        else:
          print(type)

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ .**
.**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ {} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )
#............................................ المساعد  ...........................................................................    
#............................................ تغير الاسم  ...........................................................................    
@Client.on_message(filters.command("تغير الاسم الاول", ""), group=58650)
async def changefisrt(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان الاسم الجديد")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم \n {es}")
#............................................ تغير الاسم  ...........................................................................    
#............................................ تغير البايو  ...........................................................................    
@Client.on_message(filters.command("تغير البايو", ""), group=586505)
async def changebio(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان البايو الجديد")
    name = name.text
    client = await get_userbot(bot_username)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو \n {es}")
#............................................ تغير البايو  ...........................................................................    

@Client.on_message(filters.command("تغير اسم المستخدم", ""), group=586502)
async def changeusername(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان اسم المستخدم الجديد")
    name = name.text
    client = await get_userbot(bot_username)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم \n {es}")

@Client.on_message(filters.command(["اضافه صوره"], ""), group=5865067)
async def changephoto(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  user = await get_userbot(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    m = await client.ask(message.chat.id, "قم بإرسال الصوره الجديده الان")
    photo = m.photo
    photo = await client.download_media(photo)
    await user.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح ..**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره \n {es}")

@Client.on_message(filters.command(["ازاله صوره"], ""), group=5865084)
async def changephotos(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
       try:
        user = await get_userbot(bot_username)
        async for photos in user.get_chat_photos("me"):
         await user.delete_profile_photos([p.file_id for p in photos[1:]])
         await message.reply_text("**تم ازاله صوره بنجاح ..**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره \n {es}")


@Client.on_message(filters.command("دعوه المساعد الي الانضمام", ""), group=5865024)
async def joined(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   try:
    name = await client.ask(message.chat.id, "ارسل الان الرابط")
    name = name.text
    if "https" in name:
     if not "+" in name: 
       name = name.replace("https://t.me/", "")
    client = await get_userbot(bot_username)
    await client.join_chat(name)
    await message.reply_text("**تم انضمام الحساب المساعد بنجاح ..**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء الانضمام \n {es}")

@Client.on_message(filters.command(["توجيه عام بالمساعد", "اذاعه عام بالمساعد"], ""), group=58650417)
async def cast5(client: Client, message):
  command = message.command[0]
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in caes:
   kep = ReplyKeyboardMarkup([["الغاء"], ["عوده لقسم المساعد"], ["رجوع للتحكم الكامل"]], resize_keyboard=True)
   ask = await client.ask(message.chat.id, "قم بإرسال الاذاعه الخاصه بك", reply_markup=kep)
   x = ask.id
   y = message.chat.id
   if ask.text == "الغاء":
     return await ask.reply_text("**تم الالغاء بنجاح ✅**")
   pn = await client.ask(message.chat.id, "هل تريد تثبيت الاذاعه\nارسل « نعم » او « لا »")
   await message.reply_text("**جاري الاذاعه انتظر بعض الوقت ...**")
   text = ask.text
   dn = 0
   fd = 0
   if command == "اذاعه عام بالمساعد":
     user = await get_userbot(bot_username)
     async for i in user.get_dialogs():
         try:
           m = await user.send_message(chat_id=i.chat.id, text=text)
           dn += 1
           if pn.text == "نعم":
                try:
                 await m.pin(disable_notification=False)
                except:
                   continue
         except FloodWait as e:
                    flood_time = int(e.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح ..**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")
   elif command == "توجيه عام بالمساعد":
     client = await get_userbot(bot_username)
     async for i in client.get_dialogs():
         try:
           m = await client.forward_messages(
               chat_id=i.chat.id,
               from_chat_id=message.chat.username,
               message_ids=int(x),
               )
           dn += 1
           if pn.text == "نعم":
                try:
                 await m.pin(disable_notification=False)
                except:
                   continue
         except FloodWait as e:
                    flood_time = int(e.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح ..**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")

@Client.on_message(filters.command(["حذف","مسح"], ""), group=5675436417)
async def arejg6574ply(client, message):
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    chat_id = message.chat.id  
    text = int(message.text.split(None, 1)[1])
    async for h in user.get_chat_history(message.chat.id, limit=text):
        await client.delete_messages(chat_id, h.id)

@Client.on_message(filters.command(["مسح رسايله","حذف رسايله","مسح الكل","حذف الكل","مسح رسايل","حذف رسايل","مسح كل","حذف كل"], ""), group=5607684417)
async def delete_messages(client, message):
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        replied_user = message.reply_to_message.from_user
        chat_id = message.chat.id
        async for h in user.get_chat_history(chat_id):
            if h.from_user and h.from_user.id == user_id:
                await client.delete_messages(chat_id, h.id)
        print("تم حذف")     
    else:
        await message.reply("يرجى الرد على رسالة المستخدم الذي تريد حذف رسائله.")
        
@Client.on_message(filters.command(["مسح","حذف"], ""), group=567668784417)
async def delete_mes1sages(client, message):
    if message.reply_to_message:
        await client.delete_messages(message.chat.id, message.reply_to_message.id)
    else:
        await message.reply("يرجى الرد على رسالة المستخدم الذي تريد حذفها.")

import random

ALI = ["👍", "❤", "🔥", "🥰", "🎉", "🤩", "🙏", "👌", "🕊", "😍", "😎","🍓","💋","💘","🌚"]

@Client.on_message(filters.channel, group=1234567)
async def handle_message(client, message):
    bot_username = client.me.username
    user = await get_userbot(bot_username)
    chat_id = message.chat.id
    message_id = message.id
    T = random.choice(ALI)
    try:
        await user.send_reaction(chat_id, message_id, f"{T}")
    except Exception as e:
        print(f"حدث خطأ أثناء الانضمام: {str(e)}")

#............................................ معلومات البوت والمطور  ...........................................................................    
@Client.on_message(filters.command(["معلومات", "info", "about", "حول"], ""), group=12345678)
async def bot_info(client, message):
    bot_username = client.me.username
    
    info_text = f"""
🎵 **معلومات البوت**

📱 **اسم البوت:** [اسم البوت]
🔗 **رابط البوت:** @{bot_username}
📝 **الوصف:** بوت متطور لتحميل الموسيقى والفيديوهات من YouTube
🌐 **اللغة:** العربية

⚡ **الميزات الرئيسية:**
• تحميل الموسيقى من YouTube
• دعم الأوامر مع وبدون `/`
• نظام تدوير ملفات الكوكيز
• حماية من الحظر
• جودة عالية للتحميل
• دعم الصور المصغرة

🛠️ **الأوامر المدعومة:**
• `/تحميل` - `/نزل` - `/تنزيل` - `/يوتيوب`
• `/حمل` - `/تنزل` - `/يوت` - `/بحث`
• أو بدون `/`: `تحميل` - `نزل` - `تنزيل` - `يوتيوب`

👨‍💻 **معلومات المطور:**
• **اسم المطور:** [اسم المطور]
• **رابط التواصل:** [رابط Telegram]
• **GitHub:** [رابط GitHub]

📞 **التواصل والدعم:**
• **قناة البوت:** [رابط القناة]
• **مجموعة الدعم:** [رابط المجموعة]
• **التواصل المباشر:** [رابط المطور]

🔧 **المتطلبات:**
• Python 3.8+
• Pyrogram
• yt-dlp
• ملفات كوكيز YouTube

---
**تم التطوير بواسطة:** [اسم المطور]
**آخر تحديث:** [التاريخ]
"""
    
    await message.reply_text(info_text)

@Client.on_message(filters.command(["المطور", "developer", "dev"], ""), group=12345679)
async def developer_info(client, message):
    dev_text = f"""
👨‍💻 **معلومات المطور**

👤 **اسم المطور:** [اسم المطور]
📱 **رابط التواصل:** [رابط Telegram]
🐙 **GitHub:** [رابط GitHub]
📧 **البريد الإلكتروني:** [البريد الإلكتروني]

📞 **قنوات التواصل:**
• **قناة البوت:** [رابط القناة]
• **مجموعة الدعم:** [رابط المجموعة]
• **التواصل المباشر:** [رابط المطور]

💼 **الخدمات:**
• تطوير بوتات Telegram
• برمجة تطبيقات Python
• حلول تقنية متقدمة

🌟 **المشاريع:**
• بوت تحميل YouTube
• بوتات إدارية
• تطبيقات متنوعة

---
**للاستفسارات والدعم الفني**
"""
    
    await message.reply_text(dev_text)
