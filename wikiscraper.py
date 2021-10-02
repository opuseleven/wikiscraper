from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import sys
import time

if len(sys.argv) < 2:
    print('Usage: wikiscraper.py "search name"')
    sys.exit()

if len(sys.argv) > 2:
    print('Use quotes around searches containing more than one word.')
    sys.exit()

file = open('scraped-data.txt', 'a')

driver_options = Options()
driver_options.headless = True
driver = webdriver.Firefox(options=driver_options)

driver.get("https://www.wikipedia.com")

search_input = driver.find_element(By.ID, 'searchInput')
search_input.send_keys("%s" % sys.argv[1])
time.sleep(1)
search_input.send_keys(Keys.RETURN)

time.sleep(1)
heading = driver.find_element(By.ID, 'firstHeading')
body = driver.find_element(By.ID, 'bodyContent')

print(heading.text)
print(body.text)

file.write(heading.text + '\n')
file.write(body.text + '\n' + '\n')

def tearDown(self):
    self.quit()

tearDown(driver)
file.close()
