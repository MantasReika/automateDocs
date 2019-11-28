# ~*~ coding: utf-8 ~*~

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from configparser import RawConfigParser
from time import sleep
import csv
import sys
import re


def logg(a, b):
    print("{} {}".format(a, b))

def selectDropdownById(browser, elemId, val):
    browser.execute_script("$('#{}').val('{}').trigger('chosen:updated')".format(elemId, val))

def clickElementByIdJS(browser, id):
    try:
        elem = browser.find_element_by_id(id)
        browser.execute_script("arguments[0].click();", elem)
    except NoSuchElementException:
        print("ERROR: Element not found, id='{}': ".format(id))
        return False
    return True

def clickElementByXpathJS(browser, elemXpath):
    elems = browser.find_elements_by_xpath(elemXpath)
    if len(elems) == 1:
        elem = elems[0]
        browser.execute_script("arguments[0].click();", elem)
    elif len(elems) > 1:
        print("WARNING: Found more than 1 element, count: {}, xpath: '{}'".format(len(elems), elemXpath))
        elem = elems[0]
        browser.execute_script("arguments[0].click();", elem)
    else:
        print("ERROR: Element not found, xpath: '{}': ".format(elemXpath))
        return False
    return True

def clickElementById(browser, id):
    try:
        elem = browser.find_element_by_id(id)
        elem.click()
    except NoSuchElementException:
        print("ERROR: Element not found, id='{}': ".format(id))
        return False
    return True

def clickElementByXpath(browser, elemXpath):
    elems = browser.find_elements_by_xpath(elemXpath)
    if len(elems) == 1:
        elem = elems[0]
        elem.click()
    elif len(elems) > 1:
        print("WARNING: Found more than 1 element, count: {}, xpath: '{}'".format(len(elems), elemXpath))
        elem = elems[0]
        elem.click()
    else:
        print("ERROR: Element not found, xpath: '{}': ".format(elemXpath))
        return False
    return True

def enterElementById(browser, id, content):
    try:
        elem = browser.find_element_by_id(id)
        elem.clear()
        elem.send_keys(content)
    except NoSuchElementException:
        print("ERROR: Element not found, id='{}': ".format(id))
        return False
    return True

def enterElementByXpath(browser, elemXpath, content):
    elems = browser.find_elements_by_xpath(elemXpath)
    if len(elems) == 1:
        elem = elems[0]
        elem.clear()
        elem.send_keys(content)
    elif len(elems) > 1:
        print("WARNING: Found more than 1 element, count: {}, xpath: '{}'".format(len(elems), elemXpath))
        elem = elems[0]
        elem.clear()
        elem.send_keys(content)
    else:
        print("ERROR: Element not found, xpath: '{}': ".format(elemXpath))
        return False
    return True


### TODO button actions:
def selectPeople():
    pass

