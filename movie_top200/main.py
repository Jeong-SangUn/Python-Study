from movie_crawling import movielist_excel_download
from movie_top200 import get_movie_list_start
from getscore import get_score

def main():
    # movielist, moviestart = get_movie_list_start()  #get_movie_list_start()가 리턴값 있을 때
    get_movie_list_start() #get_movie_list_start()가 csv로 바로 저장할 때
    # movielist_excel_download(movielist)
    # get_score(movielist)


if __name__ == "__main__":
    main()