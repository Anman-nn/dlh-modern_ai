#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

from bs4 import BeautifulSoup
import requests


def login_and_scrape(login_url, user, pwd):
    """def login_and_scrape(login_url, user, pwd):
    """
    session = requests.Session()

    response = session.get(login_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")

    payload = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }

    response = session.post(login_url, data=payload)
    response.raise_for_status()

    response = session.get("https://quotes.toscrape.com/")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

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

    return quotes
