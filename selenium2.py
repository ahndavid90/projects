from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import date
import math

options = Options()
options.headless = True

def Sort(element):
    return element[1]

country_info_list = []

chromedriver_path = os.getcwd() + '/chromedriver'

driver = webdriver.Chrome(executable_path = chromedriver_path, options = options)
driver.get('https://www.worldometers.info/coronavirus/')

for country in driver.find_elements_by_xpath("//tr[@class='odd' or @class='even']"):
    country_info= []
    location = country.find_elements_by_css_selector('td')[0].text
    exposure = country.find_elements_by_css_selector('td')[1].text
    deaths = country.find_elements_by_css_selector('td')[3].text

    if exposure == '':
        exposure = 0
    elif ',' in exposure:
        exposure = int("".join(exposure.split(",")))
    else:
        exposure = int(exposure)

    if deaths == '':
        deaths = 0
    elif ',' in deaths:
        deaths = int("".join(deaths.split(",")))
    else:
        deaths = int(deaths)

    if deaths > 10 and exposure > 500:
        m_x = deaths/exposure
        q_x = round(1 - math.exp(-m_x), 4)
        country_info.append(location)
        country_info.append(q_x)

    if country_info:
        country_info_list.append(country_info)

country_info_list.sort(key = lambda x: x[1], reverse = True)

print('')
print("Today's Date: {}".format(date.today()))
print('----')
for element in country_info_list[0:10]:
    print(*element)


