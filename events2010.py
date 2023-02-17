# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def moveEvent(self, a0: QtGui.QMoveEvent) -> None:
        print("x = {0}; y = {1}".format(a0.pos().x(), a0.pos().y()))
        QtWidgets.QWidget.moveEvent(self, a0)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        print("w = {0}; h = {1}".format(a0.size().width(), a0.size().height()))
        QtWidgets.QWidget.resizeEvent(self, a0)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
