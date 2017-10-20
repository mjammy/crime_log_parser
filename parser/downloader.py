import requests
from bs4 import BeautifulSoup
from downloaderHelper import *


url = 'https://police.lehigh.edu/crime-log'
page= requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#print soup


'''
for eachReport in soup.find_all('div', class_='views-row'):
    print "\n"
'''

oneReport = soup.find_all('div', class_='views-row')[0]
elements = oneReport.contents

print getReportedOn(elements)
print getIncidentDateTime(elements)
print getDisposition(elements)
print getIncidentType(elements)
print getSuspectName(elements)
print getIncidentLocation(elements)
print getReportNumber(elements)
print getDescription(elements)
