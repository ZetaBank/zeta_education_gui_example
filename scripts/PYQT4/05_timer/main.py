# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import QTimer

class TimerTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(TimerTextEdit, self).__init__(parent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.append_message)
        self.timer.start(5000)  # 5000ms = 5s

    def append_message(self):
        self.append("5 seconds have passed!")

class TimerApp(QMainWindow):
    def __init__(self):
        super(TimerApp, self).__init__()

        self.text_edit = TimerTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QTimer Example')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())
