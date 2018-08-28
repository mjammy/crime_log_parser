from __future__ import annotations
from typing import Iterable, List
import csv


class LUCrimeRecord:
    reported_on: str
    incident_date: str
    disposition: str
    incident_type: str
    suspect_name: str
    incident_location: str
    report_number: str
    description: str

    def __init__(
        self, reported_on: str, incident_date: str, disposition: str,
        incident_type: str, suspect_name: str, incident_location: str,
        report_number: str, description: str):

        self.reported_on = reported_on
        self.incident_date = incident_date
        self.disposition = disposition
        self.incident_type = incident_type
        self.suspect_name = suspect_name
        self.incident_location = incident_location
        self.report_number = report_number
        self.description = description

    def get_values(self) -> List[str]:
        return [
            self.reported_on,
            self.incident_date,
            self.disposition,
            self.incident_type,
            self.suspect_name,
            self.incident_location,
            self.report_number,
            self.description,
        ]

    @staticmethod
    def get_headers() -> List[str]:
        return [
            'Reported_On',
            'Incident_Date_Time',
            'Disposition',
            'Incident_Type',
            'Suspect_Name',
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
    path: str = './test.csv'
    
    records: List[LUCrimeRecord] = []

    for j in range(1, 5):
        i = str(j)
        record = LUCrimeRecord(
            'reported_on ' + i,
            'incident_date_time ' + i,
            'disposition ' + i,
            'incident_type ' + i,
            'suspect_name ' + i,
            'incident_location ' + i,
            'report_number ' + i,
            'description ' + i
        )
        records.append(record)
    
    LUCrimeRecord.to_csv(path, records)