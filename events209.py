# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtCore, QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def changeEvent(self, a0: QtCore.QEvent) -> None:
        if a0.type() == QtCore.QEvent.Type.WindowStateChange:
            if self.isMinimized():
                print("Окно свернуто.")
            elif self.isMaximized():
                print("Окно раскрыто до макс. размеров")
            elif self.isFullScreen():
                print("Полноэкранный режим")
            elif self.isActiveWindow():
                print("Окно находится в фокусе ввода.")
        QtWidgets.QWidget.changeEvent(self, a0)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        print("Окно отображено.")
        QtWidgets.QWidget.showEvent(self, a0)

    def hideEvent(self, a0: QtGui.QHideEvent) -> None:
        print("Окно скрыто")
        QtWidgets.QWidget.hideEvent(self, a0)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
