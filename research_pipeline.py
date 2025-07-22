print("[research_pipeline.py loaded]")

# research_pipeline.py

from formatter import format_guest_profile
from scraper import scrape_search_summary, scrape_website_summary
from question_gen import generate_questions
from summarizer import summarize_guest_profile
from bio_generator import generate_guest_bio
from pdf_creator import create_pdf


def build_guest_profile(guest_name, guest_url):
    print("[build_guest_profile called]")
    raw_info = {
        "guest_name": guest_name,
        "url": guest_url,
    }
    profile = format_guest_profile(raw_info)

    query = f"{profile['guest_name']} {profile['company']}".strip()
    profile['search_results'] = scrape_search_summary(query)

    website_url = profile['socials'].get("website") or guest_url
    profile['company_summary'] = scrape_website_summary(website_url) if website_url else ""

    profile['insight_summary'] = summarize_guest_profile(profile)
    profile['bio'] = generate_guest_bio(profile)
    profile['draft_questions'] = generate_questions(profile)

    return profile


def export_guest_profile(profile, output_path):
    create_pdf(profile, output_path)
