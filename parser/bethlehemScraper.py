import time

from bethlehemHelper import *

''' Navigate website, perform search '''
initializeDriver()
accessSite()
fillSearchCriteria()
submitSearch()

# Store search results
searchResults = grabHTML()

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

advancePage()

time.sleep(10)

searchResults2 = grabHTML()

for eachRow in range(2,12):

    # Adds leading 0's in prep to search by id value
    index = str(eachRow).zfill(2) 

    # Gets case
    case = getCase(searchResults2, index)

    # Gets DOB
    dateOfBirth = getDOB(searchResults2, index)
    
    print("-----ROW " + index + "-----")
    print(case)
    print(dateOfBirth) 


