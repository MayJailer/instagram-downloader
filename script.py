#Import packages.
import sys
import requests
import random
import urllib.request
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Instagram download'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('sources/icon.jpg'))
        self.setFixedSize(self.width, self.height)
 
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
 
        # Create a button in the window
        self.button = QPushButton('Descargar', self)
        self.button.move(20,80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        url = self.textbox.text()
        img_url = crawl(url)
        download(img_url)
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        #self.textbox.setText("")


def crawl(url):
    SourceCode = requests.get( url )
    PlainText  = SourceCode.text
    Soup       = BeautifulSoup( PlainText )

    for line in Soup.findAll('meta', {'property': 'og:image'}):
        link = line.get('content')
        return link
pass

def download(url):
    Filename = str( random.randrange(1, 10000) )
    FullName = "images/" + Filename + "_instagramcrawler" + ".jpg"
    urllib.request.urlretrieve(url, FullName)

    return FullName
pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())