import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self): #def __init__(self, parent = None)
        super().__init__() # super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 500, 700, 500)
        self.setWindowTitle('QtWindow')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())