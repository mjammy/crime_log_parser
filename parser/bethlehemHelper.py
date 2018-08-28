from bs4 import BeautifulSoup

################################
##########  Selenium  ##########
################################

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

DRIVER = None
URL = 'https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx'

def initializeDriver():
    global DRIVER
    if DRIVER is None:
        DRIVER = webdriver.Chrome('/usr/local/bin/chromedriver')

def accessSite():
    DRIVER.get(URL)

''' Making search '''

def fillSearchCriteria():

    # Search type: Date Filed
    selectSearchType = Select(DRIVER.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$ddlSearchType'))
    selectSearchType.select_by_visible_text('Date Filed')

    # County: Northampton
    selectCounty = Select(DRIVER.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$ddlCounty'))
    selectCounty.select_by_visible_text('Northampton')

    # Give the website a second to load office choices
    time.sleep(3)

    # Court Office: Northampton
    selectCourtOffice = Select(DRIVER.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$ddlCourtOffice'))
    selectCourtOffice.select_by_value("3210")

    # Choose Start Date
    startDate = DRIVER.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$drpFiled$beginDateChildControl$DateTextBox')
    for i in range(12): 
        startDate.send_keys(Keys.LEFT)
    startDate.send_keys("01102018")

    # Choose End Date
    startDate = DRIVER.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$cphSearchControls$udsDateFiled$drpFiled$endDateChildControl$DateTextBox')
    for i in range(12): 
        startDate.send_keys(Keys.LEFT)
    startDate.send_keys("01172018")

def submitSearch():
    searchButton = DRIVER.find_element_by_name('ctl00$ctl00$ctl00$cphMain$cphDynamicContent$btnSearch')
    searchButton.click()

def grabHTML():
    html = DRIVER.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def advancePage():
    time.sleep(5)
    nextButton = DRIVER.find_element_by_xpath("//a[contains(@href,'Pager$ctl07')]")
    nextButton.click()
    time.sleep(10)

#############################
########## Parsing ##########
#############################

def getNumRows(soup):
    rows = soup.find_all(class_ = 'gridViewRow')
    return len(rows)

def isLastPage(soup):
    spanID = 'ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cstPager'
    lastButton = soup.find(id = spanID).div.contents[-2].attrs
    return 'href' not in lastButton

''' Getters for each field of the row '''

BASE_ID = 'ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cphResults_gvDocket_ctl'

def getCase(soup, index):
    caseID = BASE_ID + index + '_Label2'
    case = soup.find(id = caseID).getText()
    return case

def getDate(soup):
    id = 'ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cphResults_gvDocket'
    table = soup.find(id = id)
    row1 = table.tbody.find_all('tr')[1].find_all('td')[10].getText()
    return row1

def getDOB(soup, index):
    dateOfBirthID = BASE_ID + index + '_ctl02'
    dateOfBirth = soup.find(id = dateOfBirthID).span.getText()
    return dateOfBirth