class A1Auto:
    
    def __init__(self):
        configPath = 'config/a1_config.ini'
        self.currentPersonRowNr = 2
        
        self.loadConfig(configPath)
        self.loadDataFiles()
        self.loadBrowser()
        self.openSodraMain()
        
    def loadConfig(self, configPath):
        config = RawConfigParser()
        config.read(configPath)

        self.offlineMode = bool(int(config["debug"]["debugMode"]))
        self.personsDBfile = config["A1"]["peopleDatabaseFileName"]
        self.personsToSendFile = config["A1"]["personsFileName"]
        self.webdriverPath = config["webdriver"]["webdriverPath"]
        self.offlineSodraWeb = config["debug"]["debugSodraWeb"]
        self.offlineSodraWebAnketa = config["debug"]["debugSodraWebAnketa"]
        self.sodraWeb = config["A1"]["sodraWebsiteURL"]
        self.documentNumber = config["data"]["documentNumber"]
        self.insuranceCode = config["data"]["insuranceCode"]
        self.companyAddress = config["data"]["companyAddress"]
        self.companyCity = config["data"]["companyCity"]
        self.employerPhoneNumber = config["data"]["employerPhoneNumber"]
        self.employerEmail = config["data"]["employerEmail"]
        self.employerCountry = config["data"]["employerCountry"]

    def loadDataFiles(self):
        f = open(self.personsDBfile, "r", encoding="UTF-8")
        personsperson_csv = csv.reader(f, delimiter=";")

        f2 = open(self.personsToSendFile, "r", encoding="UTF-8")
        personsToSend_csv = csv.reader(f2, delimiter=";")

        self.personsDB = []
        self.personsToSend = []
        
        for row in personsperson_csv:
            self.personsDB.append(row)

        for row in personsToSend_csv:
            self.personsToSend.append(row)
        #        print("{}".format(row[0:10]))
    
    def loadBrowser(self):

        if getattr(sys, 'frozen', False): 
            # executed as a bundled exe, the driver is in the extracted folder
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            # print("chromedriver_path: {}, sys._MEIPASS: {}".format(chromedriver_path, sys._MEIPASS))
            self.browser = webdriver.Chrome(chromedriver_path)
        else:
            # print("debug elese")
            # executed as a simple script, the driver should be in `PATH`
            self.browser = webdriver.Chrome(self.webdriverPath)

        self.browser.implicitly_wait(10)
        
        if self.offlineMode:
            self.browser.get(self.offlineSodraWeb)
        else:
            self.browser.get(self.sodraWeb)
    
    def openSodraMain(self):
        if self.offlineMode:
            self.browser.get(self.offlineSodraWeb)
            sleep(5)
        
    def openSodraForm(self):
        if self.offlineMode:
            self.browser.get(self.offlineSodraWebAnketa)
            sleep(1)

    
    def fillA1Page(self):
        self.openSodraMain()
        
        enterElementById(self.browser, "content_docNumber", self.documentNumber)
        enterElementById(self.browser, "content_declarant_dclCode", self.insuranceCode) 
        enterElementById(self.browser, "content_declarant_contactInfo_address", self.companyAddress)
        enterElementById(self.browser, "content_declarant_contactInfo_city", self.companyCity)
        selectDropdownById(self.browser, "content_declarant_contactInfo_country_value", getCountryCode(self.employerCountry))
        enterElementById(self.browser, "content_declarant_specialistInfo_communicationsInfo_phone", self.employerPhoneNumber)
        enterElementById(self.browser, "content_declarant_specialistInfo_communicationsInfo_email", self.employerEmail)

    def fillA1Form(self):
        self.openSodraForm()
        
        self.nextPerson()

        clickElementByIdJS(self.browser, "currentProfile_requestedForm_A_1")
        enterElementById(self.browser, "currentProfile_employee_surname", self.db_Surname)
        enterElementById(self.browser, "currentProfile_employee_name", self.db_Forename)
        enterElementById(self.browser, "currentProfile_employee_birthDate", self.db_BirthDate)
        selectDropdownById(self.browser, "currentProfile_employee_nationality", self.db_Citizienship)
        enterElementById(self.browser, "currentProfile_employee_personCode", self.db_PersonCode)
        enterElementById(self.browser, "currentProfile_employee_contactInfo_address", self.db_Address)
        selectDropdownById(self.browser, "currentProfile_employee_contactInfo_country_value", getCountryCode(self.db_Country))
        enterElementById(self.browser, "currentProfile_receivingEmployers__0_employerInfo_title", self.person_companyName)
        enterElementById(self.browser, "currentProfile_receivingEmployers__0_employerInfo_contactInfo_address", self.person_destinationAddress)
        enterElementById(self.browser, "currentProfile_receivingEmployers__0_employerInfo_contactInfo_city", self.person_destinationCity)
        selectDropdownById(self.browser, "currentProfile_receivingEmployers__0_employerInfo_contactInfo_country_value", getCountryCode(self.person_destinationCountry))
        clickElementByIdJS(self.browser, "currentProfile_receivingEmployers__0_employerRelationChoice_selection_OTHER")
        enterElementById(self.browser, "currentProfile_receivingEmployers__0_employerRelationChoice_otherRelationTitle", "Bendrai įmonių grupei priklausanti įmonė")
        enterElementById(self.browser, "currentProfile_dateFrom", self.person_fromDate)
        enterElementById(self.browser, "currentProfile_dateTo", self.person_toDate)
        clickElementByIdJS(self.browser, "currentProfile_employmentContractChoice_selection_SENDER")
        clickElementByIdJS(self.browser, "currentProfile_socialSecurityPaymentChoice_selection_SENDER")

        radioXpath_shiftChange = "//input[@name='currentProfile.shiftChange' and @value='false']"
        clickElementByXpathJS(self.browser, radioXpath_shiftChange)

    def nextPerson(self):
        self.currentPersonRowNr += 1
        person = self.personsToSend[self.currentPersonRowNr]

        self.person_Surname = person[0]
        self.person_Forename = person[1]
        self.person_fromDate = person[2]
        self.person_toDate = person[3]
        self.person_companyName = person[4]
        self.person_destinationAddress = person[5]
        self.person_destinationCity = person[6]
        self.person_destinationCountry = person[7]

        logg("", "Searching for person:\nperson_Surname = {}\nperson_Forename = {}\nperson_fromDate = {}\nperson_toDate = {}\nperson_companyName = {}\nperson_destinationAddress = {}\nperson_destinationCity = {}\nperson_destinationCountry = {}\ndocumentNumber = {}".format(self.person_Surname, self.person_Forename, self.person_fromDate, self.person_toDate, self.person_companyName, self.person_destinationAddress, self.person_destinationCity, self.person_destinationCountry, self.documentNumber))
        self.findPersonInDB()
        
    def findPersonInDB(self):
        foundPersonData = False
        personDBline = 0
        for db in self.personsDB:    
            personDBline += 1
            if personDBline <= 1 or db[1] == "":
                continue

            if self.person_Surname == db[1] and self.person_Forename == db[2]:
                self.db_Surname = db[1]
                self.db_Forename = db[2]
                self.db_BirthDate = db[10]
                self.db_Citizienship = db[21]
                self.db_PersonCode = db[9]
                self.db_InsuranceNumber = db[20]
                self.db_Address = db[5]
                self.db_Country = "Lietuva"
                self.db_Profesion = db[7]
                logg("","In DB:\ndb_Surname = {}\ndb_Forename = {}\ndb_BirthDate = {}\ndb_Citizienship = {}\ndb_PersonCode = {}\ndb_InsuranceNumber = {}\ndb_Address = {}\ndb_Country = {}\ndb_Profesion = {}".format(self.db_Surname, self.db_Forename, self.db_BirthDate, self.db_Citizienship, self.db_PersonCode, self.db_InsuranceNumber, self.db_Address, self.db_Country, self.db_Profesion))
                foundPersonData = True
                break
        
        #Ask for user confirmation to continue
        logg("DB searched lines: ", personDBline)
        logg("", "")
    
    def clearPerson():
        self.person_Surname = ""
        self.person_Forename = ""
        self.person_fromDate = ""
        self.person_toDate = ""
        self.person_companyName = ""
        self.person_destinationAddress = ""
        self.person_destinationCity = ""
        self.person_destinationCountry = ""

        self.db_Surname = ""
        self.db_Forename = ""
        self.db_BirthDate = ""
        self.db_Citizienship = ""
        self.db_PersonCode = ""
        self.db_InsuranceNumber = ""
        self.db_Address = ""
        self.db_Country = ""
        self.db_Profesion = ""

        
    
