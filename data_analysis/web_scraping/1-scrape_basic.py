#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    '''basic'''
    html = fetch_html(url)

    soup = BeautifulSoup(html, "html.parser")
    quotes = []
    for quote_block in soup.find_all("div", class_="quote"):
        text = quote_block.find("span", class_="text").get_text()
        author = quote_block.find("small", class_="author").get_text()

        tags = [tag.get_text()
            for tag in quote_block.find_all("a", class_="tag")]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags})
    return quotes
