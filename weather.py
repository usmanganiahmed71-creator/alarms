import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QLabel,QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,QBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap


    
class Wind(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)
        self.setWindowIcon(QIcon("C:\\Users\\My Pc\\Desktop\\wallpaper\\garen.jpg"))
        self.setWindowTitle("GUI Intro")
        picobj=QLabel(self)
        picobj.setGeometry(0,0,1920,1080)
        pic=QPixmap("C:\\Users\\My Pc\\Desktop\\wallpaper\\garen.jpg")
        picobj.setPixmap(pic)
        picobj.setAlignment(Qt.AlignTop)
        picobj.setScaledContents(False)
def main():
    app=QApplication(sys.argv)
    window=Wind()
    window.show()
    sys.exit(app.exec_())


main()
print("ok")
