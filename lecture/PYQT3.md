Advanced Widgets and Interaction
=================================

모달 및 모드리스 대화상자 생성
------------------------------

- **모달 (Modal) 대화상자**
  - 사용자가 다이얼로그를 닫기 전까지 메인 윈도우와 상호작용할 수 없습니다.
  
  - 일반적으로 사용자의 집중을 요구하는 중요한 정보나 결정에 사용됩니다.

- **모드리스 (Modeless) 대화상자**

  - 다이얼로그가 열려 있어도 메인 윈도우와 동시에 상호작용할 수 있습니다.

<br/>

### scripts/PYQT3/01_modal_modeless/main.py


```python
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

```

</br>

- **show_modal** 메소드는 모달 다이얼로그를 생성하고 화면에 표시합니다.

  - **QDialog(self)** 를 통해 **QDialog** 객체를 생성합니다.

  - **exec_()** 메소드는 모달 다이얼로그를 실행합니다.
 
- **show_modeless** 메소드는 모드리스 다이얼로그를 생성하고 화면에 표시합니다.

  - **QDialog(self)** 를 통해 **QDialog** 객체를 생성합니다.

  - **show()** 메소드는 모드리스 다이얼로그를 실행합니다.



### exec_()와 show()의 차이점

**exec_()** 와 **show()** 는 PyQt에서 다이얼로그나 위젯을 표시하는 두 가지 주요 메소드입니다. 둘의 주요 차이점은 다음과 같습니다:

1. **Block** vs **Non-Block**:

    - **exec_()**: 이 메소드는 **blocking**입니다.

        - 이것은 **exec_()** 메소드를 호출하면 해당 다이얼로그가 닫힐 때까지 코드의 실행이 일시 중지됨을 의미합니다.

        - 이것은 모달 다이얼로그에서 주로 사용됩니다.

        - 사용자가 다이얼로그에 응답하기 전까지 애플리케이션의 다른 부분과 상호작용할 수 없게 만듭니다.
    
    - **show()**: 이 메소드는 **non-blocking**입니다.
        
        - **show()** 메소드를 호출하면 다이얼로그가 표시되고 코드는 계속 실행됩니다.
        
        - 이것은 모드리스 다이얼로그에서 주로 사용됩니다.
        
        - 사용자는 다이얼로그와 함께 애플리케이션의 다른 부분과도 상호작용할 수 있습니다.

2. **Return Value**:

    - **exec_()**: 반환값이 있습니다.
        
        - 대부분의 경우 **QDialog.Accepted** 또는 **QDialog.Rejected** 중 하나의 값을 반환합니다.
        
        - 이것은 사용자가 다이얼로그에서 '**OK**' 또는 '**Cancel**' 버튼을 클릭했는지를 나타내는데 사용될 수 있습니다.
    
    - **show()**: 반환값이 없습니다.

3. **Use Cases**:

    - **exec_()**: 주로 사용자의 응답을 기다려야 할 때 사용됩니다. 예를 들어, 정보를 입력하도록 요청하는 팝업 창에서 사용자의 선택을 기다릴 필요가 있을 때입니다.

    - **show()**: 정보를 제공하거나 사용자에게 선택의 여지를 주지 않는 경우에 주로 사용됩니다.

결론적으로, 어떤 메소드를 사용할지는 다이얼로그의 목적과 사용자와의 상호작용 방식에 따라 결정

<br/>


표준 대화상자 활용
------------------

이 예제에서는 PyQt5를 사용하여 여러 표준 대화상자를 어떻게 사용하는지에 대한 방법을 알아봅니다. 대화상자는 사용자에게 파일 선택, 컬러 선택, 폰트 선택 등의 작업을 요청할 때 매우 유용합니다.

</br>

### scripts/PYQT3/02_dialog_box/main.py

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QColorDialog, QFontDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        layout = QVBoxLayout()

        # File Dialog
        self.label_file = QLabel(self)
        layout.addWidget(self.label_file)
        
        self.btn_open_file = QPushButton("Open File", self)
        self.btn_open_file.clicked.connect(self.open_file)
        layout.addWidget(self.btn_open_file)

        # Color Dialog
        self.label_color = QLabel("Selected Color", self)
        layout.addWidget(self.label_color)

        self.btn_open_color = QPushButton("Open Color Dialog", self)
        self.btn_open_color.clicked.connect(self.open_color)
        layout.addWidget(self.btn_open_color)

        # Font Dialog
        self.label_font = QLabel("Sample Text", self)
        layout.addWidget(self.label_font)

        self.btn_open_font = QPushButton("Open Font Dialog", self)
        self.btn_open_font.clicked.connect(self.open_font)
        layout.addWidget(self.btn_open_font)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.label_file.setText(u"Selected file: {}".format(file_name))

    def open_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.label_color.setText("Selected Color: {}".format(color.name()))
            self.label_color.setStyleSheet("background-color: {}".format(color.name()))

    def open_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label_font.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


