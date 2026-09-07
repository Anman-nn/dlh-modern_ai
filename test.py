#!/usr/bin/env python3
"""Data Collection - Web Scraping
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_products(url):
    '''def scrape_products(url):'''
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
            title = card.find_element(By.CSS_SELECTOR, 'a.title').get_attribute('title')
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
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
products = scrape_products(url)
try:
    products = scrape_products(url)
    output = ""
    for i, q in enumerate(products):
        output += f"Product #{i}:\n{q}\n"
    print(output)
except Exception as e:
    print(str(e))