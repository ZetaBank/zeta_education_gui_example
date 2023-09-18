Interaction and Communication
================================

키보드 입력 감지
----------------

PyQt를 사용하면 사용자의 키보드 입력을 쉽게 감지할 수 있습니다. 각 키보드 이벤트는 **keyPressEvent** 함수를 통해 처리됩니다. 예를 들면, 사용자가 'A' 키를 누르면, 특정 작업을 수행할 수 있습니다.


### scripts/PYQT4/01_key_pressed/01_A_pressed/main.py:


이 예제는 사용자가 'A' 키를 눌렀을 때 텍스트 에디터에 "You pressed the 'A' key!"라는 메시지를 출력하는 프로그램입니다.

- **CustomTextEdit**는 **QTextEdit**을 상속받아서 사용자의 키보드 입력을 감지하는 기능을 추가합니다.

- **keyPressEvent** 함수는 키보드 이벤트를 감지하고 처리하는 함수입니다. 여기서 'A' 키의 입력을 감지하면, 텍스트 에디터에 메시지를 출력하도록 정의되어 있습니다.


```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt

class CustomTextEdit(QTextEdit):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.append("You pressed the 'A' key!")
        else:
            super(CustomTextEdit, self).keyPressEvent(event)

class KeyDetectionApp(QMainWindow):
    def __init__(self):
        super(KeyDetectionApp, self).__init__()

        self.text_edit = CustomTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Keyboard Event Detection')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyDetectionApp()
    window.show()
    sys.exit(app.exec_())

```

</br>

01_key_pressed/02_move_rectangle/main.py:
이 예제는 사용자가 키보드의 A, S, W, D 키를 눌렀을 때 사각형을 상하좌우로 움직이게 하는 프로그램입니다.

- **RectangleMover** 클래스는 **QGraphicsView** 위에 파란색 사각형을 그리고, 사용자의 키보드 입력에 따라 사각형을 움직입니다.

- **keyPressEvent** 함수는 키보드 이벤트를 감지하고, 해당 키에 맞는 방향으로 사각형을 이동시킵니다.

```python
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

```

</br>

### 설명

```python
self.view = QGraphicsView(self)
self.scene = QGraphicsScene(self)
self.view.setScene(self.scene)

self.rectangle = self.scene.addRect(QRectF(0, 0, 50, 50), QPen(), QBrush(Qt.blue))
self.view.setSceneRect(0, 0, 800, 600)
```

1. **QGraphicsView**는 2D 그래픽 항목을 시각화하고, 사용자와 상호 작용할 수 있게 하는 위젯입니다.

2. **QGraphicsScene**는 2D 그래픽 항목들을 저장하는 컨테이너 역할을 합니다. 즉, 그래픽 항목들의 '캔버스'와 같습니다.

3. **setScene()** 메서드를 사용하여 **QGraphicsView**에 **QGraphicsScene**을 연결합니다.

4. **self.scene.addRect(...)**:

    - **self.scene**는 **QGraphicsScene** 객체입니다. **QGraphicsScene**는 그래픽 아이템들을 가지고 있는 컨테이너 역할을 합니다. 그래픽 아이템들을 시각적으로 표시하려면 **QGraphicsView**을 사용해야 합니다..

    - **addRect**는 **QGraphicsScene**의 메서드로, 사각형 그래픽 아이템을 추가하고 그 아이템에 대한 참조를 반환합니다.

5. **QRectF(0, 0, 50, 50)**:

    - **QRectF**는 사각형을 표현하는 PyQt 클래스입니다. 여기서는 (0, 0)을 시작점으로 가로 50, 세로 50의 크기의 사각형을 표현합니다.

6. **QPen()**:

    - **QPen** 클래스는 선의 스타일을 정의합니다. 여기서는 기본 **QPen**을 사용하므로, 사각형의 테두리는 기본 스타일로 그려집니다.

7. **QBrush(Qt.blue)**:

    - **QBrush** 클래스는 도형 내부를 채우는 스타일과 색상을 정의합니다. **Qt.blue**로 설정되어 있으므로, 사각형 내부는 파란색으로 채워집니다.


</br>

마우스 입력
------------


