import unittest
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from dateutil.parser import parse

from parser.lehigh.crime_record import CrimeRecord

now: datetime = datetime(year=2000, month=2, day=10)
yesterday: datetime = datetime(year=2000, month=2, day=9)


def _full_record() -> CrimeRecord:
    return CrimeRecord(
        reported_on=now,
        incident_date=yesterday,
        incident_type='test',
        incident_location='the cpu',
        report_number='1',
        description='I was testing code',
        disposition='instead of drinking.'
    )


def _mixed_record() -> CrimeRecord:
    return CrimeRecord(
        reported_on=now,
        incident_date=yesterday,
        incident_type='test',
        incident_location='the cpu',
        report_number=None,
        description=None,
        disposition=None,
    )


def _empty_record() -> CrimeRecord:
    return CrimeRecord(
        reported_on=None,
        incident_date=None,
        incident_type=None,
        incident_location=None,
        report_number=None,
        description=None,
        disposition=None,
    )


class CrimeRecordTest(unittest.TestCase):

    def test_init(self):
        record = _full_record()
        self.assertEqual(now, record.reported_on())
        self.assertEqual(yesterday, record.incident_date())
        self.assertEqual('instead of drinking.', record.disposition())
        self.assertEqual('test', record.incident_type())
        self.assertEqual('the cpu', record.incident_location())
        self.assertEqual('1', record.report_number())
        self.assertEqual('I was testing code',record.description())

        record = _empty_record()
        self.assertEqual(None, record.reported_on())
        self.assertEqual(None, record.incident_date())
        self.assertEqual(None, record.disposition())
        self.assertEqual(None, record.incident_type())
        self.assertEqual(None, record.incident_location())
        self.assertEqual(None, record.report_number())
        self.assertEqual(None, record.description())

    def test_header(self):
        self.assertEqual(CrimeRecord.get_headers(), [
            'Reported_On',
            'Incident_Date_Time',
            'Disposition',
            'Incident_Type',
            'Incident_Location',
            'Report_Number',
            'Description',
        ])

    def test_get_values(self):
        record = _full_record().get_values()
        val = [
            str(now),
            str(yesterday),
            'instead of drinking.',
            'test',
            'the cpu',
            '1',
            'I was testing code',
        ]
        for (r, v) in zip(record, val):
            self.assertEqual(r, v)

        record = _empty_record().get_values()
        for r in record:
            self.assertEqual('unknown', r)

    def test_parse(self):
        html = '<div class="views-field views-field-field-reported-on"> <div ' \
               'class="field-content"><div><strong>Reported on:</strong> <span class="date-display-single" ' \
               'content="2018-08-27T10:56:00-04:00" datatype="xsd:dateTime" property="dc:date">Monday, 27 August 2018 ' \
               '- 10:56am</span></div></div> </div> <div class="views-field views-field-field-incident-date-time"> ' \
               '<div class="field-content"><div><strong>Incident Date/Time:</strong> <span ' \
               'class="date-display-single" content="2018-08-26T01:36:00-04:00" datatype="xsd:dateTime" ' \
               'property="dc:date">Sunday, 26 August 2018 - 1:36am</span></div></div> </div> <div class="views-field ' \
               'views-field-field-disposition"> <div class="field-content"><div><strong>Disposition:</strong> ' \
               'Arrest</div></div> </div> <div class="views-field views-field-field-incident-type"> <strong ' \
               'class="views-label views-label-field-incident-type">Incident Type: </strong> <span ' \
               'class="field-content">Underage Drinking</span> </div> <div class="views-field ' \
               'views-field-field-incident-location"> <div class="field-content"><div><strong>Incident ' \
               'Location:</strong> Rathbone Hall</div></div> </div> <div class="views-field ' \
               'views-field-field-report-number"> <div class="field-content"><div><strong>Report Number:</strong> 18 ' \
               '002 742</div></div> </div> <div class="views-field views-field-body"> <div class="field-content"><p>A ' \
               'suspect, being less than 21 years of age, was found to be under the influence of an alcoholic ' \
               'beverage in a public place. Citations issued. </p><hr/></div> </div> '
        element = BeautifulSoup(html, 'html.parser')
        record = CrimeRecord.from_views_row(element)
        self.assertEqual(record, CrimeRecord(
            reported_on=parse('2018-08-27T10:56:00-04:00'),
            incident_date=parse('2018-08-26T01:36:00-04:00'),
            disposition='Arrest',
            incident_type='Underage Drinking',
            incident_location='Rathbone Hall',
            report_number='18 002 742',
            description='A suspect, being less than 21 years of age, was found to be under the influence of an '
                        'alcoholic beverage in a public place. Citations issued. '

        ))