```

1. **파일 선택 대화상자**: 사용자가 파일을 선택할 수 있게 해주는 대화상자입니다.

    - **QFileDialog.getOpenFileName()** 메서드를 사용하여 파일 선택 대화상자를 열 수 있습니다.

    - 사용자가 파일을 선택하면, 선택한 파일의 경로는 레이블에 표시됩니다.

2. **컬러 선택 대화상자**: 사용자가 컬러를 선택할 수 있는 대화상자입니다.

    - **QColorDialog.getColor()** 메서드를 사용하여 컬러 선택 대화상자를 열 수 있습니다.

    - 사용자가 유효한 컬러를 선택하면, 해당 컬러는 레이블의 배경색으로 설정되고, 선택한 컬러의 이름이 레이블에 표시됩니다.

3. **폰트 선택 대화상자**: 사용자가 폰트를 선택할 수 있는 대화상자입니다.

    - **QFontDialog.getFont()** 메서드를 사용하여 폰트 선택 대화상자를 열 수 있습니다.
    
    - 사용자가 폰트를 선택하면, 레이블의 폰트가 선택한 폰트로 변경됩니다.

전체 구조는 **QVBoxLayout**을 사용하여 위에서 아래로 위젯을 정렬하고, 이를 메인 윈도우의 중앙 위젯으로 설정하였습니다.


</br>

데이터 모델: 테이블, 리스트 등의 데이터 모델 및 뷰 위젯 활용 방법
-------------------------------------------------------------

PyQt5에서는 데이터 모델을 다루기 위해 MVC(Model-View-Controller) 패턴을 사용합니다. 이 패턴은 사용자 인터페이스의 기능을 모델, 뷰, 컨트롤러 세 부분으로 분리하여 각 부분을 독립적으로 개발하게 합니다. PyQt5의 **QAbstractTableModel**과 **QAbstractListModel**은 이 패턴의 모델 부분을 구현하는 클래스입니다.

**QAbstractTableModel**은 2차원의 데이터 구조, 즉 행과 열로 구성된 데이터를 표현하는 데 사용됩니다.

**QAbstractListModel**은 1차원의 데이터 구조, 즉 목록이나 배열과 같은 연속된 항목들을 표현하는 데 사용됩니다.

</br>


### scripts/PYQT3/03_data_model/01_table_view/main.py


</br>

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QTableView, QMainWindow, QVBoxLayout, QWidget

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def flags(self, index):
        return super(TableModel, self).flags(index) & ~Qt.ItemIsEditable

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.table = QTableView()

        data = [
            [1, "김", "철수"],
            [2, "박", "혁수"],
            [3, "이", "고수"],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

- **QTableView**와 **QAbstractTableModel**을 사용하여 테이블 데이터를 표시합니다.

- **TableModel** 클래스는 **QAbstractTableModel**을 상속받아 구현됩니다.

  - **rowCount**와 **columnCount** 메서드를 통해 테이블의 행과 열의 수를 반환합니다.

  - **data** 메서드는 특정 셀의 데이터를 반환합니다.

  - **flags** 메서드를 사용하여 아이템이 편집 불가능하게 설정됩니다.

```python
data = [
    [1, "김", "철수"],
    [2, "박", "혁수"],
    [3, "이", "고수"],
]
```
위 데이터를 **TableModel**을 통해 테이블 뷰에 표시합니다.

</br>


### scripts/PYQT3/03_data_model/02_list_view/main.py


</br>

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QListView, QMainWindow, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import QStringListModel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.list_view = QListView()
        self.model = QStringListModel()
        names = ["김철수", "박혁수", "이고수"]
        self.model.setStringList(names)
        self.list_view.setModel(self.model)

        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QVBoxLayout()
        layout.addWidget(self.list_view)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
```

- **QListView**와 **QStringListModel**을 사용하여 리스트 데이터를 표시합니다.

- 리스트 뷰는 아이템들을 수직으로 나열하여 표시하며, 사용자는 아이템 중 하나를 선택할 수 있습니다.

- **QStringListModel**은 문자열 리스트를 모델로 사용하여 간단한 데이터를 표시하기에 적합합니다.
```python
names = ["김철수", "박혁수", "이고수"]
```
위 데이터를 **QStringListModel**을 통해 리스트 뷰에 표시합니다. 또한, **setEditTriggers** 메서드를 사용하여 아이템 편집을 비활성화합니다.


</br>

위젯 외관 커스터마이징
---------------------

- PyQt5에서는 **setStyleSheet()** 메서드를 사용하여 위젯의 스타일을 정의할 수 있습니다.

