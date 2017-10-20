import requests
from bs4 import BeautifulSoup
from downloaderHelper import *

urlTemp = 'https://police.lehigh.edu/crime-log?page='

lastPage = getLastPage()

for eachPage in range(0,lastPage):
    url = urlTemp + str(lastPage)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for eachReport in soup.find_all('div', class_='views-row'):
        elements = eachReport.contents
        print "\n"
        print getReportedOn(elements)
        print getIncidentDateTime(elements)
        print getDisposition(elements)
        print getIncidentType(elements)
        print getSuspectName(elements)
        print getIncidentLocation(elements)
        print getReportNumber(elements)
        print getDescription(elements)

