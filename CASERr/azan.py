import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from datetime import datetime
import requests
import pytz
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
from pyrogram.errors import exceptions
from pyrogram.enums import ParseMode
from math import sqrt
from typing import Union
import random
from config import *
from config import user, dev, call, logger, logger_mode, botname, appp
from CASERr.daty import get_call, get_userbot, get_dev, get_logger
from CASERr.CASERr import get_channel, devchannel, source, caes, devgroup, devuser, group, casery, johned, photosource, caserid
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.exceptions import NoActiveGroupCall
from pyrogram.errors import ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant
from pyrogram import Client
from requests import Session
from requests import Response
from typing import Union
from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from pytz import timezone
import requests
from gtts import gTTS
import os


zone = timezone("Africa/Cairo")

s = Session()
@Client.on_message(filters.command(["مواقيت الصلاه"], ""), group=71198535)
async def sendAdhan(_: Client, message: Message) -> None:
    address: str = message.text.rsplit(maxsplit=1)[-1]
    if address in ["مواقيت صلاة", "مواقيت صلاه", "صلوات"]: return await message.reply_text("- اكتب اسم المنطقه بجانب الأمر،")
    adhan: Union[str, bool] = getAdhan(address)
    if not adhan: return await message.reply_text("- حدث خطأ أثناء جلب مواقيت الصلاة.")
    await message.reply_text(adhan)    


pnames: dict = {
    'Fajr': "الفجر", 
    'Sunrise': "الشروق", 
    'Dhuhr': "الظهر", 
    'Asr': "العصر",
    'Maghrib': "المغرب", 
    'Isha': "العشاء", 
    'Imsak': "الامساك",
    'Midnight': "منتصف الليل", 
    'Firstthird': "الثلث الأول من الليل", 
    'Lastthird': "الثلث الأخير من الليل"
}


def getAdhan(address: str) -> Union[str, bool]:
    method: int = 1
    params = {
        "address" : address,
        "method" : method, 
        "school" : 0
    }
    res: Response = s.get("http://api.aladhan.com/timingsByAddress", params=params)
    data: dict = res.json()
    if data["code"] != 200: return False
    data: dict = data["data"]
    timings: dict = data["timings"]
    date: dict = data["date"]["hijri"]
    date2: dict = data["date"]["gregorian"]
    month2: str = date2["month"]["en"]
    weekday: str = date["weekday"]["ar"] + " - " + date["weekday"]["en"]
    month: str = date["month"]["ar"] + " - " + date["month"]["en"]
    date: str = date["date"]
    date2: str = date2["date"]
    del timings['Sunset']
    next: str = getNext(timings)
    caption = f"- {next}\n"
    caption += f"- مواقيت الصلاة:"
    for prayer, time in timings.items():
        caption += f"\n    - {pnames[prayer]}: {time}"
    caption += f"\n\n- بـتـاريـخ: {date} (هـ) | {date2} (م)\n- يـوم: {weekday}\n- بـشـهـر: {month} (هـ) | {month2} (م)"
    return caption
    
    
def getNext(timings: dict) -> str:
    current_time = datetime.now(zone).strftime("%H:%M")
    next_prayer = None
    for prayer, time in timings.items():
        if current_time < time:
            next_prayer = prayer
            break
    if next_prayer is None: return "انتهت صلوات اليوم."
    next_prayer_time = datetime.strptime(timings[next_prayer], "%H:%M")
    current_time = datetime.strptime(current_time, "%H:%M")
    time_difference = next_prayer_time - current_time
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"متبقى على صلاة {pnames[next_prayer]} {hours} ساعه و {minutes} دقيقه."
    
cairo_timezone = pytz.timezone('Africa/Cairo')

azan_enabled_chats = []

prayer_stickers = {
    "الفجر": {"channel_username": "WORLED_CAESAR", "message_id": 349},
    "الظهر": {"channel_username": "WORLED_CAESAR", "message_id": 350},
    "العصر": {"channel_username": "WORLED_CAESAR", "message_id": 351},
    "المغرب": {"channel_username": "WORLED_CAESAR", "message_id": 352},
    "العشاء": {"channel_username": "WORLED_CAESAR", "message_id": 353},
}

