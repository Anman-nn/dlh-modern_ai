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
        quotes.extend(scrape_basic(url))
        html = fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")
        next_li = soup.find("li", class_="next")

        if next_li:
            next_link = next_li.find("a")

        if next_link is None:
            url = None
        else:
            href = next_link.get("href")
            url = parse.urljoin(url, href)
            time.sleep(1)

    return quotes
