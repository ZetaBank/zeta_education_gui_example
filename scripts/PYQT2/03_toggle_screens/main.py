# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create the stacked widget
        self.stack = QStackedWidget()

        # Create some sample pages
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()

        # Add pages to the stacked widget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        # Sample layout for page 1
        layout1 = QVBoxLayout(self.page1)
        layout1.addWidget(QLabel("여긴 1 페이지입니다."))
        button1 = QPushButton("2 페이지로 가기")
        layout1.addWidget(button1)
        button1.clicked.connect(self.go_to_page2)

        # Sample layout for page 2
        layout2 = QVBoxLayout(self.page2)
        layout2.addWidget(QLabel("여긴 2 페이지라고라"))
        button2 = QPushButton("3 페이지로 가기")
        layout2.addWidget(button2)
        button2.clicked.connect(self.go_to_page3)

        # Sample layout for page 3
        layout3 = QVBoxLayout(self.page3)
        layout3.addWidget(QLabel("여긴 3 페이지라고하지"))
        button3 = QPushButton("1 페이지로 가볼까")
        layout3.addWidget(button3)
        button3.clicked.connect(self.go_to_page1)

        # Set the current widget to be page 1
        self.stack.setCurrentWidget(self.page1)

        # Set the stacked widget as the central widget of the window
        self.setCentralWidget(self.stack)

    def go_to_page1(self):
        self.stack.setCurrentWidget(self.page1)

    def go_to_page2(self):
        self.stack.setCurrentWidget(self.page2)

    def go_to_page3(self):
        self.stack.setCurrentWidget(self.page3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
