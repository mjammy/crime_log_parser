from typing import Iterable
from datetime import date
import os

from options import Options
from lu_crime_record import LUCrimeRecord
from lu_crime_log_parser import get_records
from downloaderHelper import *


crime_log_url = 'https://police.lehigh.edu/crime-log'

class LUCrimeLog:
    options: Options
    records: Iterable[LUCrimeRecord]

    def __init__(self, options: Options):
        self.options = options
        self.records = None

    def process(self):
        self.records = get_records()

    def write(self):
        file_name: str = f'lehigh_log_{date.today().isoformat()}.csv'
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