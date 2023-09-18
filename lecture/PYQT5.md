Advanced Topics and Customization
==================================

사용자 정의 위젯 생성
--------------------

### scripts/PYQT4/01_customize_widget/01_random_background/main.py

</br>

```python
# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPalette, QColor

class ColorChangingWidget(QWidget):
    def __init__(self):
        super(ColorChangingWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Click to Change Color')
        self.setGeometry(100, 100, 400, 300)

    def mousePressEvent(self, event):
        # 무작위 색상으로 배경색 설정
        random_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        palette = self.palette()
        palette.setColor(QPalette.Window, random_color)
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangingWidget()
    window.show()
    sys.exit(app.exec_())

```
이 예제에서는 **QWidget**를 상속받아 사용자 정의 위젯인 **ColorChangingWidget**을 생성합니다.

- **mousePressEvent** 메서드를 오버라이드하여 위젯을 클릭할 때마다 무작위 색상으로 위젯의 배경색을 변경하는 기능을 구현합니다.
- 색상 변경은 **QPalette** 객체를 사용하여 수행됩니다.

</br>

### scripts/PYQT5/01_customize_widget/02_slider/main.py

이 예제에서는 사용자가 세 개의 슬라이더(빨강, 초록, 파랑)를 움직임에 따라 배경색이 동적으로 변경되는 PyQt5 위젯을 만들었습니다.

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class ColorSliderWidget(QWidget):
    def __init__(self):
        super(ColorSliderWidget, self).__init__()

        layout = QVBoxLayout()

        self.r_slider = QSlider(Qt.Horizontal)
        self.g_slider = QSlider(Qt.Horizontal)
        self.b_slider = QSlider(Qt.Horizontal)

        layout.addWidget(self.r_slider)
        layout.addWidget(self.g_slider)
        layout.addWidget(self.b_slider)

        self.r_slider.valueChanged.connect(self.update_color)
        self.g_slider.valueChanged.connect(self.update_color)
        self.b_slider.valueChanged.connect(self.update_color)

        self.setLayout(layout)

    def update_color(self):
        r = self.r_slider.value()
        g = self.g_slider.value()
        b = self.b_slider.value()
        
        color = QColor(r, g, b)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, color)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorSliderWidget()
    window.show()
    sys.exit(app.exec_())
```


- **QSlider(Qt.Horizontal)**: 가로 방향의 슬라이더를 만들었습니다. 세 개의 슬라이더는 각각 빨강, 초록, 파랑 값을 조절합니다.

- **valueChanged.connect()**: 슬라이더의 값이 변경될 때마다 update_color 메서드를 호출하도록 연결했습니다.

- **update_color**: 세 슬라이더의 현재 값을 사용하여 새로운 QColor 객체를 만들고, 위젯의 배경색을 해당 색으로 설정합니다.

</br>

### scripts/PYQT5/01_customize_widget/03_drag_and_drop/main.py

이 예제에서는 사용자가 텍스트 또는 이미지 파일을 위젯으로 드래그 앤 드롭했을 때 해당 내용을 위젯에 표시하는 기능을 구현했습니다.

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class DragDropWidget(QWidget):
    def __init__(self):
        super(DragDropWidget, self).__init__()

        self.label = QLabel(self)
        self.label.setText("Drag & Drop an Image or Text here!")
        self.label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)
        
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        mime = event.mimeData()
        if mime.hasImage() or mime.hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        mime = event.mimeData()
        if mime.hasUrls():  # 파일 URL이 있는지 확인
            # 첫 번째 URL만 사용 (다중 파일 선택을 지원하지 않음)
            file_url = mime.urls()[0]
            pixmap = QPixmap(file_url.toLocalFile())  # 파일 경로로 QPixmap 로드
            self.label.setFixedSize(pixmap.size())  # 라벨의 크기를 QPixmap의 크기에 맞게 조정
            self.label.setPixmap(pixmap)
            self.setFixedSize(pixmap.size())  # 메인 윈도우의 크기를 QPixmap의 크기에 맞게 조정
        elif mime.hasText():
            self.label.setText(mime.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropWidget()
    window.show()
    sys.exit(app.exec_())
```

- **setAcceptDrops(True)**: 이 위젯에서 드래그 앤 드롭을 받아들일 수 있도록 설정했습니다.

- **dragEnterEvent**: 드래그 된 데이터가 텍스트 또는 이미지인 경우 이를 받아들이도록 이벤트를 처리합니다.

