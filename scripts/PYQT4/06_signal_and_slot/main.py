# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal

class SignalTextEdit(QTextEdit):
    b_key_pressed = pyqtSignal()

    def __init__(self, parent=None):
        super(SignalTextEdit, self).__init__(parent)
        self.b_key_pressed.connect(self.on_b_key_pressed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_B:
            self.b_key_pressed.emit()
        else:
            super(SignalTextEdit, self).keyPressEvent(event)

    def on_b_key_pressed(self):
        self.append("You pressed the 'B' key!")

class SignalApp(QMainWindow):
    def __init__(self):
        super(SignalApp, self).__init__()

        self.text_edit = SignalTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Signal and Slot Example')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignalApp()
    window.show()
    sys.exit(app.exec_())
