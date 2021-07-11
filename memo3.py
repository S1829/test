import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self): #def __init__(self, parent = None)
        super().__init__() # super(MainWindow, self).__init__(parent)
        # self.statusBar()
        # メニューバー作成
        self.menubar = self.menuBar()
        self.menubar.addMenu('File')
        self.menubar.addMenu('Capture')

        self.toolbar = self.addToolBar("toolbar")
        self.button1= QPushButton("scale up")
        self.button2 = QPushButton("scale down")
        self.toolbar.addWidget(self.button1)
        self.toolbar.addWidget(self.button2)

        self.CWidgets = self.centralWidget()

        # self.menu = QMenuBar()
        # self.menu.addMenu('&File')
        
        # exitActionを紐づける
        # fileMenu.addAction(exitAction)
        
        self.hbox = QVBoxLayout(self)

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

        # self.hbox.addWidget(self.splitter4)
        # self.setLayout(self.hbox)

        self.setCentralWidget(self.splitter4)

        self.setGeometry(200, 400, 1000, 600)
        self.setWindowTitle('QtWindow')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())