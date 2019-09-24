import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import csv
from time import sleep
#1. 다음 뉴스 기사
# url='https://media.daum.net/'    

#2. 네이버 금융
# url ='https://finance.naver.com/marketindex/'

#3. 무비차트
# url='http://www.cgv.co.kr/movies/?lt=1&ft=0'

# 4. 벅스차트
# url='https://music.bugs.co.kr/chart?wl_ref=M_left_02_01'

# 5. 네이버 인기검색순위
# url='https://www.naver.com/'



#1. 다음 뉴스 기사 (헤드라인)
# for news in soup.find_all(class_="list_headline"):
#     print("-----------------------------------------")
#     for news_text in news.find_all(class_="link_txt"):
#         print(news_text.get_text().strip())

#2. 네이버 금융 (환율)
# results = soup.select('span.value')
# for result in results:
#     print(result.string)
# print('원달러환율:',results[0].string)
#--------------------------------------------------
# for financial in soup.find_all(class_="value"):
#     print(financial.get_text().strip())

#3. 무비차트 (영화 제목)
# for div in soup.find_all(class_="sect-movie-chart"):
#     for movie in div.find_all(class_="title"):
#         print(movie.get_text().strip())

# 4. 벅스차트 (노래 제목)
# result = soup.select('p.title')
# # result = soup.select('th>p>a')
# for music in result:
#     print(music.get_text().strip())

# 5. 네이버 인기검색순위 (위는 내가 짠거 밑에는 중복 막기)
# result = soup.select('span.ah_k')
# for search in result:
#     print(search.get_text())
#  -------------------------------------------------------------------
# keywords = soup.find_all('span',class_='ah_k')
# keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
# print(keywords)

# 6. 네이버 영화 평점(csv로 저장)
csvFile=open('crawling/naver_movie_score.csv','wt',newline='',encoding='utf-8')
write=csv.writer(csvFile)

api = 'https://movie.naver.com/movie/point/af/list.nhn'

i=0
values={'page':''}

write.writerow(['id','document','label'])
while i<1000:
    i= i + 1
    values['page']=str(i)

    params=urllib.parse.urlencode(values)
    url=api+'?'+params

    data=urllib.request.urlopen(url).read()
    # html=data.decode('utf-8')
    soup = BeautifulSoup(data,'html.parser')

    #1. 개인번호/ 평점/ 제목/ 댓글내용/ 아이디/ 글쓴날짜
    # num = soup.select('tbody>tr>td:first-child')
    # score = soup.select('tbody>tr>td.point')
    # title_content = soup.select('tbody>tr>td.title')
    # id_date = soup.select('tbody>tr>td:last-child')
  
    # 1.
    # try:
    #     for a,b,c,d in zip(num,score,title_content,id_date):
    #         write.writerow([a.get_text(), b.get_text(), c.get_text().split('\n')[1], c.get_text().split('\n')[2], d.get_text()[:8], d.get_text()[8:16]])
    # finally:
    #     print('csv로 저장되었습니다.')

    #2. 개인번호/ 평점/ 제목/ 댓글내용 / 라벨(평점에 따라 직접 계산)) 
    num = soup.select('tbody>tr>td:first-child')
    score = soup.select('tbody>tr>td.point')
    title_content = soup.select('tbody>tr>td.title')
    label = 0
    try:
        for a,b,c in zip(num,score,title_content):
            if int(b.get_text()) < 6:
                label = 0
            else:
                label = 1
            write.writerow([a.get_text(), c.get_text().split('\n')[2], label])
    finally:
        print('{0}번째 csv로 저장되었습니다.'.format(i))
    sleep(0.1)
csvFile.close()

# 7. 부동산 매물 시세 확인 (매물이름, 매물 가격(만원))
# url = 'https://land.naver.com/article/divisionInfo.nhn?cortarNo=2729000000&rletNo=&rletTypeCd=A01&tradeTypeCd=all&hscpTypeCd=A01%3AA03%3AA04&cpId=&location=&siteOrderCode='

# data=urllib.request.urlopen(url).read()
# # html=data.decode('utf-8')
# soup = BeautifulSoup(data,'html.parser')

# name = soup.select('td.align_l>div.inner>a')
# price = soup.select('td.align_r')
# for a,b in zip(name,price):
#     print([a.get_text().strip(), b.get_text().strip()])


