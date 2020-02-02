import os
from autoSecondment.generatorUtils.secondmentUtils import loadJsonData

class Constants:
    """
    Data class to load
    and store constants from file
    """
    TEMPLATE_NAME = ""
    INVALID_GA = []
    INVALID_SPEC = []
    COUNTRIES = []
    TIKSLAS = ""
    DOCUMENTS_DIR = ""
    FAILED_DOCUMENTS_DIR = ""
    FILE_DIR = ""
    GALININKO_LINKSNIAI = {}
    MONTHS = {}
    GA1 = {}
    GA2 = {}
    PROFESIJA = {}
    DIENPINIGIAI = {}
    KEYS = {}

    def __init__(self):
        self.TEMPLATE_NAME = "autoSecondment/generatorUtils/template.docx"
        self.INVALID_GA = ["ADM","GTS"]
        self.INVALID_SPEC = ["pavad.","sauga","techn.", "vadov.", "pat"]
        self.COUNTRIES = ["Švedija", "Prancūzija", "Belgija", "Šveicarija", "Vokietija", "Latvija", "Ryga", "Lenkija", "Estija", "Nyderlandai", "Olandija", "Suomija", "Danija"]
        self.TIKSLAS = "Atlikti paskirtus darbus objekte %s pagal sutartį."
        self.DOCUMENTS_DIR = "Komandiruočių Įsakymai"
        self.FAILED_DOCUMENTS_DIR = "Negarantuoti Komandiruočių Įsakymai"
        self.FILE_DIR = os.getcwd()
        self.GALININKO_LINKSNIAI, self.MONTHS, self.GA1, self.GA2, self.PROFESIJA, self.DIENPINIGIAI, self.KEYS = loadJsonData()
