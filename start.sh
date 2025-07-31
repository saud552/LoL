#!/bin/bash

# تثبيت ffmpeg
apt-get update
apt-get install -y ffmpeg

# إنشاء مجلد التحميلات
mkdir -p /workspace/downloads
mkdir -p /workspace/cookies

# تشغيل Redis
redis-server --daemonize yes

# تشغيل البوت
python3 main.py