"""
def mainA1():

    continueToAddPerson = input("\nAdd next person form?\n1) Continue\n2) Exit\n>>> ")
    if continueToAddPerson != '1':
        a = input("Done...")
        browser.quit()
        return

    if self.offlineMode:
        browser.get(self.offlineSodraWebAnketa)
        sleep(1)
#    else:
#        addPersonXpath = "//div[@class='content']/div[@class='main_holder']/div[@class='main']/form[@id='EBDForm']//div[@class='wrapper']//div//button[@class='btn blue_btn' and text()='Pridėti']"
#        clickElementByXpathJS(browser, addPersonXpath)
"""






"""
        if offlineMode:
            a = input("Continue...")
            browser.get(offlineSodraWeb)
            sleep(1)

        continueToAddPerson = input("\nContinue to add person form?\n1) Continue\n2) Exit\n>>> ")
        if continueToAddPerson != '1':
            a = input("Press enter to exit...")
            browser.quit()
            return

        if offlineMode:
            browser.get(offlineSodraWebAnketa)
            sleep(1)
        else:
            addPersonXpath = "//div[@class='content']/div[@class='main_holder']/div[@class='main']/form[@id='EBDForm']//div[@class='wrapper']//div//button[@class='btn blue_btn' and text()='Pridėti']"
            clickElementByXpathJS(browser, addPersonXpath)


    a = input("Completed...\nPress enter to exit...\n")
    print("Exiting...")
    browser.quit()
"""

