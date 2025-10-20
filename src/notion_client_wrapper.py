from notion_client import Client
import os

def write_to_notion(problem, summary):
    notion = Client(auth=os.environ["NOTION_TOKEN"])
    database_id = os.environ["NOTION_DATABASE_ID"]

    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Problem": {"title": [{"text": {"content": problem["title"]}}]},
            "Difficulty": {"select": {"name": problem["difficulty"]}},
            "Language": {"rich_text": [{"text": {"content": problem["language"]}}]},
            "Status": {"select": {"name": problem["status"]}},
            "Summary": {"rich_text": [{"text": {"content": summary}}]},
        }
    )
