# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()