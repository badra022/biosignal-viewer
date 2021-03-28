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
    penColors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] 

    freeChannelsNum = 3
    
    def __init__(self, x, y):
        self.time = x.copy()
        self.amplitude = y.copy()
        self.zoomFactor = 1
        self.startTimeIdx = 0
        self.startAmpIdx = -1 * self.zoomFactor
        self.endTimeIdx = 100 * self.zoomFactor
        self.endAmpIdx = 1 * self.zoomFactor
        self.__class__.timer.setInterval(30) # ms interval
        if self.__class__.freeChannelsNum > 0:
            self.channelIdx = len(graph.channels) - self.__class__.freeChannelsNum
            self.__class__.freeChannelsNum = self.__class__.freeChannelsNum - 1
            self.plot()
        else:
            print("no free channel is available, clear channels first!")
        
    def __del__(self):
        try:
            graph.channels[self.channelIdx].clear()
            self.__class__.freeChannelsNum = self.__class__.freeChannelsNum + 1
        except:
            pass
        
    def plot(self):
        graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])
        graph.channels[self.channelIdx].setYRange(-1 * self.zoomFactor , 1 * self.zoomFactor)
        self.pen = pg.mkPen(color=self.__class__.penColors[self.channelIdx])
        graph.channels[self.channelIdx].plot(self.time, self.amplitude, pen=self.pen)

    def moveGraph(self):
        self.startTimeIdx = (self.startTimeIdx + 1) % (len(self.time) - 100)
        self.endTimeIdx = self.endTimeIdx + 1 % len(self.time)
        graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])

    def zoomIn(self):
        if self.zoomFactor >= 0.2:
            self.zoomFactor = self.zoomFactor - 0.1
            self.adjustGraph()
    def zoomOut(self):
        if self.zoomFactor < 2.0:
            self.zoomFactor = self.zoomFactor + 0.1
            self.adjustGraph()
            
    def adjustGraph(self):
        self.endTimeIdx = int(self.startTimeIdx + (100 * self.zoomFactor))
        graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])
        graph.channels[self.channelIdx].setYRange(-1 * self.zoomFactor , 1 * self.zoomFactor)
        
    def getFigure(self):
        fig = plt.figure(figsize=(10, 5))
        plt.plot(self.time[self.startTimeIdx:self.endTimeIdx],self.amplitude[self.startTimeIdx:self.endTimeIdx])
        plt.xlabel('time (sec)')
        plt.ylabel('amplitude (mv)')
        return fig
    
    def getSpectrogram(self):
        fs = 1/(self.time[1] - self.time[0])
        fig = plt.figure(figsize=(10, 5))
        plt.specgram(self.amplitude, Fs= fs)
        plt.xlabel('time (sec)')
        plt.ylabel('frequency (Hz)')
        return fig