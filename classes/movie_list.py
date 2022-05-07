from bs4 import BeautifulSoup
import requests
import bs4
import warnings
import classes.JsonUtility as js

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

class Movie_list:

    main_url = 'https://movie.naver.com/movie/running/current.naver'

    json = None

    def __init__(self) -> None:
        pass

    # @brief 상영중인 영화 목록 크롤링
    def crawler(self) -> None:
        response = requests.get(self.main_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        list = soup.find('ul', 'lst_detail_t1').find_all('li')
        self.json = js.JsonUtility()
        self.json.jsonclear('movie_list.json')

        for li_item in list:
            link = li_item.find('dt', 'tit').find('a')
            img = li_item.find('img')['src']
            playtime = li_item.find('dl', 'info_txt1').find('span', 'split').next_sibling.strip()
            grade = li_item.find('div', 'star_t1').find('span', 'num').get_text()

            self.json.makeformet(link.get_text(), self.main_url + link['href'], playtime, float(grade), img)
            # print(link.get_text())
            #print(link['href'])
            # print(grade)
