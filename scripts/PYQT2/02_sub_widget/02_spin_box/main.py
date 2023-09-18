# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QVBoxLayout, QWidget, QLabel

class SpinBoxExample(QMainWindow):
    def __init__(self):
        super(SpinBoxExample, self).__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Selected Value:", self)

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0, 100)  # 0부터 100까지의 범위 설정
        self.spin_box.setSingleStep(5)  # 5단위로 값 변경
        self.spin_box.setPrefix("$")    # 접두사로 달러 표시
        self.spin_box.valueChanged.connect(self.update_label)  # 값 변경 시 라벨 업데이트

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self, value):
        self.label.setText("Selected Value: ${}".format(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpinBoxExample()
    window.show()
    sys.exit(app.exec_())
