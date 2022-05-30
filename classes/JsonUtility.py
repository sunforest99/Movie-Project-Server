import json
from multipledispatch import dispatch
import collections
import config as co
class JsonUtility:

    jsondata = None

    def __init__(self) -> None:
        pass

    # @brief json 파일 불러오기
    # @param string filename 파일 이름
    def importjson(self, filename):
        try:
            with open(filename, encoding='utf-8') as data_file:
                self.jsondata = json.loads(data_file.read())
        except:
            print("ImportJson : \"" + filename + "\"Can't open file")

    # @brief json 파일 내보내기(저장)
    # @param string filename 파일 이름
    def exportjson(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as outfile:
                json.dump(self.jsondata, outfile, indent = 4, sort_keys = True, ensure_ascii=False)
        except:
            print("ExportJson : \"" + filename + "\" can't open file")
    
    # @brief json 파일 싹 비우기
    # @param string filename 파일 이름
    def jsonclear(self, filename):
        try:
            f = open(filename, 'w')
            f.write('[\n]')
            f.close()
        except:
            print("JsonClear : \"" + filename + "\" can't open file")

    # @brief 상영 영화 리스트 json 형식 만들기
    # @param string moviename 영화 제목
    # @param string ticketlink 예매 시간 보여주는 링크
    # @param string movietime 영화 시간
    # @param float grade 평점
    # @param imgurl 영화 포스트 url 링크
    @dispatch(str, str, str, float, str)
    def makeformet(self, moviename : str, ticketlink : str, movietime : str, grade : float, imgurl : str):
        self.importjson('./' + co.listFilename)
        json_formet = { "movie_name": "" + moviename,  "ticket_link": "" + ticketlink.replace('basic', 'running'), "grade": "" + str(grade), "movie_time" : "" + movietime, "img_url": "" + str(imgurl)}
        for i in range(len(self.jsondata)):
            if moviename == self.jsondata[i]["movie_name"]:
                return None
        self.jsondata.append(json_formet)
        self.jsondata = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in self.jsondata)))

        self.exportjson('./' + co.listFilename)
    
    # @brief 영화 순위 리스트 json 형식 만들기
    # @param string moviename 영화 제목
    # @param int rank 순위
    # @param int variable 변틍폭 
    # @param String variable_img 변등폭 화살표 이미지
    # @param String count_img 순위 숫자 이미지  
    @dispatch(str, int, int, str, str)
    def makeformet(self, moviename : str, rank : int, variable : int, variable_img : str, count_img : str):
        self.importjson('./' + co.rankFilename)
        json_formet = { "movie_name": "" + moviename, "rank": "" + str(rank), "variable" : "" + str(variable), "variable_img" : variable_img, "count_img" : count_img}
        for i in range(len(self.jsondata)):
            if moviename == self.jsondata[i]["movie_name"]:
                return None
        self.jsondata.append(json_formet)
        self.jsondata = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in self.jsondata)))
        self.exportjson('./' + co.rankFilename)

    # @brief 개봉 예정 영화 리스트 json 형식 만들기
    # @param string moviename 영화 제목
    # @param string opendate 상영 예정일
    # @param string imgurl 영화 포스트 링크
    @dispatch(str, str, str)
    def makeformet(self, moviename :str, opendate : str, imgurl : str):
        self.importjson('./' + co.openFilename)
        json_formet = { "movie_name": "" + moviename,  "open_date": "" + opendate, "img_url": "" + str(imgurl)}
        for i in range(len(self.jsondata)):
            if moviename == self.jsondata[i]["movie_name"]:
                return None
        self.jsondata.append(json_formet)
        self.jsondata = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in self.jsondata)))
        self.exportjson('./' + co.openFilename)