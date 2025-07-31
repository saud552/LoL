import asyncio
import requests
import random
import re
import json
import pytz
import textwrap
import aiofiles
import aiohttp
import os
import sqlite3
import time
import datetime
from pyrogram import Client as client
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from typing import List, Union
from pyrogram import *
import pyromod.listen
from dotenv import load_dotenv
from os import getenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import aiohttp
from datetime import datetime, timedelta
from random import choice
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import ChatPermissions, ChatPrivileges
from aiohttp import ClientSession
from traceback import format_exc
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
import sys
from pyrogram.errors import FloodWait
from os import remove
from asyncio import sleep
from pyrogram.types import *
from telegraph import upload_file
from unidecode import unidecode
import sqlite3
from pyrogram import Client, idle
from random import randint
from pyrogram.enums import ChatType
from pyrogram.types import Chat, User
from asyncio import gather
from io import BytesIO
from pyrogram import Client, filters
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, johned, devphots
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
from pyrogram.errors import exceptions
from pyrogram.enums import ParseMode
from math import sqrt
from typing import Union
from CASERr.CASERr import caserid


@Client.on_message(filters.command(["اغاني"], ""), group=7328921)
async def muiwgwhsic(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.reply_text("◍ اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^music2 (\\d+)$"))
async def music2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اغاني عربي 🇪🇬", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("اغاني اجنبي 🇦🇺", callback_data="agnaby " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اهلا بيك بقائمه تصنيفات الاغاني اختر ما تريد\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^araby (\\d+)$"))
async def araby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مهرجانات 🔊", callback_data="mhrgan " + str(m.from_user.id))] +
        [InlineKeyboardButton("ادهم نابلسي 🔊", callback_data="adham " + str(m.from_user.id))],
        [InlineKeyboardButton("ويجز 🔊", callback_data="wegzz " + str(m.from_user.id))] +
        [InlineKeyboardButton("تامر حسني 🔊", callback_data="tamer " + str(m.from_user.id))],
        [InlineKeyboardButton("مروان موسي 🔊", callback_data="marwan " + str(m.from_user.id))] +
        [InlineKeyboardButton("حماده هلال 🔊", callback_data="helal " + str(m.from_user.id))],
        [InlineKeyboardButton("بابلو 🔊", callback_data="bablo " + str(m.from_user.id))] +
        [InlineKeyboardButton("اصاله 🔊", callback_data="asala " + str(m.from_user.id))],
        [InlineKeyboardButton("اليسا 🔊", callback_data="elesa " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد سعيد 🔊", callback_data="mosaeed " + str(m.from_user.id))],
        [InlineKeyboardButton("اغاني شعبي 🔊", callback_data="sahby " + str(m.from_user.id))] +
        [InlineKeyboardButton("عمار حسني 🔊", callback_data="ammarr " + str(m.from_user.id))],
        [InlineKeyboardButton("الجوكر 🔊", callback_data="joker " + str(m.from_user.id))] +
        [InlineKeyboardButton("حماقي 🔊", callback_data="hamaky " + str(m.from_user.id))],
        [InlineKeyboardButton("عمرو دياب 🔊", callback_data="dyabb " + str(m.from_user.id))] +
        [InlineKeyboardButton("احمد كامل 🔊", callback_data="kamell " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اهلا بك بقائمه الفنانين اختر احدي المغنيين\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mhrgan (\\d+)$"))
async def mhrgan(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مهرجانات 1 🔊", callback_data="mhrgan1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مهرجانات 2 🔊", callback_data="mhrgan2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مهرجانات 3 🔊", callback_data="mhrgan3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مهرجانات 4 🔊", callback_data="mhrgan4 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],
    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mhrgan1 (\\d+)$"))
async def mhrgan1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("ابوكي تاجر سلاح 🎧", callback_data="Xmhrg1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عالم تعبانه 🎧", callback_data="Xmhrg2 " + str(m.from_user.id))],
        [InlineKeyboardButton("عصام صاصا 😂 🎧", callback_data="Xmhrg3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مابغيبش اونطه 🎧", callback_data="Xmhrg4 " + str(m.from_user.id))],
        [InlineKeyboardButton("اوعي تصيع يا باي 🎧", callback_data="Xmhrg5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سلامات 🎧", callback_data="Xmhrg6 " + str(m.from_user.id))],
        [InlineKeyboardButton("داهيه 🎧", callback_data="Xmhrg7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("احنا محدش يقدرنا 🎧", callback_data="Xmhrg8 " + str(m.from_user.id))],
        [InlineKeyboardButton("خربانه انتي 🎧", callback_data="Xmhrg9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انتظرونا 🎧", callback_data="Xmhrg10 " + str(m.from_user.id))],
        [InlineKeyboardButton("بنتي قلبي 🎧", callback_data="Xmhrg11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ضربه بضربه 🎧", callback_data="Xmhrg12 " + str(m.from_user.id))],
        [InlineKeyboardButton("بنتي اه بحبك 🎧", callback_data="Xmhrg13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنت الجيران 🎧", callback_data="Xmhrg14 " + str(m.from_user.id))],
        [InlineKeyboardButton("كارثه 🎧", callback_data="Xmhrg15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يابن امك 🎧", callback_data="Xmhrg16 " + str(m.from_user.id))],
        [InlineKeyboardButton("رايحين نسهر 🎧", callback_data="Xmhrg17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عود البطل 🎧", callback_data="Xmhrg18 " + str(m.from_user.id))],
        [InlineKeyboardButton("بونبوني ساقط 🎧", callback_data="Xmhrg19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شوكلاته سايحه 🎧", callback_data="Xmhrg20 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة الهرجانات رقم 1\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mhrgan2 (\\d+)$"))
async def mhrgan2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("لعنه 🎧", callback_data="Xmhrg21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنت البطل 🎧", callback_data="Xmhrg22 " + str(m.from_user.id))],
        [InlineKeyboardButton("صاصا وسامر المدني 🎧", callback_data="Xmhrg23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تراك الاسد والرعاع 🎧", callback_data="Xmhrg24 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياطير 🎧", callback_data="Xmhrg25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القاهره فوق 🎧", callback_data="Xmhrg26 " + str(m.from_user.id))],
        [InlineKeyboardButton("هلا والله 🎧", callback_data="Xmhrg27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مولود كبير 🎧", callback_data="Xmhrg28 " + str(m.from_user.id))],
        [InlineKeyboardButton("كسر جمجمه 🎧", callback_data="Xmhrg29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قلبي عايز صرمه 🎧", callback_data="Xmhrg30 " + str(m.from_user.id))],
        [InlineKeyboardButton("حرمة 🎧", callback_data="Xmhrg31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عملت سيرش ع الجدع 🎧", callback_data="Xmhrg32 " + str(m.from_user.id))],
        [InlineKeyboardButton("اندال 🎧", callback_data="Xmhrg33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سور الجدعان 🎧", callback_data="Xmhrg34 " + str(m.from_user.id))],
        [InlineKeyboardButton("داين تدان 🎧", callback_data="Xmhrg35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحقودي 🎧", callback_data="Xmhrg36 " + str(m.from_user.id))],
        [InlineKeyboardButton("مهموم 🎧", callback_data="Xmhrg37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("روح الحب 🎧", callback_data="Xmhrg38 " + str(m.from_user.id))],
        [InlineKeyboardButton("اهلا صحابي الواطيين 🎧", callback_data="Xmhrg39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("م عارف 😂 🎧", callback_data="Xmhrg40 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة المهرجانات رقم 2\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mhrgan3 (\\d+)$"))
async def mhrgan3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("رضا البحراوي 1 🎧", callback_data="Xmhrg112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رضا البحراوي 2 🎧", callback_data="Xmhrg113 " + str(m.from_user.id))],
        [InlineKeyboardButton("مضروب بالكيف 🎧", callback_data="Xmhrg114 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كابتن كابتن 🎧", callback_data="Xmhrg115 " + str(m.from_user.id))],
        [InlineKeyboardButton("في الطفولة 🎧", callback_data="Xmhrg116 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اده اده اده 🎧", callback_data="Xmhrg117 " + str(m.from_user.id))],
        [InlineKeyboardButton("يلا بينا نتجنن 🎧", callback_data="Xmhrg118 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البنات والسوشيال ميديا 🎧", callback_data="Xmhrg119 " + str(m.from_user.id))],
        [InlineKeyboardButton("ادلعي ياموزه 🎧", callback_data="Xmhrg120 " + str(m.from_user.id))] +
        [InlineKeyboardButton("صاحبي توب 🎧", callback_data="Xmhrg121 " + str(m.from_user.id))],
        [InlineKeyboardButton("انا بيكا الاوبهه 🎧", callback_data="Xmhrg122 " + str(m.from_user.id))] +
        [InlineKeyboardButton("غصب عنك 🎧", callback_data="Xmhrg123 " + str(m.from_user.id))],
        [InlineKeyboardButton("وقوف فالقلب 🎧", callback_data="Xmhrg124 " + str(m.from_user.id))] +
        [InlineKeyboardButton("معاكي حياتي 🎧", callback_data="Xmhrg125 " + str(m.from_user.id))],
        [InlineKeyboardButton("بعد الفقدان 🎧", callback_data="Xmhrg126 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة المهرجانات رقم 3\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mhrgan4 (\\d+)$"))
async def mhrgan4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("قلبي بيرضي 🎧", callback_data="Xmhrg127 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شلة مغروره 🎧", callback_data="Xmhrg128 " + str(m.from_user.id))],
        [InlineKeyboardButton("كينج اللعبه 🎧", callback_data="Xmhrg129 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ولاد البلد 🎧", callback_data="Xmhrg130 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكتبا مليان 🎧", callback_data="Xmhrg131 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كلبش 🎧", callback_data="Xmhrg132 " + str(m.from_user.id))],
        [InlineKeyboardButton("مدينة المستقبل 🎧", callback_data="Xmhrg133 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طيارات 🎧", callback_data="Xmhrg134 " + str(m.from_user.id))],
        [InlineKeyboardButton("العين بالعين 🎧", callback_data="Xmhrg135 " + str(m.from_user.id))] +
        [InlineKeyboardButton("صاحبي توب 🎧", callback_data="Xmhrg136 " + str(m.from_user.id))],
        [InlineKeyboardButton("توينز جاحد 🎧", callback_data="Xmhrg137 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طب يلا 🎧", callback_data="Xmhrg138 " + str(m.from_user.id))],
        [InlineKeyboardButton("استبينا 🎧", callback_data="Xmhrg139 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ناس ملاعين 🎧", callback_data="Xmhrg140 " + str(m.from_user.id))],
        [InlineKeyboardButton("مفيش واحد سالك 🎧", callback_data="Xmhrg141 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mhrgan " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة المهرجانات رقم 4\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xmhrg1 (\\d+)$"))
async def Xmhrg1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/4")


@Client.on_callback_query(filters.regex("^Xmhrg2 (\\d+)$"))
async def Xmhrg2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/5")


@Client.on_callback_query(filters.regex("^Xmhrg3 (\\d+)$"))
async def Xmhrg3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/6")


@Client.on_callback_query(filters.regex("^Xmhrg4 (\\d+)$"))
async def Xmhrg4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/7")


@Client.on_callback_query(filters.regex("^Xmhrg5 (\\d+)$"))
async def Xmhrg5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/8")


@Client.on_callback_query(filters.regex("^Xmhrg6 (\\d+)$"))
async def Xmhrg6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/9")


@Client.on_callback_query(filters.regex("^Xmhrg7 (\\d+)$"))
async def Xmhrg7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/10")


@Client.on_callback_query(filters.regex("^Xmhrg8 (\\d+)$"))
async def Xmhrg8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/11")


@Client.on_callback_query(filters.regex("^Xmhrg9 (\\d+)$"))
async def Xmhrg9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/12")


@Client.on_callback_query(filters.regex("^Xmhrg10 (\\d+)$"))
async def Xmhrg10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/13")


@Client.on_callback_query(filters.regex("^Xmhrg11 (\\d+)$"))
async def Xmhrg11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/14")


@Client.on_callback_query(filters.regex("^Xmhrg12 (\\d+)$"))
async def Xmhrg12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/15")


@Client.on_callback_query(filters.regex("^Xmhrg13 (\\d+)$"))
async def Xmhrg13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/16")


@Client.on_callback_query(filters.regex("^Xmhrg14 (\\d+)$"))
async def Xmhrg14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/17")


@Client.on_callback_query(filters.regex("^Xmhrg15 (\\d+)$"))
async def Xmhrg15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/18")


@Client.on_callback_query(filters.regex("^Xmhrg16 (\\d+)$"))
async def Xmhrg16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/19")


@Client.on_callback_query(filters.regex("^Xmhrg17 (\\d+)$"))
async def Xmhrg17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/20")


@Client.on_callback_query(filters.regex("^Xmhrg18 (\\d+)$"))
async def Xmhrg18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/21")


@Client.on_callback_query(filters.regex("^Xmhrg19 (\\d+)$"))
async def Xmhrg19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/22")


@Client.on_callback_query(filters.regex("^Xmhrg20 (\\d+)$"))
async def Xmhrg20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/23")


@Client.on_callback_query(filters.regex("^Xmhrg21 (\\d+)$"))
async def Xmhrg21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/24")


@Client.on_callback_query(filters.regex("^Xmhrg22 (\\d+)$"))
async def Xmhrg22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/25")


@Client.on_callback_query(filters.regex("^Xmhrg23 (\\d+)$"))
async def Xmhrg23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/26")


@Client.on_callback_query(filters.regex("^Xmhrg24 (\\d+)$"))
async def Xmhrg24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/27")


@Client.on_callback_query(filters.regex("^Xmhrg25 (\\d+)$"))
async def Xmhrg25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/28")


@Client.on_callback_query(filters.regex("^Xmhrg26 (\\d+)$"))
async def Xmhrg26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/29")


@Client.on_callback_query(filters.regex("^Xmhrg27 (\\d+)$"))
async def Xmhrg27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/30")


@Client.on_callback_query(filters.regex("^Xmhrg28 (\\d+)$"))
async def Xmhrg28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/31")


@Client.on_callback_query(filters.regex("^Xmhrg29 (\\d+)$"))
async def Xmhrg29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/32")


@Client.on_callback_query(filters.regex("^Xmhrg30 (\\d+)$"))
async def Xmhrg30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/33")


@Client.on_callback_query(filters.regex("^Xmhrg31 (\\d+)$"))
async def Xmhrg31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/34")


@Client.on_callback_query(filters.regex("^Xmhrg32 (\\d+)$"))
async def Xmhrg32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/35")


@Client.on_callback_query(filters.regex("^Xmhrg33 (\\d+)$"))
async def Xmhrg33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/36")


@Client.on_callback_query(filters.regex("^Xmhrg34 (\\d+)$"))
async def Xmhrg34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/37")


@Client.on_callback_query(filters.regex("^Xmhrg35 (\\d+)$"))
async def Xmhrg35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/38")


@Client.on_callback_query(filters.regex("^Xmhrg36 (\\d+)$"))
async def Xmhrg36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/39")


@Client.on_callback_query(filters.regex("^Xmhrg37 (\\d+)$"))
async def Xmhrg37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/40")


@Client.on_callback_query(filters.regex("^Xmhrg38 (\\d+)$"))
async def Xmhrg38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/41")


@Client.on_callback_query(filters.regex("^Xmhrg39 (\\d+)$"))
async def Xmhrg39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/42")


@Client.on_callback_query(filters.regex("^Xmhrg40 (\\d+)$"))
async def Xmhrg40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/43")


@Client.on_callback_query(filters.regex("^Xmhrg112 (\\d+)$"))
async def Xmhrg112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/112")


@Client.on_callback_query(filters.regex("^Xmhrg113 (\\d+)$"))
async def Xmhrg113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/113")


@Client.on_callback_query(filters.regex("^Xmhrg114 (\\d+)$"))
async def Xmhrg114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/114")


@Client.on_callback_query(filters.regex("^Xmhrg115 (\\d+)$"))
async def Xmhrg115(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/115")


@Client.on_callback_query(filters.regex("^Xmhrg116 (\\d+)$"))
async def Xmhrg116(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/116")


@Client.on_callback_query(filters.regex("^Xmhrg117 (\\d+)$"))
async def Xmhrg117(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/117")


@Client.on_callback_query(filters.regex("^Xmhrg118 (\\d+)$"))
async def Xmhrg118(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/118")


@Client.on_callback_query(filters.regex("^Xmhrg119 (\\d+)$"))
async def Xmhrg119(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/119")


@Client.on_callback_query(filters.regex("^Xmhrg120 (\\d+)$"))
async def Xmhrg120(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/120")


@Client.on_callback_query(filters.regex("^Xmhrg121 (\\d+)$"))
async def Xmhrg121(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/121")


@Client.on_callback_query(filters.regex("^Xmhrg122 (\\d+)$"))
async def Xmhrg122(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/122")


@Client.on_callback_query(filters.regex("^Xmhrg123 (\\d+)$"))
async def Xmhrg123(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/123")


@Client.on_callback_query(filters.regex("^Xmhrg124 (\\d+)$"))
async def Xmhrg124(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/124")


@Client.on_callback_query(filters.regex("^Xmhrg125 (\\d+)$"))
async def Xmhrg125(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/125")


@Client.on_callback_query(filters.regex("^Xmhrg126 (\\d+)$"))
async def Xmhrg126(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/126")


@Client.on_callback_query(filters.regex("^Xmhrg127 (\\d+)$"))
async def Xmhrg127(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/127")


@Client.on_callback_query(filters.regex("^Xmhrg128 (\\d+)$"))
async def Xmhrg128(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/128")


@Client.on_callback_query(filters.regex("^Xmhrg129 (\\d+)$"))
async def Xmhrg129(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/129")


@Client.on_callback_query(filters.regex("^Xmhrg130 (\\d+)$"))
async def Xmhrg130(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/130")


@Client.on_callback_query(filters.regex("^Xmhrg131 (\\d+)$"))
async def Xmhrg131(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/131")


@Client.on_callback_query(filters.regex("^Xmhrg132 (\\d+)$"))
async def Xmhrg132(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/132")


@Client.on_callback_query(filters.regex("^Xmhrg133 (\\d+)$"))
async def Xmhrg133(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/133")


@Client.on_callback_query(filters.regex("^Xmhrg134 (\\d+)$"))
async def Xmhrg134(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/134")


@Client.on_callback_query(filters.regex("^Xmhrg135 (\\d+)$"))
async def Xmhrg135(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/135")


@Client.on_callback_query(filters.regex("^Xmhrg136 (\\d+)$"))
async def Xmhrg136(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/136")


@Client.on_callback_query(filters.regex("^Xmhrg137 (\\d+)$"))
async def Xmhrg137(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/137")


@Client.on_callback_query(filters.regex("^Xmhrg138 (\\d+)$"))
async def Xmhrg138(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/138")


@Client.on_callback_query(filters.regex("^Xmhrg139 (\\d+)$"))
async def Xmhrg139(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/139")


@Client.on_callback_query(filters.regex("^Xmhrg140 (\\d+)$"))
async def Xmhrg140(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/140")


@Client.on_callback_query(filters.regex("^Xmhrg141 (\\d+)$"))
async def Xmhrg141(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/141")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^adham (\\d+)$"))
async def adham(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كيف بحبك هبك 🎧", callback_data="Xadh1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حدا ما بينسي 🎧", callback_data="Xadh2 " + str(m.from_user.id))],
        [InlineKeyboardButton("حدك الكون 🎧", callback_data="Xadh3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مشتاق 🎧", callback_data="Xadh4 " + str(m.from_user.id))],
        [InlineKeyboardButton("النهايه السعيده 🎧", callback_data="Xadh5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بتعرف شعوري 🎧", callback_data="Xadh6 " + str(m.from_user.id))],
        [InlineKeyboardButton("هو الحب 🎧", callback_data="Xadh7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نسخه منك 🎧", callback_data="Xadh8 " + str(m.from_user.id))],
        [InlineKeyboardButton("ودعني 🎧", callback_data="Xadh9 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="araby " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني ادهم نابلسي", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xadh1 (\\d+)$"))
async def Xadh1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/123")


@Client.on_callback_query(filters.regex("^Xadh2 (\\d+)$"))
async def Xadh2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/124")


@Client.on_callback_query(filters.regex("^Xadh3 (\\d+)$"))
async def Xadh3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/125")


@Client.on_callback_query(filters.regex("^Xadh4 (\\d+)$"))
async def Xadh4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/126")


@Client.on_callback_query(filters.regex("^Xadh5 (\\d+)$"))
async def Xadh5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/127")


@Client.on_callback_query(filters.regex("^Xadh6 (\\d+)$"))
async def Xadh6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/128")


@Client.on_callback_query(filters.regex("^Xadh7 (\\d+)$"))
async def Xadh7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/129")


@Client.on_callback_query(filters.regex("^Xadh8 (\\d+)$"))
async def Xadh8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/130")


@Client.on_callback_query(filters.regex("^Xadh9 (\\d+)$"))
async def Xadh9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر ??🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/131")


@Client.on_callback_query(filters.regex("^xagn1 (\\d+)$"))
async def xagn1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/177")


@Client.on_callback_query(filters.regex("^xagn2 (\\d+)$"))
async def xagn2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/178")


@Client.on_callback_query(filters.regex("^xagn3 (\\d+)$"))
async def xagn3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/179")


@Client.on_callback_query(filters.regex("^xagn4 (\\d+)$"))
async def xagn4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/180")


@Client.on_callback_query(filters.regex("^xagn5 (\\d+)$"))
async def xagn5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/181")


@Client.on_callback_query(filters.regex("^xagn6 (\\d+)$"))
async def xagn6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/182")


@Client.on_callback_query(filters.regex("^xagn7 (\\d+)$"))
async def xagn7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/183")


@Client.on_callback_query(filters.regex("^xagn8 (\\d+)$"))
async def xagn8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/184")


@Client.on_callback_query(filters.regex("^xagn9 (\\d+)$"))
async def xagn9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/185")


@Client.on_callback_query(filters.regex("^xagn10 (\\d+)$"))
async def xagn10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/186")


@Client.on_callback_query(filters.regex("^xagn11 (\\d+)$"))
async def xagn11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/211")


@Client.on_callback_query(filters.regex("^xagn12 (\\d+)$"))
async def xagn12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/212")


@Client.on_callback_query(filters.regex("^xagn13 (\\d+)$"))
async def xagn13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/213")


@Client.on_callback_query(filters.regex("^xagn14 (\\d+)$"))
async def xagn14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/214")


@Client.on_callback_query(filters.regex("^xagn15 (\\d+)$"))
async def xagn15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/215")


@Client.on_callback_query(filters.regex("^xagn16 (\\d+)$"))
async def xagn16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/216")


@Client.on_callback_query(filters.regex("^xagn17 (\\d+)$"))
async def xagn17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/217")


@Client.on_callback_query(filters.regex("^xagn18 (\\d+)$"))
async def xagn18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/218")


@Client.on_callback_query(filters.regex("^xagn19 (\\d+)$"))
async def xagn19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/219")


@Client.on_callback_query(filters.regex("^xagn20 (\\d+)$"))
async def xagn20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/220")


@Client.on_callback_query(filters.regex("^xagn21 (\\d+)$"))
async def xagn21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/221")


@Client.on_callback_query(filters.regex("^xagn22 (\\d+)$"))
async def xagn22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/222")


@Client.on_callback_query(filters.regex("^xagn23 (\\d+)$"))
async def xagn23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/223")


@Client.on_callback_query(filters.regex("^xagn24 (\\d+)$"))
async def xagn24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/224")


@Client.on_callback_query(filters.regex("^Xagn144 (\\d+)$"))
async def Xagn144(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/144")


@Client.on_callback_query(filters.regex("^Xagn145 (\\d+)$"))
async def Xagn145(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/145")


@Client.on_callback_query(filters.regex("^Xagn161 (\\d+)$"))
async def Xagn161(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/161")


@Client.on_callback_query(filters.regex("^Xagn162 (\\d+)$"))
async def Xagn162(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/162")


@Client.on_callback_query(filters.regex("^Xagn163 (\\d+)$"))
async def Xagn163(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/163")


@Client.on_callback_query(filters.regex("^Xagn164 (\\d+)$"))
async def Xagn164(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/164")


@Client.on_callback_query(filters.regex("^Xagn165 (\\d+)$"))
async def Xagn165(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/165")


@Client.on_callback_query(filters.regex("^Xagn167 (\\d+)$"))
async def Xagn167(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/167")


@Client.on_callback_query(filters.regex("^Xagn168 (\\d+)$"))
async def Xagn168(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/168")


@Client.on_callback_query(filters.regex("^Xagn169 (\\d+)$"))
async def Xagn169(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/169")


@Client.on_callback_query(filters.regex("^Xagn170 (\\d+)$"))
async def Xagn170(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/170")


@Client.on_callback_query(filters.regex("^Xagn171 (\\d+)$"))
async def Xagn171(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/171")


@Client.on_callback_query(filters.regex("^Xagn173 (\\d+)$"))
async def Xagn173(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/173")


@Client.on_callback_query(filters.regex("^Xagn174 (\\d+)$"))
async def Xagn174(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/174")


@Client.on_callback_query(filters.regex("^Xagn175 (\\d+)$"))
async def Xagn175(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/175")


@Client.on_callback_query(filters.regex("^Xagn176 (\\d+)$"))
async def Xagn176(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/176")


@Client.on_callback_query(filters.regex("^Xagn177 (\\d+)$"))
async def Xagn177(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/177")


@Client.on_callback_query(filters.regex("^Xagn178 (\\d+)$"))
async def Xagn178(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/178")


@Client.on_callback_query(filters.regex("^Xagn179 (\\d+)$"))
async def Xagn179(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/179")


@Client.on_callback_query(filters.regex("^Xagn181 (\\d+)$"))
async def Xagn181(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/181")


@Client.on_callback_query(filters.regex("^Xagn182 (\\d+)$"))
async def Xagn182(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/182")


@Client.on_callback_query(filters.regex("^Xagn183 (\\d+)$"))
async def Xagn183(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/183")


@Client.on_callback_query(filters.regex("^Xagn184 (\\d+)$"))
async def Xagn184(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/184")


@Client.on_callback_query(filters.regex("^Xagn185 (\\d+)$"))
async def Xagn185(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/185")


@Client.on_callback_query(filters.regex("^Xagn186 (\\d+)$"))
async def Xagn186(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/186")


@Client.on_callback_query(filters.regex("^Xagn188 (\\d+)$"))
async def Xagn188(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/188")


@Client.on_callback_query(filters.regex("^Xagn189 (\\d+)$"))
async def Xagn189(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/189")


@Client.on_callback_query(filters.regex("^Xagn190 (\\d+)$"))
async def Xagn190(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/190")


@Client.on_callback_query(filters.regex("^Xagn191 (\\d+)$"))
async def Xagn191(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/191")


@Client.on_callback_query(filters.regex("^Xagn192 (\\d+)$"))
async def Xagn192(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/192")


@Client.on_callback_query(filters.regex("^Xagn193 (\\d+)$"))
async def Xagn193(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/193")


@Client.on_callback_query(filters.regex("^Xagn195 (\\d+)$"))
async def Xagn195(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/195")


@Client.on_callback_query(filters.regex("^Xagn196 (\\d+)$"))
async def Xagn196(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/196")


@Client.on_callback_query(filters.regex("^Xagn197 (\\d+)$"))
async def Xagn197(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/197")


@Client.on_callback_query(filters.regex("^Xagn198 (\\d+)$"))
async def Xagn198(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/198")


@Client.on_callback_query(filters.regex("^Xagn199 (\\d+)$"))
async def Xagn199(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/199")


@Client.on_callback_query(filters.regex("^Xagn200 (\\d+)$"))
async def Xagn200(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/200")


@Client.on_callback_query(filters.regex("^Xagn202 (\\d+)$"))
async def Xagn202(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/202")


@Client.on_callback_query(filters.regex("^Xagn203 (\\d+)$"))
async def Xagn203(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/203")


@Client.on_callback_query(filters.regex("^Xagn204 (\\d+)$"))
async def Xagn204(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/204")


@Client.on_callback_query(filters.regex("^Xagn205 (\\d+)$"))
async def Xagn205(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/205")


@Client.on_callback_query(filters.regex("^Xagn206 (\\d+)$"))
async def Xagn206(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/206")


@Client.on_callback_query(filters.regex("^Xagn207 (\\d+)$"))
async def Xagn207(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/207")


@Client.on_callback_query(filters.regex("^Xagn209 (\\d+)$"))
async def Xagn209(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/209")


@Client.on_callback_query(filters.regex("^Xagn210 (\\d+)$"))
async def Xagn210(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/210")


@Client.on_callback_query(filters.regex("^Xagn211 (\\d+)$"))
async def Xagn211(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/211")


@Client.on_callback_query(filters.regex("^Xagn212 (\\d+)$"))
async def Xagn212(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/212")


@Client.on_callback_query(filters.regex("^Xagn213 (\\d+)$"))
async def Xagn213(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/213")


@Client.on_callback_query(filters.regex("^Xagn214 (\\d+)$"))
async def Xagn214(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/214")


@Client.on_callback_query(filters.regex("^Xagn216 (\\d+)$"))
async def Xagn216(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/216")


@Client.on_callback_query(filters.regex("^Xagn217 (\\d+)$"))
async def Xagn217(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/217")


@Client.on_callback_query(filters.regex("^Xagn218 (\\d+)$"))
async def Xagn218(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/218")


@Client.on_callback_query(filters.regex("^Xagn219 (\\d+)$"))
async def Xagn219(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/219")


@Client.on_callback_query(filters.regex("^Xagn220 (\\d+)$"))
async def Xagn220(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/220")


@Client.on_callback_query(filters.regex("^Xagn221 (\\d+)$"))
async def Xagn221(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/221")


@Client.on_callback_query(filters.regex("^Xagn223 (\\d+)$"))
async def Xagn223(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/223")


@Client.on_callback_query(filters.regex("^Xagn224 (\\d+)$"))
async def Xagn224(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/224")


@Client.on_callback_query(filters.regex("^Xagn225 (\\d+)$"))
async def Xagn225(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/225")


@Client.on_callback_query(filters.regex("^Xagn226 (\\d+)$"))
async def Xagn226(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/226")


@Client.on_callback_query(filters.regex("^Xagn227 (\\d+)$"))
async def Xagn227(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/227")


@Client.on_callback_query(filters.regex("^Xagn228 (\\d+)$"))
async def Xagn228(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/228")


@Client.on_callback_query(filters.regex("^Xagn230 (\\d+)$"))
async def Xagn230(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/230")


@Client.on_callback_query(filters.regex("^Xagn231 (\\d+)$"))
async def Xagn231(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/231")


@Client.on_callback_query(filters.regex("^Xagn232 (\\d+)$"))
async def Xagn232(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/232")


@Client.on_callback_query(filters.regex("^Xagn233 (\\d+)$"))
async def Xagn233(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/233")


@Client.on_callback_query(filters.regex("^Xagn234 (\\d+)$"))
async def Xagn234(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/234")


@Client.on_callback_query(filters.regex("^Xagn235 (\\d+)$"))
async def Xagn235(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/235")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^ammarr (\\d+)$"))
async def ammarr(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("بتيجي في بالي 🎧", callback_data="Xamm1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طيب 🎧", callback_data="Xamm2 " + str(m.from_user.id))],
        [InlineKeyboardButton("برشامه منوم 🎧", callback_data="Xamm3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بساط 🎧", callback_data="Xamm4 " + str(m.from_user.id))],
        [InlineKeyboardButton("طفره 🎧", callback_data="Xamm5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ترام 🎧", callback_data="Xamm6 " + str(m.from_user.id))],
        [InlineKeyboardButton("هلوسه 🎧", callback_data="Xamm7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مسوخ 🎧", callback_data="Xamm8 " + str(m.from_user.id))],
        [InlineKeyboardButton("بلاش تغني 🎧", callback_data="Xamm9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اخر عازف ع الارض 🎧", callback_data="Xamm10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حدود 🎧", callback_data="Xamm11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("غامق 🎧", callback_data="Xamm12 " + str(m.from_user.id))],
        [InlineKeyboardButton("فاترينا 🎧", callback_data="Xamm13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جهنم 🎧", callback_data="Xamm14 " + str(m.from_user.id))],
        [InlineKeyboardButton("فستان 🎧", callback_data="Xamm15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ضي العين 🎧", callback_data="Xamm16 " + str(m.from_user.id))],
        [InlineKeyboardButton("يا ليل اندهلي 🎧", callback_data="Xamm17 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني عمار حسني", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xamm1 (\\d+)$"))
async def Xamm1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/65")


@Client.on_callback_query(filters.regex("^Xamm2 (\\d+)$"))
async def Xamm2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/66")


@Client.on_callback_query(filters.regex("^Xamm3 (\\d+)$"))
async def Xamm3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/67")


@Client.on_callback_query(filters.regex("^Xamm4 (\\d+)$"))
async def Xamm4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/68")


@Client.on_callback_query(filters.regex("^Xamm5 (\\d+)$"))
async def Xamm5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/69")


@Client.on_callback_query(filters.regex("^Xamm6 (\\d+)$"))
async def Xamm6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/70")


@Client.on_callback_query(filters.regex("^Xamm7 (\\d+)$"))
async def Xamm7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/71")


@Client.on_callback_query(filters.regex("^Xamm8 (\\d+)$"))
async def Xamm8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/72")


@Client.on_callback_query(filters.regex("^Xamm9 (\\d+)$"))
async def Xamm9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/73")


@Client.on_callback_query(filters.regex("^Xamm10 (\\d+)$"))
async def Xamm10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/74")


@Client.on_callback_query(filters.regex("^Xamm11 (\\d+)$"))
async def Xamm11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/188")


@Client.on_callback_query(filters.regex("^Xamm12 (\\d+)$"))
async def Xamm12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/189")


@Client.on_callback_query(filters.regex("^Xamm13 (\\d+)$"))
async def Xamm13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/190")


@Client.on_callback_query(filters.regex("^Xamm14 (\\d+)$"))
async def Xamm14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/191")


@Client.on_callback_query(filters.regex("^Xamm15 (\\d+)$"))
async def Xamm15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/192")


@Client.on_callback_query(filters.regex("^Xamm16 (\\d+)$"))
async def Xamm16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/193")


@Client.on_callback_query(filters.regex("^Xamm17 (\\d+)$"))
async def Xamm17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/194")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^asala (\\d+)$"))
async def asala(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("60 دقيقه 🎧", callback_data="Xasa1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("خانات الذكريات 🎧", callback_data="Xasa2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياعالم 🎧", callback_data="Xasa3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هو حبيبي 🎧", callback_data="Xasa4 " + str(m.from_user.id))],
        [InlineKeyboardButton("قد الحروف 🎧", callback_data="Xasa5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اسفه 🎧", callback_data="Xasa6 " + str(m.from_user.id))],
        [InlineKeyboardButton("اكتر 🎧", callback_data="Xasa7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جابو سيرتو 🎧", callback_data="Xasa8 " + str(m.from_user.id))],
        [InlineKeyboardButton("روحي وخداني 🎧", callback_data="Xasa9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سؤال بسيط 🎧", callback_data="Xasa10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني اصاله 🔊\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xasa1 (\\d+)$"))
async def Xasa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/142")


@Client.on_callback_query(filters.regex("^Xasa2 (\\d+)$"))
async def Xasa2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/143")


@Client.on_callback_query(filters.regex("^Xasa3 (\\d+)$"))
async def Xasa3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/144")


@Client.on_callback_query(filters.regex("^Xasa4 (\\d+)$"))
async def Xasa4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/145")


@Client.on_callback_query(filters.regex("^Xasa5 (\\d+)$"))
async def Xasa5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/146")


@Client.on_callback_query(filters.regex("^Xasa6 (\\d+)$"))
async def Xasa6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/147")


@Client.on_callback_query(filters.regex("^Xasa7 (\\d+)$"))
async def Xasa7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/148")


@Client.on_callback_query(filters.regex("^Xasa8 (\\d+)$"))
async def Xasa8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/149")


@Client.on_callback_query(filters.regex("^Xasa9 (\\d+)$"))
async def Xasa9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/150")


@Client.on_callback_query(filters.regex("^Xasa10 (\\d+)$"))
async def Xasa10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/151")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^bablo (\\d+)$"))
async def bablo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الجميزه 🎧", callback_data="Xbab1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فري 🎧", callback_data="Xbab2 " + str(m.from_user.id))],
        [InlineKeyboardButton("سندباد 🎧", callback_data="Xbab3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ابو مكة 🎧", callback_data="Xbab4 " + str(m.from_user.id))],
        [InlineKeyboardButton("افتر بارتي 🎧", callback_data="Xbab5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سكانيا 🎧", callback_data="Xbab6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ديناميت 🎧", callback_data="Xbab7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فولكلور 🎧", callback_data="Xbab8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني بابلو\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xbab1 (\\d+)$"))
async def Xbab1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/31")


@Client.on_callback_query(filters.regex("^Xbab2 (\\d+)$"))
async def Xbab2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/32")


@Client.on_callback_query(filters.regex("^Xbab3 (\\d+)$"))
async def Xbab3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/33")


@Client.on_callback_query(filters.regex("^Xbab4 (\\d+)$"))
async def Xbab4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/34")


@Client.on_callback_query(filters.regex("^Xbab5 (\\d+)$"))
async def Xbab5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/35")


@Client.on_callback_query(filters.regex("^Xbab6 (\\d+)$"))
async def Xbab6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/36")


@Client.on_callback_query(filters.regex("^Xbab7 (\\d+)$"))
async def Xbab7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/37")


@Client.on_callback_query(filters.regex("^Xbab8 (\\d+)$"))
async def Xbab8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/38")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^dyabb (\\d+)$"))
async def dyabb(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("قدام مرايتها 🎧", callback_data="Xdya1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يابلدرنا ياحلوه 🎧", callback_data="Xdya2 " + str(m.from_user.id))],
        [InlineKeyboardButton("تملي معاك 🎧", callback_data="Xdya3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يااجمل عيون 🎧", callback_data="Xdya4 " + str(m.from_user.id))],
        [InlineKeyboardButton("وماله 🎧", callback_data="Xdya5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هيعيش يفتكرني 🎧", callback_data="Xdya6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ده لو اتساب 🎧", callback_data="Xdya7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اول يوم في البعد 🎧", callback_data="Xdya8 " + str(m.from_user.id))],
        [InlineKeyboardButton("معاك قلبي 🎧", callback_data="Xdya9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وهي عامله ايه 🎧", callback_data="Xdya10 " + str(m.from_user.id))],
        [InlineKeyboardButton("مكانك يف قلبي 🎧", callback_data="Xdya11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زي مانتي 🎧", callback_data="Xdya12 " + str(m.from_user.id))],
        [InlineKeyboardButton("عم الطيب 🎧", callback_data="Xdya13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سهران 🎧", callback_data="Xdya14 " + str(m.from_user.id))],
        [InlineKeyboardButton("حلوة البدايات 🎧", callback_data="Xdya15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بالضحكه دي 🎧", callback_data="Xdya16 " + str(m.from_user.id))],
        [InlineKeyboardButton("جامده بس 🎧", callback_data="Xdya17 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xdya1 (\\d+)$"))
async def Xdya1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/89")


@Client.on_callback_query(filters.regex("^Xdya2 (\\d+)$"))
async def Xdya2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/90")


@Client.on_callback_query(filters.regex("^Xdya3 (\\d+)$"))
async def Xdya3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/91")


@Client.on_callback_query(filters.regex("^Xdya4 (\\d+)$"))
async def Xdya4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/92")


@Client.on_callback_query(filters.regex("^Xdya5 (\\d+)$"))
async def Xdya5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/93")


@Client.on_callback_query(filters.regex("^Xdya6 (\\d+)$"))
async def Xdya6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/94")


@Client.on_callback_query(filters.regex("^Xdya7 (\\d+)$"))
async def Xdya7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/95")


@Client.on_callback_query(filters.regex("^Xdya8 (\\d+)$"))
async def Xdya8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/96")


@Client.on_callback_query(filters.regex("^Xdya9 (\\d+)$"))
async def Xdya9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/97")


@Client.on_callback_query(filters.regex("^Xdya10 (\\d+)$"))
async def Xdya10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/98")


@Client.on_callback_query(filters.regex("^Xdya11 (\\d+)$"))
async def Xdya11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/99")


@Client.on_callback_query(filters.regex("^Xdya12 (\\d+)$"))
async def Xdya12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/100")


@Client.on_callback_query(filters.regex("^Xdya13 (\\d+)$"))
async def Xdya13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/101")


@Client.on_callback_query(filters.regex("^Xdya14 (\\d+)$"))
async def Xdya14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/102")


@Client.on_callback_query(filters.regex("^Xdya15 (\\d+)$"))
async def Xdya15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/103")


@Client.on_callback_query(filters.regex("^Xdya16 (\\d+)$"))
async def Xdya16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/104")


@Client.on_callback_query(filters.regex("^Xdya17 (\\d+)$"))
async def Xdya17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/105")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^elesa (\\d+)$"))
async def elesa(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("يا مرايتي 🎧", callback_data="Xeles1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("افتكرت 🎧", callback_data="Xeles2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مكتوبه ليك 🎧", callback_data="Xeles3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حاله حب 🎧", callback_data="Xeles4 " + str(m.from_user.id))],
        [InlineKeyboardButton("تعبت منك 🎧", callback_data="Xeles5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وانت قصادي 🎧", callback_data="Xeles6 " + str(m.from_user.id))],
        [InlineKeyboardButton("مباحه ليك 🎧", callback_data="Xeles7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("في عيونك 🎧", callback_data="Xeles8 " + str(m.from_user.id))],
        [InlineKeyboardButton("انا شبه نسيتك 🎧", callback_data="Xeles9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بنحب الحياه 🎧", callback_data="Xeles10 " + str(m.from_user.id))],
        [InlineKeyboardButton("حبه اهتمام 🎧", callback_data="Xeles11 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني اليسا\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xeles1 (\\d+)$"))
async def Xeles1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/153")


@Client.on_callback_query(filters.regex("^Xeles2 (\\d+)$"))
async def Xeles2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/154")


@Client.on_callback_query(filters.regex("^Xeles3 (\\d+)$"))
async def Xeles3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/155")


@Client.on_callback_query(filters.regex("^Xeles4 (\\d+)$"))
async def Xeles4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/156")


@Client.on_callback_query(filters.regex("^Xeles5 (\\d+)$"))
async def Xeles5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/157")


@Client.on_callback_query(filters.regex("^Xeles6 (\\d+)$"))
async def Xeles6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/158")


@Client.on_callback_query(filters.regex("^Xeles7 (\\d+)$"))
async def Xeles7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/159")


@Client.on_callback_query(filters.regex("^Xeles8 (\\d+)$"))
async def Xeles8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/160")


@Client.on_callback_query(filters.regex("^Xeles9 (\\d+)$"))
async def Xeles9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/161")


@Client.on_callback_query(filters.regex("^Xeles10 (\\d+)$"))
async def Xeles10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/162")


@Client.on_callback_query(filters.regex("^Xeles11 (\\d+)$"))
async def Xeles11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/163")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^hamaky (\\d+)$"))
async def hamaky(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هو ده حبيبي 🎧", callback_data="Xham1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قدام الناس 🎧", callback_data="Xham2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ياستار 🎧", callback_data="Xham3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("راسمك في خيالي 🎧", callback_data="Xham4 " + str(m.from_user.id))],
        [InlineKeyboardButton("احلي حاجه فيكي 🎧", callback_data="Xham5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مابلاش 🎧", callback_data="Xham6 " + str(m.from_user.id))],
        [InlineKeyboardButton("م البدايه 🎧", callback_data="Xham7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليله باظت 🎧", callback_data="Xham8 " + str(m.from_user.id))],
        [InlineKeyboardButton("واحده واحده 🎧", callback_data="Xham9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("واعمل ايه 🎧", callback_data="Xham10 " + str(m.from_user.id))],
        [InlineKeyboardButton("من قلبي بغني 🎧", callback_data="Xham11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حاجه مستخبيه 🎧", callback_data="Xham12 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني حماقي\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xham1 (\\d+)$"))
async def Xham1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/76")


@Client.on_callback_query(filters.regex("^Xham2 (\\d+)$"))
async def Xham2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/77")


@Client.on_callback_query(filters.regex("^Xham3 (\\d+)$"))
async def Xham3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/78")


@Client.on_callback_query(filters.regex("^Xham4 (\\d+)$"))
async def Xham4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/79")


@Client.on_callback_query(filters.regex("^Xham5 (\\d+)$"))
async def Xham5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/80")


@Client.on_callback_query(filters.regex("^Xham6 (\\d+)$"))
async def Xham6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/81")


@Client.on_callback_query(filters.regex("^Xham7 (\\d+)$"))
async def Xham7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/82")


@Client.on_callback_query(filters.regex("^Xham8 (\\d+)$"))
async def Xham8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/83")


@Client.on_callback_query(filters.regex("^Xham9 (\\d+)$"))
async def Xham9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/84")


@Client.on_callback_query(filters.regex("^Xham10 (\\d+)$"))
async def Xham10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/85")


@Client.on_callback_query(filters.regex("^Xham11 (\\d+)$"))
async def Xham11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/86")


@Client.on_callback_query(filters.regex("^Xham12 (\\d+)$"))
async def Xham12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/87")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^helal (\\d+)$"))
async def helal(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("وبحس معاك 🎧", callback_data="Xhela1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اشرب شاي 🎧", callback_data="Xhela2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ليه اختارنا البعد 🎧", callback_data="Xhela3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("دايما دموع 🎧", callback_data="Xhela4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ساعات 🎧", callback_data="Xhela5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محدش بينفع حد 🎧", callback_data="Xhela6 " + str(m.from_user.id))],
        [InlineKeyboardButton("متغيره 🎧", callback_data="Xhela7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وجمالها 🎧", callback_data="Xhela8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني حماده هلال", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xhela1 (\\d+)$"))
async def Xhela1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/275")


@Client.on_callback_query(filters.regex("^Xhela2 (\\d+)$"))
async def Xhela2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/276")


@Client.on_callback_query(filters.regex("^Xhela3 (\\d+)$"))
async def Xhela3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/277")


@Client.on_callback_query(filters.regex("^Xhela4 (\\d+)$"))
async def Xhela4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/278")


@Client.on_callback_query(filters.regex("^Xhela5 (\\d+)$"))
async def Xhela5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/279")


@Client.on_callback_query(filters.regex("^Xhela6 (\\d+)$"))
async def Xhela6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/280")


@Client.on_callback_query(filters.regex("^Xhela7 (\\d+)$"))
async def Xhela7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/281")


@Client.on_callback_query(filters.regex("^Xhela8 (\\d+)$"))
async def Xhela18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/282")


#######################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^joker (\\d+)$"))
async def joker(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الكبت 🎧", callback_data="Xjok1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقع 🎧", callback_data="Xjok2 " + str(m.from_user.id))],
        [InlineKeyboardButton("مناسك الالم 🎧", callback_data="Xjok3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فرصه تانيه 🎧", callback_data="Xjok4 " + str(m.from_user.id))],
        [InlineKeyboardButton("تسعيناتي 🎧", callback_data="Xjok5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قادرين 🎧", callback_data="Xjok6 " + str(m.from_user.id))],
        [InlineKeyboardButton("العقد 🎧", callback_data="Xjok7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الوصايا 🎧", callback_data="Xjok8 " + str(m.from_user.id))],
        [InlineKeyboardButton("دنيا 🎧", callback_data="Xjok9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حلم كبير 🎧", callback_data="Xjok10 " + str(m.from_user.id))],
        [InlineKeyboardButton("سكان الليل 🎧", callback_data="Xjok11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بعد النسيان 🎧", callback_data="Xjok12 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني الجوكر\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xjok1 (\\d+)$"))
async def Xjok1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/165")


@Client.on_callback_query(filters.regex("^Xjok2 (\\d+)$"))
async def Xjok2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/166")


@Client.on_callback_query(filters.regex("^Xjok3 (\\d+)$"))
async def Xjok3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/167")


@Client.on_callback_query(filters.regex("^Xjok4 (\\d+)$"))
async def Xjok4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/176")


@Client.on_callback_query(filters.regex("^Xjok5 (\\d+)$"))
async def Xjok5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/169")


@Client.on_callback_query(filters.regex("^Xjok6 (\\d+)$"))
async def Xjok6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/168")


@Client.on_callback_query(filters.regex("^Xjok7 (\\d+)$"))
async def Xjok7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/175")


@Client.on_callback_query(filters.regex("^Xjok8 (\\d+)$"))
async def Xjok8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/170")


@Client.on_callback_query(filters.regex("^Xjok9 (\\d+)$"))
async def Xjok9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/171")


@Client.on_callback_query(filters.regex("^Xjok10 (\\d+)$"))
async def Xjok10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/172")


@Client.on_callback_query(filters.regex("^Xjok11 (\\d+)$"))
async def Xjok11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/173")


@Client.on_callback_query(filters.regex("^Xjok12 (\\d+)$"))
async def Xjok12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/174")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^kamell (\\d+)$"))
async def kamell(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("انا مستنيك 🎧", callback_data="Xkam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تايجر خارج عن السيطره 🎧", callback_data="Xkam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("جاوبنا يا ليل 🎧", callback_data="Xkam3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زي نور 🎧", callback_data="Xkam4 " + str(m.from_user.id))],
        [InlineKeyboardButton("قصاد بابك 🎧", callback_data="Xkam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قولي غاب 🎧", callback_data="Xkam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("كان في طفل 🎧", callback_data="Xkam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كانسر 🎧", callback_data="Xkam8 " + str(m.from_user.id))],
        [InlineKeyboardButton("مبقتش اخاف 🎧", callback_data="Xkam9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("متزعليش 🎧", callback_data="Xkam10 " + str(m.from_user.id))],
        [InlineKeyboardButton("ولا بننسي 🎧", callback_data="Xkam11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مش شرط 🎧", callback_data="Xkam12 " + str(m.from_user.id))],
        [InlineKeyboardButton("يا ليل 🎧", callback_data="Xkam13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("تتجوزيني 🎧", callback_data="Xkam14 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني احمد كامل\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xkam1 (\\d+)$"))
async def Xkam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/108")


@Client.on_callback_query(filters.regex("^Xkam2 (\\d+)$"))
async def Xkam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/109")


@Client.on_callback_query(filters.regex("^Xkam3 (\\d+)$"))
async def Xkam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/110")


@Client.on_callback_query(filters.regex("^Xkam4 (\\d+)$"))
async def Xkam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/111")


@Client.on_callback_query(filters.regex("^Xkam5 (\\d+)$"))
async def Xkam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/112")


@Client.on_callback_query(filters.regex("^Xkam6 (\\d+)$"))
async def Xkam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/113")


@Client.on_callback_query(filters.regex("^Xkam7 (\\d+)$"))
async def Xkam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/114")


@Client.on_callback_query(filters.regex("^Xkam8 (\\d+)$"))
async def Xkam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/115")


@Client.on_callback_query(filters.regex("^Xkam9 (\\d+)$"))
async def Xkam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/116")


@Client.on_callback_query(filters.regex("^Xkam10 (\\d+)$"))
async def Xkam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/117")


@Client.on_callback_query(filters.regex("^Xkam11 (\\d+)$"))
async def Xkam11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/118")


@Client.on_callback_query(filters.regex("^Xkam12 (\\d+)$"))
async def Xkam12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/119")


@Client.on_callback_query(filters.regex("^Xkam13 (\\d+)$"))
async def Xkam13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/120")


@Client.on_callback_query(filters.regex("^Xkam14 (\\d+)$"))
async def Xkam14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/121")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^marwan (\\d+)$"))
async def marwan(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("البوصله ضاعت 🎧", callback_data="Xmar1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ابطال 🎧", callback_data="Xmar2 " + str(m.from_user.id))],
        [InlineKeyboardButton("النظام 🎧", callback_data="Xmar3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شيراتون 🎧", callback_data="Xmar4 " + str(m.from_user.id))],
        [InlineKeyboardButton("خربت 🎧", callback_data="Xmar5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نهاية العالم 🎧", callback_data="Xmar6 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني مروان موسي\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xmar1 (\\d+)$"))
async def Xmar1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/24")


@Client.on_callback_query(filters.regex("^Xmar2 (\\d+)$"))
async def Xmar2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/25")


@Client.on_callback_query(filters.regex("^Xmar3 (\\d+)$"))
async def Xmar3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/26")


@Client.on_callback_query(filters.regex("^Xmar4 (\\d+)$"))
async def Xmar4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/27")


@Client.on_callback_query(filters.regex("^Xmar5 (\\d+)$"))
async def Xmar5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/28")


@Client.on_callback_query(filters.regex("^Xmar6 (\\d+)$"))
async def Xmar6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/29")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^mosaeed (\\d+)$"))
async def mosaeed(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("لو 🎧", callback_data="Xsaed1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جواكي 🎧", callback_data="Xsaed2 " + str(m.from_user.id))],
        [InlineKeyboardButton("متغير 🎧", callback_data="Xsaed3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بيني وبينك 🎧", callback_data="Xsaed4 " + str(m.from_user.id))],
        [InlineKeyboardButton("مش بحكي 🎧", callback_data="Xsaed5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وحدي لكن 🎧", callback_data="Xsaed6 " + str(m.from_user.id))],
        [InlineKeyboardButton("مفيش بديل 🎧", callback_data="Xsaed7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ياويلي 🎧", callback_data="Xsaed8 " + str(m.from_user.id))],
        [InlineKeyboardButton("بدون مواعيد 🎧", callback_data="Xsaed9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شتا 🎧", callback_data="Xsaed10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني محمد سعيد\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xsaed1 (\\d+)$"))
async def Xsaed1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/40")


@Client.on_callback_query(filters.regex("^Xsaed2 (\\d+)$"))
async def Xsaed2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/41")


@Client.on_callback_query(filters.regex("^Xsaed3 (\\d+)$"))
async def Xsaed3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/42")


@Client.on_callback_query(filters.regex("^Xsaed4 (\\d+)$"))
async def Xsaed4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/43")


@Client.on_callback_query(filters.regex("^Xsaed5 (\\d+)$"))
async def Xsaed5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/44")


@Client.on_callback_query(filters.regex("^Xsaed6 (\\d+)$"))
async def Xsaed6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/45")


@Client.on_callback_query(filters.regex("^Xsaed7 (\\d+)$"))
async def Xsaed7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/46")


@Client.on_callback_query(filters.regex("^Xsaed8 (\\d+)$"))
async def Xsaed8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/47")


@Client.on_callback_query(filters.regex("^Xsaed9 (\\d+)$"))
async def Xsaed9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/45")


@Client.on_callback_query(filters.regex("^Xsaed10 (\\d+)$"))
async def Xsaed8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/55")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^sahby (\\d+)$"))
async def sahby(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("هلا والله 🎧", callback_data="Xsahb1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("وداع يادنيا وداع 🎧", callback_data="Xsahb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("باتون ساليه 🎧", callback_data="Xsahb3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هاتلي فوديكا 🎧", callback_data="Xsahb4 " + str(m.from_user.id))],
        [InlineKeyboardButton("سكينه برازيلي 🎧", callback_data="Xsahb5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("انا حبيتك وجرحتيني 🎧", callback_data="Xsahb6 " + str(m.from_user.id))],
        [InlineKeyboardButton("انا بيكا ماي لاف 🎧", callback_data="Xsahb7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عالم فاسد 🎧", callback_data="Xsahb8 " + str(m.from_user.id))],
        [InlineKeyboardButton("رب الكون ميزنا 🎧", callback_data="Xsahb9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شمس المجره 🎧", callback_data="Xsahb10 " + str(m.from_user.id))],
        [InlineKeyboardButton("بنتخان 🎧", callback_data="Xsahb11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مساء النقص 🎧", callback_data="Xsahb12 " + str(m.from_user.id))],
        [InlineKeyboardButton("صاحبي دراعي 🎧", callback_data="Xsahb13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حب عمري نسيته وفاتني 🎧", callback_data="Xsahb14 " + str(m.from_user.id))],
        [InlineKeyboardButton("مساء النقص 🎧", callback_data="Xsahb15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("شارب المرار 🎧", callback_data="Xsahb16 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة الاغاني الشعبي\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xsahb1 (\\d+)$"))
async def Xsahb1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/49")


@Client.on_callback_query(filters.regex("^Xsahb2 (\\d+)$"))
async def Xsahb2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/50")


@Client.on_callback_query(filters.regex("^Xsahb3 (\\d+)$"))
async def Xsahb3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/51")


@Client.on_callback_query(filters.regex("^Xsahb4 (\\d+)$"))
async def Xsahb4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/52")


@Client.on_callback_query(filters.regex("^Xsahb5 (\\d+)$"))
async def Xsahb5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/53")


@Client.on_callback_query(filters.regex("^Xsahb6 (\\d+)$"))
async def Xsahb6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/54")


@Client.on_callback_query(filters.regex("^Xsahb7 (\\d+)$"))
async def Xsahb7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/55")


@Client.on_callback_query(filters.regex("^Xsahb8 (\\d+)$"))
async def Xsahb8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/56")


@Client.on_callback_query(filters.regex("^Xsahb9 (\\d+)$"))
async def Xsahb9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/57")


@Client.on_callback_query(filters.regex("^Xsahb10 (\\d+)$"))
async def Xsahb10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/58")


@Client.on_callback_query(filters.regex("^Xsahb11 (\\d+)$"))
async def Xsahb11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/59")


@Client.on_callback_query(filters.regex("^Xsahb12 (\\d+)$"))
async def Xsahb12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/60")


@Client.on_callback_query(filters.regex("^Xsahb13 (\\d+)$"))
async def Xsahb13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/61")


@Client.on_callback_query(filters.regex("^Xsahb14 (\\d+)$"))
async def Xsahb14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/62")


@Client.on_callback_query(filters.regex("^Xsahb15 (\\d+)$"))
async def Xsahb15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/63")


@Client.on_callback_query(filters.regex("^Xsahb16 (\\d+)$"))
async def Xsahb16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/64")


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^tamer (\\d+)$"))
async def tamer(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("مين ممكن 🎧", callback_data="Xtam1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("دا انا بابا 🎧", callback_data="Xtam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("كل ده علي ايه 🎧", callback_data="Xtam3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زي النيل 🎧", callback_data="Xtam4 " + str(m.from_user.id))],
        [InlineKeyboardButton("العقده 🎧", callback_data="Xtam5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نرجع 🎧", callback_data="Xtam6 " + str(m.from_user.id))],
        [InlineKeyboardButton("في الحياه 🎧", callback_data="Xtam7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حلو المكان 🎧", callback_data="Xtam8 " + str(m.from_user.id))],
        [InlineKeyboardButton("نفس الحنين 🎧", callback_data="Xtam9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لينا حياه بعدين 🎧", callback_data="Xtam10 " + str(m.from_user.id))],
        [InlineKeyboardButton("اختراع 🎧", callback_data="Xtam11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بالف سلامه 🎧", callback_data="Xtam12 " + str(m.from_user.id))],
        [InlineKeyboardButton("نفس النهايه 🎧", callback_data="Xtam13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قولني كلام 🎧", callback_data="Xtam14 " + str(m.from_user.id))],
        [InlineKeyboardButton("فجأه افترقنا 🎧", callback_data="Xtam15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("جرا اي يا عيني 🎧", callback_data="Xtam16 " + str(m.from_user.id))],
        [InlineKeyboardButton("ارجل 🎧", callback_data="Xtam17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("خونتك 🎧", callback_data="Xtam18 " + str(m.from_user.id))],
        [InlineKeyboardButton("بتصعب عليا نفسي 🎧", callback_data="Xtam19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("قلبي تعبان 🎧", callback_data="Xtam20 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني تامر حسني\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xtam1 (\\d+)$"))
async def Xtam1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/58")


@Client.on_callback_query(filters.regex("^Xtam2 (\\d+)$"))
async def Xtam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/59")


@Client.on_callback_query(filters.regex("^Xtam3 (\\d+)$"))
async def Xtam3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/60")


@Client.on_callback_query(filters.regex("^Xtam4 (\\d+)$"))
async def Xtam4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/61")


@Client.on_callback_query(filters.regex("^Xtam5 (\\d+)$"))
async def Xtam5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/62")


@Client.on_callback_query(filters.regex("^Xtam6 (\\d+)$"))
async def Xtam6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/63")


@Client.on_callback_query(filters.regex("^Xtam7 (\\d+)$"))
async def Xtam7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/64")


@Client.on_callback_query(filters.regex("^Xtam8 (\\d+)$"))
async def Xtam8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/65")


@Client.on_callback_query(filters.regex("^Xtam9 (\\d+)$"))
async def Xtam9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/66")


@Client.on_callback_query(filters.regex("^Xtam10 (\\d+)$"))
async def Xtam10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/67")


@Client.on_callback_query(filters.regex("^Xtam11 (\\d+)$"))
async def Xtam11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/68")


@Client.on_callback_query(filters.regex("^Xtam12 (\\d+)$"))
async def Xtam12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/69")


@Client.on_callback_query(filters.regex("^Xtam13 (\\d+)$"))
async def Xtam13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/70")


@Client.on_callback_query(filters.regex("^Xtam14 (\\d+)$"))
async def Xtam14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/71")


@Client.on_callback_query(filters.regex("^Xtam15 (\\d+)$"))
async def Xtam15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/73")


@Client.on_callback_query(filters.regex("^Xtam16 (\\d+)$"))
async def Xtam16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/74")


@Client.on_callback_query(filters.regex("^Xtam17 (\\d+)$"))
async def Xtam17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/75")


@Client.on_callback_query(filters.regex("^Xtam18 (\\d+)$"))
async def Xtam18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/76")


@Client.on_callback_query(filters.regex("^Xtam19 (\\d+)$"))
async def Xtam19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/77")


@Client.on_callback_query(filters.regex("^Xtam20 (\\d+)$"))
async def Xtam20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMusiiic/78")


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^wegzz (\\d+)$"))
async def wegzz(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("نصين 🎧", callback_data="Xweg1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("سكرتي 🎧", callback_data="Xweg2 " + str(m.from_user.id))],
        [InlineKeyboardButton("باظت 🎧", callback_data="Xweg3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("مش هقولك بيبي 🎧", callback_data="Xweg4 " + str(m.from_user.id))],
        [InlineKeyboardButton("خربان 🎧", callback_data="Xweg5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("كدا كدا 🎧", callback_data="Xweg6 " + str(m.from_user.id))],
        [InlineKeyboardButton("حواري 🎧", callback_data="Xweg7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اي تي ام 🎧", callback_data="Xweg8 " + str(m.from_user.id))],
        [InlineKeyboardButton("تي ان تي 🎧", callback_data="Xweg9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("دارت الغساله 🎧", callback_data="Xweg10 " + str(m.from_user.id))],
        [InlineKeyboardButton("علي راحتي 🎧", callback_data="Xweg11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لقطه 🎧", callback_data="Xweg12 " + str(m.from_user.id))],
        [InlineKeyboardButton("دورك جاي 🎧", callback_data="Xweg13 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="music2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{c.me.username}?startgroup=True")],

    ])
    await m.message.edit_text("◍ اختر ماتريد من قائمة اغاني ويجز\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^Xweg1 (\\d+)$"))
async def Xweg1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/9")


@Client.on_callback_query(filters.regex("^Xweg2 (\\d+)$"))
async def Xweg2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/10")


@Client.on_callback_query(filters.regex("^Xweg3 (\\d+)$"))
async def Xweg3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/11")


@Client.on_callback_query(filters.regex("^Xweg4 (\\d+)$"))
async def Xweg4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/12")


@Client.on_callback_query(filters.regex("^Xweg5 (\\d+)$"))
async def Xweg5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/13")


@Client.on_callback_query(filters.regex("^Xweg6 (\\d+)$"))
async def Xweg6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/14")


@Client.on_callback_query(filters.regex("^Xweg7 (\\d+)$"))
async def Xweg7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/15")


@Client.on_callback_query(filters.regex("^Xweg8 (\\d+)$"))
async def Xweg8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/16")


@Client.on_callback_query(filters.regex("^Xweg9 (\\d+)$"))
async def Xweg9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/17")


@Client.on_callback_query(filters.regex("^Xweg10 (\\d+)$"))
async def Xweg10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/18")


@Client.on_callback_query(filters.regex("^Xweg11 (\\d+)$"))
async def Xweg11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/19")


@Client.on_callback_query(filters.regex("^Xweg12 (\\d+)$"))
async def Xweg12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/20")


@Client.on_callback_query(filters.regex("^Xweg13 (\\d+)$"))
async def Xweg13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/22")
