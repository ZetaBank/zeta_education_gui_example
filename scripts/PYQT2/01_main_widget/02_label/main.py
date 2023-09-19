# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLabel
)

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Create a label
        self.label = QLabel("This is a label!", self)

        # Set the position of the label
        self.label.move(50, 50)
        

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
