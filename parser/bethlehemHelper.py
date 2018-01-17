import requests
from bs4 import BeautifulSoup

###############################
########## API Stuff ##########
###############################

''' Make POST for searching by date '''

DOCKSHEET_URL = "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx"
payload = "ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24ddlSearchType=DateFiled&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCounty=Northampton&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCourtOffice=3210&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBox=01%2F10%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBox=01%2F17%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24btnSearch=Search&ctl00%24ctl00%24ctl00%24ctl05%24captchaAnswer=-298923588&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=32610cda-769b-43c4-8dd7-55b8f14767c3&__VIEWSTATEGENERATOR=4AB257F3&__SCROLLPOSITIONX=0&__SCROLLPOSITIONY=410"
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Content-Length': "1211",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "f5_cspm=1234; f5avrbbbbbbbbbbbbbbbb=GIIEJFPICDOGFADNHONPCFBIKDAPDKHCMHPKEPHMOBOLIKHEIEMJGCPAENLIKNFKNLMDCMJEEDEODKNOFAHAEPMOILIDIPMFFBPJAGFPHDKPNBGOJGJPJJANGMGAJMCO; ASP.NET_SessionId=5ljcelkwzj0wx3zumsbvbuir; f5avrbbbbbbbbbbbbbbbb=AGCPICJDBILDMLHFHNONKPIDLDONNKNHJAEBPOIFJLJIKLNIFCMNAFHJBEJONDKENFADFDBGIDGNHEDLPANAJOFEILEKBEDBABCPPLEJGNBAIPHKBDBBIILKNEJLIDEB",
    'Host': "ujsportal.pacourts.us",
    'Origin': "https://ujsportal.pacourts.us",
    'Referer': "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Postman-Token': "6f2bc860-5678-df30-0863-c6e9a723a279"
    }

def searchDateRange():
    response = requests.request("POST", DOCKSHEET_URL, data = payload, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

#############################
########## Parsing ##########
#############################

''' Getters for each field of the row '''

BASE_ID = 'ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cphResults_gvDocket_ctl'

def getCase(soup, index):
    caseID = BASE_ID + index + '_Label2'
    case = soup.find(id = caseID).getText()
    return case

def getDOB(soup, index):
    dateOfBirthID = BASE_ID + index + '_ctl02'
    dateOfBirth = soup.find(id = dateOfBirthID).span.getText()
    return dateOfBirth