#!/usr/bin/env python3
"""
MASTER AGENT CONTROLLER
Runs all income agents in parallel
"""
import subprocess
import threading
import time
import json
from datetime import datetime

# Agent scripts
AGENTS = {
    "dropshipping": "money-maker/agents/dropshipping_agent.py",
    "affiliate": "money-maker/agents/affiliate_agent.py", 
    "content": "money-maker/agents/content_agent.py",
    "leads": "money-maker/agents/lead_agent.py"
}

def run_agent(agent_name, script_path):
    """Run a single agent"""
    print(f"\n{'='*50}")
    print(f"🤖 Starting {agent_name.upper()} Agent...")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(
            ["python3", script_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
    except Exception as e:
        print(f"Error running {agent_name}: {e}")

def run_all_agents_parallel():
    """Run all agents in parallel"""
    print("🚀 STARTING ALL AGENTS IN PARALLEL...")
    print(f"Time: {datetime.now()}")
    print("=" * 60)
    
    threads = []
    
    for agent_name, script_path in AGENTS.items():
        t = threading.Thread(target=run_agent, args=(agent_name, script_path))
        t.start()
        threads.append(t)
    
    # Wait for all to complete
    for t in threads:
        t.join()
    
    print("\n" + "=" * 60)
    print("✅ ALL AGENTS COMPLETED!")
    print("=" * 60)

def run_all_agents_sequential():
    """Run all agents one by one"""
    print("🚀 STARTING ALL AGENTS SEQUENTIALLY...")
    print(f"Time: {datetime.now()}")
    
    for agent_name, script_path in AGENTS.items():
        run_agent(agent_name, script_path)
        time.sleep(1)  # Brief pause between agents
    
    print("\n✅ ALL AGENTS COMPLETED!")

# Main execution
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--parallel":
        run_all_agents_parallel()
    else:
        run_all_agents_sequential()
