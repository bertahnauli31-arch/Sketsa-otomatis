from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QThread
import sys
import cv2
import imutils
from ProcessImage import ProcessImage
class pintUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(pintUi, self).__init__()
        uic.loadUi('main.ui', self)

        ## add code here
        self.fileName = None
        self.tmp = None
        self.cannyslider1 = 0
        self.cannyslider2 = 0

        self.processImage = ProcessImage()

        ## signal and slots
        self.loadButton.clicked.connect(self.loadImage)
        self.mulaiButton.clicked.connect(self.saveImage)

        self.slider1.valueChanged['int'].connect(self.thresholdValue1)
        self.slider2.valueChanged['int'].connect(self.thresholdValue2)
        
        self.pushButton_3.clicked.connect(self.initPainting)
        
        #Thread
        self.paintThread = None
        self.show()

    def loadImage(self):
        """
        load user selected photo and set to label
        """
        self.fileName = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        if not self.fileName:
            return
        
        self.img = cv2.imread(self.fileName)
        self.processImage.loadImage(self.img)
        self.setPhoto(self.img)

    def setPhoto(self, image):
        """
        set photo over label
        """
        self.tmp = image
        image = imutils.resize(image, height=590)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def saveImage(self):
        pass

    def thresholdValue1(self, value):
        self.cannyslider1 = value
        print(f"Thresh 1: {value}")
        self.update()

    def thresholdValue2(self, value):
        self.cannyslider2 = value
        print(f"Thresh 2: {value}")
        self.update()

    def update(self):
        if not self.fileName:
            print("Select Image First")
            return
        
        self.setPhoto(self.processImage.refreshImage(self.cannyslider1, self.cannyslider2))

    def initPainting(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)


        msg.setWindowTitle("Important Information")
        msg.setText("Automated Painiting is about to start!!!")

        msg.setInformativeText("Make sure Paint app is open-and-visible. \n\n Select-the-pencil-tool-1\\nTo stop the code press CTRL + ALT + Del")
        #msg.setDetailedText("To-stop-the-code-press-CTRL+ALT+Del")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        if retval==1024:
            self.paintThread = None
            def initPaintingThread():
                self.processImage.startPaint()
            self.paintThread = QThread()
            self.paintThread.started.connect(initPaintingThread)
            self.paintThread.start()

app = QtWidgets.QApplication(sys.argv)
window = pintUi()
app.exec_()
