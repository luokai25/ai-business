#!/usr/bin/env python3
"""
Telegram Auto-Joiner - Run this on YOUR computer
Save as: telegram_auto.py
Run: pip install telethon && python3 telegram_auto.py
"""
from telethon import TelegramClient
import asyncio

# YOUR CREDENTIALS
API_ID = 32531259
API_HASH = "682286138a40699373735a68127f581f"
PHONE = "+2011553074208"

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(PHONE)
    
    print("✅ Logged in!")
    
    # Search and join business groups
    search_terms = [
        "small business owners",
        "entrepreneurs", 
        "digital marketing",
        "startups",
        "make money online"
    ]
    
    for term in search_terms:
        print(f"\n🔍 Searching: {term}")
        try:
            async for dialog in client.iter_dialogs():
                if dialog.is_group and term.lower() in dialog.title.lower():
                    print(f"   Found: {dialog.title}")
                    # Don't auto-join - just list for now
        except Exception as e:
            print(f"   Error: {e}")
    
    print("\n✅ Done! Check the list above.")
    print("Now you can join the groups you want!")

asyncio.run(main())
