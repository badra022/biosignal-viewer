from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import matplotlib.pyplot as plt

class graph(object):
    channelIdx = 0
    channels = []
    styles = {'color':'b', 'font-size':'10px'}   
    
    @classmethod 
    def createPlotWidget(cls):
        cls.channels.append(pg.PlotWidget())
        cls.channels[cls.channelIdx].setBackground('w')
        cls.channels[cls.channelIdx].setStyleSheet("background-color: rgb(255, 255, 255);")
        cls.channels[cls.channelIdx].setObjectName("channel_1")
        cls.channels[cls.channelIdx].setLabel('left', 'Amplitude', **cls.styles)
        cls.channels[cls.channelIdx].setLabel('bottom', 'time (sec)', **cls.styles)
        cls.channels[cls.channelIdx].showGrid(x=True, y=True)
        cls.channels[cls.channelIdx].setXRange(0, 0.7)
        cls.channelIdx = cls.channelIdx + 1
        
    @classmethod
    def getLastChannel(cls):
        return cls.channels[cls.channelIdx - 1]

class signal(object):
    timer = QtCore.QTimer() 

    freeChannelsNum = 3
    
    def __init__(self, x, y):
        self.time = x.copy()
        self.amplitude = y.copy()
        self.startTimeIdx = 0
        self.endTimeIdx = 100
        self.__class__.timer.setInterval(10) # ms interval
        # self.__class__.timer.timeout.connect(signal.moveGraph)
        self.pen = pg.mkPen(color=(255, 0, 0))
        if self.__class__.freeChannelsNum > 0:
            self.channelIdx = len(graph.channels) - self.__class__.freeChannelsNum
            self.__class__.freeChannelsNum = self.__class__.freeChannelsNum - 1
            self.plot()
        else:
            print("no free channel is available, clear channels first!")
        # print("free channels number: ",self.__class__.freeChannelsNum )
        
    def __del__(self):
        try:
            graph.channels[self.channelIdx].clear()
            self.__class__.freeChannelsNum = self.__class__.freeChannelsNum + 1
        except:
            pass
        
    def plot(self):
        graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])
        self.channel_reference = graph.channels[self.channelIdx].plot(self.time, self.amplitude, pen=self.pen)
        

    def moveGraph(self):
        self.startTimeIdx = self.startTimeIdx + 1 % (len(self.time) - 100)
        self.endTimeIdx = self.endTimeIdx + 1 % len(self.time)
        graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])
    
    def getFigure(self):
        fig = plt.figure()
        fig.plot(self.time,self.amplitude)
        return fig