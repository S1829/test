import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #first
        self.upper = QCheckBox('test', self)
        self.upper.move(100, 30)
        self.upper.stateChanged.connect(self.uppercase)

        self.upper2 = QCheckBox('test',self)
        self.upper2.move(200,30)
        self.upper2.stateChanged.connect(self.buttoncase)

        #horizon
        self.horizon = QHBoxLayout()
        #vertical
        self.vertical = QVBoxLayout()

        #add button
        self.button = QPushButton('exucute',self)
        self.button.clicked.connect(self.output)

        # self.horizon.addWidget(self.button)
        self.horizon.addLayout(self.vertical)
        self.setLayout(self.horizon)

        
        #グループ化することでグループ内ではチェックを1つだけつけられる
        #second
        # self.lower = QCheckBox('test2', self)
        # self.lower.move(180, 30)

        #make group
        # self.group = QButtonGroup()
        # self.group.addButton(self.upper, 1)
        # self.group.addButton(self.lower, 2)

        self.setGeometry(300, 50, 700, 500)
        self.setWindowTitle('QcheckBox')

    def uppercase(self):
        if(self.upper.isChecked()):
            self.upper_a = QCheckBox('A', self)
            self.vertical.addWidget(self.upper_a)

            self.upper_b = QCheckBox('B', self)
            self.vertical.addWidget(self.upper_b)

        else:
            self.upper_a.setVisible(False)
            self.upper_b.setVisible(False)
            # self.vertical.removeWidget(self.upper_a)
            # self.vertical.removeWidget(self.upper_b)

    def buttoncase(self):
        if(self.upper2.isChecked()) :
            self.upper_c = QCheckBox('C', self)
            self.vertical.addWidget(self.upper_c)
 
            self.upper_d = QCheckBox('D', self)
            self.vertical.addWidget(self.upper_d) 
        else:
            self.upper_c.setVisible(False)
            self.upper_d.setVisible(False)
            # self.vertical.removeWidget(self.upper_c)
            # self.vertical.removeWidget(self.upper_d)     
    
    def output(self):
        outputs = []
        if(self.upper_a.isChecked()):
            outputs.append("A")
        if(self.upper_b.isChecked()):
            outputs.append("B")
        
        for output in outputs:
            print(output)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())