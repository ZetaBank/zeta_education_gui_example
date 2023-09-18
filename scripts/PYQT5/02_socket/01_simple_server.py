# -*- coding: utf-8 -*-

import socket

def main():
    # 소켓 객체 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # IP와 포트를 바인드
    server_socket.bind(('127.0.0.1', 12345))
    
    # 클라이언트 연결을 기다리기 시작, 동시에 처리할 수 있는 최대 연결 수는 5
    server_socket.listen(5)

    print("Server waiting for a connection...")
    connection, address = server_socket.accept()
    print("Connected by", address)

    while True:
        # 클라이언트로부터 데이터를 받음
        data = connection.recv(1024)
        
        if not data:
            break

        print("Received:", data.decode())
        
        # 데이터를 클라이언트로 되돌려줌
        connection.sendall(data)

    connection.close()

if __name__ == "__main__":
    main()
