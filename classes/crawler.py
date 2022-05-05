from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytz import timezone
import time

class Crawler:

    device = None
    
    def __init__(self):
         pass

    # @brief 
    def InitSelenium(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.device = webdriver.Chrome('./chromedriver')            # <! window & mac
    
    def setWeb(self, url):
        self.device.get(url);

