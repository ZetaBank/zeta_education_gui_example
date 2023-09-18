import sys
from PyQt5 import QtWidgets

# QApplication 객체 생성
app = QtWidgets.QApplication(sys.argv)
# 위젯 생성 및 표시
button = QtWidgets.QPushButton("Hello World!")
button.show()
# 메인 루프 시작
app.exec_()
