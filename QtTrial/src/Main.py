


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtGUI import Ui_MainWindow

'''
1st Solution to call GUI
'''
'''
class MainGUI1(QMainWindow):
    def __init__(self):
        super(MainGUI1, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make some local modifications.
#         self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.ui.btnQuit.clicked.connect(self.close)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainGUI1()
    ui.show()
    sys.exit(app.exec_())

'''

#####################################################################################



'''
2nd Solution to call GUI
This is preferred solution

'''


class MainGUI2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainGUI2, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications.
#         self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.btnQuit.clicked.connect(self.close)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainGUI2()
    ui.show()
    sys.exit(app.exec_())



#####################################################################################



'''
Third solution to call GUI
'''
'''
class MainGUI0(Ui_MainWindow):
    def __init__(self):
        super(MainGUI0, self).__init__()
        
        self.window = QMainWindow()
        self.setupUi(self.window)
        
        self.btnQuit.clicked.connect(self.window.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainGUI0()
    ui.window.show()
    sys.exit(app.exec_())
'''