- **dropEvent**: 드래그 된 데이터를 라벨에 표시합니다. 이미지 파일의 경우 **QPixmap** 객체를 사용하여 이미지를 로드하고 라벨과 메인 윈도우의 크기를 이미지의 크기에 맞게 조절합니다. 텍스트의 경우 라벨에 드래그 된 텍스트를 그대로 표시합니다.


</br>

간단한 소켓통신
--------------

### scripts/PYQT5/02_socket/01_simple_server.py (서버)
```python
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
```

- **socket**을 사용하여 간단한 TCP 서버를 생성합니다.

- **socket.AF_INET**과 **socket.SOCK_STREAM**을 사용하여 IPv4 주소 체계와 TCP 소켓 유형을 지정합니다.

- **server_socket.bind()** 메서드를 사용하여 IP 주소와 포트 번호를 바인드합니다.

- 클라이언트 연결을 기다리는 동안, 서버는 데이터를 수신하고 에코(반환)합니다.


</br>


### scripts/PYQT5/02_socket/02_simple_client.py (클라이언트)

```python
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
```

- **socket**을 사용하여 간단한 TCP 클라이언트를 생성합니다.

- 서버에 메시지를 전송하고, 서버로부터 동일한 메시지를 다시 수신합니다.

</br>

멀티스레딩
---------

### scripts/PYQT5/03_thread/01_single_thread/main.py

```python
# -*- coding: utf-8 -*-

import time

def print_numbers():
    for i in range(1, 11):
        print("Number {}".format(i))
        time.sleep(0.5)

def print_letters():
    for letter in 'abcdefghij':
        print("Letter {}".format(letter))
        time.sleep(1)

# 함수 순차 실행
print_numbers()
print_letters()

print("Done!")

```

- **print_numbers**와 **print_letters**라는 두 함수를 순차적으로 호출하여 숫자와 알파벳을 출력합니다.

- 각 함수에서는 일정 시간 간격으로 숫자 또는 문자를 출력하며, 이 예제는 순차 실행을 보여줍니다.


</br>

### scripts/PYQT5/03_thread/02_multi_thread/main.py
 
```python
# -*- coding: utf-8 -*-

import threading
import time

def print_numbers():
    for i in range(1, 11):
        print("Number {}".format(i))
        time.sleep(0.5)

def print_letters():
    for letter in 'abcdefghij':
        print("Letter {}".format(letter))
        time.sleep(1)

# 두 개의 스레드 생성
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 스레드 시작
thread1.start()
thread2.start()

# 주 스레드에서 두 스레드가 종료될 때까지 기다림
thread1.join()
thread2.join()

print("Done!")
```

- **threading** 모듈을 사용하여 **print_numbers**와 **print_letters** 함수를 별도의 스레드에서 동시에 실행합니다.

- 두 함수는 동시에 실행되므로, 숫자와 알파벳이 교차하여 출력됩니다.

- **thread1.join()**과 **thread2.join()**은 주 스레드가 해당 스레드들이 모두 종료될 때까지 기다리게 합니다.

</br>

### scripts/PYQT5/03_thread/03_background_data_update/main.py

이 프로그램은 현재 시간을 실시간으로 업데이트하는 간단한 PyQt5 위젯을 생성합니다. 이 위젯은 1초마다 현재 시간을 화면에 표시합니다.

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QDateTime

class TimeUpdateWidget(QWidget):
    def __init__(self):
        super(TimeUpdateWidget, self).__init__()

        self.initUI()

        # QTimer 객체 생성
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)  # 타이머 시간이 끝날 때마다 update_time 함수 호출
        self.timer.start(1000)  # 1초마다 타이머 시작

    def initUI(self):
        self.label = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss')
        self.label.setText(current_time)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = TimeUpdateWidget()
    mainWindow.show()
    app.exec_()
