# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 362)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainPage_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.MainPage_tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainPage_tab.setSizeIncrement(QtCore.QSize(100, 0))
        self.MainPage_tab.setObjectName("MainPage_tab")
        self.tab_a1 = QtWidgets.QWidget()
        self.tab_a1.setObjectName("tab_a1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_a1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.initA1MainPage_button = QtWidgets.QPushButton(self.tab_a1)
        self.initA1MainPage_button.setObjectName("initA1MainPage_button")
        self.verticalLayout.addWidget(self.initA1MainPage_button)
        self.ReloadConfig_button = QtWidgets.QPushButton(self.tab_a1)
        self.ReloadConfig_button.setObjectName("ReloadConfig_button")
        self.verticalLayout.addWidget(self.ReloadConfig_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.FillA1MainPage_button = QtWidgets.QPushButton(self.tab_a1)
        self.FillA1MainPage_button.setCheckable(False)
        self.FillA1MainPage_button.setDefault(False)
        self.FillA1MainPage_button.setFlat(False)
        self.FillA1MainPage_button.setObjectName("FillA1MainPage_button")
        self.verticalLayout.addWidget(self.FillA1MainPage_button)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FillPerson_button = QtWidgets.QPushButton(self.tab_a1)
        self.FillPerson_button.setObjectName("FillPerson_button")
        self.horizontalLayout_3.addWidget(self.FillPerson_button)
        self.NextPerson_button = QtWidgets.QPushButton(self.tab_a1)
        self.NextPerson_button.setObjectName("NextPerson_button")
        self.horizontalLayout_3.addWidget(self.NextPerson_button)
        self.PreviousPerson_button = QtWidgets.QPushButton(self.tab_a1)
        self.PreviousPerson_button.setObjectName("PreviousPerson_button")
        self.horizontalLayout_3.addWidget(self.PreviousPerson_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.A1nextPersonStatus_label = QtWidgets.QLabel(self.tab_a1)
        self.A1nextPersonStatus_label.setObjectName("A1nextPersonStatus_label")
        self.verticalLayout.addWidget(self.A1nextPersonStatus_label)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.MainPage_tab.addTab(self.tab_a1, "")
        self.tab_copy_summary = QtWidgets.QWidget()
        self.tab_copy_summary.setObjectName("tab_copy_summary")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_copy_summary)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.initSummaryMainPage_button = QtWidgets.QPushButton(self.tab_copy_summary)
        self.initSummaryMainPage_button.setObjectName("initSummaryMainPage_button")
        self.verticalLayout_2.addWidget(self.initSummaryMainPage_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.SummaryFileName_line = QtWidgets.QLineEdit(self.tab_copy_summary)
        self.SummaryFileName_line.setText("Naujausia-kom.-suvestinė-2019m.xlsx")
        self.SummaryFileName_line.setObjectName("SummaryFileName_line")
        self.verticalLayout_2.addWidget(self.SummaryFileName_line)
        self.SummaryMonth_dropdown = QtWidgets.QComboBox(self.tab_copy_summary)
        self.SummaryMonth_dropdown.setMaxVisibleItems(12)
        self.SummaryMonth_dropdown.setObjectName("SummaryMonth_dropdown")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.SummaryMonth_dropdown.addItem("")
        self.verticalLayout_2.addWidget(self.SummaryMonth_dropdown)
        self.SummaryCopy_button = QtWidgets.QPushButton(self.tab_copy_summary)
        self.SummaryCopy_button.setObjectName("SummaryCopy_button")
        self.verticalLayout_2.addWidget(self.SummaryCopy_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.MainPage_tab.addTab(self.tab_copy_summary, "")
        self.generate_secondments = QtWidgets.QWidget()
        self.generate_secondments.setObjectName("generate_secondments")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.generate_secondments)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.initSecondmentGenerateMainPage_button = QtWidgets.QPushButton(self.generate_secondments)
        self.initSecondmentGenerateMainPage_button.setObjectName("initSecondmentGenerateMainPage_button")
        self.verticalLayout_4.addWidget(self.initSecondmentGenerateMainPage_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.SecondmentSummaryFileName_line = QtWidgets.QLineEdit(self.generate_secondments)
        self.SecondmentSummaryFileName_line.setText("Naujausia-kom.-suvestinė-2019m.xlsx")
        self.SecondmentSummaryFileName_line.setObjectName("SecondmentSummaryFileName_line")
        self.verticalLayout_4.addWidget(self.SecondmentSummaryFileName_line)
        self.SecondmentSummaryMonth_dropdown = QtWidgets.QComboBox(self.generate_secondments)
        self.SecondmentSummaryMonth_dropdown.setMaxVisibleItems(12)
        self.SecondmentSummaryMonth_dropdown.setObjectName("SecondmentSummaryMonth_dropdown")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.SecondmentSummaryMonth_dropdown.addItem("")
        self.verticalLayout_4.addWidget(self.SecondmentSummaryMonth_dropdown)
        self.SecondmentGenerate_button = QtWidgets.QPushButton(self.generate_secondments)
        self.SecondmentGenerate_button.setObjectName("SecondmentGenerate_button")
        self.verticalLayout_4.addWidget(self.SecondmentGenerate_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.MainPage_tab.addTab(self.generate_secondments, "")
        self.horizontalLayout.addWidget(self.MainPage_tab)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.EventLog_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.EventLog_listWidget.setObjectName("EventLog_listWidget")
        self.verticalLayout_3.addWidget(self.EventLog_listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainPage_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.FillA1MainPage_button, self.SummaryFileName_line)
        MainWindow.setTabOrder(self.SummaryFileName_line, self.SummaryMonth_dropdown)
        MainWindow.setTabOrder(self.SummaryMonth_dropdown, self.SummaryCopy_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutomateDocs"))
        self.initA1MainPage_button.setText(_translate("MainWindow", "Pradėti"))
        self.ReloadConfig_button.setText(_translate("MainWindow", "Perkrauti nustatymus"))
        self.FillA1MainPage_button.setToolTip(_translate("MainWindow", "Užpildyti naujos A1 formos pradinį puslapį"))
        self.FillA1MainPage_button.setText(_translate("MainWindow", "Užpildyti A1 pradinį puslapį"))
        self.FillPerson_button.setToolTip(_translate("MainWindow", "Pridėkite naują anketą o tada paspauskite kad jį būtų užpildyta su sekančio asmens informacija"))
        self.FillPerson_button.setText(_translate("MainWindow", "Užpildyti asmens anketą"))
        self.NextPerson_button.setToolTip(_translate("MainWindow", "Pasirinkti sekantį asmenį iš sąrašo"))
        self.NextPerson_button.setText(_translate("MainWindow", "Sekantis asmuo"))
        self.PreviousPerson_button.setText(_translate("MainWindow", "Praeitas asmuo"))
        self.A1nextPersonStatus_label.setText(_translate("MainWindow", "Nėra pasirinkto žmogaus"))
        self.MainPage_tab.setTabText(self.MainPage_tab.indexOf(self.tab_a1), _translate("MainWindow", "A1 pildymas"))
        self.initSummaryMainPage_button.setText(_translate("MainWindow", "Pradėti"))
        self.SummaryMonth_dropdown.setItemText(0, _translate("MainWindow", "Sausis"))
        self.SummaryMonth_dropdown.setItemText(1, _translate("MainWindow", "Vasaris"))
        self.SummaryMonth_dropdown.setItemText(2, _translate("MainWindow", "Kovas"))
        self.SummaryMonth_dropdown.setItemText(3, _translate("MainWindow", "Balandis"))
        self.SummaryMonth_dropdown.setItemText(4, _translate("MainWindow", "Gegužė"))
        self.SummaryMonth_dropdown.setItemText(5, _translate("MainWindow", "Birželis"))
        self.SummaryMonth_dropdown.setItemText(6, _translate("MainWindow", "Liepa"))
        self.SummaryMonth_dropdown.setItemText(7, _translate("MainWindow", "Rugpjūtis"))
        self.SummaryMonth_dropdown.setItemText(8, _translate("MainWindow", "Rugsėjis"))
        self.SummaryMonth_dropdown.setItemText(9, _translate("MainWindow", "Spalis"))
        self.SummaryMonth_dropdown.setItemText(10, _translate("MainWindow", "Lapkritis"))
        self.SummaryMonth_dropdown.setItemText(11, _translate("MainWindow", "Gruodis"))
        self.SummaryCopy_button.setText(_translate("MainWindow", "Nukopijuoti duomenis į sekantį mėnesį"))
        self.MainPage_tab.setTabText(self.MainPage_tab.indexOf(self.tab_copy_summary), _translate("MainWindow", "Suvestinės pildymas"))
        self.initSecondmentGenerateMainPage_button.setText(_translate("MainWindow", "Pradėti"))
        self.SecondmentSummaryMonth_dropdown.setItemText(0, _translate("MainWindow", "Sausis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(1, _translate("MainWindow", "Vasaris"))
        self.SecondmentSummaryMonth_dropdown.setItemText(2, _translate("MainWindow", "Kovas"))
        self.SecondmentSummaryMonth_dropdown.setItemText(3, _translate("MainWindow", "Balandis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(4, _translate("MainWindow", "Gegužė"))
        self.SecondmentSummaryMonth_dropdown.setItemText(5, _translate("MainWindow", "Birželis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(6, _translate("MainWindow", "Liepa"))
        self.SecondmentSummaryMonth_dropdown.setItemText(7, _translate("MainWindow", "Rugpjūtis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(8, _translate("MainWindow", "Rugsėjis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(9, _translate("MainWindow", "Spalis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(10, _translate("MainWindow", "Lapkritis"))
        self.SecondmentSummaryMonth_dropdown.setItemText(11, _translate("MainWindow", "Gruodis"))
        self.SecondmentGenerate_button.setText(_translate("MainWindow", "Generuoti įsakymų dokumentus"))
        self.MainPage_tab.setTabText(self.MainPage_tab.indexOf(self.generate_secondments), _translate("MainWindow", "Įsakymų generavimas"))
        self.label.setText(_translate("MainWindow", "Įvykiai:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
