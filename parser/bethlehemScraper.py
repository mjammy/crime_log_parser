import requests
from bs4 import BeautifulSoup

from bethlehemHelper import *

''' # Searches court records for given dates
searchResults = searchstartDate()

for eachRow in range(2,12):

    # Adds leading 0's in prep to search by id value
    index = str(eachRow).zfill(2) 

    # Gets case
    case = getCase(searchResults, index)

    # Gets DOB
    dateOfBirth = getDOB(searchResults, index)
    
    print("-----ROW " + index + "-----")
    print(case)
    print(dateOfBirth) '''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.set_page_load_timeout(10)

driver.get('https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx')

# Search type: Date Filed
selectSearchType = Select(driver.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$ddlSearchType'))
selectSearchType.select_by_visible_text('Date Filed')

# County: Northampton
selectCounty = Select(driver.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$ddlCounty'))
selectCounty.select_by_visible_text('Northampton')

# Give the website a second to load office choices
time.sleep(1)

# Court Office: Northampton
selectCourtOffice = Select(driver.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$ddlCourtOffice'))
selectCourtOffice.select_by_value("3210")

# Choose Start Date
startDate = driver.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$drpFiled$beginDateChildControl$DateTextBox')
for i in range(12): 
    startDate.send_keys(Keys.LEFT)
startDate.send_keys("01102018")

# Choose End Date
startDate = driver.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$drpFiled$endDateChildControl$DateTextBox')
for i in range(12): 
    startDate.send_keys(Keys.LEFT)
startDate.send_keys("01172018")

# Submit Search
searchButton = driver.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$btnSearch')
searchButton.click()