def removeAccents(string):
    string = str(string)
    string = re.sub(u"[Ą]", 'A', string)
    string = re.sub(u"[Č]", 'C', string)
    string = re.sub(u"[Ę]", 'E', string)
    string = re.sub(u"[Ė]", 'E', string)
    string = re.sub(u"[Į]", 'I', string)
    string = re.sub(u"[Š]", 'S', string)
    string = re.sub(u"[Ų]", 'U', string)
    string = re.sub(u"[Ū]", 'U', string)
    string = re.sub(u"[Ž]", 'Z', string)

    return string

def getCountryCode(countryName):
    countriesDict = {"" : "",
        "ALBANIJA" : "AL",
        "ALZYRAS" : "DZ",
        "AMERIKOS SAMOA" : "AS",
        "ANGOLA" : "AO",
        "ANGILIJA" : "AI",
        "ANTARKTIDA" : "AQ",
        "ANTIGVA IR BARBUDA" : "AG",
        "ARGENTINA" : "AR",
        "ARMENIJA" : "AM",
        "ARUBA" : "AW",
        "AUSTRALIJA" : "AU",
        "AUSTRIJA" : "AT",
        "AZERBAIDZANAS" : "AZ",
        "BAHAMOS" : "BS",
        "BAHREINAS" : "BH",
        "BARBADOSAS" : "BB",
        "BALTARUSIJA" : "BY",
        "BELGIJA" : "BE",
        "BELIZAS" : "BZ",
        "BERMUDA" : "BM",
        "BHUTANAS" : "BT",
        "BOLIVIJA" : "BO",
        "BOSNIJA IR HERCEGOVINA" : "BA",
        "BOTSVANA" : "BW",
        "BUVE SALA" : "BV",
        "BRAZILIJA" : "BR",
        "BULGARIJA" : "BG",
        "BURUNDIS" : "BI",
        "KAMBODZA" : "KH",
        "KAMERUNAS" : "CM",
        "KANADA" : "CA",
        "VERDE ISKISULYS" : "CV",
        "KAIMANU SALOS" : "KY",
        "CENTRINE AFRIKOS RESPUBLIKA" : "CF",
        "CADAS" : "TD",
        "KINIJA" : "CN",
        "COCOSO (KELINGO) SALOS" : "CC",
        "KONGAS" : "CG",
        "KOSTA RIKA" : "CR",
        "CTE D'IVOIRE" : "CI",
        "KROATIJA" : "HR",
        "KUBA" : "CU",
        "KIPRAS" : "CY",
        "DZIBUTI" : "DJ",
        "DOMINIKOS RESPUBLKA" : "DO",
        "EGIPTAS" : "EG",
        "SALVADORAS" : "SV",
        "ERITREJA" : "ER",
        "ESTIJA" : "EE",
        "FARERU SALOS" : "FO",
        "FIDZI" : "FJ",
        "SUOMIJA" : "FI",
        "GAMBIA" : "GM",
        "GRUZIJA" : "GE",
        "GIBRALTARAS" : "GI",
        "GRAIKIJA" : "GR",
        "GRENLANDIJA" : "GL",
        "GVADELUPE" : "GP",
        "HAITI" : "HT",
        "VATIKANAS" : "VA",
        "HONDURAS" : "HN",
        "VENGRIJA" : "HU",
        "ISLANDIJA" : "IS",
        "INDONEZIJA" : "ID",
        "AIRIJA" : "IE",
        "IZRAELIS" : "IL",
        "ITALIJA" : "IT",
        "JAMAIKA" : "JM",
        "JAPONIJA" : "JP",
        "KENIJA" : "KE",
        "PIETU KOREJA" : "KR",
        "KUVEITAS" : "KW",
        "KIRGIZIJA" : "KG",
        "LATVIJA" : "LV",
        "LIBANAS" : "LB",
        "LESOTHO" : "LS",
        "LIBERIJA" : "LR",
        "LICHTENSTEINAS" : "LI",
        "MAKAO" : "MO",
        "MADAGASKARAS" : "MG",
        "MALAIZIJA" : "MY",
        "MALI" : "ML",
        "MALTA" : "MT",
        "MARSALO SALOS" : "MH",
        "MAURITANIJA" : "MR",
        "MAURICIJUS" : "MU",
        "MOLDOVA" : "MD",
        "MONAKAS" : "MC",
        "MONGOLIJA" : "MN",
        "MAROKAS" : "MA",
        "NAMIBIJA" : "NA",
        "SUDANAS" : "SD",
        "SURINAMAS" : "SR",
        "SVALBARD AND JAN MAYEN" : "SJ",
        "SVAZILANDAS" : "SZ",
        "SVEDIJA" : "SE",
        "SVEICARIJA" : "CH",
        "TAIVANAS" : "TW",
        "TADZIKIJA" : "TJ",
        "TANZANIJA" : "TZ",
        "TAILANDAS" : "TH",
        "TOGAS" : "TG",
        "TOKELAU" : "TK",
        "TONGA" : "TO",
        "TUNISAS" : "TN",
        "TURKIJA" : "TR",
        "TURKMENIJA" : "TM",
        "UGANDA" : "UG",
        "UKRAINA" : "UA",
        "JUNGTINIAI ARABU EMIRATAI" : "AE",
        "JUNGTINES AMERIKOS VALSTIJOS" : "US",
        "JUNGTINES MINOR OUTLYING SALOS" : "UM",
        "URUGUAJUS" : "UY",
        "UZBEKIJA" : "UZ",
        "VANUATU" : "VU",
        "VENESUELA" : "VE",
        "VIETNAMAS" : "VN",
        "VIRGINJOS SALOS" : "VG",
        "VIRGINJOS SALOS, JAV" : "VI",
        "VALLISAS IR FUTUNA" : "WF",
        "VAKARU SACHARA" : "EH",
        "ZIMBABVE" : "ZW",
        "NEPALAS" : "NP",
        "NAUJOJI KALEDONIJA" : "NC",
        "NAUJOJI ZEALANDIJA" : "NZ",
        "NIKARAGVA" : "NI",
        "NIGERIS" : "NE",
        "NIGERIJA" : "NG",
        "NIUE" : "NU",
        "NORFOLKAS" : "NF",
        "NORTHERN MARIANA ISLANDS" : "MP",
        "NORVEGIJA" : "NO",
        "OMANAS" : "OM",
        "PAKISTANAS" : "PK",
        "PALAU" : "PW",
        "PALESTINA" : "PS",
        "PANAMA" : "PA",
        "PARAGVAJUS" : "PY",
        "PERU" : "PE",
        "LENKIJA" : "PL",
        "PORTUGALIJA" : "PT",
        "PUERTO RIKAS" : "PR",
        "KATARAS" : "QA",
        "RÉUNIONAS" : "RE",
        "RUSIJA" : "RU",
        "SVENTOJI ELENA" : "SH",
        "SAINT KITTS AND NEVIS" : "KN",
        "SEN PJERAS IR MIKELONAS" : "PM",
        "SENT VINCENTAS IR GRENADINAI" : "VC",
        "SAMOA" : "WS",
        "SAN MARINAS" : "SM",
        "SAN TOME IR PRINSIPE" : "ST",
        "SIERA LEONE" : "SL",
        "SINGAPURAS" : "SG",
        "SLOVAKIJA" : "SK",
        "SLOVENIJA" : "SI",
        "SALIAMONO SALOS" : "SB",
        "PIETU AFRIKA" : "ZA",
        "PIETU GEORGIA IR  SANDVICHO SALOS" : "GS",
        "ISPANIJA" : "ES",
        "SRI LANKA" : "LK",
        "CILE" : "CL",
        "CHRISTMAS ISLAND" : "CX",
        "KOLUMBIJA" : "CO",
        "KONGAS, THE DEMOCRATIC REPUBLIC OF THE" : "CD",
        "CEKIJA" : "CZ",
        "DOMINIKA" : "DM",
        "EKVADORAS" : "EC",
        "EKVATORIALINE GVINEJA" : "GQ",
        "FOLKLENDU SALOS (MALVINAI)" : "FK",
        "PRANCUZU GVIANA" : "GF",
        "PRANCUZU POLINEZIJA" : "PF",
        "GABONAS" : "GA",
        "VOKIETIJA" : "DE",
        "GRENADA" : "GD",
        "GUAM" : "GU",
        "GVINEJA" : "GN",
        "GUYANA" : "GY",
        "HEARD ISLAND AND MCDONALD ISLANDS" : "HM",
        "HONG KONGAS" : "HK",
        "INDIJA" : "IN",
        "IRANAS" : "IR",
        "KAZACHSTANAS" : "KZ",
        "SIAURES KOREJA" : "KP",
        "LAOSAS" : "LA",
        "LIBYAN ARAB JAMAHIRIYA" : "LY",
        "MAKEDONIJA" : "MK",
        "MARTINIKA" : "MQ",
        "MAJOTAS" : "YT",
        "MICRONEZIJA" : "FM",
        "MONTSERATAS" : "MS",
        "MJANMARAS" : "MM",
        "JUNGTINE KARALYSTE" : "UK",
        "PITCAIRNAS" : "PN",
        "SENT LUSIJA" : "LC",
        "SENEGALAS" : "SN",
        "TUVALU" : "TV",
        "JEMENAS" : "YE",
        "LIETUVA" : "LT",
        "RUMUNIJA" : "RO",
        "LUKSEMBURGAS" : "LU",
        "DANIJA" : "DK",
        "PRANCUZIJA" : "FR",
        "NYDERLANDAI" : "NL",
        "SEISELIAI" : "SC",
        "DIDZIOJI BRITANIJA" : "GB",
        "AFGANISTANAS" : "AF",
        "JUODKALNIJA" : "ME",
        "SERBIJA" : "RS",
        "MENO SALA" : "IM",
        "DZERSIS" : "JE",
        "ALANDU SALOS" : "AX",
        "KOSOVAS" : "XK",
        "KIURASAO" : "CW",
        "PIETU SUDANAS" : "SS",
        "SEN BARTELEMI" : "BL",
        "SEN MARTENAS" : "MF",
        "SINT MARTENAS" : "SX",
        "RYTU TIMORO DEMOKRATINE RESPUBLIKA" : "TL",
        "GERNSIS" : "GG",
        "BONERAS, SINT EUSTATIJUS IR SABA" : "BQ",
        "ANDORA" : "AD",
        "BANGLADESAS" : "BD",
        "BRUNEJAUS DARUSALAMAS" : "BN",
        "KOMORAI" : "KM",
        "GUATEMALA" : "GT",
        "IRAKAS" : "IQ",
        "JORDANIJA" : "JO",
        "MALAVI" : "MW",
        "MEKSIKA" : "MX",
        "MOZAMBIKAS" : "MZ",
        "PAPUANAUJOJI GVINEJA" : "PG",
        "GVINEJA-BISAU" : "GW",
        "RUANDA" : "RW",
        "SAUDO ARABIJA" : "SA",
        "SOMALIS" : "SO",
        "SIRIJA" : "SY",
        "TRINIDADAS IR TOBAGAS" : "TT",
        "ZAMBIJA" : "ZM",
        "ETIOPIJA" : "ET",
        "BRITISH INDIAN OCEAN TERRITORY" : "IO",
        "BENINAS" : "BJ",
        "PRANCUZU  PIETU IR ANTARKTIES TERITORIJOS" : "TF",
        "NAURU" : "NR",
        "BURKINA FASAS" : "BF",
        "KUKO SALOS" : "CK",
        "GHANA" : "GH",
        "KIRIBATI" : "KI",
        "MALDIVAI" : "MV",
        "FILIPINAI" : "PH",
        "TURKSO IR CAICOSO SALOS""" : "TC"}

    try:
        return countriesDict[removeAccents(countryName.upper())]
    except KeyError:
        return ""
