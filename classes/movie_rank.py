from itertools import count
from bs4 import BeautifulSoup
import requests
import warnings
import classes.JsonUtility as js
import config as co

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

class Movie_rank:

    main_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

    json = None

    count = 0

    def __init__(self) -> None:
        pass

    # @brief 상영중인 영화 목록 크롤링
    def crawler(self) -> None:
        response = requests.get(self.main_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        list = soup.find('tbody').find_all('tr')

        self.json = js.JsonUtility()
        self.json.jsonclear(co.rankFilename)
        self.count = 0

        for tr_item in list:
            a_tag = tr_item.select_one('td.title > div > a')
            variable = tr_item.select_one('td.range.ac')
            variable_img = tr_item.find('img','arrow')

            if variable_img is not None:
                print(type(variable_img['src']))

            if a_tag is not None or variable is not None and variable_img is not None :
                self.count += 1
                self.json.makeformet(a_tag.get_text(), int(self.count), int(variable.get_text()), variable_img['src'])
                # print(a_tag.get_text())
                # print(variable.get_text())