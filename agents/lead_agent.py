#!/usr/bin/env python3
"""
Lead Generation Agent
Finds and qualifies leads for all income streams
"""
import random
from datetime import datetime

# Lead sources
SOURCES = [
    "Telegram Groups",
    "Facebook Groups", 
    "LinkedIn",
    "Twitter",
    "Instagram",
    "Cold Email",
    "Referrals"
]

# Lead qualifications
QUALIFICATIONS = [
    "Budget Confirmed",
    "Need Identified",
    "Timeline Set",
    "Decision Maker",
    "Ready to Buy"
]

def find_leads():
    """Find potential leads"""
    leads = []
    niches = [
        "Salon & Spa",
        "Restaurant",
        "Retail Store",
        "E-commerce",
        "Real Estate",
        "Fitness Gym",
        "Medical Practice",
        "Law Firm"
    ]
    
    statuses = ["New", "Contacted", "Qualified", "Proposal", "Negotiation"]
    
    for i in range(10):
        lead = {
            "id": i + 1,
            "name": f"{random.choice(['John', 'Sarah', 'Mike', 'Lisa', 'David', 'Emma'])} {random.choice(['Smith', 'Johnson', 'Brown', 'Wilson', 'Davis'])}",
            "business": f"{random.choice(niches)} Business",
            "location": random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Miami", "London", "Dubai"]),
            "source": random.choice(SOURCES),
            "status": random.choice(statuses),
            "budget": f"${random.randint(100, 2000)}/mo",
            "need": random.choice(["AI客服", "自动化", "Lead Gen", "Marketing", "Website"]),
            "score": random.randint(5, 10),
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        leads.append(lead)
    
    return leads

def qualify_lead(lead):
    """Qualify a lead"""
    score = lead["score"]
    
    if score >= 8:
        return "Hot - Close within 1 week"
    elif score >= 6:
        return "Warm - Close within 1 month"
    else:
        return "Cold - Nurture"

def create_outreach_message(lead, channel="telegram"):
    """Create outreach message for lead"""
    
    telegram_msg = f"""Hi {lead['name'].split()[0]}! 👋

I help businesses like yours automate with AI - handling customer support, scheduling, and emails 24/7.

Would you be interested in a free demo? 

Best,
AI Assistant"""

    email_msg = f"""Subject: Free AI Demo for Your {lead['business']}

Hi {lead['name'].split()[0]},

I help {lead['business']} owners save 10+ hours/week through AI automation.

Quick question: What's your biggest time-waster right now?

I'd love to show you how AI can help.

Book a time: [Link]

Best,
Luo Kai"""

    messages = {
        "telegram": telegram_msg,
        "email": email_msg,
        "whatsapp": telegram_msg  # Same as telegram for now
    }
    
    return messages.get(channel, telegram_msg)

def generate_lead_report():
    """Generate lead generation report"""
    leads = find_leads()
    
    report = {
        "total_leads": len(leads),
        "by_status": {},
        "by_source": {},
        "by_budget": {},
        "hot_leads": [],
        "action_items": []
    }
    
    # Aggregate by status
    for lead in leads:
        status = lead["status"]
        source = lead["source"]
        budget = lead["budget"]
        
        report["by_status"][status] = report["by_status"].get(status, 0) + 1
        report["by_source"][source] = report["by_source"].get(source, 0) + 1
        report["by_budget"][budget] = report["by_budget"].get(budget, 0) + 1
        
        if lead["score"] >= 8:
            report["hot_leads"].append(lead)
    
    # Action items
    hot_count = len(report["hot_leads"])
    report["action_items"] = [
        f"Follow up with {hot_count} hot leads today",
        "Add 5 new leads from Telegram groups",
        "Send outreach to 10 cold leads",
        "Schedule demos for qualified leads"
    ]
    
    return report

def run_lead_agent():
    """Main lead generation agent"""
    print("🎯 Running Lead Generation Agent...")
    
    report = generate_lead_report()
    
    print(f"\n📊 Lead Report:")
    print(f"   Total Leads: {report['total_leads']}")
    print(f"   Hot Leads: {len(report['hot_leads'])}")
    
    print(f"\n📈 By Status:")
    for status, count in report["by_status"].items():
        print(f"   {status}: {count}")
    
    print(f"\n🔥 Top Leads to Contact:")
    for lead in report["hot_leads"][:3]:
        print(f"   - {lead['name']} ({lead['business']}) - {lead['budget']}")
    
    print(f"\n✅ Action Items:")
    for item in report["action_items"]:
        print(f"   • {item}")
    
    return report

if __name__ == "__main__":
    run_lead_agent()
