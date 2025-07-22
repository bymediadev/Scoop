from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_guest_profile(profile):
    context = f"""
    Guest Name: {profile['guest_name']}
    Company: {profile['company']}
    Website Summary: {profile['company_summary']}
    Search Results: {"; ".join([r['snippet'] for r in profile['search_results']])}
    """
    prompt = f"Summarize this for a podcast host to understand the guest:\n{context[:3000]}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
