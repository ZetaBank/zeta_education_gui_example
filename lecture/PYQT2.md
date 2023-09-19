 Basic Widgets and User Interaction
===================================

라벨 및 버튼 생성
-----------------
### scripts/PYQT2/01_main_widget/01_empty/main.py

- 이 첫번째 예제는 **QMainWindow** 기반의 기본 창만을 보여줍니다. 특별한 위젯이나 요소가 추가되지 않았습니다. **QMainWindow**는 PyQt5의 주 윈도우 클래스입니다. 여기에 다양한 위젯, 툴바, 메뉴바, 상태바 등을 추가할 수 있습니다.
```python
from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
```

</br>

### scripts/PYQT2/01_main_widget/02_label/main.py

- 두번째 예제에서는 기본 창에 **QLabel** 위젯을 추가하여 텍스트 라벨을 표시합니다. **QLabel**은 간단한 텍스트나 이미지를 표시하는 데 사용됩니다.

```python
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QLabel
)

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Create a label
        self.label = QLabel("This is a label!", self)
        # Set the position of the label
        self.label.move(50, 50)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()

```

</br>

버튼 추가 및 이벤트 처리
-----------------------

### scripts/PYQT2/01_main_widget/03_button/main.py

- 세번째 예제에서는 **QPushButton** 위젯을 사용하여 버튼을 추가합니다. 버튼은 사용자 입력을 받는 대표적인 위젯 중 하나입니다.

```python
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPushButton
)

class MainWindow(QMainWindow, object):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Create a button
        self.button = QPushButton("This is a button!", self)
        # Set the position and size of the button
        self.button.move(50, 20)
        self.button.setFixedSize(100, 50)
        
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()

```

</br>

### script/PYQT2/01_main_widget/04_button_click/main.py


- 네번째 예제에서는 버튼에 클릭 이벤트를 연결하여 라벨의 텍스트를 변경하는 동작을 추가합니다. **clicked.connect()** 메서드를 사용하여 버튼 클릭 시 실행될 메서드(**on_button_click** 함수)를 연결합니다.

```python
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

```

</br>

서브 위젯 생성
--------------

### scripts/PYQT2/02_sub_widget/01_many_widget/main.py

- 이 예제에서는 다양한 PyQt5 서브 위젯을 소개합니다.


```python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, 
                             QRadioButton, QComboBox, QCheckBox, QSlider, QTextEdit, QDateEdit, QTimeEdit, 
                             QDateTimeEdit, QDial, QProgressBar)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()

        # QLineEdit: 텍스트 입력 상자
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Type something here")
        layout.addWidget(self.text_input)
        
        # QTextEdit: 멀티라인 텍스트 입력 상자
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)
        
        # QRadioButton: 라디오 버튼
        self.radio_button1 = QRadioButton("Option 1", self)
        self.radio_button2 = QRadioButton("Option 2", self)
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        
        # QCheckBox: 체크박스
        self.checkbox = QCheckBox("Check me out!", self)
        layout.addWidget(self.checkbox)

        # QComboBox: 드롭다운 메뉴
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["Choice 1", "Choice 2", "Choice 3"])
        layout.addWidget(self.combo_box)

        # QSlider: 슬라이더
        self.slider = QSlider(self)
        layout.addWidget(self.slider)

        # QDial: 다이얼
        self.dial = QDial(self)
        layout.addWidget(self.dial)

        # QDateEdit, QTimeEdit, QDateTimeEdit: 날짜 및 시간 선택
        self.date_edit = QDateEdit(self)
        layout.addWidget(self.date_edit)
        
        self.time_edit = QTimeEdit(self)
        layout.addWidget(self.time_edit)
        
        self.datetime_edit = QDateTimeEdit(self)
        layout.addWidget(self.datetime_edit)

        # QProgressBar: 진행 바
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        # 버튼 추가: 사용자 입력 확인
        self.submit_button = QPushButton("Submit", self)
        layout.addWidget(self.submit_button)
        
        # 사용자 입력 내용을 출력할 라벨 추가
        self.output_label = QLabel("", self)
        layout.addWidget(self.output_label)

        # 버튼 클릭 시 실행될 슬롯(함수) 연결
        self.submit_button.clicked.connect(self.display_input)

        # QVBoxLayout을 메인 윈도우에 설정
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def display_input(self):
        text = self.text_input.text()
        text_edit_content = self.text_edit.toPlainText()
        option = self.radio_button1.text() if self.radio_button1.isChecked() else self.radio_button2.text()
        checkbox_status = "Checked" if self.checkbox.isChecked() else "Not Checked"
        choice = self.combo_box.currentText()
        slider_value = str(self.slider.value())
        dial_value = str(self.dial.value())
        date_value = self.date_edit.date().toString()
        time_value = self.time_edit.time().toString()
        datetime_value = self.datetime_edit.dateTime().toString()

        output = ("Text Input: %s\n"
                "Text Edit: %s\n"
                "Selected Option: %s\n"
                "Checkbox Status: %s\n"
                "Selected Choice: %s\n"
                "Slider Value: %s\n"
                "Dial Value: %s\n"
                "Date: %s\n"
                "Time: %s\n"
                "DateTime: %s") % (text, text_edit_content, option, checkbox_status, choice, slider_value, dial_value, date_value, time_value, datetime_value)

        self.output_label.setText(output)
        
if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()

```

