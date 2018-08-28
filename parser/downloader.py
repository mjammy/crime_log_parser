import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

from downloaderHelper import *
from options import Options

options: Options = Options.from_cli()

urlTemp = 'https://police.lehigh.edu/crime-log?page='
lastPage = getLastPage()

reportedOnList = []
incidentDateTimeList = []
dispositionList = []
incidentTypeList = []
suspectNameList = []
incidentLocationList = []
reportNumberList = []
descriptionList = []
allLists = [reportedOnList,incidentDateTimeList,dispositionList,incidentTypeList,suspectNameList,incidentLocationList,reportNumberList,descriptionList]

for eachPage in range(0,lastPage+1):
    url = urlTemp + str(eachPage)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for eachReport in soup.find_all('div', class_='views-row'):
        elements = eachReport.contents
        report = getReport(elements)
        appendReport(report,allLists)


d = {
    "Reported_On" : reportedOnList,
    "Incident_Date_Time" : incidentDateTimeList,
    "Disposition" : dispositionList,
    "Incident_Type" : incidentTypeList,
    "Suspect_Name" : suspectNameList,
    "Incident_Location" : incidentLocationList,
    "Report_Number" : reportNumberList,
    "Description" : descriptionList
}

df = pd.DataFrame(d)

# Set up file name structure
now = datetime.datetime.now().strftime("%Y-%m-%d")
fileName = f'lehigh_log({now}).csv'

# Output to CSV
df.to_csv(os.path.join(f'/{options.directory}', fileName))