import requests

url = "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx"

payload = "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=839a2ef2-77a8-473f-8475-84b70786daf0&__VIEWSTATEGENERATOR=4AB257F3&__SCROLLPOSITIONX=0&__SCROLLPOSITIONY=458&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24ddlSearchType=DateFiled&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCounty=Northampton&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24ddlCourtOffice=3210&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBox=01%2F11%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24beginDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBox=01%2F15%2F2018&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24cphSearchControls%24udsDateFiled%24drpFiled%24endDateChildControl%24DateTextBoxMaskExtender_ClientState=&ctl00%24ctl00%24ctl00%24cphMain%24cphDynamicContent%24btnSearch=Search&ctl00%24ctl00%24ctl00%24ctl05%24captchaAnswer=-830208557"
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Content-Length': "1211",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "f5avrbbbbbbbbbbbbbbbb=LNEGHGBCHNHBKFNLGJFPKBFLBFGIHOOJBPKDPOIOLGKDAFGOEMNLDNMKHNCPHHKAJDEDIELPCKNGOFFCACNAJGGKAFGGMEIKNCLMAELLKFOLKEEAOLKCJHNAEAPLHKIP; f5_cspm=1234; ASP.NET_SessionId=5ljcelkwzj0wx3zumsbvbuir; f5avrbbbbbbbbbbbbbbbb=BGOHOMEAPJNKNBGDIOFKAGJJPKHMLAHLNGFHMLJCHGKKFCLJJFILJDEFOKPHHDAOEKGDJAGINOPMBHEIKABABBPBFFLCKAHEOPJLKCNBJHLOJGONKKMEOBJNLJECMFHF",
    'Host': "ujsportal.pacourts.us",
    'Origin': "https://ujsportal.pacourts.us",
    'Referer': "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Postman-Token': "7a1897a4-fc95-bf38-3c88-7c6a363c8e40"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.content)

