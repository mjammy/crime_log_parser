import requests
from bs4 import BeautifulSoup

def getLastPage(url='https://police.lehigh.edu/crime-log'):
    page= requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    wrapLast = soup.find('li',class_='pager-last')
    href = wrapLast.find('a')['href']
    return int(href[-1:])

def getReportedOn(OGForm):
    return OGForm[1].contents[1].getText()

def getIncidentDateTime(OGForm):
    return OGForm[3].contents[1].getText()

def getDisposition(OGForm):
    return OGForm[5].contents[1].getText()

def getIncidentType(OGForm):
    return OGForm[7].contents[3].getText()

def getSuspectName(OGForm):
    return OGForm[9].contents[1].getText()

def getIncidentLocation(OGForm):
    return OGForm[11].contents[1].getText()

def getReportNumber(OGForm):
    return OGForm[13].contents[1].getText()

def getDescription(OGForm):
    return OGForm[15].contents[1].getText()