#!/usr/bin/env python3
"""
Telegram AI Lead Bot - Full Version
"""
import requests
import json

BOT_TOKEN = "8049158564:AAF79Q0ZSKkwZ1ewjTpynXLMjvQHvm8ZBAk"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
ADMIN_CHAT_ID = "7877343272"

# Lead capture
leads = []

def send_message(chat_id, text, keyboard=None):
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if keyboard:
        data["reply_markup"] = keyboard
    requests.post(url, json=data)

def notify_admin(lead_info):
    msg = f"🎯 NEW LEAD!\n\n{lead_info}"
    send_message(ADMIN_CHAT_ID, msg)

def get_leadKeyboard():
    return {
        "inline_keyboard": [
            [{"text": "💰 Get Pricing", "callback_data": "pricing"}],
            [{"text": "🤖 View Services", "callback_data": "services"}],
            [{"text": "📞 Contact Human", "callback_data": "contact"}]
        ]
    }

# Responses
RESPONSES = {
    "pricing": """💰 **Pricing**

**Starter (FREE)**
- 10 hrs/month
- Basic support

**Growth ($199/mo)**
- 40 hrs/month
- Priority support
- Custom integrations

**Enterprise ($499/mo)**
- Unlimited hours
- 24/7 support
- Dedicated manager

Want to proceed? Click below! 👇""",

    "services": """🤖 **Our Services**

• Customer Support (24/7)
• Scheduling & Calendar
• Email Management
• Data Processing
• E-commerce Operations
• Lead Generation
• Market Research

All powered by AI! Want details? 👇""",

    "contact": """📞 **Contact**

Talk to a human: @luokai25

Or visit: https://scintillating-cocada-354a69.netlify.app""",

    "start": """👋 **Welcome!**

I help businesses automate with AI.

What would you like?
👇 Choose below:""",

    "default": """👋 Hi! I help businesses with AI automation.

Choose an option:"""
}

def handle_callback(callback):
    chat_id = callback["from"]["id"]
    data = callback["data"]
    
    if data == "pricing":
        send_message(chat_id, RESPONSES["pricing"], get_leadKeyboard())
        notify_admin(f"User asked about pricing: {chat_id}")
    elif data == "services":
        send_message(chat_id, RESPONSES["services"], get_leadKeyboard())
    elif data == "contact":
        send_message(chat_id, RESPONSES["contact"])
        notify_admin(f"User wants to contact: {chat_id}")

def handle_message(msg):
    text = msg.get("text", "").lower()
    chat = msg.get("chat", {})
    chat_id = chat.get("id")
    chat_type = chat.get("type")
    
    # Only respond in private chats or if mentioned
    if chat_type != "private":
        # Check if bot was mentioned or it's a keyword
        keywords = ["ai", "automation", "help", "service", "price", "cost", "business"]
        if any(k in text for k in keywords):
            if "price" in text or "cost" in text or "how much" in text:
                send_message(chat_id, RESPONSES["pricing"], get_leadKeyboard())
            elif "service" in text or "what do you do" in text:
                send_message(chat_id, RESPONSES["services"], get_leadKeyboard())
            elif "contact" in text or "human" in text:
                send_message(chat_id, RESPONSES["contact"])
            else:
                send_message(chat_id, RESPONSES["default"], get_leadKeyboard())
        return
    
    # Private chat
    if "/start" in text:
        send_message(chat_id, RESPONSES["start"], get_leadKeyboard())
    elif "price" in text or "cost" in text:
        send_message(chat_id, RESPONSES["pricing"], get_leadKeyboard())
        notify_admin(f"Price inquiry: {chat_id}")
    elif "service" in text:
        send_message(chat_id, RESPONSES["services"], get_leadKeyboard())
    elif "contact" in text or "human" in text:
        send_message(chat_id, RESPONSES["contact"])
    else:
        send_message(chat_id, RESPONSES["default"], get_leadKeyboard())

def main():
    print("🤖 Lead Bot Running...")
    offset = None
    while True:
        try:
            url = f"{BASE_URL}/getUpdates"
            params = {"timeout": 30}
            if offset:
                params["offset"] = offset
            resp = requests.get(url, params=params).json()
            if resp.get("ok"):
                for update in resp.get("result", []):
                    offset = update["update_id"] + 1
                    if "callback_query" in update:
                        handle_callback(update["callback_query"])
                    elif "message" in update:
                        handle_message(update["message"])
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
