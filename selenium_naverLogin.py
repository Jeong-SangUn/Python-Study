from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

# url에 접근한다
driver.get('https://nid.naver.com/nidlogin.login')

id='tkddns6928'  #자신의 네이버 아이디 
pw='dns1684818'  #자신의 네이버 비밀번호 

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(1)

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
point = soup.select_one("#container > div > div.snb > div.member_sc > dl > dd > strong")
print(point.string)

time.sleep(15)
driver.close()