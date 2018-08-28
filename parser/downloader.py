import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

from downloaderHelper import *
from commandArgs import *

# Set up directory to be the location for the saved csv
DIR = ''
argDir = getDir()
if (argDir):
        DIR = argDir
print (DIR)

urlTemp = 'https://police.lehigh.edu/crime-log?page='

data = []

for pageNum in range(0,getLastPage() + 1):
    url = urlTemp + str(pageNum)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for entry in soup.find_all('div', class_='views-row'):
        report = getReport(entry)
        data.append(report)

# Data Frame format
df = pd.DataFrame.from_records(data, columns=["Date Reported","Incident Date","Disposition","Crime","Location","Report Number","Description"])

# Set up file name structure
now = datetime.datetime.now()
fileName = "lehigh_log(" + now.strftime("%Y-%m-%d") + ").csv"

# Output to CSV
df.to_csv(os.path.join(DIR,fileName))