import asyncio
import os
import sys
import random
from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from bot import *
from pyromod import listen

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_zombiebot())