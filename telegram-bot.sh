#!/bin/bash
# Telegram Bot Auto-Responder

BOT_TOKEN="8049158564:AAF79Q0ZSKkwZ1ewjTpynXLMjvQHvm8ZBAk"
GROUP_ID="-1003709163740"

# Welcome message
curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
  -H "Content-Type: application/json" \
  -d "{\"chat_id\": \"${GROUP_ID}\", \"text\": \"👋 Welcome! I'm your AI Business Assistant.\", \"parse_mode\": \"Markdown\"}"

echo "Bot activated in group!"
