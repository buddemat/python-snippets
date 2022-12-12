'''Simple scraper

Example scraper that goes through static html pages, extracts data 
from a table and saves it as csv.
'''

import requests 
from bs4 import BeautifulSoup

url = 'https://www.namenforschung.net/dfd/woerterbuch/liste/'

website = requests.get(url)
results = BeautifulSoup(website.content, 'html.parser')

names_table = results.find('table', class_='nameslist')
names_table_body = names_table.find('tbody')
names_table_rows = names_table_body.find_all('tr')

for row in names_table_rows:
    name = row.find('td').text.strip()
    print(name)

