# -*- coding: utf-8 -*-

import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSignal

class ChatClient(QWidget):
    received_msg_signal = pyqtSignal(str)

    def __init__(self):
        super(ChatClient, self).__init__()

        self.initUI()
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 8080))
        self.client.settimeout(1)

        self.running = True
        self.thread = threading.Thread(target=self.receive_message)
        self.thread.daemon = True
        self.thread.start()

    def initUI(self):
        self.setWindowTitle('Chat Client')

        layout = QVBoxLayout()

        self.output_window = QTextEdit(self)
        self.output_window.setReadOnly(True)
        layout.addWidget(self.output_window)

        self.input_line = QLineEdit(self)
        self.input_line.returnPressed.connect(self.send_message)
        layout.addWidget(self.input_line)

        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        # Connect the signal to slot
        self.received_msg_signal.connect(self.display_received_message)

        self.setLayout(layout)

    def send_message(self):
        msg = self.input_line.text()
        self.client.send(msg.encode('utf-8'))
        self.output_window.append("You: {}".format(msg))
        self.input_line.clear()

    def receive_message(self):
        while self.running: 
            try:
                msg = self.client.recv(1024).decode('utf-8')
                if not msg:  # 소켓이 종료되면 빈 문자열을 반환합니다.
                    break
                self.received_msg_signal.emit(msg)
            except socket.timeout:  # 타임아웃 예외를 처리합니다.
                continue
            except:
                self.received_msg_signal.emit("An error occurred!")
                self.client.close()
                break


    def display_received_message(self, msg):
        self.output_window.append("Received: {}".format(msg))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Exit', 'Are you sure you want to exit the client?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.running = False
            self.client.close()
            self.thread.join(2)  # Wait for the receive_message thread to finish
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_window = ChatClient()
    chat_window.show()
    sys.exit(app.exec_())
