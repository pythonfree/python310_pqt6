from PyQt6 import QtGui, QtWidgets, QtCore

import time


class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Закрыть окно")
        self.clicked.connect(QtWidgets.QApplication.instance().quit)

    def load_data(self, sp):
        for i in range(1, 11):
            time.sleep(2)
            sp.showMessage("Загрузка данных...{0}%".format(i * 10),
                           QtCore.Qt.AlignmentFlag.AlignHCenter |
                           QtCore.Qt.AlignmentFlag.AlignBottom,
                           QtCore.Qt.GlobalColor.black
                           )
            QtWidgets.QApplication.instance().processEvents()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("Water arch isolated.svg"))
    splash.showMessage("Загрузка данных.... 0%",
                       QtCore.Qt.AlignmentFlag.AlignHCenter |
                       QtCore.Qt.AlignmentFlag.AlignBottom,
                       QtGui.QColor("black")
                       )
    splash.show()
    QtWidgets.QApplication.instance().processEvents()
    window = MyWindow()
    window.setWindowTitle("Вывод заставки")
    window.resize(300, 30)
    window.load_data(splash)
    window.show()
    splash.finish(window)
    sys.exit(app.exec())
