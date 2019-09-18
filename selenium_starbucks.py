from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('./chromedriver.exe',  options=chrome_options)
driver.implicitly_wait(3)

# url에 접근한다
driver.get('https://www.istarbucks.co.kr/store/store_map.do')

time.sleep(2)
id='동성로'

driver.execute_script("document.getElementsByName('quickSearchText')[0].value=\'"+id+"\'")
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[1]/div[1]/div/a').click()
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
store_name = soup.select("#mCSB_1_container > ul > li > strong")
store_location = soup.select("#mCSB_1_container > ul > li > p")

for name,location in zip(store_name,store_location):
    print("{0} / {1}".format(name.get_text().strip(),location.get_text().strip()))

driver.close()