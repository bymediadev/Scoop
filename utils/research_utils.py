import os
import re
from dotenv import load_dotenv
import openai

# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_guest_profile(name, url, debug=False):
    if not OPENAI_API_KEY:
        return {
            "bio": "",
            "company": "",
            "insight": "",
            "questions": [],
            "error": "OpenAI API key not set."
        }

    prompt = f"""
You are a podcast research assistant. Create a structured guest profile for the guest named "{name}" using context from the provided URL: {url}.

Return these sections clearly and explicitly:
Bio:
Company Summary:
Insight Summary:
Generated Questions:

Format each section with clear section headers. Provide at least 3 custom podcast questions based on the insight.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=750
        )
        text = response.choices[0].message.content.strip()

        if debug:
            print("=== Prompt Sent ===")
            print(prompt)
            print("=== GPT Response ===")
            print(text)

        sections = {
            "bio": "",
            "company": "",
            "insight": "",
            "questions": [],
            "error": ""
        }

        def extract_section(label, text):
            match = re.search(rf"{label}[:\-\n]*\s*(.+?)(?=\n[A-Z][a-z]+(?:\sSummary)?:|\Z)", text, re.DOTALL | re.IGNORECASE)
            return match.group(1).strip() if match else ""

        sections["bio"] = extract_section("Bio", text)
        sections["company"] = extract_section("Company Summary", text)
        sections["insight"] = extract_section("Insight Summary", text)

        questions = re.findall(r"(?:^|\n)[\d\-•]+\s+(.*?)(?=\n[\d\-•]|\n[A-Z][a-z]|\Z)", text, re.DOTALL)
        sections["questions"] = [q.strip() for q in questions if q.strip()]

        return sections

    except Exception as e:
        return {
            "bio": "",
            "company": "",
            "insight": "",
            "questions": [],
            "error": f"Error: {e}"
        }
