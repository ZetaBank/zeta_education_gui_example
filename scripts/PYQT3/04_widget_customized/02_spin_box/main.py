# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QVBoxLayout, QWidget, QLabel

class SpinBoxStyled(QMainWindow):
    def __init__(self):
        super(SpinBoxStyled, self).__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Selected Value:", self)
        self.apply_label_style()

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0, 100)  # 0부터 100까지의 범위 설정
        self.spin_box.setSingleStep(5)  # 5단위로 값 변경
        self.spin_box.setPrefix("$")    # 접두사로 달러 표시
        self.spin_box.valueChanged.connect(self.update_label)  # 값 변경 시 라벨 업데이트
        self.apply_spinbox_style()

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self, value):
        self.label.setText("Selected Value: ${}".format(value))

    def apply_label_style(self):
        style = """
            QLabel {
                font-size: 18px;
                color: #3498db;
            }
        """
        self.label.setStyleSheet(style)

    def apply_spinbox_style(self):
        style = """
            QSpinBox {
                border: 2px solid #dcdde1;
                border-radius: 5px;
                padding: 5px;
                background-color: #f1f2f6;
                min-width: 200px;
                min-height: 100px;
            }

            QSpinBox::up-button {
                width: 50px;
                height: 50px;
                border: none;
                background: #2ecc71;
            }

            QSpinBox::down-button {
                width: 50px;
                height: 50px;
                border: none;
                background: #e74c3c;
            }

            QSpinBox::up-arrow {
                width: 15px;
                height: 15px;
                border: solid black;
                border-width: 0 7px 7px 0;
            }

            QSpinBox::down-arrow {
                width: 15px;
                height: 15px;
                border: solid white;
                border-width: 0 7px 7px 0;
            }
        """
        self.spin_box.setStyleSheet(style)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpinBoxStyled()
    window.show()
    sys.exit(app.exec_())
