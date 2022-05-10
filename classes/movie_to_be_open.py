from cgitb import text
from bs4 import BeautifulSoup
import requests
import warnings
import classes.JsonUtility as js

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

class Movie_to_be_open:

    main_url = 'https://movie.naver.com/movie/running/premovie.naver'

    json = None

    count = 0

    temp_srt = ' '
    def __init__(self) -> None:
        pass

    # @brief 상영중인 영화 목록 크롤링
    def crawler(self) -> None:
        response = requests.get(self.main_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.json = js.JsonUtility()
        self.json.jsonclear('movie_list.json')

        list = soup.find('div', 'article').find_all('div', 'lst_wrap')

        for div_item in list:
            open_date = div_item.select('span.blind')
            movie_name = div_item.select('li > dl > dt > a')
            img = div_item.select('li > div > a > img')

            for i in open_date:
                if 'yyyy' in i.get_text():
                    self.temp_srt = ' '
                    continue
                else:
                    self.temp_srt += i.get_text()

            for i in range(len(movie_name)):
                self.json.makeformet(movie_name[i].get_text(), self.temp_srt, img[i]['src'])