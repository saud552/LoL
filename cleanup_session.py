#!/usr/bin/env python3
"""
سكريبت تنظيف جلسة البوت لحل مشاكل Peer ID
"""

import os
import time
import schedule

def clean_session_files():
    """تنظيف ملفات الجلسة القديمة"""
    try:
        session_files = [f for f in os.listdir('.') if f.endswith('.session')]
        for session_file in session_files:
            file_age = time.time() - os.path.getmtime(session_file)
            # حذف الملفات الأقدم من 7 أيام
            if file_age > 7 * 24 * 3600:
                os.remove(session_file)
                print(f"✅ تم حذف ملف الجلسة القديم: {session_file}")
        
        # تنظيف ملفات المؤقتة
        temp_files = [f for f in os.listdir('.') if f.endswith(('.jpg', '.mp3', '.m4a', '.webp', '.tmp'))]
        for temp_file in temp_files:
            try:
                os.remove(temp_file)
                print(f"🧹 تم حذف الملف المؤقت: {temp_file}")
            except:
                pass
                
        print("✨ تم تنظيف النظام بنجاح")
        
    except Exception as e:
        print(f"❌ خطأ في التنظيف: {e}")

if __name__ == "__main__":
    clean_session_files()