- **QLineEdit**: 한 줄의 텍스트를 입력받는 위젯입니다.
- **QTextEdit**: 여러 줄의 텍스트를 입력받는 위젯입니다.
- **QRadioButton**: 사용자에게 여러 옵션 중 하나를 선택하게 하는 위젯입니다.
- **QCheckBox**: 선택 상자 위젯입니다. 체크되었는지 아닌지를 나타냅니다.
- **QComboBox**: 드롭다운 목록에서 선택할 수 있는 위젯입니다.
- **QSlider** 및 QDial: 값을 슬라이드 혹은 회전시켜 선택하게 하는 위젯입니다.
- **QDateEdit**, **QTimeEdit**, **QDateTimeEdit**: 날짜, 시간, 날짜 및 시간을 선택하는 위젯입니다.
- **QProgressBar**: 진행 상태를 그래픽적으로 표시하는 위젯입니다.
- 이러한 서브 위젯들은 사용자에게 다양한 유형의 입력을 받거나 정보를 제공하는 데 사용됩니다. 이 예제에서는 각 위젯의 기본 기능과 어떻게 사용되는지를 보여줍니다.


</br>

### scripts/PYQT2/02_sub_widget/02_spin_box/main.py

- 이 예제에서는 QSpinBox 위젯의 사용법을 보여줍니다.

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QVBoxLayout, QWidget, QLabel

