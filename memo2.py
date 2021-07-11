# import sys
# from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, 
#     QSplitter, QStyleFactory, QApplication)
# from PyQt5.QtCore import Qt


# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):      

#         hbox = QHBoxLayout(self)

#         # フレームオブジェクトの作成
#         topleft = QFrame(self)
#         # フレームの形状設定
#         topleft.setFrameShape(QFrame.StyledPanel)

#         topright = QFrame(self)
#         topright.setFrameShape(QFrame.StyledPanel)

#         bottom = QFrame(self)
#         bottom.setFrameShape(QFrame.StyledPanel)

#         # 水平方向のQSplitterオブジェクトを作成して、フレームを追加
#         splitter1 = QSplitter(Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)

#         # # 垂直方向のQSplitterオブジェクトを作成して、フレームを追加
#         splitter2 = QSplitter(Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)

#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QSplitter')
#         self.show()


#     def onChanged(self, text):

#         self.lbl.setText(text)
#         self.lbl.adjustSize()        


# if __name__ == '__main__':

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        first = QFrame(self)
        first.setFrameShape(QFrame.StyledPanel)
        scrollAreaLeft = QScrollArea()
        scrollAreaLeft.setWidgetResizable(True)
        scrollAreaLeft.setWidget(first)
        second = QFrame(self)
        second.setFrameShape(QFrame.StyledPanel)
        scrollAreaRight = QScrollArea()
        scrollAreaRight.setWidgetResizable(True)
        scrollAreaRight.setWidget(second)
        splitter = QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(scrollAreaLeft)
        splitter.addWidget(scrollAreaRight)
        splitter.setStretchFactor(1, 10)
        hbox.addWidget(splitter)
        self.setLayout(hbox)
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle("QSplitter")
        self.show()
        print ("scrollAreaLeft width: "+str(scrollAreaLeft.width()))
        print ("scrollAreaRight width: "+str(scrollAreaRight.width()))

    def main():
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


if __name__ == "__main__":
    Example.main()