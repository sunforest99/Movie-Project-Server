import classes.crawler as crawler
import schedule
import time

import classes.ExportJson as ex

def root():
    test = crawler.Crawler()
    test.getPage()
    print("in")

t = ex.Jsontility()
t.makeformet('asdf', 'https://qwer', '100분', float(4.5), 'https://asdf')
t.makeformet('닥스', 10, 1)
t.makeformet('닥스', '2021-10-02', '100분', 'https://asdf')


# while True:
#     schedule.run_pending()
#     time.sleep(1)