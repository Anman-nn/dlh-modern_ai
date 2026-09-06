#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

import json
fetch_html = __import__('0-fetch_html').fetch_html
from bs4 import BeautifulSoup


def extract_jsonld(url):
    '''def extract_jsonld(url):'''
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    blocks = soup.find_all("script", type="application/ld+json")
    for block in blocks:
        data = json.loads(block.get_text())

        if isinstance(data, dict):
            items = [data]
        else:
            items = data

        for item in items:
            if item.get("@type") == "Quote":
                keywords = item.get("keywords", [])

                if isinstance(keywords, str):
                    tags = [tag.strip() for tag in keywords.split(",")]
                else:
                    tags = keywords

                quotes.append({
                    "text": item.get("text"),
                    "author": item.get("author", {}).get("name"),
                    "tags": tags
                })

    return quotes
