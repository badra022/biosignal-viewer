from PyQt5 import QtCore
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import matplotlib.pyplot as plt
import numpy as np
import math

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

class spectrogram(object):
    windowIdx = 0
    spectrogramsWindows = []
    spectrogramPlotItems = []
    spectrogramImageItems = []
    spectrogramHistItems = []

    @classmethod
    def getLastWindow(cls):
        return cls.spectrogramsWindows[cls.windowIdx - 1]

    @classmethod
    def createSpectrogramWindow(cls):
        # Interpret image data as row-major instead of col-major
        pg.setConfigOptions(imageAxisOrder='row-major')

        pg.mkQApp()
        cls.spectrogramsWindows.append(pg.GraphicsLayoutWidget())
        # A plot area (ViewBox + axes) for displaying the image
        cls.spectrogramPlotItems.append(cls.spectrogramsWindows[cls.windowIdx].addPlot())
        # Add labels to the axis
        cls.spectrogramPlotItems[cls.windowIdx].setLabel('bottom', "Time", units='sec')
        # If you include the units, Pyqtgraph automatically scales the axis and adjusts the SI prefix (in this case kHz)
        # self.SpectrogramPlotItem.setLabel('left', "Frequency", units='Hz')

        # Item for displaying image data
        cls.spectrogramImageItems.append(pg.ImageItem())
        cls.spectrogramPlotItems[cls.windowIdx].addItem(cls.spectrogramImageItems[cls.windowIdx])
        # Add a histogram with which to control the gradient of the image
        cls.spectrogramHistItems.append(pg.HistogramLUTItem())
        # Link the histogram to the image
        cls.spectrogramHistItems[cls.windowIdx].setImageItem(cls.spectrogramImageItems[cls.windowIdx])

        cls.spectrogramHistItems[cls.windowIdx].gradient.restoreState({'mode': 'rgb','ticks': [(0.5, (0, 182, 188, 255)),
                                                            (1.0, (246, 111, 0, 255)),
                                                            (0.0, (75, 0, 113, 255))]})
        cls.spectrogramHistItems[cls.windowIdx].gradient.saveState()
        # If you don't add the histogram to the window, it stays invisible, but I find it useful.
        cls.spectrogramsWindows[cls.windowIdx].addItem(cls.spectrogramHistItems[cls.windowIdx])
        # Show the window
        cls.spectrogramsWindows[cls.windowIdx].show()    
        cls.windowIdx = cls.windowIdx + 1    

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
        self.__class__.timer.setInterval(100) # ms interval
        if self.__class__.freeChannelsNum > 0:
            self.channelIdx = len(graph.channels) - self.__class__.freeChannelsNum
            self.__class__.freeChannelsNum = self.__class__.freeChannelsNum - 1
            self.plot()
            self.plotSpectrogram()
            self.initSpectrogram()
        else:
            print("no free channel is available, clear channels first!")
        
    def __del__(self):
        try:
            graph.channels[self.channelIdx].clear()
            spectrogram.spectrogramImageItems[self.channelIdx].clear()
            self.__class__.freeChannelsNum = self.__class__.freeChannelsNum + 1
        except:
            pass
        
    def plot(self):
        graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])
        graph.channels[self.channelIdx].setYRange(-1 * self.zoomFactor , 1 * self.zoomFactor)
        self.pen = pg.mkPen(color=self.__class__.penColors[self.channelIdx])
        graph.channels[self.channelIdx].plot(self.time, self.amplitude, pen=self.pen)

    def moveGraph(self, speed):
        try:
            self.startTimeIdx = self.startTimeIdx + speed
            self.endTimeIdx = self.endTimeIdx + speed
            graph.channels[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])
        except:
            self.startTimeIdx = 0
            self.endTimeIdx = 100 * self.zoomFactor
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

    def initSpectrogram(self):
        # Scale the X and Y Axis to time and frequency (standard is pixels)
        spectrogram.spectrogramImageItems[self.channelIdx].scale(self.time[-1]/np.size(self.powerSpectrum, axis=1), math.pi/np.size(self.powerSpectrum, axis=0))
 
    def plotSpectrogram(self):
        fs = 1/(self.time[1] - self.time[0])
        self.powerSpectrum, self.freqenciesFound, _, _ = plt.specgram(self.amplitude, Fs=fs)
        # for more colormaps: https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
        # Sxx contains the amplitude for each pixel
        spectrogram.spectrogramImageItems[self.channelIdx].setImage(self.powerSpectrum)
    
    def moveSpectrogram(self):
        # Fit the min and max levels of the histogram to the data available
        # min = np.min(self.powerSpectrum)
        # max = np.max(self.powerSpectrum)
        # spectrogram.spectrogramHistItems[self.channelIdx].setLevels(min , max)
        spectrogram.spectrogramPlotItems[self.channelIdx].setXRange(self.time[self.startTimeIdx], self.time[self.endTimeIdx])