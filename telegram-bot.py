#!/usr/bin/env python3
"""
Telegram AI Business Assistant Bot
"""
import requests
import json

BOT_TOKEN = "8049158564:AAF79Q0ZSKkwZ1ewjTpynXLMjvQHvm8ZBAk"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Knowledge base
RESPONSES = {
    "price": "💰 Our AI Assistant starts at $0/mo for basic and $199/mo for pro. Contact us for custom solutions!",
    "pricing": "💰 Our AI Assistant starts at $0/mo for basic and $199/mo for pro. Contact us for custom solutions!",
    "cost": "💰 Our AI Assistant starts at $0/mo for basic and $199/mo for pro. Contact us for custom solutions!",
    "service": "🤖 We offer: Customer Support, Scheduling, Email Management, Data Processing, Lead Generation - all automated 24/7!",
    "services": "🤖 We offer: Customer Support, Scheduling, Email Management, Data Processing, Lead Generation - all automated 24/7!",
    "what": "🤖 We offer AI automation for businesses - handles customer support, scheduling, emails, and more 24/7!",
    "help": "🙋 I can help you with pricing, services, or connect you with a human. What do you need?",
    "contact": "📞 To talk to a human: @luokai25",
    "hello": "👋 Hey! Need help with AI for your business? Just ask!",
    "hi": "👋 Hey! Need help with AI for your business? Just ask!",
    "website": "🌐 Check us out: https://scintillating-cocada-354a69.netlify.app",
    "ai": "🤖 We're an AI business automation company - we help businesses automate customer support, scheduling, and more!",
    "automation": "⚙️ We automate: Customer Support, Scheduling, Emails, Data Entry, Lead Gen - 24/7!",
    "automation": "⚙️ We automate: Customer Support, Scheduling, Emails, Data Entry, Lead Gen - 24/7!",
}

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=data)

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    return requests.get(url, params=params).json()

def process_message(update):
    msg = update.get("message", {})
    text = msg.get("text", "").lower()
    chat_id = msg.get("chat", {}).get("id")
    
    if not text or not chat_id:
        return
    
    # Check for keywords
    for key, response in RESPONSES.items():
        if key in text:
            send_message(chat_id, response)
            return
    
    # Default response
    send_message(chat_id, "👋 Thanks for reaching out! For pricing or inquiries, visit: https://scintillating-cocada-354a69.netlify.app\n\nOr contact @luokai25")

def main():
    print("🤖 Bot starting...")
    offset = None
    while True:
        try:
            result = get_updates(offset)
            if result.get("ok"):
                updates = result.get("result", [])
                for update in updates:
                    offset = update["update_id"] + 1
                    process_message(update)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
