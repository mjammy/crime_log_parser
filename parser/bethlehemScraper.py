import time

from bethlehemHelper import *

# Navigate website, perform search
initializeDriver()
accessSite()
fillSearchCriteria()
submitSearch()

while True:

    # Store search results
    searchResults = grabHTML()

    # Sees how many rows are on the page and processes each
    numRows = getNumRows(searchResults)
    for eachRow in range(2,numRows+2):

        # Adds leading 0's in prep to search by id value
        index = str(eachRow).zfill(2) 

        # Gets case
        case = getCase(searchResults, index)

        # Gets DOB
        dateOfBirth = getDOB(searchResults, index)
        
        print(f"-----ROW {index}-----")
        print(case)
        print(dateOfBirth) 

    # Make sure we're not done
    if isLastPage(searchResults):
        break

    # Moves on to the next page
    advancePage()


