#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

from bs4 import BeautifulSoup
import time
from urllib import parse
fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    '''paginated'''
    quotes = []
    url = base_url

    while url:
        html = fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")

        for quote_block in soup.find_all("div", class_="quote"):
            text = quote_block.find("span", class_="text").get_text()
            author = quote_block.find("small", class_="author").get_text()
            tags = [
                tag.get_text()
                for tag in quote_block.find_all("a", class_="tag")
            ]

            quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })

        next_link = soup.select_one("li.next a")

        if next_link is None:
            url = None
        else:
            url = parse.urljoin(url, next_link.get("href"))
            time.sleep(0.1)

    return quotes
