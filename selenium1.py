from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

options = Options()
options.headless = True

chromedriver_path = os.getcwd() + '/chromedriver'
country = 'S. Korea'

driver = webdriver.Chrome(executable_path = chromedriver_path, options = options)
driver.get('https://www.worldometers.info/coronavirus/')
time.sleep(5)

selection = driver.find_element_by_link_text(country)
selection.send_keys(Keys.ENTER)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincounter-wrap"]/div/span')))

total_cases = driver.find_element_by_xpath('//*[@id="maincounter-wrap"]/div/span').text
driver.close()

print('{} total cases: {}'.format(country, total_cases))