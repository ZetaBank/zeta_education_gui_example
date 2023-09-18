# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPalette, QColor

class ColorChangingWidget(QWidget):
    def __init__(self):
        super(ColorChangingWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Click to Change Color')
        self.setGeometry(100, 100, 400, 300)

    def mousePressEvent(self, event):
        # 무작위 색상으로 배경색 설정
        random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        palette = self.palette()
        palette.setColor(QPalette.Window, random_color)
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangingWidget()
    window.show()
    sys.exit(app.exec_())
