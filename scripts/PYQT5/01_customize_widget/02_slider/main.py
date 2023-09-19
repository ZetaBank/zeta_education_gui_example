# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class ColorSliderWidget(QWidget):
    def __init__(self):
        super(ColorSliderWidget, self).__init__()

        layout = QVBoxLayout()

        self.r_slider = QSlider(Qt.Horizontal)
        self.g_slider = QSlider(Qt.Horizontal)
        self.b_slider = QSlider(Qt.Horizontal)

        self.r_slider.setRange(0, 255)  # Set the range for red slider
        self.g_slider.setRange(0, 255)  # Set the range for green slider
        self.b_slider.setRange(0, 255)  # Set the range for blue slider

        layout.addWidget(self.r_slider)
        layout.addWidget(self.g_slider)
        layout.addWidget(self.b_slider)

        self.r_slider.valueChanged.connect(self.update_color)
        self.g_slider.valueChanged.connect(self.update_color)
        self.b_slider.valueChanged.connect(self.update_color)

        self.setLayout(layout)

    def update_color(self):
        r = self.r_slider.value()
        g = self.g_slider.value()
        b = self.b_slider.value()
        
        color = QColor(r, g, b)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, color)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorSliderWidget()
    window.show()
    sys.exit(app.exec_())
