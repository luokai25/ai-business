#!/usr/bin/env python3
"""
Simple Telegram Client using requests (no pip install needed)
"""
import requests
import time

API_ID = "32531259"
API_HASH = "682286138a40699373735a68127f581f"
PHONE = "+2011553074208"

# We'll use the bot API which is already working
BOT_TOKEN = "8049158564:AAF79Q0ZSKkwZ1ewjTpynXLMjvQHvm8ZBAk"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, json=data)

# Test
send_message("7877343272", "✅ Telethon not available, but bot is working! Add me to groups to start getting leads!")

print("Bot is working! Add it to groups!")
