from PyQt5 import QtCore, QtGui, QtWidgets
from query import query


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(422, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))

        # For displaying confirmation message along with user's info.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))

        # Keeping the text of label empty initially.
        self.label.setText("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.pushButton.clicked.connect(self.takeinputs)

    def takeinputs(self):
        name, done1 = QtWidgets.QInputDialog.getText(
        self, 'Input Dialog', 'Enter your name:')

        roll, done2 = QtWidgets.QInputDialog.getInt(
        self, 'Input Dialog', 'Enter your roll:')

        cgpa, done3 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Enter your CGPA:')

        langs =['C', 'c++', 'Java', 'Python', 'Javascript']
        lang, done4 = QtWidgets.QInputDialog.getItem(
        self, 'Input Dialog', 'Language you know:', langs)

        if done1 and done2 and done3 and done4 :
            # Showing confirmation message along
            # with information provided by user.
            self.label.setText('Information stored Successfully\nName: '
            +str(name)+'('+str(roll)+')'+'\n'+'CGPA: '
            +str(cgpa)+'\nSelected Language: '+str(lang))

            # Hide the pushbutton after inputs provided by the use.
            self.pushButton.hide()






















# class FileWindow(QWidget):
#     def __init__(self, parent=None):
#         super(FileWindow, self).__init__(parent)
        
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title='Search engine test.'
#         self.left=10
#         self.top=10
#         self.width=640
#         self.height=480
#         self.search_value = ""
        
#         self.initLayout()
            
#     def clearSearch(self):
#         self.search_value = ""
              
#     def searchFieldAction(self,e):
#         search_value = e.text()
#         self.search_value = search_value
#         print(e.text())

#     def buttonstate(self,b):
#         if b.text() == "Get Your Guide":
#             if b.isChecked() == True:
#                 print(b.text()+" is selected")
#         else:
#             print(b.text()+" is deselected")
				
#         if b.text() == "Swiss Tours":
#             if b.isChecked() == True:
#                 print(b.text()+" is selected")
#             else:
#                 print(b.text()+" is deselected")
                
#         if b.text() == "Viator":
#             if b.isChecked() == True:
#                 print(b.text()+" is selected")
#             else:
#                 print(b.text()+" is deselected")
                
                
#     def returnButtonState(self):
#         if self.buttonget.checkState() == True and self.buttonswiss.checkState() == False and self.buttonviator.checkState() == False:
#             print("Hello")
#             return 1
#         if self.buttonget.checkState() == False and self.buttonswiss.checkState() == True and self.buttonviator.checkState() == False:
#             return 2
#         if self.buttonget.checkState() == False and self.buttonswiss.checkState() == False and self.buttonviator.checkState() == True:
#             return 3
#         else:
#             return 0
            
            
#     def onPressedEnter(self):
#         choice = self.returnButtonState()
#         question = self.e.text()
#         if (choice!= 0):
#             print("Sup")
#             query(choice,question)
#             newWindow = FileWindow(self)
#         return 0
#         # Open document in new window
        
#     def keyPressEvent(self,e):
#         if e.key() == Qt.Key_Return:
#             self.onPressedEnter()
        

        
#     def initLayout(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left,self.top,self.width,self.height)
        
#         self.buttonget = QCheckBox("Get Your Guide")
#         self.buttonswiss = QCheckBox("Swiss Tours")
#         self.buttonviator = QCheckBox("Viator")
        
#         self.buttonget.setChecked(False)
#         self.buttonswiss.setChecked(False)
#         self.buttonviator.setChecked(False)
        
#         self.buttonget.stateChanged.connect(lambda:self.buttonstate(self.buttonget))
#         self.buttonswiss.stateChanged.connect(lambda:self.buttonstate(self.buttonswiss))
#         self.buttonviator.stateChanged.connect(lambda:self.buttonstate(self.buttonviator))
            
#         self.outerlayout = QVBoxLayout()
#         self.toplayout = QHBoxLayout()
#         self.toplayout.addWidget(self.buttonget)
#         self.toplayout.addWidget(self.buttonswiss)
#         self.toplayout.addWidget(self.buttonviator)
        
#         self.centerlayout = QFormLayout()
        
#         self.e = QLineEdit()
#         self.centerlayout.addRow("Search:",self.e)
#         # self.e.returnPressed.connect(lambda:self.onPressedEnter())
        
        
        
#         self.outerlayout.addLayout(self.toplayout)
#         self.outerlayout.addLayout(self.centerlayout)
#         self.setLayout(self.outerlayout)

    
