import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create the stacked widget
        self.stack = QStackedWidget()

        # Create some sample pages with images
        self.page1 = self.create_page("images/twinkle_bocchi.png", "Go to Ai")
        self.page2 = self.create_page("images/twinkle_ai.jpg", "Go to Anay")
        self.page3 = self.create_page("images/twinkle_anya.jpg", "Go to Bocchi")

        # Add pages to the stacked widget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        # Set the current widget to be page 1
        self.stack.setCurrentWidget(self.page1)

        # Set the stacked widget as the central widget of the window
        self.setCentralWidget(self.stack)

    def create_page(self, image_path, button_text):
        page = QWidget()
        layout = QVBoxLayout(page)

        pixmap = QPixmap(image_path)
        image_label = QLabel(page)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        btn = QPushButton(button_text, page)
        layout.addWidget(btn)

        if button_text == "Go to Bocchi":
            btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))
        elif button_text == "Go to Ai":
            btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page2))
        elif button_text == "Go to Anay":
            btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page3))
        
        return page

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
