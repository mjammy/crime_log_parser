import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os
from typing import List

from downloaderHelper import *
from options import Options
from lu_crime_record import LUCrimeRecord

options: Options = Options.from_cli()

urlTemp = 'https://police.lehigh.edu/crime-log?page='
lastPage = getLastPage()

records: List[LUCrimeRecord] = []

for eachPage in range(0,lastPage+1):
    url = urlTemp + str(eachPage)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for eachReport in soup.find_all('div', class_='views-row'):
        elements = eachReport.contents
        records.append(get_record(elements))


# Set up file name structure
now = datetime.datetime.now().strftime("%Y-%m-%d")
fileName = f'lehigh_log({now}).csv'

# Output to CSV
LUCrimeRecord.to_csv(os.path.join(f'/{options.directory}', fileName), records)