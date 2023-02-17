# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets, QtGui


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, id, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = id

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("Получен фокус полем - ", self.id)
        QtWidgets.QLineEdit.focusInEvent(self, a0)

    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("Фокус потерян полем - ", self.id)
        QtWidgets.QLineEdit.focusOutEvent(self, a0)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)
        self.button = QtWidgets.QPushButton("Установить фокус на поле 2")
        self.line1 = MyLineEdit(1)
        self.line2 = MyLineEdit(2)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.line1)
        self.vbox.addWidget(self.line2)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)
        QtWidgets.QWidget.setTabOrder(self.line1, self.line2)
        QtWidgets.QWidget.setTabOrder(self.line2, self.button)

    def on_clicked(self):
        self.line2.setFocus()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
