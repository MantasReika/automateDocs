import logging
import sys

from PyQt5 import QtWidgets
from autoUI import MainView as MainViewUI

import Logger
from autoA1.a1 import A1Auto
from autoSummary.Summary import Summary as SummaryAuto
from autoSecondment.SecondmentGenerator import SecondmentGenerator
from autoSecondment.generatorUtils.SummaryReader import SummaryReader

class ApplicationWindow(QtWidgets.QMainWindow, MainViewUI.Ui_MainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setupUi(self)
        
        self.enableA1Forms(False)
        self.enableSummaryForms(False)
        self.enableSecondmentForms(False)
        
        self.initA1MainPage_button.released.connect(self.initA1)
        
        self.initSummaryMainPage_button.released.connect(self.initSummary)
        
        self.initSecondmentGenerateMainPage_button.released.connect(self.initSecondment)
        
    def logEvent(self, message):
        self.EventLog_listWidget.addItem(QtWidgets.QListWidgetItem(message))

    def enableA1Forms(self, mode):
        self.initA1MainPage_button.setEnabled(not mode)
        self.FillA1MainPage_button.setEnabled(mode)
        self.FillPerson_button.setEnabled(mode)
        self.NextPerson_button.setEnabled(mode)
        self.ReloadConfig_button.setEnabled(mode)
        self.PreviousPerson_button.setEnabled(mode)

    def enableSummaryForms(self, mode):
        self.initSummaryMainPage_button.setEnabled(not mode)
        self.SummaryFileName_line.setEnabled(mode)
        self.SummaryMonth_dropdown.setEnabled(mode)
        self.SummaryCopy_button.setEnabled(mode)

    def enableSecondmentForms(self, mode):
        self.initSecondmentGenerateMainPage_button.setEnabled(not mode)
        self.SecondmentSummaryFileName_line.setEnabled(mode)
        self.SecondmentSummaryMonth_dropdown.setEnabled(mode)
        self.SecondmentGenerate_button.setEnabled(mode)
    
    def initA1(self):
        self.A1 = A1Auto()
        
        self.FillA1MainPage_button.released.connect(self.A1.fillA1Page)
        self.FillPerson_button.released.connect(self.fillNextA1Form)
        self.NextPerson_button.released.connect(self.findNextPerson)
        self.PreviousPerson_button.released.connect(self.findPreviousPerson)
        self.ReloadConfig_button.released.connect(self.reloadConfig)
        self.enableA1Forms(True)

    def reloadConfig(self):
        self.A1.loadConfig(self.A1.configPath)
        self.A1.loadDataFiles()
        popupInfo = PopupInfo("Success", "Reloaded configuration from: {}".format(self.A1.configPath))
    
    def fillNextA1Form(self):
        if self.A1.isPersonAvailable():
            self.A1.fillA1Form()
        
    def findNextPerson(self):
        self.A1.nextPerson()
        if not self.A1.isPersonCurrentlySelected:
            self.A1nextPersonStatus_label.setText("Nėra sekančio asmens")
            return
        elif not self.A1.isPersonFoundInDB:
            self.A1nextPersonStatus_label.setText("'{} {}' nerastas duombazėje".format(self.A1.person_Surname, self.A1.person_Forename))
            return
            
        self.A1nextPersonStatus_label.setText("Dabar pasirinktas asmuo: '{} {}'".format(self.A1.person_Surname, self.A1.person_Forename))
        QtWidgets.qApp.processEvents()
    
    def findPreviousPerson(self):
        self.A1.previousPerson()
        if not self.A1.isPersonCurrentlySelected:
            self.A1nextPersonStatus_label.setText("Nėra praeito asmens")
            return
        elif not self.A1.isPersonFoundInDB:
            self.A1nextPersonStatus_label.setText("'{} {}' nerastas duombazėje".format(self.A1.person_Surname, self.A1.person_Forename))
            return
            
        self.A1nextPersonStatus_label.setText("Dabar pasirinktas asmuo: '{} {}'".format(self.A1.person_Surname, self.A1.person_Forename))
        QtWidgets.qApp.processEvents()
                
    def initSummary(self):
        self.SummaryCopy_button.released.connect(self.runSummary)
        self.enableSummaryForms(True)

    def runSummary(self):
        fileName = self.SummaryFileName_line.text()
        currentMonth = int(self.SummaryMonth_dropdown.currentIndex()) + 1
        
        try:
            summ = SummaryAuto(fileName, currentMonth)
            summ.isValidStructuredDocument()
            summ.processRows()
            summ.saveFile()
            popupInfo = PopupInfo("Success", "New file generated:\n{}".format(summ.newFileName))
        except FileNotFoundError:
            popupError = PopupError("File not found", fileName)
            self.logEvent("File '{}' not found".format(fileName))
        except Exception as e:
            logging.error("Failed to copy summary file='{}', currentMonth='{}'; error: {}".format(fileName, currentMonth, e))
            self.logEvent("Failed to copy summary file='{}', currentMonth='{}'".format(file, currentMonth))

    def initSecondment(self):
        self.SecondmentGenerate_button.released.connect(self.runSecondments)
        self.enableSecondmentForms(True)
        
    def runSecondments(self):
        self.EventLog_listWidget.clear()
        fileName = self.SecondmentSummaryFileName_line.text()
        currentMonth = int(self.SecondmentSummaryMonth_dropdown.currentIndex()) + 1
        logging.info("Secondment parameters: secondmentfileName={}, currentMonth={}".format(fileName, currentMonth))
        
        try:
            summaryReader = SummaryReader()
            summaryReader.openSummaryFile(fileName, currentMonth)
            summaryReader.setSummaryRelativeCollumn(currentMonth)
            summaryReader.readInPersonRecords()
        except FileNotFoundError as e:
            popupError = PopupError("File not found", fileName)
            self.logEvent("File not found")
            return

        sec = SecondmentGenerator()
        sec.setPersonRecords(summaryReader.getPersonRecords())
        sec.generateSecondments()
        Logger.formLogHtml()
        for err in Logger.getLogEntries("WARNING,ERROR"):
            self.logEvent(err)


class PopupError():
    def __init__(self, errorName, errorMessage):
        popupError = QtWidgets.QMessageBox()
        popupError.setModal(True)
        popupError.setIcon(QtWidgets.QMessageBox.Critical)
        popupError.setWindowTitle('Error: {}'.format(errorName))
        popupError.setText(errorName)
        popupError.setInformativeText("{}".format(errorMessage))
        popupError.setStandardButtons(QtWidgets.QMessageBox.Ok)
        popupError.exec_()
        
class PopupInfo():
    def __init__(self, infoName, infoMessage):
        popupInfo = QtWidgets.QMessageBox()
        popupInfo.setModal(True)
        popupInfo.setIcon(QtWidgets.QMessageBox.Information)
        popupInfo.setWindowTitle('Info: {}'.format(infoName))
        popupInfo.setText(infoName)
        popupInfo.setInformativeText("{}".format(infoMessage))
        popupInfo.setStandardButtons(QtWidgets.QMessageBox.Ok)
        popupInfo.exec_()


def main():
    Logger.startLogger()
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()