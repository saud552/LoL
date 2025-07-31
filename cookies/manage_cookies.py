#!/usr/bin/env python3
"""
سكريبت إدارة ملفات الكوكيز
يستخدم لإدارة وتحديث ملفات الكوكيز للبوتات
"""

import os
import shutil
from datetime import datetime
from config import COOKIES_DIR, YOUTUBE_COOKIES_FILE, SPOTIFY_COOKIES_FILE, DEEZER_COOKIES_FILE

def check_cookies_exist():
    """فحص وجود ملفات الكوكيز"""
    files = {
        "YouTube (cookies1.txt)": YOUTUBE_COOKIES_FILE,
        # "Spotify (cookies2.txt)": SPOTIFY_COOKIES_FILE,  # إذا كنت تريد Spotify
        # "Deezer (cookies3.txt)": DEEZER_COOKIES_FILE     # إذا كنت تريد Deezer
    }
    
    print("🔍 فحص ملفات الكوكيز...")
    for service, file_path in files.items():
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {service}: موجود ({size} bytes)")
        else:
            print(f"❌ {service}: غير موجود")
    
    return files

def backup_cookies():
    """إنشاء نسخة احتياطية من ملفات الكوكيز"""
    backup_dir = os.path.join(COOKIES_DIR, "backup")
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"cookies_backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)
    
    files_to_backup = [
        YOUTUBE_COOKIES_FILE,
        # SPOTIFY_COOKIES_FILE,  # إذا كنت تريد Spotify
        # DEEZER_COOKIES_FILE     # إذا كنت تريد Deezer
    ]
    
    print(f"💾 إنشاء نسخة احتياطية في: {backup_path}")
    
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            filename = os.path.basename(file_path)
            backup_file = os.path.join(backup_path, filename)
            shutil.copy2(file_path, backup_file)
            print(f"✅ تم نسخ: {filename}")
    
    print("✅ تم إنشاء النسخة الاحتياطية بنجاح")

def validate_cookies_format():
    """التحقق من تنسيق ملفات الكوكيز"""
    print("🔍 التحقق من تنسيق ملفات الكوكيز...")
    
    files = [YOUTUBE_COOKIES_FILE]  # يمكنك إضافة المزيد إذا كنت تريد
    
    for file_path in files:
        if not os.path.exists(file_path):
            continue
            
        filename = os.path.basename(file_path)
        print(f"\n📄 فحص: {filename}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            if not lines:
                print(f"❌ {filename}: الملف فارغ")
                continue
                
            # فحص التنسيق الأساسي
            valid_lines = 0
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('\t')
                    if len(parts) >= 7:
                        valid_lines += 1
            
            print(f"✅ {filename}: {valid_lines} كوكيز صالح")
            
        except Exception as e:
            print(f"❌ {filename}: خطأ في القراءة - {e}")

def main():
    """الدالة الرئيسية"""
    print("🍪 إدارة ملفات الكوكيز")
    print("=" * 40)
    
    # فحص وجود الملفات
    check_cookies_exist()
    
    print("\n" + "=" * 40)
    
    # التحقق من التنسيق
    validate_cookies_format()
    
    print("\n" + "=" * 40)
    
    # إنشاء نسخة احتياطية
    response = input("هل تريد إنشاء نسخة احتياطية؟ (y/n): ")
    if response.lower() in ['y', 'yes', 'نعم']:
        backup_cookies()
    
    print("\n✅ تم الانتهاء من فحص ملفات الكوكيز")

if __name__ == "__main__":
    main()