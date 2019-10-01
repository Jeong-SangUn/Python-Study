import urllib.request
from bs4 import BeautifulSoup
from urllib import parse
import re
import csv

def get_score(movielist):
    # scorelist=[]
    csvFile=open('movie_top200_score.csv','wt',newline='',encoding='utf-8')     #csv로 영화이름, 개봉일 저장
    write=csv.writer(csvFile)
    write.writerow(['movie','start'])

    for movie in movielist:
        score_save = 0
        url='https://movie.naver.com/movie/search/result.nhn?query='
        url_str = parse.quote(movie)
        full_url = url + url_str + '&section=all&ie=utf8'
        data=urllib.request.urlopen(full_url).read()
        
        soup = BeautifulSoup(data,'html.parser')
        movie_score = soup.select('em.num')
        write_score = soup.select('em.cuser_cnt')
        max = 0
        for score,num in zip(movie_score,write_score):
            write_num = int(re.findall(r"\d+", num.get_text())[0])
            if max < write_num:
                max = write_num     
                score_save = score.get_text() #가장 참여율 높은 영화 평점 저장
            # scorelist.append([movie,score_save]) # list에 평점 저장
        write.writerow([movie, score_save]) # csv로 저장

        # return scorelist #list로 저장 시 반환