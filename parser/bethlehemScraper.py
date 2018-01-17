import requests
from bs4 import BeautifulSoup

url = "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx"

payload = "ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24ddlSearchType=DateFiled&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCounty=Northampton&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCourtOffice=3210&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBox=01%2F10%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBox=01%2F16%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24btnSearch=Search&ctl00%24ctl00%24ctl00%24ctl05%24captchaAnswer=1482804406&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=21c354fe-479a-48ec-84ea-3eec527671bd&__VIEWSTATEGENERATOR=4AB257F3&__SCROLLPOSITIONX=0&__SCROLLPOSITIONY=366"
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Content-Length': "1211",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "f5_cspm=1234; f5avrbbbbbbbbbbbbbbbb=GEIBGMHNLIFIFILFGIPIOIAHCBOKKEGBOHKPMNOLPHLBAEBKAIEHOKKMHJEPMPBPJHKDGGBBLBHJMGHHHPCAOOOBLMOPDOOEMDMIBLDACOBCCDMIKAJJLEGDOKCKKDMG; ASP.NET_SessionId=5ljcelkwzj0wx3zumsbvbuir; f5avrbbbbbbbbbbbbbbbb=FNDBFEGJOIEMEJBNDLGJFFBAJGJLOFMJHLNBFKGPFOIGLFOPHDBKNDCBKIFFCMJGLFCDLCMJCPIFDHCLALNAODOICLBCEMEACJDHEJGJIPPDEOCEEDPBHBDBKIGNFALH",
    'Host': "ujsportal.pacourts.us",
    'Origin': "https://ujsportal.pacourts.us",
    'Referer': "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Postman-Token': "c05d30eb-b3f7-c9e7-5532-121a1348b7dd"
    }

response = requests.request("POST", url, data = payload, headers = headers)

soup = BeautifulSoup(response.content, 'html.parser')

baseID = 'ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cphResults_gvDocket_ctl'

for eachRow in range(2,12):
    index = str(eachRow).zfill(2)
    caseID = baseID + index + '_Label2'
    dateOfBirthID = baseID + index + '_ctl02'
    case = soup.find(id = caseID).getText()
    dateOfBirth = soup.find(id = dateOfBirthID).span.getText()
    print("-----ROW " + index + "-----")
    print(case)
    print(dateOfBirth)

