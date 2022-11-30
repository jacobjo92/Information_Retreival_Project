from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout,QLineEdit)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title='Search engine test.'
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.search_value = ""
        
        self.buttonget = QPushButton("Get Your Guide")
        self.buttonswiss = QPushButton("Swiss Tours")
        self.buttonviator = QPushButton("Viator")
        
        self.buttonget.clicked.connect(self.buttongetfunction)
        self.buttonswiss.clicked.connect(self.buttonswissfunction)
        self.buttonviator.clicked.connect(self.buttonviatorfunction)
            
        self.outerlayout = QVBoxLayout()
        self.toplayout = QHBoxLayout()
        self.toplayout.addWidget(self.buttonget)
        self.toplayout.addWidget(self.buttonswiss)
        self.toplayout.addWidget(self.buttonviator)
        
        self.centerlayout = QFormLayout()
        
        self.outerlayout.addLayout(self.toplayout)
        self.outerlayout.addLayout(self.centerlayout)
        self.setLayout(self.outerlayout)
        self.initUI()
        
        
    def buttongetfunction(self):
        print("Button get clicked")
    def buttonswissfunction(self):
        print("Button swiss clicked")
    def buttonviatorfunction(self):
        print("Button viat clicked")
            
    def clearSearch(self):
        self.search_value = ""
              
    def UiComponents(self):
        e = QLineEdit()
        self.centerlayout.addRow("Search:",e)
        e.returnPressed.connect(lambda:do_action())
        
        
        def do_action():
            search_value = e.text()
            self.search_value = search_value

        
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.UiComponents()
            # widgetEngineTitle = QLabel("Dylan & Johan Serach Engine",self)
            # font = widgetEngineTitle.font()
            # font.setPointSize(12)
            # widgetEngineTitle.setFont(font)
            # widgetEngineTitle.setLayout(Qt.A)
            
            
            # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
            # self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
            # self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

            # for i in range(1,50):
            #     object = QLabel("TextLabel")
            #     self.vbox.addWidget(object)

            # self.widget.setLayout(self.vbox)

            # #Scroll Area Properties
            # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            # self.scroll.setWidgetResizable(True)
            # self.scroll.setWidget(self.widget)

            # self.setCentralWidget(self.scroll)
            
            
            
        self.show()

    
