from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.init_ui()
        
    def init_ui(self):
        self.button = QPushButton("Click Me!", self)
        self.label = QLabel("Button not clicked.", self)
        
        self.button.move(50, 20)
        self.button.clicked.connect(self.on_button_click)
        
        self.label.move(50, 60)
        
    def on_button_click(self):
        self.label.setText("Button clicked!")
        
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
