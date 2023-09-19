# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPushButton
)

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Create a button
        self.button = QPushButton("This is a button!", self)

        # Set the position of the button
        self.button.move(50, 20)
        self.button.setFixedSize(100, 50)
        
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
