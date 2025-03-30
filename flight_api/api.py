from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

def get_airline_name(code):
    driver = webdriver.Chrome()
    driver.get("https://www.iata.org/en/publications/directories/code-search/")
    search_input = driver.find_element("name", "airline.search")
    search_input.send_keys(code)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "td[data-heading='Company name']")
    airline_name = result.text.strip()
    return airline_name
