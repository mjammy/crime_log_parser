from typing import Iterable
from datetime import date
import os

from config.options import Options
from lehigh.crime_record import CrimeRecord
from lehigh.helper import get_records


class CrimeLog:
    options: Options
    records: Iterable[CrimeRecord]

    def __init__(self, options: Options):
        self.options = options
        self.records = None

    def process(self):
        self.records = get_records()

    def write(self):
        dt: str = date.today().strftime('%Y_%m_%d')
        file_name: str = f'lehigh_log_{dt}.csv'
        path: str = os.path.join(self.options.directory, file_name)
        CrimeRecord.to_csv(path, self.records)
