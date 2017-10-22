import requests
from bs4 import BeautifulSoup

def getLastPage(url='https://police.lehigh.edu/crime-log'):
    page= requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    wrapLast = soup.find('li',class_='pager-last')
    href = wrapLast.find('a')['href']
    return int(href[-1:])

def getReportedOn(OGForm):
    whole = OGForm[1].contents[1].getText()
    part = whole[13:]
    return part

def getIncidentDateTime(OGForm):
    whole = OGForm[3].contents[1].getText()
    part = whole[20:]
    return part

def getDisposition(OGForm):
    whole = OGForm[5].contents[1].getText()
    part = whole[13:]
    return part

def getIncidentType(OGForm):
    whole = OGForm[7].contents[3].getText()
    part = whole[9:]
    return part

def getSuspectName(OGForm):
    whole = OGForm[9].contents[1].getText()
    part = whole[14:]
    return part

def getIncidentLocation(OGForm):
    whole = OGForm[11].contents[1].getText()
    part = whole[19:]
    return part

def getReportNumber(OGForm):
    whole = OGForm[13].contents[1].getText()
    part = whole[15:]
    return part

def getDescription(OGForm):
    return OGForm[15].contents[1].getText()

def getReport(elements):
    report = []
    report.append(getReportedOn(elements))
    report.append(getIncidentDateTime(elements))
    report.append(getDisposition(elements))
    report.append(getIncidentType(elements))
    report.append(getSuspectName(elements))
    report.append(getIncidentLocation(elements))
    report.append(getReportNumber(elements))
    report.append(getDescription(elements))
    return report

def printReport(elements):
    print getReportedOn(elements)
    print getIncidentDateTime(elements)
    print getDisposition(elements)
    print getIncidentType(elements)
    print getSuspectName(elements)
    print getIncidentLocation(elements)
    print getReportNumber(elements)
    print getDescription(elements)
    print ('\n')

def appendReport(report, allLists):
    for eachPart in range(0,8):
        allLists[eachPart].append(report[eachPart])
    
    