```

- **QTimer**: 이 클래스는 주어진 시간 간격마다 시그널을 발생시킵니다. 여기서는 1초마다 **timeout** 시그널을 발생시켜 **update_time** 함수를 호출합니다.

- **update_time** 함수: 이 함수는 현재 시간을 가져와서 라벨에 표시합니다.

</br>

### scripts/PYQT5/03_thread/04_progressbar/main.py

이 프로그램은 두 개의 진행바를 표시하는 PyQt5 위젯을 생성합니다. 각 진행바는 별도의 스레드에서 작동하며, 하나는 0.1초 간격으로, 다른 하나는 0.2초 간격으로 업데이트됩니다.

```python
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
```

- **Worker** 클래스: 이 클래스는 **QThread**를 상속받아 새로운 스레드에서 실행될 코드를 정의합니다. **run** 메서드에서 0%에서 100%까지 진행률을 업데이트하며, 이때 업데이트 간격은 생성자에서 받은 **sleep_time**에 따라 결정됩니다.

- **progress** 시그널: **Worker** 클래스에서 진행 상태가 업데이트될 때마다 이 시그널을 발생시켜 UI를 업데이트합니다.

- **MultiProgressBarWidget** 클래스: 두 개의 진행바를 포함하는 메인 위젯입니다. 두 개의 **Worker** 인스턴스를 생성하고, 각각을 진행바에 연결한 다음 스레드를 시작합니다.


PYQT GUI 융합
---------------

### scripts/PYQT5/04_fusion/01_main_server.py

```python
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
```


- 개요: **ChatServer**는 간단한 채팅 서버 애플리케이션을 구현한 클래스입니다. PyQt를 사용하여 그래픽 사용자 인터페이스를 제공하며, 여러 클라이언트와 동시에 소통할 수 있습니다.

- 서버 초기화:

  - 소켓 생성: 주소 '0.0.0.0'와 포트 8080에 바인드된 TCP 소켓을 사용합니다. 이 주소는 모든 사용 가능한 네트워크 인터페이스를 수신 대기 상태로 설정합니다.

  - 동시 접속: 최대 300개의 동시 연결을 처리할 수 있도록 설정합니다.

  - 클라이언트 리스트: **self.clients** 리스트는 현재 연결된 모든 클라이언트의 소켓을 추적합니다.

- UI 구성:

  - 로그 창: 서버의 활동 및 클라이언트 메시지를 표시하는 창입니다.
  
  - 상태 라벨: 서버의 현재 상태를 나타냅니다.
  
  - 서버 시작 버튼: 실제로는 서버를 시작하지 않지만, 예제의 목적상 UI에 포함되어 있습니다.

- 멀티 스레딩:

  - 서버는 threading 모듈을 사용하여 별도의 스레드에서 클라이언트의 연결을 수락하고 각 클라이언트를 처리합니다.
  
  - 별도의 스레드를 사용하면 서버가 여러 작업을 동시에 처리할 수 있으며, UI는 항상 반응적으로 유지됩니다.

- 메시지 브로드캐스팅:

  - **broadcast** 함수는 연결된 모든 클라이언트에게 메시지를 전송합니다.
  
  - 메시지 발신자는 메시지 수신자 목록에서 제외됩니다.



### scripts/PYQT5/04_fusion/02_client.py


```python
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

```

- 개요: **ChatClient**는 서버와 통신하는 간단한 채팅 클라이언트 애플리케이션을 구현한 클래스입니다.

- 클라이언트 초기화:

  - 소켓 생성 및 연결: 서버의 IP 주소인 '127.0.0.1'와 포트 8080에 연결하려는 TCP 소켓을 생성합니다.

  - 소켓 타임아웃: 1초의 타임아웃을 설정하여, 데이터 수신을 기다리는 동안 메인 스레드가 블로킹되지 않도록 합니다.

- UI 구성:

  - 출력 창: 서버와의 채팅 내역을 표시합니다.
  
  - 입력 라인: 사용자가 메시지를 입력할 수 있는 곳입니다.
  
  - 전송 버튼: 입력한 메시지를 서버로 전송합니다.

- 스레딩:

  - 별도의 스레드에서 **receive_message** 함수를 실행하여, 서버로부터의 메시지를 지속적으로 수신합니다. 이렇게 함으로써 메인 스레드는 항상 반응성을 유지할 수 있습니다.

- 시그널 & 슬롯:

  - PyQt의 시그널-슬롯 메커니즘을 사용하여, 메시지를 받았을 때 메인 스레드에서 UI를 안전하게 업데이트합니다. 이는 스레드 간의 데이터를 안전하게 전달하는 방법입니다.

- 메시지 수신:

  - 메시지를 수신하면, **received_msg_signal** 시그널을 발생시켜 메인 스레드에서 UI를 업데이트합니다.

- 예외 처리:

  - 네트워크 작업 중 발생할 수 있는 예외 상황을 처리하기 위해 다양한 예외 처리 코드가 포함되어 있습니다.