### scripts/PYQT4/01_key_pressed/02_mouse_clicked/main.py
```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class MouseDetectionApp(QMainWindow):
    def __init__(self):
        super(MouseDetectionApp, self).__init__()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Click or move the mouse!")
        self.label.setMouseTracking(True)  # 마우스 이동 감지 활성화
        self.setCentralWidget(self.label)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Mouse Event Detection')
        self.setGeometry(100, 100, 400, 300)

    def mousePressEvent(self, event):
        self.label.setText("Mouse Pressed: Button {} at {}".format(event.button(), event.pos()))

    def mouseReleaseEvent(self, event):
        self.label.setText("Mouse Released: Button {} at {}".format(event.button(), event.pos()))

    def mouseMoveEvent(self, event):
        self.label.setText("Mouse Moved: Position {}".format(event.pos()))

    def mouseDoubleClickEvent(self, event):
        self.label.setText("Mouse Double Clicked: Button {} at {}".format(event.button(), event.pos()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MouseDetectionApp()
    window.show()
    sys.exit(app.exec_())

```

- **mousePressEvent(event):** 마우스 버튼이 클릭될 때 호출되는 메서드입니다. 여기서는 눌린 마우스 버튼과 클릭된 위치 정보를 표시합니다.

- **mouseReleaseEvent(event):** 마우스 버튼이 떼어질 때 호출되는 메서드입니다. 여기서도 마우스 버튼과 위치 정보를 표시합니다.

- **mouseMoveEvent(event):** 마우스가 움직일 때 호출되는 메서드입니다. 마우스의 현재 위치를 표시합니다.

- **mouseDoubleClickEvent(event):** 마우스 버튼이 더블 클릭될 때 호출되는 메서드입니다. 더블 클릭된 버튼과 위치 정보를 표시합니다.

- **self.label.setMouseTracking(True):** 이 코드는 마우스가 위젯 위에서 움직일 때마다 **mouseMoveEvent**를 호출하도록 설정합니다. 만약 **setMouseTracking**이 **False**로 설정되면, 마우스 버튼을 누르면서만 **mouseMoveEvent**가 호출됩니다.

- **event.button():** 발생한 마우스 이벤트와 관련된 버튼(왼쪽, 오른쪽, 중앙) 정보를 반환합니다.

- **event.pos():** 마우스 이벤트가 발생한 위치의 좌표 정보를 반환합니다.

</br>


키보드와 마우스 입력 감지
-----------------------

PyQt는 키보드와 마우스 이벤트를 동시에 감지하고 처리할 수 있습니다. 이 예제에서는 사용자가 'A' 키를 누른 상태에서 마우스를 클릭하면 화면에 표시되는 메시지가 변경됩니다.

