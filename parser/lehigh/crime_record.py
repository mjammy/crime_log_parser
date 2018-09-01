from __future__ import annotations
from typing import Iterable, List
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil.parser import parse
import csv


class CrimeRecord:
    _description: str
    _disposition: str
    _incident_date: datetime
    _incident_location: str
    _incident_type: str
    _report_number: str
    _reported_on: datetime

    def __init__(self, reported_on: datetime or None,
                 incident_date: datetime or None, disposition: str or None,
                 incident_type: str or None, incident_location: str or None,
                 report_number: str or None, description: str or None):
        self._reported_on = reported_on
        self._incident_date = incident_date
        self._disposition = disposition
        self._incident_type = incident_type
        self._incident_location = incident_location
        self._report_number = report_number
        self._description = description

    def reported_on(self) -> datetime or None:
        return self._reported_on or None

    def incident_date(self) -> datetime or None:
        return self._incident_date or None

    def disposition(self) -> str or None:
        return self._disposition or None

    def incident_type(self) -> str or None:
        return self._incident_type or None

    def incident_location(self) -> str or None:
        return self._incident_location or None

    def report_number(self) -> str or None:
        return self._report_number or None

    def description(self) -> str or None:
        return self._description or None

    def get_values(self) -> List[str]:
        return [
            str(self.reported_on() or 'unknown'),
            str(self.incident_date() or 'unknown'),
            str(self.disposition() or 'unknown'),
            str(self.incident_type() or 'unknown'),
            str(self.incident_location() or 'unknown'),
            str(self.report_number() or 'unknown'),
            str(self.description() or 'unknown'),
        ]

    def __eq__(self, other: CrimeRecord):
        return (
            self.reported_on() == other.reported_on()
            and self.incident_date() == other.incident_date()
            and self.disposition() == other.disposition()
            and self.incident_type() == other.incident_type()
            and self.incident_location() == other.incident_location()
            and self.report_number() == other.report_number()
            and self.description() == other.description()
        )

    def __str__(self) -> str:
        description = []
        for (title, value) in zip(CrimeRecord.get_headers(), self.get_values()):
            description.append(f'{title}: {value}')
        return '\n'.join(description)

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def from_views_row(views_row: BeautifulSoup) -> CrimeRecord:
        return CrimeRecord(
            CrimeRecord._get_reported_on_date(views_row),
            CrimeRecord._get_incident_date(views_row),
            CrimeRecord._get_disposition(views_row),
            CrimeRecord._get_incident_type(views_row),
            CrimeRecord._get_incident_location(views_row),
            CrimeRecord._get_report_number(views_row),
            CrimeRecord._get_description(views_row),
        )

    @staticmethod
    def _get_description(views_row: BeautifulSoup):
        raw = views_row.find('div', class_='views-field-body')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        return raw.getText().strip()

    @staticmethod
    def _get_report_number(views_row: BeautifulSoup):
        raw = views_row.find('div', class_='views-field-field-report-number')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        return raw.getText().lstrip('Report Number: ').strip()

    @staticmethod
    def _get_incident_location(views_row: BeautifulSoup):
        raw = views_row.find('div', class_='views-field-field-incident-location')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        return raw.getText().lstrip('Incident Location: ').strip()

    @staticmethod
    def _get_incident_type(views_row: BeautifulSoup):
        raw = views_row.find('div', class_='views-field-field-incident-type')
        if raw is None:
            return None

        raw = raw.find(class_='field-content')
        if raw is None:
            return None

        return raw.getText().strip()

    @staticmethod
    def _get_disposition(views_row: BeautifulSoup):
        raw = views_row.find('div', class_='views-field-field-disposition')
        if raw is None:
            return None

        raw = raw.find('div', class_='field-content')
        if raw is None:
            return None

        return raw.getText().lstrip('Disposition: ').strip()

    @staticmethod
    def _get_incident_date(views_row: BeautifulSoup):
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
    def _get_reported_on_date(views_row: BeautifulSoup):
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
    def to_csv(path: str, records: Iterable[CrimeRecord]):
        # open csv writer
        with open(path, 'w+', newline='') as file:
            writer = csv.writer(file, dialect='excel')

            # write header
            writer.writerow(CrimeRecord.get_headers())

            # write all records
            for record in records:
                writer.writerow(record.get_values())