- CSS와 유사한 문법을 사용하여 각 위젯의 속성을 설정할 수 있습니다. 예를 들어, 배경색, 테두리 두께, 패딩, 글꼴 크기 및 색상 등을 설정할 수 있습니다.

</br>

### scripts/PYQT3/04_widget_customized/01_many_widget/main.py

- 앞에서 했던 다양한 위젯을 대상으로 위젯의 외관을 변경했습니다.

- **apply_styles()** 메서드에서 각 위젯에 대한 스타일이 정의되어 있습니다. 예를 들어, **QLineEdit** 위젯은 검은색 배경, 노란색 텍스트, 주황색 테두리를 가지며, 테두리는 둥글게 설정되어 있습니다.

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
        self.apply_styles()

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

    def apply_styles(self):
        style = """
                QLineEdit {
                    background-color: #2c3e50;
                    color: #f7dc6f;
                    border: 2px solid #27ae60;
                    border-radius: 5px;
                    padding: 5px;
                    margin: 5px;
                }
                QTextEdit {
                    background-color: #2980b9;
                    color: #f4d313;
                    border: 2px solid #8e44ad;
                    border-radius: 5px;
                    padding: 5px;
                    margin: 5px;
                }
                QRadioButton {
                    spacing: 5px;
                    color: #f39c12;
                    margin: 5px;
                }
                QCheckBox {
                    spacing: 5px;
                    color: #e74c3c;
                    margin: 5px;
                }
                QComboBox {
                    background-color: #c0392b;
                    color: #ecf0f1;
                    border: 2px solid #3498db;
                    border-radius: 5px;
                    padding: 5px;
                    margin: 5px;
                }
                QSlider::groove:horizontal {
                    background: #1abc9c;
                    height: 5px;
                    border-radius: 2px;
                }
                QSlider::handle:horizontal {
                    background: #d35400;
                    width: 18px;
                    height: 18px;
                    border-radius: 9px;
                    margin: -7px 0;
                }
                QDial::groove {
                    background: #f1c40f;
                }
                QDial::handle {
                    background: #c74b3b;
                    width: 10px;
                    height: 10px;
                    border-radius: 5px;
                }
                QDateEdit, QTimeEdit, QDateTimeEdit {
                    background-color: #8e44ad;
                    color: #f0e68c;
                    border: 2px solid #2e8b57;
                    border-radius: 5px;
                    padding: 5px;
                    margin: 5px;
                }
                QProgressBar {
                    text-align: center;
                    border: 2px solid #4682b4;
                    border-radius: 5px;
                }
                QProgressBar::chunk {
                    background-color: #d2b48c;
                    width: 20px;
                }
                QPushButton {
                    background-color: #5f9ea0;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    color: #daa520;
                    margin: 5px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #20b2aa;
                }
                QPushButton:pressed {
                    background-color: #556b2f;
                }
            """

        self.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()

```

</br>

### scripts/PYQT3/04_widget_customized/02_spin_box/main.py

- **apply_spinbox_style()** 메서드에서 스핀 박스의 스타일이 정의되어 있습니다. 스핀 박스에는 회색 배경, 약간 둥근 테두리가 있으며, 위쪽 화살표는 녹색, 아래쪽 화살표는 빨간색으로 표시됩니다.

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QVBoxLayout, QWidget, QLabel

class SpinBoxStyled(QMainWindow):
    def __init__(self):
        super(SpinBoxStyled, self).__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Selected Value:", self)
        self.apply_label_style()

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0, 100)  # 0부터 100까지의 범위 설정
        self.spin_box.setSingleStep(5)  # 5단위로 값 변경
        self.spin_box.setPrefix("$")    # 접두사로 달러 표시
        self.spin_box.valueChanged.connect(self.update_label)  # 값 변경 시 라벨 업데이트
        self.apply_spinbox_style()

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self, value):
        self.label.setText("Selected Value: ${}".format(value))

    def apply_label_style(self):
        style = """
            QLabel {
                font-size: 18px;
                color: #3498db;
            }
        """
        self.label.setStyleSheet(style)

    def apply_spinbox_style(self):
        style = """
            QSpinBox {
                border: 2px solid #dcdde1;
                border-radius: 5px;
                padding: 5px;
                background-color: #f1f2f6;
                min-width: 200px;
                min-height: 100px;
            }

            QSpinBox::up-button {
                image: url('_icon/up.png');
                subcontrol-origin: border;
                subcontrol-position: top right;
                
                border-width: 1px;
                width: 50px;
                height: 50px;
                background: #2ecc71;
            }

            QSpinBox::down-button {
                image: url('_icon/down.png');
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                
                border-width: 1px;
                width: 50px;
                height: 50px;
                background: #e74c3c;
            }
        """
        self.spin_box.setStyleSheet(style)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpinBoxStyled()
    window.show()
    sys.exit(app.exec_())
```

