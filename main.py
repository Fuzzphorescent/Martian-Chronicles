import requests
import json
import Constants
import ezgmail, os
os.chdir(r'./')
ezgmail.init()
import urllib.request

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):

    photoLinks = []
    pos = 0
    loaded = []
    centralwidget = None
    emailid = ''
    subject = ''
    emailbody = ''
    emages = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 579)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 0, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 46, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 38, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 21, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 0, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 0, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 46, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 38, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 21, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 0, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(71, 0, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 46, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 38, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 21, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(18, 15, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 31, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.mypopup = QtWidgets.QMainWindow()
        self.popupcontent = QtWidgets.QWidget(self.mypopup)
        self.popupcontent = QtWidgets.QWidget(MainWindow)
        self.popupcontent.setObjectName("popupcontent")
        self.popupcontent.setGeometry(QtCore.QRect(210, 44, 131, 61))
        self.popupcontent.setWindowTitle("Something")
        self.mypopup.setCentralWidget(self.popupcontent)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(210, 44, 131, 61))
        self.centralwidget.setWindowTitle("Something")
        self.messagebox = QtWidgets.QMessageBox()
        self.messagebox.setText("Something")
        self.messagebox.setWindowTitle("Something")
        self.EarthDate = QtWidgets.QLabel(self.centralwidget)
        self.EarthDate.setGeometry(QtCore.QRect(210, 44, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.EarthDate.setFont(font)
        self.centralwidget.setFont(font)
        self.EarthDate.setObjectName("EarthDate")
        self.Camera = QtWidgets.QLabel(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(210, 104, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Camera.setFont(font)
        self.Camera.setObjectName("Camera")
        self.CameraSelector = QtWidgets.QComboBox(self.centralwidget)
        self.CameraSelector.setGeometry(QtCore.QRect(390, 104, 86, 25))

        

        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.CameraSelector.setFont(font)
        self.CameraSelector.setObjectName("CameraSelector")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.addItem("")
        self.CameraSelector.setItemText(7, "")
        self.DateSelector = QtWidgets.QDateEdit(self.centralwidget)

        self.DateSelector.setGeometry(QtCore.QRect(370, 64, 110, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.DateSelector.setFont(font)
        self.DateSelector.setObjectName("DateSelector")
        self.Load = QtWidgets.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(270, 144, 131, 25))
        self.Load.clicked.connect(lambda: self.load(self.DateSelector, self.CameraSelector))

        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Load.setFont(font)
        self.Load.setObjectName("Load")
        self.Previous = QtWidgets.QPushButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(130, 484, 101, 31))
        self.Previous.clicked.connect(self.previous)

        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Previous.setFont(font)
        self.Previous.setObjectName("Previous")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(430, 484, 111, 31))
        self.Next.clicked.connect(self.next)

        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Next.setFont(font)
        self.Next.setObjectName("Next")
        self.Share = QtWidgets.QPushButton(self.centralwidget)
        self.Share.setGeometry(QtCore.QRect(270, 484, 131, 31))
        self.Share.clicked.connect(self.share)

        font = QtGui.QFont()
        font.setFamily(
            "Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Share.setFont(font)
        self.Share.setObjectName("Share")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(130, 234, 411, 211))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Image.setFont(font)
        self.Image.setScaledContents(True)
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(170, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def fetch(self):
        global photoLinks
        urllib.request.urlretrieve(self.photoLinks[self.pos + 5], "%s.jpg" % (self.pos + 5))
        

    def load(self, DS, CS):

        # retrieve json from API

        earthDate = str(DS.date().toPyDate())
        camera = CS.currentText()
        key = Constants.NASA_API_KEY
        link = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=' + key + '&earth_date=' + earthDate + '&name=' + camera
        print(link)
        Result = json.loads(requests.get(link).text)

        # store image links

        n = len(Result['photos'])
        print(n)
        global photoLinks
        global pos
        global loaded
        for i in range(n):
            self.photoLinks.append(Result['photos'][i]["img_src"])
        print(self.photoLinks[0])
    
        # download first five images
        n = min(len(self.photoLinks), 5)
        for i in range(n):
            self.pos += 1
            self.loaded.append(self.pos)
            self.fetch()

        # display first image
        self.display()


    def next(self):
        print("Next")
        global pos
        if self.pos < len(self.photoLinks - 1):
            self.pos += 1
            # display next image
            self.display()
            # load one more image
            if pos != len(self.photoLinks - 7) and pos not in self.loaded:
               fetch()
        

    def previous(self):
        print("Button")
        global pos
        if self.pos > 0:
            self.pos -= 1
            # display previous image
            self.display()

    def share(self):
        print("Share")
        # prompt open email widget
        self.popupcontent.show()
        print("Hello")
    
    def email(self):
        ezgmail.send(self.emailid, self.subject, self.emailbody, self.emages)

    def display(self):
        self.im = QPixmap("%s.jpg" % self.pos)
        self.Image.setPixmap(self.im)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EarthDate.setText(_translate("MainWindow", "Date on Earth :"))
        self.Camera.setText(_translate("MainWindow", "Camera :"))
        self.CameraSelector.setItemText(0, _translate("MainWindow", "FHAZ"))
        self.CameraSelector.setItemText(1, _translate("MainWindow", "RHAZ"))
        self.CameraSelector.setItemText(2, _translate("MainWindow", "MAST"))
        self.CameraSelector.setItemText(3, _translate("MainWindow", "CHEMCAM"))
        self.CameraSelector.setItemText(4, _translate("MainWindow", "MAHLI"))
        self.CameraSelector.setItemText(5, _translate("MainWindow", "MARDI"))
        self.CameraSelector.setItemText(6, _translate("MainWindow", "NAVCAM"))
        self.Load.setText(_translate("MainWindow", "Load Images"))
        self.Previous.setText(_translate("MainWindow", "Previous"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.Share.setText(_translate("MainWindow", "Share Image"))
        self.Image.setText(_translate("MainWindow", "TextLabel"))
        self.Title.setText(_translate("MainWindow", "Curiosity Rover Images"))

    def email(self):
        for i in range(len(self.photoLinks)):
            urllib.request.urlretrieve(self.photoLinks[i], "00000001.jpg")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.centralwidget.show()
    MainWindow.show()
    sys.exit(app.exec_())
