# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets, QtWebEngineWidgets, QtCore
from inspect import currentframe, getframeinfo
import time

cf = currentframe()
filename = getframeinfo(cf).filename

class Web(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.web = QtWebEngineWidgets.QWebEngineView()
        # self.web.load(QtCore.QUrl('https://www.zdrav29.ru/'))
        self.web.load(QtCore.QUrl('https://2ip.ru/'))

        print(self.web.title())
        # print("Python says line ", cf.f_lineno)
        print(self.web.title())

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.web)
        self.setLayout(self.vbox)

        print(self.web.page().contentsSize().toSize())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    web = Web()
    web.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
    web.show()

    sys.exit(app.exec())
