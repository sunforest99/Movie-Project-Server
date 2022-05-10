# import classes.crawler as crawler
# import schedule
# import time
# from keep_alive import keep_alive
import classes.JsonUtility as ex
import classes.movie_rank
import classes.movie_list
import classes.movie_to_be_open

# crawler = crawler.Crawler()
# crawler.InitSelenium();

movie = classes.movie_to_be_open.Movie_to_be_open()
movie.crawler()

def Root():
  crawler.setWeb('https://naver.com')

# schedule.every(1).minutes.do(Root)

# keep_alive()
# while True:
#   schedule.run_pending()
#   time.sleep(1)