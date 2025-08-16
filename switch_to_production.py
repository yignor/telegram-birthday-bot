#!/usr/bin/env python3
"""
Скрипт для переключения на продакшн настройки
"""

import os
import shutil

def switch_to_production():
    """Переключает на продакшн настройки"""
    print("🔄 Переключение на продакшн настройки...")
    
    # Создаем .env файл с продакшн настройками
    env_content = """# Продакшн настройки
BOT_TOKEN=7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw
CHAT_ID=-1001535261616

# Тестовые настройки (для тестирования функционала)
TEST_BOT_TOKEN=7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw
TEST_CHAT_ID=-15573582

# Google Sheets настройки
SPREADSHEET_ID=1evCO5a8q3w4EP9ydbVfDr92u_w33Mcq1B4Wt9q-9bkA
ANNOUNCEMENTS_TOPIC_ID=your_topic_id_here
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Продакшн настройки установлены!")
        print("   BOT_TOKEN: 7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw")
        print("   CHAT_ID: -1001535261616")
        print("   TEST_BOT_TOKEN: 7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw")
        print("   TEST_CHAT_ID: -15573582")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def switch_to_test():
    """Переключает на тестовые настройки"""
    print("🔄 Переключение на тестовые настройки...")
    
    # Создаем .env файл с тестовыми настройками
    env_content = """# Тестовые настройки (активные)
BOT_TOKEN=7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw
CHAT_ID=-15573582

# Продакшн настройки (неактивные)
PROD_BOT_TOKEN=7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw
PROD_CHAT_ID=-1001535261616

# Google Sheets настройки
SPREADSHEET_ID=1evCO5a8q3w4EP9ydbVfDr92u_w33Mcq1B4Wt9q-9bkA
ANNOUNCEMENTS_TOPIC_ID=your_topic_id_here
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Тестовые настройки установлены!")
        print("   BOT_TOKEN: 7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw")
        print("   CHAT_ID: -15573582")
        print("   PROD_BOT_TOKEN: 7772125141:AAHqFYGm3I6MW516aCq3K0FFjK2EGKk0wtw")
        print("   PROD_CHAT_ID: -1001535261616")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def show_current_settings():
    """Показывает текущие настройки"""
    print("📋 Текущие настройки:")
    
    try:
        with open('.env', 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("❌ Файл .env не найден")
    except Exception as e:
        print(f"❌ Ошибка чтения: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "prod" or command == "production":
            switch_to_production()
        elif command == "test":
            switch_to_test()
        elif command == "show" or command == "current":
            show_current_settings()
        else:
            print("❌ Неизвестная команда")
            print("Использование:")
            print("  python switch_to_production.py prod    - переключиться на продакшн")
            print("  python switch_to_production.py test    - переключиться на тест")
            print("  python switch_to_production.py show    - показать текущие настройки")
    else:
        print("🔄 Переключение на продакшн настройки...")
        switch_to_production()
