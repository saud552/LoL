import asyncio
from pytgcalls import idle
import os
import sys
import random
import asyncio
import redis, re
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import user, dev, call, logger, logger_mode, botname, appp
from bot import bot_id

API_ID = int("8186557")
API_HASH = "efd77b34c69c164ce158037ff5a0d117"

r = redis.Redis(
    host="127.0.0.1",
    port=6379,)

def add_Bots(bots):
    if is_Bots(bots):
        return
    r.sadd(f"maker{bot_id}", str(bots))

async def get_devss(bot_username: str) -> int:
    dev_id = dev.get(bot_username)
    if not dev_id:
        for x in get_Bots():
            if x[0] == bot_username:
                dev_id = x[1]
                dev[bot_username] = dev_id
                break
    if dev_id is None:
        raise ValueError(f"لم يتم العثور على معرف المالك للبوت: {bot_username}")
    return int(dev_id)

def is_Bots(bots):
    try:
        a = get_Bots()
        if bots in a:
            return True
        return False
    except:
        return False

def del_Bots(bots):
    if not is_Bots(bots):
        return False
    r.srem(f"maker{bot_id}", str(bots))

def get_Bots():
    try:
        lst = []
        for a in r.smembers(f"maker{bot_id}"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []
        
async def get_dev(bot_username):
  dev_id = dev.get(bot_username)
  if not dev_id:
   for x in get_Bots():
    if x[0] == bot_username:
     dev_id = x[1]
     dev[bot_username] = dev_id
     return dev_id
  return dev_id

async def get_logger(bot_username):
  logg = logger.get(bot_username)
  if not logg:
   for x in get_Bots():
    if x[0] == bot_username:
     logg = x[4]
     logger[bot_username] = logg
     return logg
  return logg
  
async def get_owner_id(client):
    bot_username = client.me.username
    for x in get_Bots():
        if x[0] == bot_username:
            owner_id = x[1]
            dev[bot_username] = owner_id
            return int(owner_id)
            
async def get_userbot(bot_username):
  userbot = user.get(bot_username)
  if not userbot:
   for x in get_Bots():
    if x[0] == bot_username:
     SESSION = x[3]
     userbot = Client("CASER", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
     user[bot_username] = userbot
     return userbot
  return userbot

async def del_userbot(bot_username):
    if bot_username in user:
        del user[bot_username]
        print(f"تم حذف {bot_username} بنجاح.")
    else:
        print(f"{bot_username} غير موجود في التخزين.")
  
async def del_call(bot_username):
    if bot_username in call:
        del call[bot_username]
        print(f"تم حذف {bot_username} بنجاح.")
    else:
        print(f"{bot_username} غير موجود في التخزين.")
  
async def get_call(bot_username):
  calll = call.get(bot_username)
  if not calll:
   for x in get_Bots():
    if x[0] == bot_username:
     userbot = await get_userbot(bot_username)
     calo = PyTgCalls(userbot, cache_duration=100)
     await calo.start()
     call[bot_username] = calo
     return calo
  return calll  
  