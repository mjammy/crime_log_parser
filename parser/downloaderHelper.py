import requests
from bs4 import BeautifulSoup

def getLastPage(url='https://police.lehigh.edu/crime-log'):
    page= requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    wrapLast = soup.find('li',class_='pager-last')
    href = wrapLast.find('a')['href']
    return int(href[-1:])

''' For Dates (So Tableau is happy) '''

def formatDate(unformatted):
    withoutDay = unformatted.split(',',1)[1][1:]
    separatedDate = withoutDay.split(' ',3)
    month = convertMonth(separatedDate[1])
    day = separatedDate[0]
    year = separatedDate[2]
    formattedDate = str(month) + "/" + str(day) + "/" + str(year)
    return formattedDate

def convertMonth(strMonth):
    months = {"January" : 1,
              "February" : 2,
              "March" : 3,
              "April" : 4,
              "May" : 5,
              "June" : 6,
              "July" : 7,
              "August" : 8,
              "September" : 9,
              "October" : 10,
              "November" : 11,
              "December" : 12
    }
                    
    return months[strMonth]

''' Getters for each field of the entry '''

def getReportedOn(OGForm):
    whole = OGForm[1].contents[1].getText()
    part = whole[13:]
    return formatDate(part)

def getIncidentDateTime(OGForm):
    whole = OGForm[3].contents[1].getText()
    part = whole[20:]
    return formatDate(part)

def getDisposition(OGForm):
    whole = OGForm[5].contents[1].getText()
    part = whole[13:]
    return part

def getIncidentType(OGForm):
    return OGForm[7].contents[3].getText()
    
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

''' High level helpers '''

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
    print(getReportedOn(elements))
    print(getIncidentDateTime(elements))
    print(getDisposition(elements))
    print(getIncidentType(elements))
    print(getSuspectName(elements))
    print(getIncidentLocation(elements))
    print(getReportNumber(elements))
    print(getDescription(elements))
    print('\n')

def appendReport(report, allLists):
    for eachPart in range(0,8):
        allLists[eachPart].append(report[eachPart])
    
    