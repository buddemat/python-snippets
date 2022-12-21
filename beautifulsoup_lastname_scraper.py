'''Simple scraper

Example scraper that goes through static html pages, extracts data
from a table and saves it as csv.
'''

import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.namenforschung.net/dfd/woerterbuch/liste/?tx_dfd_names[offset]='
MAX_PAGES = 1178

print(f'Scraping "{BASE_URL}" ...', end='', flush=True)
with open('lastnames.csv', 'w', encoding='utf-8') as file_handle:
    writer = csv.writer(file_handle)
    writer.writerow(['lastname', 'rank', 'occurrence'])

    for page_no in range(1, MAX_PAGES + 1):
        website = requests.get(f'{BASE_URL}{page_no}', timeout=60)
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
        print('.', end='', flush=True)
print("\nCompleted.")
