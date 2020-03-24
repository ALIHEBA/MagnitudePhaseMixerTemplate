from PyQt5 import QtWidgets
from <...> import Ui_MainWindow 
# replace <...> with your py file generate from pyuic5 command - without .py-

# It's preferaple to work on MainWindow in qt designer to support layouts
# use Dialog for relatively small windows or windows that don't have too much elements  

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import QApplication , QMainWindow ,QFileDialog,QLabel
from PyQt5.QtGui import QIcon
import numpy as np
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixamp
import cv2
from matplotlib import pyplot as plt
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"Task3.ui"))

from imageModel import ImageModel


class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self, parent = None):
          super(MainApp,self).__init__(parent)
          QMainWindow.__init__(self)
          self.setupUi(self)
          self.Browse.clicked.connect(self.pushButton_handler)
          self.View1_edit.toggled.connect(self.widget)
          self.Control_edit1.currentText()
          self.Control_edit1.currentTextChanged.connect(self.on_combobox_changed)
          self.Control_edit2.currentText()
          self.Control_edit2.currentTextChanged.connect(self.on_combobox_changed)
          self.Control_op1.currentText()
          self.Control_op1.currentTextChanged.connect(self.on_combobox_changed)
          self.Control_op2.currentText()
          self.Control_op2.currentTextChanged.connect(self.on_combobox_changed)
          self.View1.setPixmap(QPixmap(pixmap))
          self.View2.setPixmap(QPixmap(pixmap))
          self.resize(pixmap.width(), pixmap.height())
        
        def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()
          
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(self)
        path = filename[0]
        print(path)
        print(filename)
        View1 = QLabel(self)
        pixmap = QPixmap(os.getcwd() + 'self.filename.jpeg)  
        View1.setPixmap(pixmap)
        self.setCentralWidget(View1 )
        self.resize(pixmap.width(), pixmap.height()


    def magnitude_spectrum (self):
        img = cv2.imread('virus.jpeg',0)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        plt.subplot(121),plt.imshow(img, cmap = 'gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()

    def phase_spectrum (self):
        img = cv2.imread('virus.jpeg',0)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        np.angle(fshfit)
        phase_spectrum = 20*np.log(np.abs(fshift))
        plt.subplot(121),plt.imshow(img, cmap = 'gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        plt.title('phase Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()

    if  fshift = np.fft.fftshift(f):
        fshift.real=20*np.log(np.abs(fshift))
        fshift.imag=20*np.log(np.abs(fshift))
        plt.subplot(121),plt.imshow(img, cmap = 'gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        plt.title('phase Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
