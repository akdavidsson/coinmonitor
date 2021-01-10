# Overview

This is a scraper of coinmarketcap to get the high level prices of the main cryptocurrencies.

## To run the scraper 

First install the dependencies

```
poetry install
````
Then initialize the local sqlite3 db
```
poetry run python database.py
```
Then run the scraper
```
poetry run python scraper.py
```
To run the scraper as a cron job then
```
potery run python cron_job.py
```