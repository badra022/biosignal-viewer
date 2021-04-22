###########################################################
# authors: Ahmed Badra,
#          Hassan Hosni,
#          Yousof Elhely,
#          Moamen Gamal
#
# title: Biosignal viewer
#
# file: main program file (RUN THIS FILE)
############################################################


# libraries needed for main python file
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from gui import Ui_MainWindow
import numpy as np
import os
import pathlib
from matplotlib.backends.backend_pdf import PdfPages
from classes import signal


# class definition for application window components like the ui
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.channelSelector.setRange(1, 3)   # setting range to the spin box
        self.ui.open.triggered.connect(self.open)
        self.ui.clearButton.clicked.connect(self.clearChannels)
        self.ui.startButton.clicked.connect(self.startChannels)
        self.ui.stopButton.clicked.connect(self.stopChannels)
        self.ui.zoomIn.clicked.connect(self.zoomIn)
        self.ui.zoomOut.clicked.connect(self.zoomOut)
        self.ui.save.triggered.connect(self.saveAs)
        signal.timer.timeout.connect(self.moveSignals)    
        self.signals = []

    def zoomIn(self):
            try:
                self.signals[(self.ui.channelSelector.value() - 1) % 4].zoomIn()
            except:
                pass
    def zoomOut(self):
            try:
                self.signals[(self.ui.channelSelector.value() - 1) % 4].zoomOut()
            except:
                pass
    def open(self):
        files_name = QtGui.QFileDialog.getOpenFileName( self, 'Open only txt or CSV or xls', os.getenv('HOME') ,"csv(*.csv);; text(*.txt) ;; xls(*.xls)" )
        path = files_name[0]

        if pathlib.Path(path).suffix == ".txt" :
            data = np.genfromtxt(path, delimiter = ',')
            x= data[: , 0]
            y =data[: , 1] 
            x= list(x[:])
            y= list(y[:])
            self.signals.append(signal(x, y))
        elif pathlib.Path(path).suffix == ".csv" :
            data = np.genfromtxt(path, delimiter = ' ')
            x= data[: , 0]
            y =data[: , 1] 
            x= list(x[:])
            y= list(y[:])
            self.signals.append(signal(x, y))
        elif pathlib.Path(path).suffix == ".xls" :
            data = np.genfromtxt(path, delimiter = ',')
            x= data[: , 0]
            y =data[: , 1] 
            x= list(x[:])
            y= list(y[:])
            self.signals.append(signal(x, y))

    def moveSignals(self):
        for signal in self.signals:
            signal.moveGraph(self.ui.speedSelector.value())
        
    def clearChannels(self):
        while len(self.signals):
            self.signals.pop()
            
    def startChannels(self):
        signal.timer.start()
        
    def stopChannels(self):
        signal.timer.stop()

    def saveAs(self):
        report = PdfPages('report.pdf')
        for signal in self.signals:
            report.savefig(signal.getFigure())
            report.savefig(signal.getSpectrogram())
        report.close()

# function for launching a QApplication and running the ui and main window
def window():
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win.show()
    sys.exit(app.exec_())


# main code
if __name__ == "__main__":
    window()