class SpinBoxExample(QMainWindow):
    def __init__(self):
        super(SpinBoxExample, self).__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Selected Value:", self)

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0, 100)  # 0부터 100까지의 범위 설정
        self.spin_box.setSingleStep(5)  # 5단위로 값 변경
        self.spin_box.setPrefix("$")    # 접두사로 달러 표시
        self.spin_box.valueChanged.connect(self.update_label)  # 값 변경 시 라벨 업데이트

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self, value):
        self.label.setText("Selected Value: ${}".format(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpinBoxExample()
    window.show()
    sys.exit(app.exec_())

```

- **QSpinBox**: 사용자에게 정수 값을 입력하도록 하는 위젯입니다. 사용자는 위젯 내의 화살표를 클릭하거나 직접 숫자를 입력하여 값을 변경할 수 있습니다.
- 이 예제에서 **QSpinBox**는 0부터 100까지의 범위를 갖고, 5단위로 값을 변경합니다. 또한, 선택된 값 앞에 '$' 기호를 접두사로 추가하여 화면에 표시됩니다. 사용자가 값에 변화를 주면 연결된 슬롯 함수 **update_label**이 호출되어 라벨 위젯의 텍스트가 업데이트됩니다.


</br>

화면전환: 스택 위젯 활용
-----------------------

- **화면 전환**: 스택 위젯 활용하여 여러 화면을 전환하는 방법

- PyQt에서는 **QStackedWidget**를 활용해 여러 개의 화면 (또는 페이지) 중 하나만을 표시하게끔 할 수 있습니다.
- 이 예제에서는 세 개의 페이지를 **QStackedWidget**에 추가하고, 각 페이지는 버튼을 포함하여 다른 페이지로 전환될 수 있습니다.

### scripts/PYQT2/03_toggle_screens/main.py

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create the stacked widget
        self.stack = QStackedWidget()

        # Create some sample pages
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()

        # Add pages to the stacked widget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        # Sample layout for page 1
        layout1 = QVBoxLayout(self.page1)
        layout1.addWidget(QLabel("여긴 1 페이지입니다."))
        button1 = QPushButton("2 페이지로 가자")
        layout1.addWidget(button1)
        button1.clicked.connect(self.go_to_page2)

        # Sample layout for page 2
        layout2 = QVBoxLayout(self.page2)
        layout2.addWidget(QLabel("여긴 2 페이지라고라"))
        button2 = QPushButton("3 페이지로 가기")
        layout2.addWidget(button2)
        button2.clicked.connect(self.go_to_page3)

        # Sample layout for page 3
        layout3 = QVBoxLayout(self.page3)
        layout3.addWidget(QLabel("여긴 3 페이지라고하지"))
        button3 = QPushButton("1 페이지로 가볼까")
        layout3.addWidget(button3)
        button3.clicked.connect(self.go_to_page1)

        # Set the current widget to be page 1
        self.stack.setCurrentWidget(self.page1)

        # Set the stacked widget as the central widget of the window
        self.setCentralWidget(self.stack)

    def go_to_page1(self):
        self.stack.setCurrentWidget(self.page1)

    def go_to_page2(self):
        self.stack.setCurrentWidget(self.page2)

    def go_to_page3(self):
        self.stack.setCurrentWidget(self.page3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

```
- 버튼이 클릭될 때 **clicked.connect()** 함수를 활용하여 연결된 슬롯 함수를 실행하고, 해당 함수 내에서 **setCurrentWidget()** 함수를 사용하여 현재 화면을 변경합니다.

- **QStackedWidget**: 여러 페이지를 포함하고 한 번에 하나의 페이지만 표시하는 위젯입니다.

- **setCurrentWidget()**: **QStackedWidget**의 현재 표시되는 페이지를 설정하는 함수입니다.


### 상세 분석

1. 스택 위젯 생성
    ```python
    self.stack = QStackedWidget()
    ```
2.  샘플 페이지 생성 및 추가
    ```python
    self.page1 = QWidget()
    ...
    self.stack.addWidget(self.page1)
    ```
3. 페이지 내용 설정: 각 페이지에는 라벨과 버튼이 포함됩니다. 버튼을 클릭하면 다른 페이지로 전환됩니다.
    ```python
    layout1 = QVBoxLayout(self.page1)
    layout1.addWidget(QLabel("여긴 1 페이지입니다."))
    button1 = QPushButton("2 페이지로 가기")
    ```
4. 버튼 클릭 이벤트 연결: **go_to_page2**와 같은 메서드들을 활용하여 각 버튼을 해당 페이지로 전환하는 로직과 연결합니다.
    ```python
    button1.clicked.connect(self.go_to_page2)
    ```
5. 초기 페이지 설정: 앱이 실행될 때 기본적으로 보여질 페이지를 설정합니다.
    ```python
    self.stack.setCurrentWidget(self.page1)
    ```

</br>

이미지 전환: 화면 전환 시각화
----------------------------

- **이미지 전환**: 이미지를 사용하여 화면 전환 시각화하는 방법

- 이미지 전환도 기본 원리는 위와 동일합니다. 차이점은 각 페이지에 이미지 (**QLabel**에 설정된 **QPixmap**)가 포함되어 있다는 것입니다.
- **create_page** 함수를 사용하여 이미지 경로와 버튼 텍스트를 입력으로 받아, 페이지를 생성합니다.
- 이 함수에서는 입력된 이미지 경로를 사용해 **QPixmap** 객체를 생성하고, 이를 **QLabel** 위젯에 설정하여 이미지를 표시합니다.

</br>

### scripts/PYQT2/04_toggle_images/main.py

```python
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

```


- 람다 함수를 사용하여 버튼 클릭 시에 연결될 슬롯을 정의합니다. 이 방법을 통해 버튼 클릭 시 특정 페이지로 전환될 수 있게 됩니다.

- **이미지 표시**: **QPixmap** 객체를 생성하여 이미지를 로드하고, 이를 **QLabel** 위젯에 설정하여 화면에 표시할 수 있습니다.

- **람다 함수**: PyQt에서는 시그널-슬롯 연결 시, 특정 함수에 인자를 전달하거나 간단한 로직을 정의하기 위해 람다 함수를 활용할 수 있습니다.

### 상세 분석

1. 스택 위젯 생성
    ```python
    self.stack = QStackedWidget()
    ```
2. 이미지가 포함된 페이지 생성: **create_page** 메서드를 통해 이미지와 버튼을 포함한 페이지를 생성합니다.
    ```python
    self.page1 = self.create_page("images/twinkle_bocchi.png", "Go to Ai")
    ```
3. 이미지 로딩 및 표시: **QPixmap**을 사용하여 이미지를 로드하고, **QLabel**에 설정하여 화면에 표시합니다.
    ```python
    pixmap = QPixmap(image_path)
    image_label.setPixmap(pixmap)
    ```
4. 버튼 클릭 이벤트 연결: 람다 함수를 사용하여 각 버튼을 해당 페이지로 전환하는 로직과 연결합니다.
    ```python
    btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))
    ```
