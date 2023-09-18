# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtWidgets import QApplication, QProgressBar, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    progress = pyqtSignal(int)  # 작업 진행 상황을 나타내는 신호

    def __init__(self, sleep_time=0.1):
        super(Worker, self).__init__()
        self.sleep_time = sleep_time

    def run(self):
        for i in range(101):
            time.sleep(self.sleep_time)
            self.progress.emit(i)

class MultiProgressBarWidget(QWidget):
    def __init__(self):
        super(MultiProgressBarWidget, self).__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.progressBar1 = QProgressBar(self)
        self.progressBar2 = QProgressBar(self)

        layout.addWidget(self.progressBar1)
        layout.addWidget(self.progressBar2)

        self.setLayout(layout)

        self.worker1 = Worker(0.1)  # 0.1초 간격
        self.worker2 = Worker(0.2)  # 0.5초 간격

        self.worker1.progress.connect(self.progressBar1.setValue)
        self.worker2.progress.connect(self.progressBar2.setValue)

        self.worker1.start()
        self.worker2.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultiProgressBarWidget()
    window.show()
    sys.exit(app.exec_())
