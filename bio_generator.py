from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_guest_bio(profile):
    prompt = f"Write a short professional bio for {profile['guest_name']} based on their company ({profile['company']}) and this context:\n\n{profile['company_summary']}\n"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
