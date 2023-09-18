# -*- coding: utf-8 -*-

import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel

class ChatServer(QWidget):
    def __init__(self):
        super(ChatServer, self).__init__()

        self.initUI()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 8080))
        self.server.listen(300)

        self.clients = []

        self.running = True
        self.thread = threading.Thread(target=self.accept_connections)
        self.thread.daemon = True  # 주 스레드가 종료될 때 함께 종료됩니다.
        self.thread.start()

    def initUI(self):
        self.log_window = QTextEdit(self)
        self.log_window.setReadOnly(True)

        self.status_label = QLabel('Server is running...', self)

        self.start_button = QPushButton('Start Server', self)
        self.start_button.clicked.connect(self.start_server)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.log_window)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def closeEvent(self, event):
        """어플리케이션 종료 이벤트를 오버라이드하여 소켓과 스레드를 종료합니다."""
        self.running = False
        self.server.close()
        event.accept()

    def start_server(self):
        self.log_window.append('Server started!')

    def accept_connections(self):
        while self.running:
            try:
                client_socket, addr = self.server.accept()
                self.clients.append(client_socket)
                self.log_window.append('Accepted connection from {}'.format(addr))
                thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                thread.start()
            except:
                pass


    def handle_client(self, client_socket):
        while self.running:  # self.running을 추가하여 서버가 실행 중일 때만 클라이언트를 처리
            try:
                msg = client_socket.recv(1024).decode('utf-8')
                if not msg:  # 클라이언트가 연결을 끊었거나 메시지를 보내지 않은 경우
                    break
                self.broadcast(msg, client_socket)
                self.log_window.append('Received message: {}'.format(msg))
            except:
                self.clients.remove(client_socket)
                client_socket.close()
                break  # 연결이 끊어진 경우 루프를 종료

    def broadcast(self, msg, sending_client):
        for client in self.clients:
            if client != sending_client:
                try:
                    client.send(msg.encode('utf-8'))
                except:
                    client.close()
                    self.clients.remove(client)

app = QApplication(sys.argv)
server_window = ChatServer()
server_window.show()
sys.exit(app.exec_())
