import urllib.request
import os

#이미지의 주소
url='https://developers.naver.com/docs/papago/'

#실행하는 파일의 경로를 찾아서 같은 경로에 이미지 저장
dirname=os.path.dirname(__file__)
savename=dirname +'/test.png'
'''
# 파일로 저장 (바로 저장하기)
urllib.request.urlretrieve(url,savename)
'''
# 파일을 열고.. 활용 할수 있다. (이건 열기 밑에껀 쓰기)
mem = urllib.request.urlopen(url).read()

# 위에서 불러온 파일을 저장함.
print(savename)
print(mem)
with open(savename,mode='wb') as f:
    f.write(mem)
    print('저장되었습니다.')
