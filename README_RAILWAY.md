# 🚀 دليل النشر على Railway

## 📋 المتطلبات

### 1. حساب على Railway
- اذهب إلى [railway.app](https://railway.app)
- سجل حساب جديد أو سجل دخول

### 2. متغيرات البيئة المطلوبة

#### متغيرات Telegram:
```
BOT_TOKEN=7305811865:AAF_PKkBWEUw-QdLg1ee5Xp7oksTG6XGK8c
API_ID=8186557
API_HASH=efd77b34c69c164ce158037ff5a0d117
OWNER_ID=985612253
OWNER_USERNAME=AAAKP
```

#### متغيرات Redis (اختياري):
```
REDIS_URL=redis://localhost:6379
```

#### متغيرات أخرى:
```
DOWNLOAD_FOLDER=/workspace/downloads
COOKIES_DIR=/workspace/cookies
```

## 🚀 خطوات النشر

### 1. رفع الكود إلى GitHub
```bash
git add .
git commit -m "إعداد Railway"
git push origin main
```

### 2. ربط المشروع بـ Railway
1. اذهب إلى [railway.app](https://railway.app)
2. اضغط على "New Project"
3. اختر "Deploy from GitHub repo"
4. اختر مستودعك
5. اضغط "Deploy Now"

### 3. إعداد متغيرات البيئة
1. في لوحة تحكم Railway
2. اذهب إلى "Variables" tab
3. أضف المتغيرات المطلوبة أعلاه

### 4. إعداد Redis (اختياري)
1. في Railway، اضغط "New Service"
2. اختر "Redis"
3. انسخ رابط Redis وأضفه كمتغير `REDIS_URL`

### 5. تشغيل البوت
- البوت سيعمل تلقائياً بعد النشر
- يمكنك مراقبة السجلات في "Deployments" tab

## 📁 هيكل الملفات المطلوبة

```
├── railway.json          # تكوين Railway
├── Procfile             # أمر التشغيل
├── runtime.txt          # إصدار Python
├── requirements.txt     # المكتبات المطلوبة
├── start.sh            # سكريبت التشغيل
├── config.py           # إعدادات البوت
├── main.py             # نقطة البداية
└── bot.py              # إعدادات البوت
```

## 🔧 استكشاف الأخطاء

### مشاكل شائعة:

1. **خطأ في تثبيت المكتبات:**
   - تأكد من صحة `requirements.txt`
   - تحقق من سجلات البناء

2. **خطأ في متغيرات البيئة:**
   - تأكد من إضافة جميع المتغيرات المطلوبة
   - تحقق من صحة القيم

3. **خطأ في Redis:**
   - تأكد من تشغيل خدمة Redis
   - تحقق من صحة `REDIS_URL`

4. **خطأ في Telegram:**
   - تأكد من صحة `BOT_TOKEN`
   - تحقق من `API_ID` و `API_HASH`

## 📊 مراقبة الأداء

- استخدم "Metrics" tab لمراقبة استخدام الموارد
- تحقق من "Logs" tab لمراقبة السجلات
- استخدم "Deployments" tab لمراقبة النشرات

## 🔄 التحديثات

لتحديث البوت:
```bash
git add .
git commit -m "تحديث البوت"
git push origin main
```

سيتم النشر التلقائي على Railway.

## 💡 نصائح

1. **استخدم متغيرات البيئة** بدلاً من القيم الثابتة
2. **راقب استخدام الموارد** لتجنب تجاوز الحد المجاني
3. **احتفظ بنسخة احتياطية** من الكود
4. **اختبر البوت** قبل النشر النهائي

## 🆘 الدعم

إذا واجهت مشاكل:
1. تحقق من سجلات Railway
2. تأكد من صحة متغيرات البيئة
3. تحقق من توافق الكود مع Railway
4. راجع هذا الدليل مرة أخرى