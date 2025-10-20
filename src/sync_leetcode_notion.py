import os
from leetcode_client import fetch_recent_problems
from chatgpt_client import analyze_solution
from notion_client_wrapper import write_to_notion

def run_sync(limit=5):
    problems = fetch_recent_problems(limit)
    for p in problems:
        print(f"Processing {p['title']}...")
        summary = analyze_solution(p["code"], p["title"])
        write_to_notion(p, summary)
        print(f"✔ Synced {p['title']}")

if __name__ == "__main__":
    limit = int(os.getenv("INPUT_LIMIT", "5"))
    run_sync(limit)
