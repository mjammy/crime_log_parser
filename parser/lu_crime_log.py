from typing import List
from datetime import date
import os

import requests
from bs4 import BeautifulSoup

from options import Options
from lu_crime_record import LUCrimeRecord
from downloaderHelper import *

class LUCrimeLog:
    options: Options
    records: List[LUCrimeRecord]

    def __init__(self, options: Options):
        self.options = options
        self.records = []

    def process(self):
        urlTemp = 'https://police.lehigh.edu/crime-log?page='
        lastPage = getLastPage()

        for eachPage in range(0,lastPage+1):
            url = urlTemp + str(eachPage)

            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            for eachReport in soup.find_all('div', class_='views-row'):
                elements = eachReport.contents
                self.records.append(get_record(elements))

    def write(self):
        file_name: str = f'lehigh_log_${date.today().isoformat()}.csv'
        path: str = os.path.join(self.options.directory, file_name)
        LUCrimeRecord.to_csv(path, self.records)

if __name__ == "__main__":
    options: Options = Options.from_cli()
    print(f'Options:\n{str(options)}')

    crime_log: LUCrimeLog = LUCrimeLog(options)
    
    print(f'Processing crime log...')
    crime_log.process()

    print(f'Writing crime log...')
    crime_log.write()