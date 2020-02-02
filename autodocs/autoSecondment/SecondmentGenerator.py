# ~*~ coding: utf-8 ~*~

import copy
import datetime
import json
import os

import docx
import openpyxl
from docx import Document
from openpyxl import load_workbook

from autoSecondment.generatorUtils.Constants import Constants as SecondmentConstants
from autoSecondment.generatorUtils.secondmentUtils import (createSecondmentDocument, indexParagrahps, indexRuns, mapCodeToCountry, calculateLastWorkingDate)
from autoSecondment.generatorUtils.PersonRecord import PersonRecord

class SecondmentGenerator:
    """
    Should accept secondment data, 
    and generate secondment docx files
    """
    wb = None
    ws = None
    currentMonth = None
    fileName = None

    def __init__(self):
        
        self.startingRow = 6
        self.lastRow = 200 #1850 + 1
        
        self.currentRowId = 0
        self.personFirstRowId = 0
              
        self.personRecords = []
        
    def setSummaryRelativeCollumn(self, relativeToMonth):
        if type(relativeToMonth) != int and (relativeToMonth < 1 or relativeToMonth > 12):
            raise Exception("summary month='{}' value passed is invalid".format(month))

        self.relativeCol = 10 + ((relativeToMonth - 1 ) * 7)
    
    def getSummaryFileName(self):
        return self.fileName + ".xlsx"

    def openSummaryFile(self, fileName, month):
        if type(month) != int and (month < 1 or month > 12):
            raise Exception("summary month='{}' value passed is invalid".format(month))

        self.currentMonth = month
        
        if not os.path.isfile(fileName):
            raise FileNotFoundError("summary file='{}' does not exist at path='{}'".format(fileName, os.getcwd()))
        self.fileName = fileName.split('.xlsx')[0]

        self.wb = load_workbook(filename=self.getSummaryFileName())
        self.ws = self.wb.active

    def getCellValue(self, rowId, collumnId):
        try:
            return self.ws.cell(row=rowId, column=collumnId).value
        except Exception as e:
            log("getCellValue Exception: {}".format(e))
            return None
    
    def getCellDate(self, rowId, collumnId):
        cell = self.getCellValue(rowId, collumnId)
        if not self.isCellDate(cell):
            return None
            
        return cell.strftime("%Y-%m-%d")
        
    def isCellDate(self, cell):
        if cell == None or type(cell) is not datetime.datetime:
            return False
        return True

    def isEmptyRow(self, rowId):
        if rowId > self.lastRow:
            log("rowId > self.lastRow, {} , {}".format(rowId, self.lastRow))
            return True
        try:
            if self.getCellValue(rowId, 2) == None:
                return True
        except Exception as e:
            log("isEmptyRow Exception: {}".format(e))
            return True
        return False
    
    def readAllRows(self):
        log("readAllRows, self.relativeCol: {}".format(self.relativeCol))
        self.currentRowId = self.startingRow
        previousFullName = ""

        while not self.isEmptyRow(self.currentRowId):
            fullName = self.getCellValue(self.currentRowId, 2)
            
            # take only if new person 
            if fullName != previousFullName:
                workDistrict = str(self.getCellValue(self.currentRowId, 4)).upper()
                proffesion = str(self.getCellValue(self.currentRowId, 5)).lower()
            
            docNr = self.getCellValue(self.currentRowId, self.relativeCol + 4)
            sentCountry = mapCodeToCountry(self.getCellValue(self.currentRowId, self.relativeCol + 1))
            dateFrom = self.getCellDate(self.currentRowId, self.relativeCol + 5)
            dateTo = self.getCellDate(self.currentRowId, self.relativeCol + 6)
            # docDate = "2020-01-01" #[input or look *]
            docDate = calculateLastWorkingDate(dateFrom)
            record = PersonRecord(fullName, workDistrict, proffesion, docNr, docDate, sentCountry, dateFrom, dateTo)
           
            if record.hasAllFieldsFilled():
                self.personRecords.append(record)
                log([self.currentRowId, record.hasAllFieldsFilled(), record])
             
            self.currentRowId += 1
            previousFullName = fullName

    # def saveRowData(self, row):
        pass
        # Move creating person records to here
    
    def readCollumns(self):
        for i in range(1, 20):
            log("row: 1, col: {}, val: '{}'".format(i, self.getCellValue(6, i)))
    
    def generateSecondments(self):
        # Constants for placeholders, template name, mappings and parameters.
        c = SecondmentConstants()

        # Open template .docx file, to use in each following file creation
        doc = Document(c.TEMPLATE_NAME)
        try:
            os.mkdir(c.DOCUMENTS_DIR)
        except FileExistsError:
            pass

        # Index all placeholder locations in the template .docx file
        paragraphIdx = indexParagrahps(c)
        runIdx = indexRuns(c, paragraphIdx)
        
        for record in self.personRecords:
            createSecondmentDocument(record.returnRecordArray(), copy.deepcopy(doc), paragraphIdx, runIdx, c, True)

        
def log(msg):
    print("DEBUG: {}".format(msg))

def main():
    fileName = "../summary"
    month = 1
    sec = SecondmentGenerator(fileName, month)
    sec.readAllRows()
    sec.generateSecondments()
    
    #sec.readCollumns()
    
if __name__ == "__main__":
    main()
