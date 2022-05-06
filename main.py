import classes.crawler as crawler
import schedule
import time
# from keep_alive import keep_alive
import classes.JsonUtility as ex

crawler = crawler.Crawler()
crawler.InitSelenium();

def Root():
  crawler.setWeb('https://naver.com')

schedule.every(1).minutes.do(Root)

# keep_alive()
while True:
  schedule.run_pending()
  time.sleep(1)

# while True:
#     schedule.run_pending()
#     time.sleep(1)