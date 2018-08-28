from __future__ import annotations
from typing import Iterable, List
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil.parser import parse
import csv


class LUCrimeRecord:
    reported_on: datetime
    incident_date: datetime
    disposition: str
    incident_type: str
    incident_location: str
    report_number: str
    description: str

    def __init__(
        self, reported_on: datetime, incident_date: datetime, disposition: str, incident_type: str,
        incident_location: str, report_number: str, description: str):

        self.reported_on = reported_on
        self.incident_date = incident_date
        self.disposition = disposition
        self.incident_type = incident_type
        self.incident_location = incident_location
        self.report_number = report_number
        self.description = description

    def get_values(self) -> List[str]:
        return [
            self.reported_on.isoformat() if self.reported_on else 'unknown',
            self.incident_date.isoformat() if self.incident_date else 'unknown',
            self.disposition or 'unknown',
            self.incident_type or 'unknown',
            self.incident_location or 'unknown',
            self.report_number or 'unknown',
            self.description or 'unknown',
        ]

    def __str__(self) -> str:
        description = []
        for (title, value) in zip(LUCrimeRecord.get_headers(), self.get_values()):
            description.append(f'{title}: {value}')
        return '\n'.join(description)

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def from_views_row(views_row: BeautifulSoup) -> LUCrimeRecord:
        return LUCrimeRecord(
            LUCrimeRecord._get_reported_on_date(views_row),
            LUCrimeRecord._get_incident_date(views_row),
            LUCrimeRecord._get_disposition(views_row),
            LUCrimeRecord._get_incident_type(views_row),
            LUCrimeRecord.get_incident_location(views_row),
            LUCrimeRecord._get_report_number(views_row),
            LUCrimeRecord._get_description(views_row),
        )

    @staticmethod
    def _get_description(views_row: BeautifulSoup):
        raw = views_row.find('div', class_='views-field-body')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        raw = raw.stripped_strings
        if raw is None:
            return None

        return ' '.join(raw).replace('\n', ' ')

    @staticmethod
    def _get_report_number(views_row):
        raw = views_row.find('div', class_='views-field-field-report-number')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        raw = raw.stripped_strings
        if raw is None:
            return None

        return ' '.join(raw).lstrip('Report Number: ')

    @staticmethod
    def get_incident_location(views_row):
        raw = views_row.find('div', class_='views-field-field-incident-location')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        raw = raw.stripped_strings
        if raw is None:
            return None

        return ' '.join(raw).lstrip('Incident Location: ')

    @staticmethod
    def _get_incident_type(views_row):
        raw = views_row.find('div', class_='views-field-field-incident-type')
        if raw is None:
            return None

        raw = raw.find(class_='field-content')
        if raw is None:
            return None

        raw = raw.strings
        if raw is None:
            return None

        return ' '.join(raw)

    @staticmethod
    def _get_disposition(views_row):
        raw = views_row.find('div', class_='views-field-field-disposition')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        raw = raw.stripped_strings
        if raw is None:
            return None

        return ' '.join(raw).lstrip('Disposition: ')

    @staticmethod
    def _get_incident_date(views_row):
        raw = views_row.find('div', class_='views-field-field-incident-date-time')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        raw = raw.find(class_='date-display-single')
        if raw is None:
            return None

        raw = raw['content']
        if raw is None:
            return None

        return parse(raw)

    @staticmethod
    def _get_reported_on_date(views_row):
        raw = views_row.find('div', class_='views-field-field-reported-on')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        raw = raw.find(class_='date-display-single')
        if raw is None:
            return None

        raw = raw['content']
        if raw is None:
            return None

        return parse(raw)

    @staticmethod
    def get_headers() -> List[str]:
        return [
            'Reported_On',
            'Incident_Date_Time',
            'Disposition',
            'Incident_Type',
            'Incident_Location',
            'Report_Number',
            'Description',
        ]

    @staticmethod
    def to_csv(path: str, records: Iterable[LUCrimeRecord]):
        # open csv writer
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file, dialect='excel')

            # write header
            writer.writerow(LUCrimeRecord.get_headers())

            # write all records
            for record in records:
                writer.writerow(record.get_values())


if __name__ == '__main__':
    # path: str = './test.csv'
    #
    # records: List[LUCrimeRecord] = []
    #
    # for j in range(1, 5):
    #     i = str(j)
    #     record = LUCrimeRecord(
    #         datetime.now(),
    #         datetime.now(),
    #         'disposition ' + i,
    #         'incident_type ' + i,
    #         'incident_location ' + i,
    #         'report_number ' + i,
    #         'description ' + i
    #     )
    #     records.append(record)
    #
    # LUCrimeRecord.to_csv(path, records)
    html: str = '<div class="views-field views-field-field-reported-on"> <div class="field-content"><div><strong>Reported on:</strong> <span class="date-display-single" content="2018-08-27T10:56:00-04:00" datatype="xsd:dateTime" property="dc:date">Monday, 27 August 2018 - 10:56am</span></div></div> </div> <div class="views-field views-field-field-incident-date-time"> <div class="field-content"><div><strong>Incident Date/Time:</strong> <span class="date-display-single" content="2018-08-26T01:36:00-04:00" datatype="xsd:dateTime" property="dc:date">Sunday, 26 August 2018 - 1:36am</span></div></div> </div> <div class="views-field views-field-field-disposition"> <div class="field-content"><div><strong>Disposition:</strong> Arrest</div></div> </div> <div class="views-field views-field-field-incident-type"> <strong class="views-label views-label-field-incident-type">Incident Type: </strong> <span class="field-content">Underage Drinking</span> </div> <div class="views-field views-field-field-incident-location"> <div class="field-content"><div><strong>Incident Location:</strong> Rathbone Hall</div></div> </div> <div class="views-field views-field-field-report-number"> <div class="field-content"><div><strong>Report Number:</strong> 18 002 742</div></div> </div> <div class="views-field views-field-body"> <div class="field-content"><p>A suspect, being less than 21 years of age, was found to be under the influence of an alcoholic beverage in a public place. Citations issued. </p><hr/></div> </div>'
    element = BeautifulSoup(html, 'html.parser')
    print(LUCrimeRecord.from_views_row(element))
