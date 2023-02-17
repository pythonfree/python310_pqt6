# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets, QtCore


class MyWindow(QtWidgets.QWidget):
    mysignal = QtCore.pyqtSignal(int, int)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Пользовательский сигнал")
        self.resize(300, 100)
        self.button1 = QtWidgets.QPushButton("Нажми меня")
        self.button2 = QtWidgets.QPushButton("Кнопка 2")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        self.setLayout(vbox)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.mysignal.connect(self.on_mysignal)

    def on_clicked_button1(self):
        print("Нажата кнопка button1")
        self.button2.clicked[bool].emit(False)
        self.mysignal.emit(10, 20)

    def on_clicked_button2(self):
        print("Нажата кнопка button2")

    def on_mysignal(self, x, y):
        print("Обработан пользовательский сигнал mysignal()")
        print("x = ", x, "y = ", y)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
