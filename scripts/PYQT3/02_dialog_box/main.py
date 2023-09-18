# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QColorDialog, QFontDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        layout = QVBoxLayout()

        # File Dialog
        self.label_file = QLabel(self)
        layout.addWidget(self.label_file)
        
        self.btn_open_file = QPushButton("Open File", self)
        self.btn_open_file.clicked.connect(self.open_file)
        layout.addWidget(self.btn_open_file)

        # Color Dialog
        self.label_color = QLabel("Selected Color", self)
        layout.addWidget(self.label_color)

        self.btn_open_color = QPushButton("Open Color Dialog", self)
        self.btn_open_color.clicked.connect(self.open_color)
        layout.addWidget(self.btn_open_color)

        # Font Dialog
        self.label_font = QLabel("Sample Text", self)
        layout.addWidget(self.label_font)

        self.btn_open_font = QPushButton("Open Font Dialog", self)
        self.btn_open_font.clicked.connect(self.open_font)
        layout.addWidget(self.btn_open_font)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.label_file.setText(u"Selected file: {}".format(file_name))

    def open_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.label_color.setText("Selected Color: {}".format(color.name()))
            self.label_color.setStyleSheet("background-color: {}".format(color.name()))

    def open_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label_font.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
