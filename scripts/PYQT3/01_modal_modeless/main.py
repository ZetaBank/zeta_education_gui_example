import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()
            
    def init_ui(self):
        self.button_modal = QPushButton("Open Modal Dialog", self)
        self.button_modal.clicked.connect(self.show_modal)
        self.button_modal.move(10, 10)
        self.button_modal.resize(150, 40)

        self.button_modeless = QPushButton("Open Modeless Dialog", self)
        self.button_modeless.clicked.connect(self.show_modeless)
        self.button_modeless.move(10, 60)
        self.button_modeless.resize(150, 40)
        
    def show_modal(self):
        self.modal_dialog = QDialog(self)
        self.modal_dialog.setWindowTitle("Modal Dialog")
        
        layout = QVBoxLayout()
        label = QLabel("This is a Modal Dialog. You can't interact with the main window until you close this.")
        layout.addWidget(label)
        
        self.modal_dialog.setLayout(layout)
        self.modal_dialog.exec_()

    def show_modeless(self):
        self.modeless_dialog = QDialog(self)
        self.modeless_dialog.setWindowTitle("Modeless Dialog")

        layout = QVBoxLayout()
        label = QLabel("This is a Modeless Dialog. You can still interact with the main window.")
        layout.addWidget(label)
        
        self.modeless_dialog.setLayout(layout)
        self.modeless_dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
