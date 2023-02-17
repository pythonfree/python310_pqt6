# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(self,
                                                "Подтверждение закрытия окна",
                                                "Вы действительно хотите закрыть окно?"
                                                )
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            a0.accept()
            QtWidgets.QWidget.closeEvent(self, a0)
        else:
            a0.ignore()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
