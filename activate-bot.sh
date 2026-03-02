#!/bin/bash
# Telegram Bot Activation Script

BOT_TOKEN="8049158564:AAF79Q0ZSKkwZ1ewjTpynXLMjvQHvm8ZBAk"
GROUP_ID="-1003709163740"

curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\": \"${GROUP_ID}\", \"text\": \"✅ Bot is now active! Need AI for your business? Ask me anything!\"}"

echo "Bot ready!"
