import logging
import os

def startLogger(logFileName="app.log"):
    logging.getLogger().setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

    fh = logging.FileHandler(logFileName, mode='w')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    logging.getLogger().addHandler(ch)
    logging.getLogger().addHandler(fh)

def formLogHtml(logFileName="app.log"):
    htmlHeader = """ <meta http-equiv='Content-Type' content='text/html; charset=windows-1257'>
    <style>
        table, th, td { border: 1px solid black; border-collapse: collapse; }
        .warning td { background-color: #F0B27A; }
        .error td { background-color: #F1948A; }
        .header { background-color: #BDC3C7; }
    </style>
    <h2>Results</h2>
    <p>Please check error/warn details bellow.<br>
    <table style='width:100%'>
"""

    os.chdir("C:/Users/s3223b/Work Folders/Documents/PythonWorkspace/AutomateDocs/AutomateDocs/autodocs")
    with open('SecondmentLog.html', 'w+') as htmlFile:
        htmlFile.write(htmlHeader)
        htmlFile.write("<tr class='header'><th>Level</th><th>Message</th><th>Error</th></tr>")
        with open(logFileName, 'r') as logFile:
            for logEntry in logFile:
                try:
                    logLevel = logEntry.split('|')[1]
                    if logLevel == 'INFO' or logLevel == 'DEBUG':
                        continue
                    logTime = logEntry.split('|')[0]
                    logMessage = ";".join(logEntry.split('|')[2].split(';')[:-1])
                    logError = logEntry.split(';')[-1]

                    htmlFile.write("<tr class='{}'><td>{}</td><td>{}</td><td>{}</td></tr>".format(logLevel.lower(), logLevel.upper(), logMessage, logError))
                except IndexError as e:
                    htmlFile.write("<tr class='{}'><td>{}</td><td>{}</td><td>-</td></tr>".format("error".lower(), "error".upper(), logEntry))

        htmlFile.write("</table>")

def getLogEntries(errorLevels, logFileName="app.log"):
    entries = []
    with open(logFileName, 'r') as logFile:
        for logEntry in logFile:
            logLevel = logEntry.split('|')[1]
            if logLevel in errorLevels.split(','):
                logMessage = ";".join(logEntry.split('|')[1:])
                entries.append(logMessage.strip())
    return entries