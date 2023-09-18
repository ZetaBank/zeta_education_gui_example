# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QTableView, QMainWindow, QVBoxLayout, QWidget

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def flags(self, index):
        return super(TableModel, self).flags(index) & ~Qt.ItemIsEditable

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.table = QTableView()

        data = [
            [1, "김", "철수"],
            [2, "박", "혁수"],
            [3, "이", "고수"],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
