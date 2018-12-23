
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from recommendations import recGen,tinderlogin
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tinder_api as ti
import shutil
import pandas as pd
import os
import errno
import numpy as np
import time
import webbrowser

#gobal vars/functions
_translate = QtCore.QCoreApplication.translate

def mkdir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory) 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 750)

        MainWindow.setWindowIcon(QtGui.QIcon('tinder.png'))
        MainWindow.setFixedSize(1120,750)
        self.profileNum=0
        self.df = pd.DataFrame()
        self.id = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1121, 701))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btnlogin = QtWidgets.QPushButton(self.tab)
        self.btnlogin.setGeometry(QtCore.QRect(330, 330, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnlogin.setFont(font)
        self.btnlogin.setObjectName("btnlogin")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(330, 170, 451, 36))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelUsername = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelUsername.setFont(font)
        self.labelUsername.setObjectName("labelUsername")
        self.horizontalLayout_4.addWidget(self.labelUsername)
        self.valueUsername = QtWidgets.QLineEdit(self.layoutWidget1)
        self.valueUsername.setText("")
        self.valueUsername.setObjectName("valueUsername")
        self.horizontalLayout_4.addWidget(self.valueUsername)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(330, 250, 451, 36))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelPassword = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.horizontalLayout_5.addWidget(self.labelPassword)
        self.valuePassword = QtWidgets.QLineEdit(self.layoutWidget2)
        self.valuePassword.setObjectName("valuePassword")
        self.horizontalLayout_5.addWidget(self.valuePassword)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btnGenerateData = QtWidgets.QPushButton(self.tab_2)
        self.btnGenerateData.setGeometry(QtCore.QRect(330, 330, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerateData.setFont(font)
        self.btnGenerateData.setObjectName("btnGenerateData")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(780, 160, 51, 141))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.valueAgeMin = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.valueAgeMin.setFont(font)
        self.valueAgeMin.setObjectName("valueAgeMin")
        self.verticalLayout_4.addWidget(self.valueAgeMin)
        self.valueAgeMax = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.valueAgeMax.setFont(font)
        self.valueAgeMax.setObjectName("valueAgeMax")
        self.verticalLayout_4.addWidget(self.valueAgeMax)
        self.valueDistance = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.valueDistance.setFont(font)
        self.valueDistance.setObjectName("valueDistance")
        self.verticalLayout_4.addWidget(self.valueDistance)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(350, 160, 421, 141))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sliderAgeMin = QtWidgets.QSlider(self.layoutWidget4)
        self.sliderAgeMin.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAgeMin.setObjectName("sliderAgeMin")
        self.verticalLayout_2.addWidget(self.sliderAgeMin)
        self.sliderAgeMax = QtWidgets.QSlider(self.layoutWidget4)
        self.sliderAgeMax.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAgeMax.setObjectName("sliderAgeMax")
        self.verticalLayout_2.addWidget(self.sliderAgeMax)
        self.sliderDistance = QtWidgets.QSlider(self.layoutWidget4)
        self.sliderDistance.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDistance.setObjectName("sliderDistance")
        self.verticalLayout_2.addWidget(self.sliderDistance)
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(220, 160, 112, 141))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelAgeMin = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelAgeMin.setFont(font)
        self.labelAgeMin.setObjectName("labelAgeMin")
        self.verticalLayout_3.addWidget(self.labelAgeMin)
        self.labelAgeMax = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelAgeMax.setFont(font)
        self.labelAgeMax.setObjectName("labelAgeMax")
        self.verticalLayout_3.addWidget(self.labelAgeMax)
        self.labelDistance = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelDistance.setFont(font)
        self.labelDistance.setObjectName("labelDistance")
        self.verticalLayout_3.addWidget(self.labelDistance)
        self.t = QtWidgets.QLabel(self.tab_2)
        self.t.setGeometry(QtCore.QRect(371, 101, 108, 28))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t.setFont(font)
        self.t.setObjectName("t")
        self.valueLongitude = QtWidgets.QLineEdit(self.tab_2)
        self.valueLongitude.setGeometry(QtCore.QRect(510, 101, 239, 34))
        self.valueLongitude.setText("")
        self.valueLongitude.setObjectName("valueLongitude")
        self.textLatitude = QtWidgets.QLabel(self.tab_2)
        self.textLatitude.setGeometry(QtCore.QRect(371, 41, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textLatitude.setFont(font)
        self.textLatitude.setObjectName("textLatitude")
        self.valueLatitude = QtWidgets.QLineEdit(self.tab_2)
        self.valueLatitude.setGeometry(QtCore.QRect(510, 41, 239, 34))
        self.valueLatitude.setText("")
        self.valueLatitude.setObjectName("valueLatitude")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.imageSpace = QtWidgets.QGroupBox(self.tab_3)
        self.imageSpace.setGeometry(QtCore.QRect(420, 10, 640, 640))
        self.imageSpace.setObjectName("imageSpace")
        self.imagePlaceholder = QtWidgets.QLabel(self.imageSpace)
        self.imagePlaceholder.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.imagePlaceholder.setText("")
        self.imagePlaceholder.setObjectName("imagePlaceholder")
        self.labelBio = QtWidgets.QLabel(self.tab_3)
        self.labelBio.setGeometry(QtCore.QRect(20, 150, 42, 87))
        self.labelBio.setObjectName("labelBio")
        self.textBio = QtWidgets.QTextBrowser(self.tab_3)
        self.textBio.setGeometry(QtCore.QRect(70, 180, 311, 261))
        self.textBio.setObjectName("textBio")
        self.labelName = QtWidgets.QLabel(self.tab_3)
        self.labelName.setGeometry(QtCore.QRect(21, 51, 71, 21))
        self.labelName.setObjectName("labelName")
        self.labelAge = QtWidgets.QLabel(self.tab_3)
        self.labelAge.setGeometry(QtCore.QRect(20, 120, 61, 31))
        self.labelAge.setObjectName("labelAge")
        self.textName = QtWidgets.QTextBrowser(self.tab_3)
        self.textName.setGeometry(QtCore.QRect(100, 50, 121, 41))
        self.textName.setObjectName("textName")
        self.textAge = QtWidgets.QTextBrowser(self.tab_3)
        self.textAge.setGeometry(QtCore.QRect(100, 120, 121, 41))
        self.textAge.setObjectName("textAge")
        self.layoutWidget6 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget6.setGeometry(QtCore.QRect(20, 510, 361, 39))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnDislike = QtWidgets.QPushButton(self.layoutWidget6)
        self.btnDislike.setObjectName("btnDislike")
        self.horizontalLayout_3.addWidget(self.btnDislike)
        self.btnLike = QtWidgets.QPushButton(self.layoutWidget6)
        self.btnLike.setObjectName("btnLike")
        self.horizontalLayout_3.addWidget(self.btnLike)
        self.btnLoadCsv = QtWidgets.QPushButton(self.tab_3)
        self.btnLoadCsv.setGeometry(QtCore.QRect(265, 50, 121, 37))
        self.btnLoadCsv.setObjectName("btnLoadCsv")
        self.layoutWidget7 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget7.setGeometry(QtCore.QRect(20, 570, 361, 39))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnPrevious = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnPrevious.setObjectName("btnPrevious")
        self.horizontalLayout_6.addWidget(self.btnPrevious)
        self.btnNext = QtWidgets.QPushButton(self.layoutWidget7)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout_6.addWidget(self.btnNext)
        self.valueGoto = QtWidgets.QLineEdit(self.tab_3)
        self.valueGoto.setGeometry(QtCore.QRect(206, 451, 176, 40))
        self.valueGoto.setObjectName("valueGoto")
        self.btnGoto = QtWidgets.QPushButton(self.tab_3)
        self.btnGoto.setGeometry(QtCore.QRect(21, 452, 176, 37))
        self.btnGoto.setObjectName("btnGoto")
        self.textProfileNum = QtWidgets.QTextBrowser(self.tab_3)
        self.textProfileNum.setGeometry(QtCore.QRect(290, 120, 91, 41))
        self.textProfileNum.setObjectName("textProfileNum")
        self.labelProfileNum = QtWidgets.QLabel(self.tab_3)
        self.labelProfileNum.setGeometry(QtCore.QRect(250, 120, 61, 31))
        self.labelProfileNum.setObjectName("labelProfileNum")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImages_Folder = QtWidgets.QAction(MainWindow)
        self.actionImages_Folder.setObjectName("actionImages_Folder")
        self.actionLog_In = QtWidgets.QAction(MainWindow)
        self.actionLog_In.setObjectName("actionLog_In")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sliderAgeMin.setRange(1,100)
        self.sliderAgeMax.setRange(1,100)
        self.sliderDistance.setRange(1,100)
        self.sliderAgeMin.setValue(18)
        self.sliderAgeMax.setValue(22)
        self.sliderDistance.setValue(50)
        
        self.btnlogin.clicked.connect(self.login)
        self.sliderAgeMin.valueChanged.connect(self.valuechangeAgeMin)
        self.sliderAgeMax.valueChanged.connect(self.valuechangeAgeMax)
        self.sliderDistance.valueChanged.connect(self.valuechangeDistance)
        self.btnGenerateData.clicked.connect(self.genData)
        self.btnLoadCsv.clicked.connect(self.loadCsv)
        self.btnLike.clicked.connect(self.chooseLike)
        self.btnDislike.clicked.connect(self.chooseDislike)
        self.btnPrevious.clicked.connect(self.prevID)
        self.btnNext.clicked.connect(self.nextID)
        self.btnGoto.clicked.connect(self.gotoprofile)
        self.actionExit_2.triggered.connect(QtCore.QCoreApplication.quit)
        self.actionExit.triggered.connect(self.dir_open)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoTinder Data Creation Tool"))
        self.btnlogin.setText(_translate("MainWindow", "Login"))
        self.labelUsername.setText(_translate("MainWindow", "Facebook Username"))
        self.labelPassword.setText(_translate("MainWindow", "Facebook Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Login"))
        self.btnGenerateData.setText(_translate("MainWindow", "Generate Data"))
        self.valueAgeMin.setText(_translate("MainWindow", "18"))
        self.valueAgeMax.setText(_translate("MainWindow", "22"))
        self.valueDistance.setText(_translate("MainWindow", "50")) 
        self.valueLatitude.setText(_translate("MainWindow", "Enter Latitude"))
        self.valueLongitude.setText(_translate("MainWindow", "Enter Longitude"))
        self.valueGoto.setText(_translate("MainWindow", "Enter #"))
        self.labelAgeMin.setText(_translate("MainWindow", "Age (Min)"))
        self.labelAgeMax.setText(_translate("MainWindow", "Age (Max)"))
        self.labelDistance.setText(_translate("MainWindow", "Distance"))
        self.t.setText(_translate("MainWindow", "Longitude"))
        self.textLatitude.setText(_translate("MainWindow", "Latitude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Generate Data"))
        self.imageSpace.setTitle(_translate("MainWindow", "Image"))
        self.labelBio.setText(_translate("MainWindow", "Bio:"))
        self.textBio.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nexa Bold\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.labelName.setText(_translate("MainWindow", "Name:"))
        self.labelAge.setText(_translate("MainWindow", "Age:"))
        self.btnDislike.setText(_translate("MainWindow", "Dislike"))
        self.btnLike.setText(_translate("MainWindow", "Like"))
        self.btnLoadCsv.setText(_translate("MainWindow", "Load "))
        self.btnPrevious.setText(_translate("MainWindow", "Previous"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.btnGoto.setText(_translate("MainWindow", "Goto"))
        self.labelProfileNum.setText(_translate("MainWindow", "#"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Label Data"))
        self.menuFile.setTitle(_translate("MainWindow", "Home"))
        self.actionImages_Folder.setText(_translate("MainWindow", "Images"))
        self.actionLog_In.setText(_translate("MainWindow", "Log In"))
        self.actionExit.setText(_translate("MainWindow", "Images folder"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
    
    def dir_open(self):
        webbrowser.open("//data//images//unlabeled")   
        
    
    def login (self):
        tinderlogin(self.valueUsername.text(),self.valuePassword.text())


    def renderImage(self,id_):
        PATH = './data/images/unlabeled'
        self.imagePlaceholder.setPixmap(QtGui.QPixmap(f"{PATH}/{id_}.jpg"))
        self.imagePlaceholder.setGeometry(0,0,640,640)  
        self.imagePlaceholder.show()
        
    def renderProfile(self,i,df):
        id_ = df.iloc[i]["ID"]
        Name = df.iloc[i]["name"]
        Age = df.iloc[i]["age"]
        Bio = df.iloc[i]["bio"]
        self.id = id_
        self.renderImage(id_)
        self.textAge.setText(str(Age))
        self.textBio.setText(str(Bio))
        self.textName.setText(str(Name))
        self.textProfileNum.setText(str(i+1))

    def nextID(self):
        if self.profileNum == len(self.df)-1:
            pass
        else:
            self.profileNum+=1
            self.renderProfile(self.profileNum,self.df)
    
    def prevID(self):
        if self.profileNum==0:
            pass
        else:
            self.profileNum-=1
            self.renderProfile(self.profileNum,self.df)

    def chooseDislike(self):
        ti.dislike(self.id)
        if(self.df.iloc[self.profileNum]['liked'] == 1):
            self.df.at[self.profileNum,'liked'] = 0
            os.remove(f"./data/images/liked/{self.id}.jpg")
        self.df.at[self.profileNum,'dislike'] = 1
        shutil.copy(f"./data/images/unlabeled/{self.id}.jpg", f"./data/images/disliked/{self.id}.jpg")
        self.nextID()

    def chooseLike(self):
        ti.like(self.id)
        if(self.df.iloc[self.profileNum]['disliked'] == 1):
            self.df.at[self.profileNum,'disliked'] = 0
            os.remove(f"./data/images/disliked/{self.id}.jpg")
        self.df.at[self.profileNum,'liked'] = 1
        shutil.copy(f"./data/images/unlabeled/{self.id}.jpg", f"./data/images/liked/{self.id}.jpg")
        self.nextID()

    def saveImagefromURL(self,url,id_):
        if os.path.isfile(f'./data/images/unlabeled/{id_}.jpg') == False:
            mkdir(f'./data/images/unlabeled')
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img.save(f'./data/images/unlabeled/{id_}.jpg')

    def createDataFolders(self):
        labels = ['liked','disliked','superliked']
        PATH = './data/images'
        for i in labels:
            mkdir(f'{PATH}/{i}')

    def loadCsv(self):
        self.df = pd.read_csv("./data/rec.csv")
        self.df = self.df.drop_duplicates(subset=['ID'])
        self.df = self.df.fillna('Bio not available.') 
        self.df.to_csv("./data/rec.csv",mode='a',header=False, sep=',',index=False)
        print("Saving Images to /data/images/unlabeled....\n")
        for url,id_ in zip(self.df.imgurl.values,self.df.ID.values):
            self.saveImagefromURL(url,id_)
        print(f"{len(self.df)} unique records loaded!....\n")
        self.renderProfile(0,self.df)
        self.createDataFolders()
            
    def valuechangeAgeMin(self):
      size = self.sliderAgeMin.value()
      maxv = self.sliderAgeMax.value()
      x = 18
      if size >maxv:
        x = maxv -1
      elif size>46:
        x = 46
      elif size<18 :
        x = 18
      else:
        x = size
      self.sliderAgeMin.setValue(x)
      self.valueAgeMin.setText(_translate("MainWindow", str(x)))  
      
    def valuechangeAgeMax(self):
      size = self.sliderAgeMax.value()
      minv = self.sliderAgeMin.value()
      x = 22
      if size - minv < 4:
        x = minv + 4 
      elif size >55 :
        x = 55
      else:
        x = size
      self.sliderAgeMax.setValue(x)
      self.valueAgeMax.setText(_translate("MainWindow", str(x)))

    def valuechangeDistance(self):
      size = self.sliderDistance.value()
      self.valueDistance.setText(_translate("MainWindow", str(size)))

    def gotoprofile(self, num):
        num = int(self.valueGoto.text())
        if num>1 and num < len(self.df):
            self.profileNum = num
            self.renderProfile(num,self.df)

    def genData (self):
        try:
            mkdir("./data/")
            lat  = self.valueLatitude.text()
            lon  = self.valueLongitude.text()
            if isinstance(lat, int) and isinstance(lon,int):
                ti.update_location(lat,lon)
            data = recGen(self.sliderAgeMin.value(),self.sliderAgeMax.value(),self.sliderDistance.value())  
            s = pd.Series(np.zeros(len(data),dtype=int)).values
            data = data.assign(liked=s,disliked=s)   
            if os.path.isfile('./data/rec.csv'):
                data.to_csv("./data/rec.csv",mode='a',header=False, sep=',',index=False)
            else:
                data.to_csv("./data/rec.csv",mode='a',header=True, sep=',',index=False)
            print(f"{len(data)} new records generated at ./data/rec.csv .")
        except:
            print("You're, not logged in!")

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

