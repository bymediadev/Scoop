# question_gen.py

def generate_questions(profile):
    name = profile.get("guest_name", "the guest")
    company = profile.get("company", "")
    summary = profile.get("company_summary", "")
    socials = profile.get("socials", {})
    topics = profile.get("topics", [])

    questions = []

    # Icebreaker
    questions.append(f"{name}, can you tell us a bit about your journey and what inspired you to start {company}?")

    # Company/Product
    if company:
        questions.append(f"What’s the core mission of {company}, and how do you differentiate yourselves in the market?")

    # Website summary insight
    if summary:
        questions.append(f"I read that {summary[:150]}... Can you elaborate on that and how it shapes your strategy?")

    # Social media / digital presence
    if socials.get("linkedin") or socials.get("twitter"):
        questions.append("How has your online presence influenced your business growth or personal brand?")

    # Topics — if you later add research-based topic extraction, can customize further
    for topic in topics[:3]:
        questions.append(f"Let’s dive into {topic}. How has that impacted your work?")

    # Reflection
    questions.append("Looking back, what’s one lesson you wish you’d learned earlier in your entrepreneurial journey?")

    # Fundraising / Team / Challenges (add as needed)
    questions.append("What are the biggest challenges your team faces today, and how are you tackling them?")

    return questions

if __name__ == "__main__":
    import json
    # For quick testing
    with open("sample_profile.json", "r") as f:
        profile = json.load(f)

    qs = generate_questions(profile)
    print("\nGenerated Questions:\n")
    for q in qs:
        print(f"- {q}")
