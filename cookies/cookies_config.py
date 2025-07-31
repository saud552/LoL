#!/usr/bin/env python3
"""
ملف تكوين مرن لملفات الكوكيز
يمكنك تغيير أسماء الملفات هنا حسب ما تريد
"""

import os

# مجلد الكوكيز
COOKIES_DIR = "/workspace/cookies"

# أسماء ملفات الكوكيز - يمكنك تغييرها حسب ما تريد
COOKIES_NAMES = {
    "youtube": "cookies1.txt",      # يمكنك تغييرها إلى أي اسم تريده
    "spotify": "cookies2.txt",      # إذا كنت تريد Spotify
    "deezer": "cookies3.txt",       # إذا كنت تريد Deezer
    "custom1": "my_cookies.txt",    # ملف كوكيز مخصص
    "custom2": "backup_cookies.txt" # ملف كوكيز احتياطي
}

# مسارات كاملة لملفات الكوكيز
COOKIES_PATHS = {
    service: os.path.join(COOKIES_DIR, filename)
    for service, filename in COOKIES_NAMES.items()
}

# الملفات المستخدمة حالياً في البوت
ACTIVE_COOKIES = {
    "youtube": COOKIES_PATHS["youtube"],  # ملف YouTube الرئيسي
    # "spotify": COOKIES_PATHS["spotify"],  # إذا كنت تريد Spotify
    # "deezer": COOKIES_PATHS["deezer"],    # إذا كنت تريد Deezer
}

def get_cookies_path(service="youtube"):
    """الحصول على مسار ملف الكوكيز للخدمة المطلوبة"""
    return ACTIVE_COOKIES.get(service)

def list_available_cookies():
    """عرض جميع ملفات الكوكيز المتاحة"""
    print("📁 ملفات الكوكيز المتاحة:")
    for service, path in COOKIES_PATHS.items():
        status = "✅ موجود" if os.path.exists(path) else "❌ غير موجود"
        print(f"  {service}: {COOKIES_NAMES[service]} - {status}")

def create_cookies_template():
    """إنشاء قوالب لملفات الكوكيز"""
    templates = {
        "youtube": """# Netscape HTTP Cookie File
# ملف كوكيز YouTube
# استبدل example_value بالقيم الحقيقية من متصفحك

.youtube.com	TRUE	/	FALSE	1735689600	VISITOR_INFO1_LIVE	example_value
.youtube.com	TRUE	/	FALSE	1735689600	LOGIN_INFO	example_value
.youtube.com	TRUE	/	FALSE	1735689600	SID	example_value
.youtube.com	TRUE	/	FALSE	1735689600	HSID	example_value
.youtube.com	TRUE	/	FALSE	1735689600	SSID	example_value""",
        
        "spotify": """# Netscape HTTP Cookie File
# ملف كوكيز Spotify
# استبدل example_value بالقيم الحقيقية من متصفحك

.spotify.com	TRUE	/	FALSE	1735689600	sp_t	example_value
.spotify.com	TRUE	/	FALSE	1735689600	sp_dc	example_value
.spotify.com	TRUE	/	FALSE	1735689600	sp_key	example_value""",
        
        "deezer": """# Netscape HTTP Cookie File
# ملف كوكيز Deezer
# استبدل example_value بالقيم الحقيقية من متصفحك

.deezer.com	TRUE	/	FALSE	1735689600	dzr_uniq_id	example_value
.deezer.com	TRUE	/	FALSE	1735689600	dzr_consent	example_value
.deezer.com	TRUE	/	FALSE	1735689600	dzr_analytics	example_value"""
    }
    
    for service, template in templates.items():
        if service in COOKIES_NAMES:
            file_path = COOKIES_PATHS[service]
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(template)
                print(f"✅ تم إنشاء قالب: {COOKIES_NAMES[service]}")

if __name__ == "__main__":
    print("🍪 إعداد ملفات الكوكيز")
    print("=" * 40)
    
    # إنشاء مجلد الكوكيز
    os.makedirs(COOKIES_DIR, exist_ok=True)
    
    # عرض الملفات المتاحة
    list_available_cookies()
    
    print("\n" + "=" * 40)
    
    # إنشاء قوالب
    response = input("هل تريد إنشاء قوالب لملفات الكوكيز؟ (y/n): ")
    if response.lower() in ['y', 'yes', 'نعم']:
        create_cookies_template()
    
    print("\n✅ تم الانتهاء من الإعداد")