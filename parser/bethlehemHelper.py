import requests
from bs4 import BeautifulSoup

###############################
########## API Stuff ##########
###############################

''' Make POST for searching by date '''

DOCKSHEET_URL = "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx"
payload = ""
headers = {
    'origin': "https://ujsportal.pacourts.us",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'x-devtools-emulate-network-conditions-client-id': "(26392B431ACC5F9C636883E3DBF5039F)",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://ujsportal.pacourts.us/DocketSheets/MDJ.aspx",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cookie': "f5_cspm=1234; ASP.NET_SessionId=5ljcelkwzj0wx3zumsbvbuir; f5avr1149697488aaaaaaaaaaaaaaaa=MPLEAIDIODICPBFIAIPFALHMMGNJHFJELPLHMEIIMMGLKALNNDHOIMANCIOLPPNCEGCCOGJDJJGACOJDKNFAIPFNBGEBBMFOFJGONHCIPADJAOGHAGKGJFLNFOJFNGJA; f5avrbbbbbbbbbbbbbbbb=DDJJNMKIKJGMGLHOFKBBOAPGBOENDGGIILFGDEMNICPIBPCLAEGPJADDCFOJPGDILFGDEIHOAOFCOBJLCDNAKPHLKMMEDNPGMLHPADMIGLAHLCAMEACNBGBDLANKHAKJ; ASP.NET_SessionId=5ljcelkwzj0wx3zumsbvbuir; f5avrbbbbbbbbbbbbbbbb=BKIJHJMAABAGNNLAIOJCGFOJHCFNCHBJGFGIOPGFLFJNBNPFPJBGGPNIOGFELDJEIJEDEEFECAEJLEMCGMJAANFHLNBHALOELJAJIGOEMIBNFACGPMIGMFOLLEAGIKNO",
    'cache-control': "no-cache",
    'postman-token': "a88a55d1-41bb-f598-1032-05f296c3929c"
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