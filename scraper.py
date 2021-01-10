import requests
from bs4 import BeautifulSoup
from coins_monitored import COINS
from database import DataBase

class CoinmarketcapScraper():
    def __init__(self):
        self.URL = 'https://coinmarketcap.com/'
        self.page = requests.get(self.URL)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.db = DataBase()
        self.table = self.collect_table()
        self.persist_rows()

    def collect_table(self):
        return self.soup.find(lambda tag: tag.name=='table')
    
    def collect_rows(self):
        rows = self.table.find_all('tr')
        selected_rows =[]
        for row in rows:
            td = row.find_all('td')
            row = [i.text for i in td]
            try:
                if row[2] in COINS:
                    selected_rows.append(row[2:4])
            except:
                continue
        return selected_rows
    
    def persist_rows(self):
        rows = self.collect_rows()
        self.db.persist_coin_entries(rows)
        self.db.close_connection()


if __name__ == "__main__": 
    cms = CoinmarketcapScraper()

