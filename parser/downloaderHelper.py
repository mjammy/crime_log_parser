import requests
from bs4 import BeautifulSoup

def getLastPage(url='https://police.lehigh.edu/crime-log'):
    page= requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    wrapLast = soup.find('li',class_='pager-last')
    href = wrapLast.find('a')['href']
    pageNumIndex = href.find('page=') + 5
    lastPageNum = int(href[pageNumIndex:]) #it will be less 1 because indeces include 0
    return lastPageNum

''' High level helpers '''

def getReport(entry):
    report = []
    for field in entry.find_all('div', class_='views-field'):
        fieldText = field.getText()
        fieldContentText = fieldText[fieldText.find(':') + 1:].lstrip()
        report.append(fieldContentText)
    return report
    
    