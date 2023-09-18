# -*- coding: utf-8 -*-

import socket

def main():
    # 소켓 객체 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버에 연결
    client_socket.connect(('127.0.0.1', 12345))

    message = raw_input("Enter your message: ")
    client_socket.sendall(message.encode())

    # 서버로부터 데이터를 받음
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
