# import classes.crawler as crawler
import schedule
import time
from keep_alive import keep_alive
from cgi import test
import classes.JsonUtility as ex
import classes.movie_rank
import classes.movie_list
import classes.movie_to_be_open
import classes.ftp_file_upload

import pytz
from datetime import datetime

molist = classes.movie_list.Movie_list()
tobeopen = classes.movie_to_be_open.Movie_to_be_open()
rank = classes.movie_rank.Movie_rank();
fildupload = classes.ftp_file_upload.FileUpload()

def Root():
  molist.crawler();
  tobeopen.crawler()
  rank.crawler();
  fildupload.UploadFunc()

schedule.every(1).hour.do(Root)

keep_alive()
KST = pytz.timezone('Asia/Seoul')
while True:
  print(datetime.now(KST))
  schedule.run_pending()
  time.sleep(1)