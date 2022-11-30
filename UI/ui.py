from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout,QLineEdit,QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from query import query

class FileWindow(QWidget):
    def __init__(self, parent=None):
        super(FileWindow, self).__init__(parent)
        
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title='Search engine test.'
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.search_value = ""
        
        self.initLayout()
            
    def clearSearch(self):
        self.search_value = ""
              
    def searchFieldAction(self,e):
        search_value = e.text()
        self.search_value = search_value
        print(e.text())

    def buttonstate(self,b):
        if b.text() == "Get Your Guide":
            if b.isChecked() == True:
                print(b.text()+" is selected")
        else:
            print(b.text()+" is deselected")
				
        if b.text() == "Swiss Tours":
            if b.isChecked() == True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")
                
        if b.text() == "Viator":
            if b.isChecked() == True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")
                
                
    def returnButtonState(self):
        if self.buttonget.checkState() == True and self.buttonswiss.checkState() == False and self.buttonviator.checkState() == False:
            print("Hello")
            return 1
        if self.buttonget.checkState() == False and self.buttonswiss.checkState() == True and self.buttonviator.checkState() == False:
            return 2
        if self.buttonget.checkState() == False and self.buttonswiss.checkState() == False and self.buttonviator.checkState() == True:
            return 3
        else:
            return 0
            
            
    def onPressedEnter(self):
        choice = self.returnButtonState()
        question = self.e.text()
        if (choice!= 0):
            print("Sup")
            query(choice,question)
            newWindow = FileWindow(self)
        return 0
        # Open document in new window
        
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Return:
            self.onPressedEnter()
        

        
    def initLayout(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.buttonget = QCheckBox("Get Your Guide")
        self.buttonswiss = QCheckBox("Swiss Tours")
        self.buttonviator = QCheckBox("Viator")
        
        self.buttonget.setChecked(False)
        self.buttonswiss.setChecked(False)
        self.buttonviator.setChecked(False)
        
        self.buttonget.stateChanged.connect(lambda:self.buttonstate(self.buttonget))
        self.buttonswiss.stateChanged.connect(lambda:self.buttonstate(self.buttonswiss))
        self.buttonviator.stateChanged.connect(lambda:self.buttonstate(self.buttonviator))
            
        self.outerlayout = QVBoxLayout()
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.buttonget)
        self.toplayout.addWidget(self.buttonswiss)
        self.toplayout.addWidget(self.buttonviator)
        
        self.centerlayout = QFormLayout()
        
        self.e = QLineEdit()
        self.centerlayout.addRow("Search:",self.e)
        self.
        # self.e.returnPressed.connect(lambda:self.onPressedEnter())
        
        
        
        self.outerlayout.addLayout(self.toplayout)
        self.outerlayout.addLayout(self.centerlayout)
        self.setLayout(self.outerlayout)

    
