import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow
from PyQt5.QtGui import QIcon
class UI(QMainWindow):
    def __init__(self):
              super().__init__()
              self.title='Hello, world!'
              self.left=10
              self.top=10
              self.width=640
              self.height=480
              self.initUI()
    def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left,self.top,self.width,self.height)
            self.show()

    
