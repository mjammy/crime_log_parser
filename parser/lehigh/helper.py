from typing import Iterator
import requests
from bs4 import BeautifulSoup

from lehigh.crime_record import CrimeRecord

CRIME_LOG_URL = 'https://police.lehigh.edu/crime-log'


def _get_page_count() -> int:
    response = requests.get(CRIME_LOG_URL)
    page = BeautifulSoup(response.content, 'html.parser')
    last_page_item = page.find('li', class_='pager-last')
    link = last_page_item.find('a')['href']
    page_count = int(link[-1:]) + 1
    return page_count


def get_records() -> Iterator[CrimeRecord]:
    for page_number in range(_get_page_count()):
        page_url = f'{CRIME_LOG_URL}?page={page_number}'
        response = requests.get(page_url)
        page = BeautifulSoup(response.content, 'html.parser')

        for row in page.find_all('div', class_='views-row'):
            record = CrimeRecord.from_views_row(row)
            if record is not None:
                yield record


if __name__ == '__main__':
    print('page count: ' + str(_get_page_count()))
    print('Records: ')
    for record in get_records():
        print(record)
        print('\n')