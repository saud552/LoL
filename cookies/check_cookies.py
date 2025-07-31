#!/usr/bin/env python3
"""
فحص حالة ملفات الكوكيز
"""

import os
import sys

def check_cookies_status():
    """فحص حالة جميع ملفات الكوكيز"""
    cookies_dir = "/workspace/cookies"
    
    print("🍪 فحص ملفات الكوكيز")
    print("=" * 50)
    
    if not os.path.exists(cookies_dir):
        print("❌ مجلد الكوكيز غير موجود")
        return
    
    cookie_files = []
    
    # البحث عن ملفات الكوكيز
    for file in os.listdir(cookies_dir):
        if file.endswith('.txt') and 'cookie' in file.lower():
            file_path = os.path.join(cookies_dir, file)
            size = os.path.getsize(file_path)
            cookie_files.append((file, file_path, size))
    
    if not cookie_files:
        print("❌ لم يتم العثور على ملفات كوكيز")
        return
    
    print(f"📁 تم العثور على {len(cookie_files)} ملف كوكيز:")
    print()
    
    valid_count = 0
    
    for filename, filepath, size in cookie_files:
        status = "✅ صالح" if size > 100 else "❌ فارغ/غير صالح"
        if size > 100:
            valid_count += 1
        
        print(f"📄 {filename}")
        print(f"   الحجم: {size} بايت")
        print(f"   الحالة: {status}")
        
        # فحص المحتوى
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'example_value' in content:
                    print(f"   ⚠️  يحتوي على قيم تجريبية (example_value)")
                elif '.youtube.com' in content:
                    print(f"   ✅ يحتوي على كوكيز YouTube")
                else:
                    print(f"   ❓ محتوى غير معروف")
        except Exception as e:
            print(f"   ❌ خطأ في قراءة الملف: {e}")
        
        print()
    
    print("=" * 50)
    print(f"📊 الإحصائيات:")
    print(f"   إجمالي الملفات: {len(cookie_files)}")
    print(f"   الملفات الصالحة: {valid_count}")
    print(f"   الملفات غير الصالحة: {len(cookie_files) - valid_count}")
    
    if valid_count == 0:
        print("\n⚠️  تحذير: لا توجد ملفات كوكيز صالحة!")
        print("يجب عليك إضافة كوكيز حقيقية لملفات الكوكيز")
    elif valid_count < 2:
        print("\n⚠️  تحذير: عدد قليل من ملفات الكوكيز الصالحة")
        print("يُنصح بإضافة المزيد من ملفات الكوكيز للتدوير")
    else:
        print("\n✅ ممتاز! لديك ملفات كوكيز كافية للتدوير")

def show_usage_instructions():
    """عرض تعليمات الاستخدام"""
    print("\n📖 كيفية الحصول على كوكيز YouTube:")
    print("=" * 50)
    print("1. افتح متصفح Chrome أو Firefox")
    print("2. اذهب إلى YouTube وتسجيل الدخول")
    print("3. اضغط F12 لفتح أدوات المطور")
    print("4. اذهب إلى تبويب Application/Storage")
    print("5. ابحث عن Cookies > https://youtube.com")
    print("6. انسخ الكوكيز المهمة مثل:")
    print("   - VISITOR_INFO1_LIVE")
    print("   - LOGIN_INFO")
    print("   - SID")
    print("   - HSID")
    print("   - SSID")
    print("7. استبدل 'example_value' بالقيم الحقيقية")

if __name__ == "__main__":
    check_cookies_status()
    show_usage_instructions()