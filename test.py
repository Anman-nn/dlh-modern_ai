#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    '''def scrape_product_detail(url, delay=2.0)'''
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")            # modern headless mode
    options.add_argument("--window-size=1920,1080")   # real desktop viewport
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    product = {}
    try:
        driver.get(url)
        time.sleep(delay)
        card = driver.find_element("class name", "caption")

        h4s = card.find_elements("css selector", "h4")
        price = h4s[0].text
        title = h4s[1].text
        description = card.find_element(
            "css selector", "p.description"
        ).text
        rating = len(driver.find_elements(
            "css selector",
            ".ws-icon.ws-icon-star"
        ))

        product = {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }

    finally:
        driver.quit()

    return product



url = "https://webscraper.io/test-sites/e-commerce/static/product/32"
detail = scrape_product_detail(url)
print(f"Product details: {detail}")