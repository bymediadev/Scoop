import requests
import os  # also needed if you use os.getenv()

print("[scraper.py LOADED]")

def scrape_website_summary(url):
    print("[scrape_website_summary FUNCTION FOUND]")
    ...

def scrape_search_summary(query, num_results=5):
    """
    Search using SerpAPI, return a list of dicts with title, snippet, and url.
    Requires environment variable SERPAPI_API_KEY to be set.
    """
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise ValueError("SERPAPI_API_KEY environment variable not set.")

    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": num_results,
    }
    url = "https://serpapi.com/search"
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    results = []
    organic_results = data.get("organic_results", [])
    for r in organic_results[:num_results]:
        results.append({
            "title": r.get("title"),
            "snippet": r.get("snippet") or r.get("snippet_highlighted", ""),
            "url": r.get("link"),
        })
    return results
