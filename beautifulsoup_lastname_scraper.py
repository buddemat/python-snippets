'''Simple scraper

Example scraper that goes through static html pages, extracts data 
from a table and saves it as csv.
'''

import requests 
import csv
from bs4 import BeautifulSoup

base_url = 'https://www.namenforschung.net/dfd/woerterbuch/liste/?tx_dfd_names[offset]='
max_pages = 1178

with open('lastnames.csv', 'w') as file_handle:
    writer = csv.writer(file_handle)
    writer.writerow(['lastname', 'rank', 'occurrence'])

    for page_no in range(1, max_pages + 1):
         website = requests.get(f'{base_url}{page_no}')
         results = BeautifulSoup(website.content, 'html.parser')
         
         names_table = results.find('table', class_='nameslist')
         names_table_body = names_table.find('tbody')
         names_table_rows = names_table_body.find_all('tr')
         
         for row in names_table_rows:
             cells = row.find_all('td')
             cols = []
             for item in cells:
                 cols.append(item.text.strip())
             writer.writerow(cols)
             print(cols)
     
