from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

def get_movie_list_start():
    csvFile=open('movie_top200_start.csv','wt',newline='',encoding='utf-8')     #csv로 영화이름, 개봉일 저장
    write=csv.writer(csvFile)
    write.writerow(['movie','start'])

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome('./chromedriver.exe',  options=chrome_options)
    driver.implicitly_wait(1)

    driver.get('http://www.kobis.or.kr/kobis/business/stat/boxs/findFormerBoxOfficeList.do')
    driver.implicitly_wait(3)
    
    # 구한 값들을 list에 저장 및 반환
    # movielist=[]
    # moviestart=[]
    # for num in range(1,201):
    #     name_xpath="/html/body/div/div[2]/div[2]/div[4]/table/tbody/tr["+str(num)+"]/td[2]/span/a"
    #     start_xpath="/html/body/div/div[2]/div[2]/div[4]/table/tbody/tr["+str(num)+"]/td[3]"
    #     movielist.append(driver.find_element_by_xpath(name_xpath).text)
    #     moviestart.append(driver.find_element_by_xpath(start_xpath).text)
    # return movielist, moviestart

    # 구한 값들을 csv로 바로 저장
    for num in range(1,201):    # 영화진흥원에서 역대 흥행순위 200까지 제목과 개봉일 저장
        name_xpath="/html/body/div/div[2]/div[2]/div[4]/table/tbody/tr["+str(num)+"]/td[2]/span/a"  
        start_xpath="/html/body/div/div[2]/div[2]/div[4]/table/tbody/tr["+str(num)+"]/td[3]"
        movie_name = driver.find_element_by_xpath(name_xpath).text
        movie_start = driver.find_element_by_xpath(start_xpath).text
        write.writerow([movie_name, movie_start])
    
    