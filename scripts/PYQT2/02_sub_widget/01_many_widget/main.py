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
