# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class CombinedEventApp(QMainWindow):
    def __init__(self):
        super(CombinedEventApp, self).__init__()
        self.key_pressed = None
        self.a_clicked = False
        self.label = QLabel("Press 'A' and then click the mouse!", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Combined Keyboard and Mouse Event')
        self.setGeometry(100, 100, 400, 300)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            if not self.a_clicked:
                self.key_pressed = Qt.Key_A
                self.a_clicked = True
            else:
                self.key_pressed = None
                self.a_clicked = False
        else:
            self.key_pressed = None
            self.a_clicked = False

    def mousePressEvent(self, event):
        if self.key_pressed == Qt.Key_A:
            self.label.setText("You pressed 'A' and clicked the mouse!")
            self.key_pressed = None
        else:
            self.label.setText("Press 'A' and then click the mouse!")
        self.a_clicked = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CombinedEventApp()
    window.show()
    sys.exit(app.exec_())
