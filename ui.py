# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from classes import graph, signal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 500, 274, 71))
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        
        self.startButton = QtWidgets.QPushButton(self.splitter)
        self.startButton.setObjectName("startButton")
        self.startButton.setIcon(QtGui.QIcon(QtGui.QPixmap("play.png")))
        
        self.stopButton = QtWidgets.QPushButton(self.splitter)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setIcon(QtGui.QIcon(QtGui.QPixmap("pause.png")))
        
        self.clearButton = QtWidgets.QPushButton(self.splitter)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setIcon(QtGui.QIcon(QtGui.QPixmap("eraser.png")))
        
        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        
        self.signalsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.signalsBox.setGeometry(QtCore.QRect(630, 10, 131, 151))
        self.signalsBox.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.signalsBox.setObjectName("signalsBox")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 611, 491))
        self.widget.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        
        graph.createPlotWidget()
        
        self.horizontalLayout_3.addWidget(graph.getLastChannel())
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)

        graph.createPlotWidget()
        
        self.horizontalLayout_4.addWidget(graph.getLastChannel())
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        
        graph.createPlotWidget()
        
        self.horizontalLayout_5.addWidget(graph.getLastChannel())
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        
        self.zoomIn = QtWidgets.QPushButton(self.widget)
        self.zoomIn.setObjectName("zoomIn")
        self.zoomIn.setIcon(QtGui.QIcon(QtGui.QPixmap("zoomin.png")))
        
        self.horizontalLayout.addWidget(self.zoomIn)
        
        self.zoomOut = QtWidgets.QPushButton(self.widget)
        self.zoomOut.setObjectName("zoomOut")
        self.zoomOut.setIcon(QtGui.QIcon(QtGui.QPixmap("zoomout.png")))
        
        self.horizontalLayout.addWidget(self.zoomOut)
                
        self.channelSelector = QtWidgets.QSpinBox(self.widget)
        self.channelSelector.setObjectName("channelSelector")
        
        self.horizontalLayout.addWidget(self.channelSelector)
        spacerItem10 = QtWidgets.QSpacerItem(500, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.open.setShortcut(QKeySequence("Ctrl+Shift+N"))        
        
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.save.setShortcut(QKeySequence("Ctrl+Shift+R"))
        
        self.menufile.addAction(self.open)
        self.menufile.addAction(self.save)
        self.menubar.addAction(self.menufile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "process control"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.clearButton.setText(_translate("MainWindow", "clear"))
        self.signalsBox.setTitle(_translate("MainWindow", "signals"))
        self.zoomIn.setText(_translate("MainWindow", "Zoom  in"))
        self.zoomOut.setText(_translate("MainWindow", "Zoom out"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.open.setText(_translate("MainWindow", "open"))
        self.save.setText(_translate("MainWindow", "save"))
        