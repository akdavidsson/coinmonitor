import schedule
import time
from scraper import CoinmarketcapScraper

def job():
    CoinmarketcapScraper()

schedule.every(1).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)