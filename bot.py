from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"985612253")
ch = "AAAKP" 
OWNER_USERNAME = "AAAKP"
ST = "AAAKP"
LT = "AAAKP"
DEVS = []
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "𝐷𝑟. 𝐾ℎ𝑎𝑦𝑎𝑙 𓏺"

bot_token="7305811865:AAF_PKkBWEUw-QdLg1ee5Xp7oksTG6XGK8c"
bot_token2="كود جلسه بايروجرام "


bot = Client("ITA", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
