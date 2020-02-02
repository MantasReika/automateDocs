class PersonRecord:
    """
    Data class for storing person secondment data
    """
    def __init__(self, fullName = None, workDistrict = None, proffesion = None, docNr = None, docDate = None, sentCountry = None, dateFrom = None, dateTo = None):
        self.fullName = fullName
        self.workDistrict = workDistrict
        self.proffesion = proffesion
        self.docNr = docNr
        self.docDate = docDate
        self.sentCountry = sentCountry
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        
    def __repr__(self):
        return "fullName='{}', workDistrict='{}', proffesion='{}', docNr='{}', docDate='{}', sentCountry='{}', dateFrom='{}', dateTo='{}'".format(self.fullName, self.workDistrict, self.proffesion, self.docNr, self.docDate, self.sentCountry, self.dateFrom, self.dateTo)
    
    def hasAllFieldsFilled(self):
        if self.fullName != None and self.workDistrict != None and self.proffesion != None and self.docNr != None and self.docDate != None and self.sentCountry != None and self.dateFrom != None and self.dateTo != None:
            return True
        return False

    def returnRecordArray(self):
        """[nr,date_created, surname_name, place, specialybe, country, date_from, date_to, galininkas_full_name]"""
        return [self.docNr, self.docDate, self.fullName, self.workDistrict, self.proffesion, self.sentCountry, self.dateFrom, self.dateTo, self.fullName]
        ##return [self.fullName, self.workDistrict, self.proffesion, self.docNr, self.docDate, self.sentCountry, self.dateFrom, self.dateTo]

    def mockRecord(self):
        self.fullName = "fullNameMock"
        self.workDistrict = "workDistrictMock"
        self.proffesion = "proffesionMock"
        self.docNr = "docNrMock"
        self.docDate = "docDateMock"
        self.sentCountry = "sentCountryMock"
        self.dateFrom = "dateFromMock"
        self.dateTo = "dateToMock"
