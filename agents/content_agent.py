#!/usr/bin/env python3
"""
Content Creation Agent
Creates posts, ads, and content for all platforms
"""
import random

# Content templates
POST_TEMPLATES = {
    "twitter": [
        "🤖 {hook}\n\n{body}\n\n{cta}\n\n{hashtags}",
        "💡 {hook}\n\n{body}\n\n{link}",
    ],
    "instagram": [
        "📸 {hook}\n\n{body}\n\n👇 {cta}\n\n{hashtags}",
    ],
    "facebook": [
        "🚀 {hook}\n\n{body}\n\n{cta}\n\n#AI #Automation #Business",
    ]
}

def create_twitter_post(service_or_product):
    """Create a Twitter/X post"""
    hooks = [
        "Just launched! 🎉",
        "Stop wasting time on...",
        "What if you could automate this?",
        "Game changer alert! 🚀",
        "Finally, something that works!"
    ]
    
    bodies = {
        "ai_assistant": "Our AI handles customer support, scheduling, and emails - 24/7. While you sleep.",
        "dropshipping": "Find winning products in minutes. Our AI researches Amazon for you.",
        "affiliate": "Earn passive income promoting products you love. Here's how...",
    }
    
    ctas = [
        "Learn more 👉 [link]",
        "DM me for details!",
        "Check the link in bio",
        "Book a call → [link]"
    ]
    
    hook = random.choice(hooks)
    body = bodies.get(service_or_product, "Amazing product you need!")
    cta = random.choice(ctas)
    hashtags = "#AI #Automation #Business #Tech #Innovation"
    
    return f"🤖 {hook}\n\n{body}\n\n{cta}\n\n{hashtags}"

def create_instagram_post(service_or_product):
    """Create an Instagram post"""
    hooks = [
        "✨ NEW!",
        "🎯 PRODUCTS THAT SELL",
        "💰 SIDE HUSTLE ALERT"
    ]
    
    return f"{random.choice(hooks)}\n\n{descriptions[service_or_product]}\n\n👇 DM for more info!\n\n#AI #Business #Entrepreneur #SideHustle #Automation #Tech"

def create_facebook_post(service_or_product):
    """Create a Facebook post"""
    return f"""🚀 {headlines[service_or_product]}

{description[service_or_product]}

💬 Drop a comment if you want to know more!

#AI #Automation #SmallBusiness #Entrepreneur #DigitalMarketing"""

# Product/service descriptions
descriptions = {
    "ai_assistant": "AI that handles your customer support, scheduling, and emails - 24/7. Stop doing repetitive work. Start scaling your business.",
    "dropshipping": "Find winning products in minutes with AI-powered research. Amazon, eBay, Etsy - we analyze them all.",
    "affiliate": "Earn 20-50% commission promoting products. We give you the products, ads, and tracking.",
}

headlines = {
    "ai_assistant": "This AI Assistant Works While You Sleep",
    "dropshipping": "AI-Powered Product Research That Finds Winners",
    "affiliate": "Turn Your Social Media Into Passive Income",
}

def generate_content_calendar():
    """Generate a week's content calendar"""
    calendar = []
    platforms = ["Twitter", "Instagram", "Facebook", "LinkedIn"]
    topics = ["ai_assistant", "dropshipping", "affiliate"]
    
    for day in range(7):
        post = {
            "day": day + 1,
            "platform": random.choice(platforms),
            "topic": random.choice(topics),
            "content": create_twitter_post(random.choice(topics))
        }
        calendar.append(post)
    
    return calendar

def run_content_agent():
    """Main content agent"""
    print("✍️ Running Content Creation Agent...")
    
    print("\n📱 Twitter Posts:")
    for topic in ["ai_assistant", "dropshipping", "affiliate"]:
        print(f"\n--- {topic} ---")
        print(create_twitter_post(topic)[:200] + "...")
    
    print("\n📸 Instagram:")
    print(create_instagram_post("ai_assistant")[:200] + "...")
    
    print("\n📘 Facebook:")
    print(create_facebook_post("ai_assistant")[:200] + "...")
    
    print("\n📅 This Week's Content Calendar:")
    calendar = generate_content_calendar()
    for post in calendar:
        print(f"Day {post['day']}: {post['platform']} - {post['topic']}")

if __name__ == "__main__":
    run_content_agent()