@Client.on_message(filters.text & ~filters.private(), group=20)
async def handle_azan_command(c, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذان":
        if chat_id in azan_enabled_chats:
            await msg.reply_text("تنبيه الأذان مفعل هنا من قبل 😊♥️ ")
        else:
            azan_enabled_chats.append(chat_id)
            await msg.reply_text("تم تفعيل الاذان في هذه المحادثة بنجاح ♥️🌿")
    elif msg.text == "تعطيل الاذان":
        if chat_id in azan_enabled_chats:
            azan_enabled_chats.remove(chat_id)
            await msg.reply_text("تم الغاء تفعيل الاذان في هذه المحادثة بنجاح ♥️🌿")
        else:
            await msg.reply_text("تنبيه الأذان معطل هنا من قبل 😊♥️")

async def stop_azan(bot_username):
    hoss = await get_call(bot_username)
    for chat_id in azan_enabled_chats:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception as e:
            pass

async def play_azan(chat_id, bot_username, client):
    hoss = await get_call(bot_username)    
    azan_audio_path = "./Hossam/azan.mp3"
    stream = MediaStream(azan_audio_path)
    try:
        await hoss.join_group_call(
            chat_id,
            stream,
            stream_type=StreamType.PULSE_STREAM,
        )
    except NoActiveGroupCall:
        try:
            await hoss.join_assistant(chat_id, chat_id)
        except Exception as e:
            await client.send_message(chat_id, f"يرجي تشغيل المكالمه اولا..!🎧")
    except TelegramServerError:
        await client.send_message(chat_id, "عذرا هناك مشكلات في سيرفر التليجرام")
    except Exception as e:
        await stop_azan(bot_username)
        try:
            await hoss.join_group_call(
                chat_id,
                stream,
                stream_type=StreamType.PULSE_STREAM,
            )
        except Exception as e:
            await client.send_message(chat_id, f"الكول مش شغال مش هقدر اطلع أأذن 😔💔")

def get_prayer_time():
    try:
        prayer_times_response = requests.get("http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0").json()
        fajr_time = datetime.strptime(prayer_times_response['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
        dhuhr_time = datetime.strptime(prayer_times_response['data']['timings']['Dhuhr'], '%H:%M').strftime('%I:%M %p')
        asr_time = datetime.strptime(prayer_times_response['data']['timings']['Asr'], '%H:%M').strftime('%I:%M %p')
        maghrib_time = datetime.strptime(prayer_times_response['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
        isha_time = datetime.strptime(prayer_times_response['data']['timings']['Isha'], '%H:%M').strftime('%I:%M %p')
        
        current_time = datetime.now(cairo_timezone).strftime('%I:%M %p')

        if current_time == fajr_time:
            return "الفجر"
        elif current_time == dhuhr_time:
            return "الظهر"
        elif current_time == asr_time:
            return "العصر"
        elif current_time == maghrib_time:
            return "المغرب"
        elif current_time == isha_time:
            return "العشاء"
    except Exception as e:
        print(e)
        return None

async def send_prayer_message(app, chat_id, prayer_name):
    message = f"حان الآن موعد أذان {prayer_name} 🕊❤"
    
    await app.send_message(chat_id, message)

    sticker_info = prayer_stickers[prayer_name]
    channel_username = sticker_info["channel_username"]
    message_id = sticker_info["message_id"]
    
    sticker_message = await app.get_messages(channel_username, message_id)
    sticker_file_id = sticker_message.sticker.file_id
    
    await app.send_sticker(chat_id, sticker_file_id)

async def azan(bot_username):
    app = appp[bot_username]
    while True:
        prayer_name = get_prayer_time()
        if prayer_name:
            await stop_azan(bot_username)
            for chat_id in azan_enabled_chats:
                await send_prayer_message(app, chat_id, prayer_name)
                await play_azan(chat_id, bot_username, app)
            await asyncio.sleep(177)
        await asyncio.sleep(60)

    asyncio.create_task(azan(bot_username))

azkar_ses = [] 

@Client.on_message(filters.text & ~filters.private(), group=220)
async def azkar_command(c, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذكار الصوتيه":
        if chat_id in azkar_ses:
            await msg.reply_text("تنبيه الاذكار مفعله هنا من قبل 😊♥️")
        else:
            azkar_ses.append(chat_id)
            await msg.reply_text("تم تفعيل الاذكار الصوتيه بنجاح 🤍")
    elif msg.text == "تعطيل الاذكار الصوتيه":
        if chat_id in azkar_ses:
            azkar_ses.remove(chat_id)
            await msg.reply_text("تم تعطيل الاذكار الصوتيه بنجاح 🤍")
        else:
            await msg.reply_text("الاذكار الصوتيه معطله بالفعل في هذه المجموعة")

async def stop_azkar(bot_username):
    hoss = await get_call(bot_username)
    for chat_id in azkar_ses:
        try:
            await hoss.leave_group_call(chat_id)
        except Exception as e:
            pass

async def play_azkar(chat_id, bot_username, client):
    hoss = await get_call(bot_username)    
    azan_audio_path = "./Hossam/saly.mp3"
    stream = MediaStream(azan_audio_path)
    try:
        await hoss.join_group_call(
            chat_id,
            stream,
            stream_type=StreamType.PULSE_STREAM,
        )
    except NoActiveGroupCall:
        try:
            await hoss.join_assistant(chat_id, chat_id)
        except Exception as e:
            await client.send_message(chat_id, f"يرجي تشغيل المكالمه اولا..!🎧")
    except TelegramServerError:
        await client.send_message(chat_id, "عذرا هناك مشكلات في سيرفر التليجرام")
    except Exception as e:
        await stop_azan(bot_username)
        try:
            await hoss.join_group_call(
                chat_id,
                stream,
                stream_type=StreamType.PULSE_STREAM,
            )
        except Exception as e:
            await client.send_message(chat_id, f"يرجي تشغيل المكالمه اولا..!🎧")

async def azkar(bot_username):
    app = appp[bot_username]
    while True:
        await stop_azkar(bot_username)
        for chat_id in azkar_ses:
            await play_azkar(chat_id, bot_username, app)
        await asyncio.sleep(600)
    asyncio.create_task(azkar(bot_username))    
    
azkar_chat = [] 

@Client.on_message(filters.text & filters.group, group=2220)
async def azkar_comm55and(c, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذكار":
        if chat_id in azkar_chat:
            await msg.reply_text("الاذكار مفعل بالفعل في هذه المجموعة")
        else:
            azkar_chat.append(chat_id)
            await msg.reply_text("تم تفعيل الاذكار بنجاح 🤍")
    elif msg.text == "تعطيل الاذكار":
        if chat_id in azkar_chat:
            azkar_chat.remove(chat_id)
            await msg.reply_text("تم تعطيل الاذكار بنجاح 🤍")
        else:
            await msg.reply_text("الاذكار معطله في هذه المجموعة")

xt = ["لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
                     "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
                     "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
                     "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "سبحان الله وبحمده سبحان الله العظيم🌸",
                     "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
                     "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
                     "استغفر الله العظيم وأتوبُ إليه 🌹",
                     "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
                     "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
                     "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
                     "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
                     "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
                     "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
                     "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
                     "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
                     "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
                     "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
                     "استغفر الله العظيم وأتوبُ إليه.",
                     "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
                     " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
                     "ماتستغفر ربنا كده🥺❤️",
                     "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
                     "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
                     "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
                     "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
                     "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
                     "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
                     "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
                     "أصبحنا وأصبح الملك لله ولا اله الا الله.",
                     "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
                     "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
                     "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
                     "- اللهم القبول الذي لا يزول ❤️🍀.",
                     "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
                     "سبحان الله وبحمده ،سبحان الله العظيم.",
                     "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
                     " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
                     "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
                     "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
                     "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
                     "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
                     "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
                     "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
                     "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
                     "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
                     "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت ??💜.",
                     "- وبك أصبحنا يا عظيم الشأن ??❤️.",
                     "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
                     "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
                     "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
                     "صلي على النبي بنيه الفرج❤️",
                     "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
                     "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
                     "لا اله الا الله سيدنا محمد رسول الله🌿💜",
                     "قول معايا - استغفر الله استفر الله استغفر الله -",
                     "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
                     "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
                     "صلي على محمد❤️",
                     "ماتيجو نقرء الفاتحه سوا🥺"]
async def azkar_chatt(bot_username):
    app = appp[bot_username]
    while True:
        for chat_id in azkar_chat:
            a = random.choice(xt)
            await app.send_message(chat_id, a)
        await asyncio.sleep(600)
    asyncio.create_task(azkar_chatt(bot_username))    

nday_chattm = [] 

@Client.on_message(filters.text & filters.group, group=207380)
async def nday_chattm54(c, msg):
    chat_id = msg.chat.id
    if msg.text in ["تفعيل النداء","فتح النداء","تفعيل الندائ","فتح الندائ","تفعيل المنشن التلقائي"]:
        if chat_id in nday_chattm:
            await msg.reply_text("النداء مفعل بالفعل في هذه المجموعة")
        else:
            nday_chattm.append(chat_id)
            await msg.reply_text("تم تفعيل النداء بنجاح 🤍")
    elif msg.text in ["تعطيل النداء","قفل النداء","تعطيل الندائ","قفل الندائ","تعطيل المنشن التلقائي"]:
        if chat_id in nday_chattm:
            nday_chattm.remove(chat_id)
            await msg.reply_text("تم تعطيل النداء بنجاح🤍")
        else:
            await msg.reply_text("النداء معطل بالفعل في هذه المجموعة")
                     
async def nday_catt(bot_username):
    app = appp[bot_username]
    while True:
        for chat_id in nday_chattm:
            members = []
            async for member in app.get_chat_members(chat_id):
                if not member.user.is_bot:
                    members.append(member)
            random_member = random.choice(members)
            random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
            random_message = random.choice([
                f"بقلنا ساعه مستنينك فينك 😾 {random_member_mention}",
                f"• يـا قمـري ❤️‍🔥 {random_member_mention}",
                f"حبيبي لي م بتتكلم معنا 🤔 {random_member_mention}",
                f"• يـا تفاحه 🍏 فينك {random_member_mention}",
                f"• هو انت لي قمر كده 🌚♥ {random_member_mention}"
                f"• ويــن طامــس يحـلــو : {random_member_mention}"
                f"• الأشياء معك لها طعم آخر بنكهة الحب 🤍 {random_member_mention}"
                f"• مشتاقيـن حــب وينڪ : {random_member_mention}"
                f"• أجمل وجهات النظر هي النظر لوجهك ♥️. {random_member_mention}"
                f"• أنـتِ مسائي وأجمـل مسـاء, وأنا مع كـل مسـاء أحـبـك . 💕 {random_member_mention}"
                f"مشتهين عسل؟ {random_member_mention}"
                f"حياة المشاهير صعبه بس وحشتنى : {random_member_mention}"
                f"وش الشي الي تفكر فيه الحين ؟ {random_member_mention}"
                f"هل تفضلين الزواج عن حب أم زواج الصالونات؟ {random_member_mention}"
                f"ستبقي أنت أهم وأول أمنياتي في هذه الحياة مهما زادت طموحاتي 💜 {random_member_mention}"
                f"عرفناا عنك؟ {random_member_mention}"
                f"لست أمام عيوني لكن كل يوم أراك  🍂 {random_member_mention}"
                f"أحبتتك لدرجة كبيرة جداً ، فلا تغيب عني أبداً ، فعند غيابك تغيب كل الأشياء معك. 💐! {random_member_mention}"
                f"الثلج يكون بمثابة الهدية للشتاء، والشمس تكون كالهدية للصيف، والزهور هدية الربيع ، وأنت هديتي طوال العمر. 🧡 {random_member_mention}"
                f"وكأن حديثك موسيّقى هادئة ينصت لها قلبي 💜 {random_member_mention}"
            ])
            try:
              await app.send_message(chat_id, random_message)
            except Exception as e:
             print(e)            
        await asyncio.sleep(600)
    asyncio.create_task(azkar_catt(bot_username))    
                    