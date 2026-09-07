#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

import time
from selenium import webdriver


def scrape_products(url):
    '''def scrape_products(url):'''
    By = webdriver.common.by.By
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")            # modern headless mode
    options.add_argument("--window-size=1920,1080")   # real desktop viewport
    options.add_argument("--no-sandbox")              # needed in many containers
    options.add_argument("--disable-dev-shm-usage")   # avoid /dev/shm crashes in Docker

    driver = webdriver.Chrome(options=options)
    products = []
    try:
        driver.get(url)
        time.sleep(1)
        cards = driver.find_elements(By.CLASS_NAME, 'thumbnail')

        for card in cards:
            title = card.find_element(By.CSS_SELECTOR, 'a.title').get_attribute(
                'title')
            price = card.find_element(By.CSS_SELECTOR, 'h4.price').text
            description = card.find_element(
                By.CSS_SELECTOR,
                "p.description"
            ).text
            rating = card.find_element(
                By.CSS_SELECTOR,
                ".ratings p[data-rating]"
            ).get_attribute("data-rating")

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })

    finally:
        driver.quit()

    return products
