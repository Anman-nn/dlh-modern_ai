#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    '''API'''
    page_num = 1
    has_next = True
    quotes = []
    while has_next:
        comb_url = base_url + '/api/quotes?page=' + str(page_num)
        page_num += 1
        page = fetch_html(comb_url)
        data = json.loads(page)
        has_next = data['has_next']

        for quote_block in data['quotes']:
            quotes.append({
                "text": quote_block['text'],
                "author": quote_block['author']['name'],
                "tags": quote_block['tags']})
    return quotes
