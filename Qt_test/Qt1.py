import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMainWindow

class MainWindow(QWidget):
    def __init__(self): #def __init__(self, parent = None)
        super().__init__() # super(MainWindow, self).__init__(parent)

        self.vbox = QVBoxLayout(self)
        self.buttonlayout1 = QHBoxLayout(self)

        #button top
        self.button1 = QPushButton("ファイル",self)
        self.button2 = QPushButton("キャプチャ",self)
        self.menu1 = QHBoxLayout(self)
        # self.menu1.addWidget(self.button1)
        # self.menu1.addWidget(self.button2)
        self.button1.setGeometry(0,0,30,10)
        self.button2.setGeometry(40,0,30,10)

        #button bottom
        self.button3 = QPushButton("ズームイン",self)
        self.button4 = QPushButton("ズームアウト",self)
        self.menu2 = QHBoxLayout(self)
        # self.menu2.addWidget(self.button3)
        # self.menu2.addWidget(self.button4)
        self.button1.setGeometry(0,20,30,10)
        self.button2.setGeometry(40,20,30,10)


        #frame
        self.top = QFrame(self)
        self.top.setFrameShape(QFrame.StyledPanel)

        self.bottomleft = QFrame(self)
        self.bottomleft.setFrameShape(QFrame.StyledPanel)

        self.bottomright = QFrame(self)
        self.bottomright.setFrameShape(QFrame.StyledPanel)

        self.sidetop = QFrame(self)
        self.sidetop.setFrameShape(QFrame.StyledPanel)

        self.sidemiddle = QFrame(self)
        self.sidemiddle.setFrameShape(QFrame.StyledPanel)

        self.sidebottom = QFrame(self)
        self.sidebottom.setFrameShape(QFrame.StyledPanel)


        # #layout
        # self.sidelayout = QVBoxLayout()
        # self.sidelayout.addWidget(self.sidetop)
        # self.sidelayout.addWidget(self.sidemiddle)
        # self.sidelayout.addWidget(self.sidebottom)
        
        #splitter horizontal1
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.bottomleft)
        self.splitter1.addWidget(self.bottomright)

        #splitter vertical1
        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.top)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.setStretchFactor(1,1)
     
        #splitter vertical2
        self.splitter3 = QSplitter(Qt.Vertical)
        self.splitter3.addWidget(self.sidetop)
        self.splitter3.addWidget(self.sidemiddle)
        self.splitter3.addWidget(self.sidebottom)

        #splitter horizontal2
        self.splitter4 = QSplitter(Qt.Horizontal)
        self.splitter4.addWidget(self.splitter2)
        self.splitter4.addWidget(self.splitter3)
        # self.splitter4.setStretchFactor(0,2)
        # self.splitter4.setStretchFactor(1,1)
        # self.splitter2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.splitter3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.vbox.addLayout(self.menu1)
        self.vbox.addLayout(self.menu2)
        self.vbox.addWidget(self.splitter4)
        self.setLayout(self.vbox)

        # #layout
        # self.layout_main = QHBoxLayout()
        # self.layout1 = QVBoxLayout()
        # self.layout2 = QHBoxLayout()
        # self.layout3 = QVBoxLayout()

        # #button
        # self.button1 = QPushButton()
        # self.button2 = QPushButton()
        # self.button3 = QPushButton()
        # self.button4 = QPushButton()
        # self.button5 = QPushButton()
        # self.button6 = QPushButton()

        # #set layout left
        # self.layout1.addWidget(self.button1)
        # self.layout2.addWidget(self.button2)
        # self.layout2.addWidget(self.button3)
        # self.layout1.addLayout(self.layout2)

        # #set layout right
        # self.layout3.addWidget(self.button4)
        # self.layout3.addWidget(self.button5)
        # self.layout3.addWidget(self.button6)

        # self.layout_main.addLayout(self.layout1)
        # self.layout_main.addLayout(self.layout3)

        # self.setLayout(self.layout_main)

        self.setGeometry(200, 400, 1000, 600)
        self.setWindowTitle('QtWindow')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())