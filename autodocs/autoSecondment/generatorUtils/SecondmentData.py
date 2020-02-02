class SecondmentData:
    """
    Data class for storing Person objects
    and formating information for secondments
    """
    record = []
    err = False
    
    GALININKO_LINKSNIAI = {}
    MONTHS = {}
    GA1 = {}
    GA2 = {}
    PROFESIJA = {}
    DIENPINIGIAI = {}
    KEYS = {}

    def __init__(self, rec):
        self.record = rec

    def setConstants(self, GALININKO_LINKSNIAI, MONTHS, GA1, GA2, PROFESIJA, DIENPINIGIAI, KEYS):
        self.GALININKO_LINKSNIAI = GALININKO_LINKSNIAI
        self.MONTHS = MONTHS
        self.GA1 = GA1
        self.GA2 = GA2
        self.PROFESIJA = PROFESIJA
        self.DIENPINIGIAI = DIENPINIGIAI
        self.KEYS = KEYS
        
    def translateKeyToValue(self, key):
        if key == '#DOKYEAR#':
            return self.getDocYear()
        elif key == '#DOKMONTH#':
            return self.getDocMonth()
        elif key == '#DOKDAY#':
            return self.getDocDay()
        elif key == '#DOKNUM#':
            return self.getDocNum()
        elif key == '#GA1#':
            return self.getGa1()
        elif key == '#GA2#':
            return self.getGa2()
        elif key == '#CNTRY1#':
            return self.getCountry1()
        elif key == '#CNTRY2#':
            return self.getCountry2()
        elif key == '#KOMANDYEAR#':
            return self.getSecondmentYear()
        elif key == '#KOMANDMONTHDAY#':
            return self.getSecondmentDates()
        elif key == '#PERSONNAME#':
            return self.getPersonName()
        elif key == '#PERSONNAMECASED#':
            return self.getPersonNameCased()
        elif key == '#CNTRY3#':
            return self.geCountry3()
        elif key == '#PROFESSION#':
            return self.getProfesion()
        elif key == '#MONEY1#':
            return self.getAllowence1()
        elif key == '#MONEY2#':
            return self.getAllowence2()
        else:
            raise ValueError("Unexpected Key: ", key)
            #return None
        
    def getDocYear(self):
        return self.record[1].strip()[:4]
    def getDocMonth(self):
        return self.MONTHS[self.record[1].strip()[5:7]]
    def getDocDay(self):
        return self.record[1].strip()[-2:]
    def getDocNum(self):
        return self.record[0].strip()
    def getGa(self):
        return self.record[3].strip()
    def getGa1(self):
        return self.GA1[self.getGa()]
    def getGa2(self):
        return self.GA2[self.getGa()]
    def getCountry(self):
        return self.record[5].strip().split(" ")[0]
    def getCountry1(self):
        return self.getCountry()[:-1] + "os"
    def getCountry2(self):
        return self.getCountry()[:-1] + "ą"
    def getSecondmentYear(self):
        return self.record[6].strip()[:4]
    def getSecondmentMonth1(self):
        return self.MONTHS[self.record[6].strip()[5:7]]
    def getSecondmentMonth2(self):
        return self.MONTHS[self.record[7].strip()[5:7]]
    def getSecondmentDay1(self):
        return self.record[6].strip()[-2:]
    def getSecondmentDay2(self):
        return self.record[7].strip()[-2:]
    def getPersonName(self):
        return self.record[2].strip()
    def getPersonNameCased(self):
        return self.record[8].strip().upper()
    def geCountry3(self):
        return self.getCountry()[:-1] + 'oje'
    def getProfesion(self):
        return self.PROFESIJA[self.record[4].strip()]
    def getAllowence1(self):
        val = self.getDienpinigiai(self.DIENPINIGIAI, self.getCountry(), "min")
        if val == False:
            self.err = "FAIL"
        else:
            return val
    def getAllowence2(self):
        val = self.getDienpinigiai(self.DIENPINIGIAI, self.getCountry(), "max")
        if val == False:
            self.err = "FAIL"
        else:
            return val
    def getSecondmentDates(self):
        if (self.getSecondmentMonth1() == self.getSecondmentMonth2()) and (self.getSecondmentDay1() == self.getSecondmentDay2()):
            return "%s %s dieną" % (self.getSecondmentMonth1(), self.getSecondmentDay1())
        elif (self.getSecondmentMonth1() == self.getSecondmentMonth2()) and (self.getSecondmentDay1() != self.getSecondmentDay2()):
            return "%s %s-%s dienomis imt." % (self.getSecondmentMonth1(), self.getSecondmentDay1(), self.getSecondmentDay2())
        else:
            return "%s %s - %s %s dienomis imt." % (self.getSecondmentMonth1(), self.getSecondmentDay1(), self.getSecondmentMonth2(), self.getSecondmentDay2())

    def getDienpinigiai(self, dienpinigiai_dic, country, value):
        try:    
            if value == 'max':
                return dienpinigiai_dic[country][1]
            else:
                return dienpinigiai_dic[country][0]
        except KeyError:
            return False