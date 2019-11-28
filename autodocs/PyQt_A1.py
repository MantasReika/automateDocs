from PyQt5 import QtWidgets
from autoUI import MainView as MainViewUI
import sys

from autoA1.a1 import A1Auto
from autoSummary.Summary import Summary as SummaryAuto

class ApplicationWindow(QtWidgets.QMainWindow, MainViewUI.Ui_MainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.setupUi(self)
        
        self.enableA1Forms(False)
        self.enableSummaryForms(False)
        
        self.initA1MainPage_button.released.connect(self.initA1)
        
        self.initSummaryMainPage_button.released.connect(self.initSummary)
        
    def enableA1Forms(self, mode):
        self.FillA1MainPage_button.setEnabled(mode)
        self.FillNextPersonForm_button.setEnabled(mode)
        self.initA1MainPage_button.setEnabled(not mode)

    def enableSummaryForms(self, mode):
        self.SummaryFileName_line.setEnabled(mode)
        self.SummaryMonth_dropdown.setEnabled(mode)
        self.SummaryCopy_button.setEnabled(mode)
        self.initSummaryMainPage_button.setEnabled(not mode)

    def initA1(self):
        self.A1 = A1Auto()
        self.FillA1MainPage_button.released.connect(self.A1.fillA1Page)
        self.FillNextPersonForm_button.released.connect(self.A1.fillA1Form)
        self.enableA1Forms(True)

    def initSummary(self):
        self.SummaryCopy_button.released.connect(self.copySummary)
        self.enableSummaryForms(True)


    def copySummary(self):
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
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()