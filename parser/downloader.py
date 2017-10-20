import requests
from bs4 import BeautifulSoup


url = 'https://police.lehigh.edu/crime-log'
page= requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#print soup
'''
for reportedOn in soup.find_all('span',class_="date-display-single"):
    wrapDiv = reportedOn.parent.parent.parent
    if wrapDiv.name == 'div' and wrapDiv['class'] == 'views-field-field-reported-on':
        print reportedOn'''

for reportedOn in soup.find_all('span',class_='date-display-single'):
    label = reportedOn.previous_sibling.previous_sibling.getText()
    if label == 'Reported on:':
        print reportedOn

for incidentDateTime in soup.find_all('span',class_='date-display-single'):
    label = incidentDateTime.previous_sibling.previous_sibling.getText()
    if label == 'Incident Date/Time:':
        print incidentDateTime

for incidentType in soup.find_all('span',class_='field-content'):
    if incidentType.parent.name == 'div':
        print incidentType
