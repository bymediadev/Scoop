def get_guest_info():
    print("Enter guest details:")
    name = input("Full Name: ").strip()
    company = input("Company Name: ").strip()
    linkedin = input("LinkedIn URL (optional): ").strip()
    twitter = input("Twitter/X URL (optional): ").strip()
    website = input("Personal/Company Website (optional): ").strip()

    return {
        "guest_name": name,
        "company": company,
        "socials": {
            "linkedin": linkedin or None,
            "twitter": twitter or None,
            "website": website or None
        }
    }
