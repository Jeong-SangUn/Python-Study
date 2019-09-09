import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url='https://media.daum.net/'

data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')

soup = BeautifulSoup(text,'html.parser')

for news in soup.find_all(class_="list_headline"):
    for news_text in news.find_all(class_="link_txt"):
        print(news_text.get_text().strip())


