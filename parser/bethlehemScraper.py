import requests
from bs4 import BeautifulSoup

from bethlehemHelper import *

# Searches court records for given dates
searchResults = searchDateRange()

for eachRow in range(2,12):

    # Adds leading 0's in prep to search by id value
    index = str(eachRow).zfill(2) 

    # Gets case
    case = getCase(searchResults, index)

    # Gets DOB
    dateOfBirth = getDOB(searchResults, index)
    
    print("-----ROW " + index + "-----")
    print(case)
    print(dateOfBirth)