### scripts/PYQT4/01_key_pressed/03_key_and_mouse_detection/main.py

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class CombinedEventApp(QMainWindow):
    def __init__(self):
        super(CombinedEventApp, self).__init__()
        self.key_pressed = None
        self.a_clicked = False
        self.label = QLabel("Press 'A' and then click the mouse!", self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Combined Keyboard and Mouse Event')
        self.setGeometry(100, 100, 400, 300)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            if not self.a_clicked:
                self.key_pressed = Qt.Key_A
                self.a_clicked = True
            else:
                self.key_pressed = None
                self.a_clicked = False
        else:
            self.key_pressed = None
            self.a_clicked = False

    def mousePressEvent(self, event):
        if self.key_pressed == Qt.Key_A:
            self.label.setText("You pressed 'A' and clicked the mouse!")
            self.key_pressed = None
        else:
            self.label.setText("Press 'A' and then click the mouse!")
        self.a_clicked = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CombinedEventApp()
    window.show()
    sys.exit(app.exec_())

```

### 설명

이 예제에서 중요한 부분은 keyPressEvent와 mousePressEvent 함수입니다.

- **keyPressEvent**: 이 함수는 키보드 이벤트를 감지하며, 사용자가 'A' 키를 누르면 라벨의 텍스트를 변경합니다.

- **mousePressEvent**: 이 함수는 마우스 이벤트를 감지합니다. 만약 'A' 키가 눌러진 상태에서 마우스를 클릭하면, 라벨의 텍스트가 다시 변경됩니다.

이렇게 두 함수를 활용하여 키보드와 마우스 입력을 동시에 감지하고 처리하는 동작을 구현했습니다.

</br>


File I/O and Persistence
---------------------------
### scripts/PYQT4/04_data/01_json/main.py:

```python
# -*- coding: utf-8 -*-

import json

data = {"name": "John", "age": 30, "city": "New York"}

# 데이터 저장
with open("data.json", "w") as file:
    json.dump(data, file)

# 데이터 읽기
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

이 예제는 Python 딕셔너리 데이터를 JSON 파일로 저장하고, 저장된 JSON 파일을 다시 읽어서 출력하는 프로그램입니다.
- **json.dump()** 함수를 사용하여 데이터를 JSON 형식으로 파일에 저장합니다.
- *json.load()* 함수를 사용하여 JSON 파일의 데이터를 다시 불러와 출력합니다.

</br>

### scripts/PYQT4/04_data/02_data_read/main.py


```python
# -*- coding: utf-8 -*-

import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableApp(QMainWindow):
    def __init__(self):
        super(TableApp, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Data from JSON')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # 데이터 로드
        with open("../01_json/data.json", "r") as file:
            data = json.load(file)

        # 표 생성
        table = QTableWidget(self)
        table.setRowCount(len(data))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['Key', 'Value'])

        for row, (key, value) in enumerate(data.items()):
            table.setItem(row, 0, QTableWidgetItem(str(key)))
            table.setItem(row, 1, QTableWidgetItem(str(value)))

        layout.addWidget(table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableApp()
    window.show()
    sys.exit(app.exec_())

```

이 예제는 JSON 파일로 저장된 데이터를 읽어와서 PyQt의 테이블 위젯에 표시하는 프로그램입니다.

- **TableApp** 클래스는 저장된 JSON 데이터를 읽어와 **QTableWidget**에 데이터를 표시합니다.

- 테이블의 각 행은 JSON 데이터의 키와 값을 표시합니다.

타이머
--------

- **QTimer**는 주기적으로 시그널을 발생시키는 타이머를 제공합니다.

</br>

### scripts/PYQT4/05_timer/main.py


```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import QTimer

class TimerTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(TimerTextEdit, self).__init__(parent)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.append_message)
        self.timer.start(5000)  # 5000ms = 5s

    def append_message(self):
        self.append("5 seconds have passed!")

class TimerApp(QMainWindow):
    def __init__(self):
        super(TimerApp, self).__init__()

        self.text_edit = TimerTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QTimer Example')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())

```


이 스크립트는 PyQt5를 사용하여 간단한 타이머 애플리케이션을 구현한 것입니다. 사용자에게 **QTextEdit** 위젯을 제공하며, 이 위젯 내에서 **QTimer**를 설정하여 5초마다 메시지를 출력합니다.

- **TimerTextEdit**: **QTextEdit**의 하위 클래스로, **QTimer**를 사용하여 5초마다 메시지를 추가합니다.
- **TimerApp**: 메인 윈도우 클래스로, **TimerTextEdit**를 중앙 위젯으로 사용합니다.


</br>

신호 및 슬롯
----------

- PyQt의 중심적인 특징 중 하나는 신호 및 슬롯 메커니즘이 있습니다.

- 위젯이나 다른 객체에서 발생하는 이벤트(신호)를 처리하는 함수(슬롯)에 연결할 수 있습니다.

### scripts/PYQT4/05_timer/main.py

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal

class SignalTextEdit(QTextEdit):
    a_key_pressed = pyqtSignal()

    def __init__(self, parent=None):
        super(SignalTextEdit, self).__init__(parent)
        self.a_key_pressed.connect(self.on_a_key_pressed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.a_key_pressed.emit()
        else:
            super(SignalTextEdit, self).keyPressEvent(event)

    def on_a_key_pressed(self):
        self.append("You pressed the 'A' key!")

class SignalApp(QMainWindow):
    def __init__(self):
        super(SignalApp, self).__init__()

        self.text_edit = SignalTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Signal and Slot Example')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignalApp()
    window.show()
    sys.exit(app.exec_())
```
이 스크립트는 PyQt5의 신호 및 슬롯 메커니즘을 활용하여 키보드 입력을 감지하는 애플리케이션을 구현한 것입니다. 사용자가 'B' 키를 누르면 텍스트 영역에 메시지가 추가됩니다.

- **SignalTextEdit**: **QTextEdit**의 하위 클래스로, 'B' 키 입력을 감지하여 사용자 정의 시그널 **a_key_pressed**를 발생시킵니다.

- **SignalApp**: 메인 윈도우 클래스로, **SignalTextEdit**를 중앙 위젯으로 사용합니다.


### 위의 01_key_pressed/01_A_pressed/main.py 와의 차이점

1. 이벤트 처리 방식:

    - 제공된 예제는 직접 keyPressEvent를 재정의하여 'A' 키를 감지합니다.
    
    - ### scripts/PYQT4/06_signal_and_slot/main.py는 사용자 정의 시그널 및 슬롯 메커니즘을 사용하여 'B' 키를 감지합니다.

2. 유연성:

    - 신호 및 슬롯 메커니즘은 여러 시그널을 여러 슬롯에 연결할 수 있어 유연성이 더 높습니다. 따라서 후자의 방식은 복잡한 상호 작용이나 확장성을 고려할 때 더 적합합니다.

    - 직접 이벤트 처리 방식은 간단하고 직관적입니다. 간단한 상호 작용이 필요할 때 적합합니다.