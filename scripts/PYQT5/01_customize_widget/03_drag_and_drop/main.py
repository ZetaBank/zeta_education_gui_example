# -*- coding: utf-8 -*-

import sys
import codecs
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class DragDropWidget(QWidget):
    def __init__(self):
        super(DragDropWidget, self).__init__()

        self.label = QLabel(self)
        self.label.setText("Drag & Drop an Image or Text here!")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)
        
        self.setAcceptDrops(True)
        self.setMinimumSize(300, 200)

    def dragEnterEvent(self, event):
        mime = event.mimeData()
        if mime.hasImage() or mime.hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        mime = event.mimeData()
        if mime.hasUrls():  # 파일 URL이 있는지 확인
            # 첫 번째 URL만 사용 (다중 파일 선택을 지원하지 않음)
            file_url = mime.urls()[0].toLocalFile()
            if file_url.endswith('.txt'):
                with codecs.open(file_url, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.label.setText(content)
                self.label.adjustSize()
                self.resize(self.label.width(), self.label.height() + 50)
            else:
                pixmap = QPixmap(file_url)
                self.label.setPixmap(pixmap)
                self.label.setFixedSize(pixmap.size())
                self.setFixedSize(pixmap.size())
        elif mime.hasText():
            self.label.setText(mime.text())
            self.label.adjustSize()  # 라벨 크기를 텍스트 크기에 맞게 조절
            self.resize(self.label.width(), self.label.height() + 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropWidget()
    window.show()
    sys.exit(app.exec_())
