from openai import OpenAI
import os

def analyze_solution(code_snippet, title):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    prompt = f"""
    Analyze the following LeetCode solution:
    Problem: {title}
    Code:
    {code_snippet}

    Provide:
    1. Time and space complexity.
    2. One potential optimization.
    3. One key learning takeaway.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
