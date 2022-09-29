import time

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')
chrome_webdriver_path = "/Users/hinasamreen/PycharmProjects/climatechange/chromedriver"

# First website
driver2 = webdriver.Chrome(chrome_webdriver_path, options=options)

driver2.get("https://www.natureandculture.org/news/")
driver2.implicitly_wait(3)
# Getting the articles
more_button1 = driver2.find_element(by=By.XPATH, value="//li[@class='active']")

print(more_button1.text)

driver2.implicitly_wait(3)

records2 = []

time.sleep(3)
results3 = driver2.find_elements(by=By.TAG_NAME, value="article")
print(results3.__len__())


def display_articles():
    page_source_1 = driver2.page_source
    soup1 = BeautifulSoup(page_source_1, 'html.parser')
    results2 = soup1.findAll('article')
    print(results2.__len__())
    for result_new in results2:
        date2 = result_new.find('time', class_='entry-time').text
        url2 = result_new.find('a', class_='entry-title-link')['href']
        teaser2 = result_new.find('a', class_='entry-title-link').text
        # teaser2 = result_new.find('div', class_='entry-content').text
        records2.append((date2, teaser2.strip(), url2))


time.sleep(3)

more_button1 = driver2.find_element(by=By.XPATH, value="//li[@class='active']//following-sibling::li//a")
more_button1.text
next_button = driver2.find_element(by=By.XPATH, value="//li[@class='pagination-next']")
i = 2
while next_button.is_displayed():
    try:
        time.sleep(3)
        display_articles()
        time.sleep(3)
        more_button1 = driver2.find_element(by=By.XPATH, value="//li[@class='active']//following-sibling::li//a")
        print(next_button.is_enabled())
        print(more_button1.text)
        print(next_button.text)
        more_button1.click()
        time.sleep(3)
        next_button = driver2.find_element(by=By.XPATH, value="//li[@class='pagination-next']")
    except NoSuchElementException:
        display_articles()
        print("except block is displayed")
        break

# second website
driver2.get("https://climate.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2C+created_at+desc&search"
            "=&category=19%2C98")
driver2.implicitly_wait(4)
# Getting the articles

more_button = driver2.find_element(by=By.XPATH, value="//footer[@class='list_footer more_button']//a")

i = 0

while i < 60:
    if more_button.is_displayed():
        more_button.click()
        i = i + 1
        time.sleep(1)

driver2.implicitly_wait(3)
page_source = driver2.page_source

soup = BeautifulSoup(page_source, 'html.parser')
results = soup.findAll('li', class_='slide')
print(len(results))

for result in results:
    date = result.find('div', class_='list_date').text
    url = result.find_next('a')['href']
    teaser = result.find('div', class_='article_teaser_body').text
    title = teaser.strip()
    records2.append((date, title, url))

# third website
options1 = webdriver.ChromeOptions()
options1 = webdriver.ChromeOptions()
options1.add_argument('--incognito')

driver = webdriver.Chrome(chrome_webdriver_path, options=options1)
driver.get("https://www.greenpeace.org/international/?s=&orderby=post_date&f%5Btag%5D%5BClimate%5D=89")

driver.implicitly_wait(3)

time.sleep(3)
SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(3)

button = driver.find_element(by=By.XPATH,
                             value="//button[@class='btn btn-secondary more-btn btn-load-more-click-scroll']")

while button.is_displayed():
    button = driver.find_element(by=By.XPATH,
                                 value="//button[@class='btn btn-secondary more-btn btn-load-more-click-scroll']")
    button.click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

time.sleep(3)
page_source = driver.page_source

print(page_source)
soup = BeautifulSoup(page_source, 'html.parser')

time.sleep(3)
articles = soup.findAll('div', class_="search-result-item-body tease tease-post")

for article in articles:
    title1 = article.find_next('a', class_='search-result-item-headline').text
    url1 = article.find_next('a', class_='search-result-item-headline')['href']
    date1 = article.find_next('span', 'search-result-item-date').text
    records2.append((date1, title1.strip(), url1))

df = pd.DataFrame(records2, columns=['date', 'title', 'URL'])
df.to_csv('Climate_articles_new-website_newVersion.csv')

driver.quit()
driver.close()
driver2.quit()
driver2.close()
# records = []
# for result in results:
# date = result.find('div', class_='list_date').text
# url = result.find('div', xpath_="//div[@class='content_title']")
# teaser = result.find('div', class_='article_teaser_body').text
# title = teaser
# records.append((date, title))

# df = pd.DataFrame(records, columns=['date', 'title'])
# df.to_csv('Climate_articles_new.csv')
