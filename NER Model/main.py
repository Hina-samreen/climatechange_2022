# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

chrome_webdriver_path = "/Users/hinasamreen/PycharmProjects/climatechange/chromedriver"
driver = webdriver.Chrome(chrome_webdriver_path)
driver.get("https://climate.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2C+created_at+desc&search"
           "=&category=19%2C98")
driver.implicitly_wait(6)
# Getting the articles


articles = driver.find_element(by=By.CLASS_NAME, value="item_list ")


article_URLS = [link.get_attribute("href") for link in articles.find_elements_by_css_selector(".content_title a")]


articles_teaser_body = [teaser.text for teaser in articles.find_elements_by_class_name("article_teaser_body")]

articles_date = [date.text for date in articles.find_elements_by_class_name("list_text")]

data_dict = {"Dates": articles_date, "Title_articles": articles_teaser_body + article_URLS}

print(len(articles_date), len(article_URLS), len(articles_teaser_body), len(articles_teaser_body + article_URLS))

data_frame = pd.DataFrame(data_dict)

data_frame.to_csv("Articles related to climate change in NASA_new.csv")

driver.quit()
