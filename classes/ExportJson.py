import json
from multipledispatch import dispatch

class Jsontility:

    jsondata = None

    def __init__(self) -> None:
        pass

    def importjson(self, filename):
        try:
            with open(filename, encoding='utf-8') as data_file:
                self.jsondata = json.loads(data_file.read())
        except:
            print("ImportJson : Can't open file")

    def exportjson(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as outfile:
                json.dump(self.jsondata, outfile, indent = 4, sort_keys = True, ensure_ascii=False)
        except:
            print("ExportJson : can't open file")
    
    @dispatch(str, str, str, float, str)
    def makeformet(self, moviename : str, ticketlink : str, movietime : str, grade : float, imgurl : str):
        self.importjson('./movie_list.json')
        json_formet = { "movie_name": "" + moviename,  "ticket_link": "" + ticketlink, "grade": "" + str(grade), "movie_time" : "" + movietime, "img_url": "" + str(imgurl)}
        for i in range(len(self.jsondata)):
            if moviename == self.jsondata[i]["movie_name"]:
                return None
        self.jsondata.append(json_formet)
        self.jsondata = list(map(dict, set(tuple(sorted(d.items())) for d in self.jsondata)))
        self.exportjson('./movie_list.json')
    
    # 변등폭 구현
    @dispatch(str, int, int)
    def makeformet(self, moviename : str, rank : int, variable : int):
        self.importjson('./movie_rank.json')
        json_formet = { "movie_name": "" + moviename, "before_rank" : "", "rank": "" + str(rank), "variable" : "" + str(variable)}
        for i in range(len(self.jsondata)):
            if moviename == self.jsondata[i]["movie_name"]:
                return None
        self.jsondata.append(json_formet)
        self.jsondata = list(map(dict, set(tuple(sorted(d.items())) for d in self.jsondata)))
        self.exportjson('./movie_rank.json')

    @dispatch(str, str, str, str)
    def makeformet(self, moviename :str, opendate : str, movietime : str, imgurl : str):
        self.importjson('./movie_to_be_open.json')
        json_formet = { "movie_name": "" + moviename,  "open_date": "" + opendate, "movie_time" : "" + movietime, "img_url": "" + str(imgurl)}
        for i in range(len(self.jsondata)):
            if moviename == self.jsondata[i]["movie_name"]:
                return None
        self.jsondata.append(json_formet)
        self.jsondata = list(map(dict, set(tuple(sorted(d.items())) for d in self.jsondata)))
        self.exportjson('./movie_to_be_open.json')