# How to Make Me Join Groups Automatically

## Option 1: Run This Script on Your Computer

1. Install Python: https://python.org/downloads
2. Open terminal/command prompt
3. Run:
```bash
pip install telethon
```

4. Save the code below as `telegram_auto.py`

5. Run:
```bash
python3 telegram_auto.py
```

6. Enter the login code sent to your Telegram

---

## The Code (telegram_auto.py):

```python
from telethon import TelegramClient
import asyncio

API_ID = 32531259
API_HASH = "682286138a40699373735a68127f581f"
PHONE = "+2011553074208"

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(PHONE)
    print("✅ Logged in!")
    
    # Get your groups
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            print(f"Group: {dialog.title}")
            print(f"   Invite: t.me/{dialog.entity.username}" if dialog.entity.username else "")
    
    # Join specific group
    # await client.join_chat("link_or_username")

asyncio.run(main())
```

---

## Option 2: Ask Me About Specific Groups

Tell me the exact name or link of groups you want to join, and I'll try to find them!

What groups do you want me to join?
