# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# import sip
 
# class MainWindow(QWidget):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
 
#         # 一つ目のチェックボックス
#         self.upper = QCheckBox('大文字', self)
#         self.upper.move(100, 30)
#         self.upper.stateChanged.connect(self.uppercase)

#         self.button = QPushButton('test',self)
#         self.button.move(200,30)
#         # 横のレイアウト
#         self.horizon = QHBoxLayout()
#         # 縦のレイアウト
#         self.vertical1 = QVBoxLayout()
#         self.vertical2 = QVBoxLayout()
 
#         self.horizon.addLayout(self.vertical1)
#         self.horizon.addLayout(self.vertical2)
#         self.setLayout(self.horizon)
 
#         self.setGeometry(300, 50, 500, 350)
#         self.setWindowTitle('QCheckBox')
 
#     def uppercase(self):
#         if(self.upper.isChecked()):
#             self.upper_a = QCheckBox('A', self)
#             self.vertical1.addWidget(self.upper_a)
 
#             self.upper_b = QCheckBox('B', self)
#             self.vertical1.addWidget(self.upper_b)
            

#             self.upper_c = QCheckBox('C', self)
#             self.vertical2.addWidget(self.upper_c)
 
#             self.upper_d = QCheckBox('D', self)
#             self.vertical2.addWidget(self.upper_d)
#         else:
#             self.vertical1.removeWidget(self.upper_a)
#             self.vertical1.removeWidget(self.upper_b)
#             self.vertical2.removeWidget(self.upper_c)
#             self.vertical2.removeWidget(self.upper_d)

#     # def buttoncase(self):
#     #     if(self.button.isDown() and self.upper.isChecked()) :
#     #         self.upper_c = QCheckBox('C', self)
#     #         self.vertical2.addWidget(self.upper_c)
 
#     #         self.upper_d = QCheckBox('D', self)
#     #         self.vertical2.addWidget(self.upper_d) 
#     #     else:
#     #         self.vertical2.removeWidget(self.upper_c)
#     #         self.vertical2.removeWidget(self.upper_d)         
 
 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,QCheckBox, QApplication)
from PyQt5 import QtCore

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.checkBoxA = QCheckBox("Select This.")
        self.labelA = QLabel("Not slected.")
        
        self.checkBoxA.stateChanged.connect(self.checkBoxChangedAction)
        
        layout.addWidget(self.checkBoxA)
        layout.addWidget(self.labelA)
        
        self.setGeometry(200, 200, 300, 200)            
                
        self.setWindowTitle('CheckBox Example')
    
    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            self.labelA.setText("Selected.")
        else:
            self.labelA.setText("Not Selected.")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())