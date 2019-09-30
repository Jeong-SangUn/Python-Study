from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def movielist_excel_download(movie_name_list):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.implicitly_wait(3)

    driver.get('http://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do')
    driver.implicitly_wait(3)

    movielist = movie_name_list
    for i,movie_name in enumerate(movielist):
        print(i,'번째 다운로드 중...')
        driver.execute_script("document.getElementsByName('sMovName')[1].value=\'"+movie_name+"\'")
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/div[5]/button[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="content"]/div[4]/table/tbody/tr[1]/td[1]/span/a').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/ul/li[2]/a').click()
        driver.implicitly_wait(300)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div/a').click()
        driver.switch_to.alert.accept()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/a[2]').click()
        driver.implicitly_wait(2)
    