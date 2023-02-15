import sys
import ui_MyForm

from PyQt6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = ui_MyForm.Ui_MyForm()
    ui.setupUi(window)
    ui.btnQuit.clicked.connect(QtWidgets.QApplication.instance().quit)
    window.show()
    sys.exit(app.exec())
