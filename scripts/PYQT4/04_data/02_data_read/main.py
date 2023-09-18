# -*- coding: utf-8 -*-

import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableApp(QMainWindow):
    def __init__(self):
        super(TableApp, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Data from JSON')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # 데이터 로드
        with open("../01_json/data.json", "r") as file:
            data = json.load(file)

        # 표 생성
        table = QTableWidget(self)
        table.setRowCount(len(data))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['Key', 'Value'])

        for row, (key, value) in enumerate(data.items()):
            table.setItem(row, 0, QTableWidgetItem(str(key)))
            table.setItem(row, 1, QTableWidgetItem(str(value)))

        layout.addWidget(table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableApp()
    window.show()
    sys.exit(app.exec_())
