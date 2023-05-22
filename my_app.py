from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QGroupBox, QRadioButton, QLabel, QListWidget, QLineEdit

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        #устанавливает, как будет выглядеть окно(надпись, размер, место)
        self.set_appear()
        #Создаем и настраиваем графические элементы:
        self.iniUI()
        #Устанавливает связи между элементами
        self.connects()
        #старт:
        self.show()


    def initUI(self):
        #Создает графические элементы
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.istruction = QLabel(txt_istruction)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment= Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment= Qt. AlignLeft)
        self.layout.addWidget(self.btn_next, alignment= Qt.AlignCenter)
        self.setLayout(self.Layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    #устанавливает, как будет выглядеть окно(надпись, размер, место)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_wigth, win_height)
        self.move(win_x, win_y)

#обернуть запуск в функцию
def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()


main()#вызов функции    