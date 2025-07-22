def format_guest_profile(raw_data):
    return {
        "guest_name": raw_data.get("guest_name"),
        "title": "",
        "company": raw_data.get("company"),
        "company_summary": "",
        "bio": "",
        "socials": raw_data.get("socials", {}),
        "recent_posts": [],
        "news_mentions": [],
        "notable_appearances": [],
        "topics": [],
        "draft_questions": {
            "icebreaker": "",
            "product": "",
            "fundraising": "",
            "team": "",
            "reflection": ""
        }
    }
