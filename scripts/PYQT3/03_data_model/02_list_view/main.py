# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QListView, QMainWindow, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.list_view = QListView()
        self.model = QStringListModel()
        names = ["김철수", "박혁수", "이고수"]
        self.model.setStringList(names)
        self.list_view.setModel(self.model)

        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QVBoxLayout()
        layout.addWidget(self.list_view)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
