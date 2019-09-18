# 유튜브 최근 한달 내의 내용 제목 가져오기

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()

driver = webdriver.Chrome('./chromedriver.exe',  options=chrome_options)
driver.implicitly_wait(3)

# url에 접근한다
driver.get('https://www.youtube.com/')

time.sleep(3)
id='BTS'
# //*[@id="video-title"]
driver.execute_script("document.getElementById('search[1]').value=\'"+id+"\'")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="button"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="endpoint"]').click()
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
video_name = soup.select("#video-title")

for name in video_name:
    print(name.get_text().strip())

driver.close()