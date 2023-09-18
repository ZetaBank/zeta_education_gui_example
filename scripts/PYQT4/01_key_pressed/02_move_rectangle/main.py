# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QBrush, QPen

class RectangleMover(QMainWindow):
    def __init__(self):
        super(RectangleMover, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Move Rectangle with ASWD')

        self.setGeometry(100, 100, 800, 600)

        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        self.rectangle = self.scene.addRect(QRectF(0, 0, 50, 50), QPen(), QBrush(Qt.blue))
        self.view.setSceneRect(0, 0, 800, 600)

        self.setCentralWidget(self.view)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:  # Move left
            self.rectangle.setPos(self.rectangle.x() - 10, self.rectangle.y())
        elif event.key() == Qt.Key_D:  # Move right
            self.rectangle.setPos(self.rectangle.x() + 10, self.rectangle.y())
        elif event.key() == Qt.Key_W:  # Move up
            self.rectangle.setPos(self.rectangle.x(), self.rectangle.y() - 10)
        elif event.key() == Qt.Key_S:  # Move down
            self.rectangle.setPos(self.rectangle.x(), self.rectangle.y() + 10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RectangleMover()
    window.show()
    sys.exit(app.exec_())
