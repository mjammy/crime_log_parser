import requests
from bs4 import BeautifulSoup

url = "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx"

payload = "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=d26570e9-e715-40b2-bd6a-a0b295fb1593&__VIEWSTATEGENERATOR=4AB257F3&__SCROLLPOSITIONX=0&__SCROLLPOSITIONY=507&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24ddlSearchType=DateFiled&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCounty=Northampton&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCourtOffice=3210&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBox=01%2F07%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBox=01%2F16%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24btnSearch=Search&ctl00%24ctl00%24ctl00%24ctl05%24captchaAnswer=-1343900328"
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Content-Length': "1212",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "f5_cspm=1234; f5avrbbbbbbbbbbbbbbbb=PHLDPMEBPJNKNBGDNALEDGJJPKHMLAHLNGFHMLJCHGKKFCLJJFILJDEFOKPHHDAOEKGDJAGIJEMMFNHIKABABBPBDGLCMDHEOPJLKCNBJHLOJGEMKKMEOBJNLJECMFMN; ASP.NET_SessionId=5ljcelkwzj0wx3zumsbvbuir; f5avrbbbbbbbbbbbbbbbb=NBMDMCJCBILDMLHFGIBMLPIDLDONNKNHJAEBPOIFJLJIKLNIFCMNAFHJBEJONDKENFADFDBGJEHNIFCLPANAJOFEDGEKFJDBABCPPLEJGNBAIPKEBDBBIILKNEJLIDFN; f5avr1149697488aaaaaaaaaaaaaaaa=KJIOKNLBLNEDBKACJHJOGKHPCFFAJIKLCKEKEAANHJOJNJKDMFEHOICHMAANDGDOHDOCAKOBOMDBFOEOONCAIECCAHAAPKLLMCJCDDOBBHLPAFDLEFEKJILFGACJHGLC",
    'Host': "ujsportal.pacourts.us",
    'Origin': "https://ujsportal.pacourts.us",
    'Referer': "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Postman-Token': "8955c676-2e58-76aa-6d0f-8c5617dd57f5"
    }

response = requests.request("POST", url, data=payload, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

case1 = soup.find(id='ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cphResults_gvDocket_ctl06_Label2')
DOB1 = soup.find(id='ctl00_ctl00_ctl00_cphMain_cphDynamicContent_cphResults_gvDocket_ctl06_ctl02')

print(case1)
print(DOB1)

