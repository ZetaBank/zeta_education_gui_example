# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MouseDetectionApp(QMainWindow):
    def __init__(self):
        super(MouseDetectionApp, self).__init__()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Click or move the mouse!")
        self.label.setMouseTracking(True)  # 마우스 이동 감지 활성화
        self.setCentralWidget(self.label)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Mouse Event Detection')
        self.setGeometry(100, 100, 400, 300)

    def mousePressEvent(self, event):
        self.label.setText("Mouse Pressed: Button {} at {}".format(event.button(), event.pos()))

    def mouseReleaseEvent(self, event):
        self.label.setText("Mouse Released: Button {} at {}".format(event.button(), event.pos()))

    def mouseMoveEvent(self, event):
        self.label.setText("Mouse Moved: Position {}".format(event.pos()))

    def mouseDoubleClickEvent(self, event):
        self.label.setText("Mouse Double Clicked: Button {} at {}".format(event.button(), event.pos()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseDetectionApp()
    window.show()
    sys.exit(app.exec_())
