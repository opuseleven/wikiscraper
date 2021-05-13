from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys

if len(sys.argv) < 2:
    print('Usage: wikiscraper.py "search name"')
    sys.exit()

if len(sys.argv) > 2:
    print('Use quotes around searches containing more than one word.')
    sys.exit()

file = open('scraped-data.txt', 'a')

PATH = "/home/cody/.local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.wikipedia.com")
search_input = driver.find_element(By.ID, 'searchInput')
search_input.send_keys("%s" % sys.argv[1])
search_input.send_keys(Keys.RETURN)

heading = driver.find_element(By.ID, 'firstHeading')
body = driver.find_element(By.ID, 'bodyContent')

print(heading.text)
print(body.text)

file.write(heading.text + '\n')
file.write(body.text + '\n' + '\n')

file.close()
