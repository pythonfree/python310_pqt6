from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle("First app on PyQt")
window.resize(300, 70)

vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel("<center>Hello World</center>")
vbox.addWidget(label)
btnQuit = QtWidgets.QPushButton("Close window")
vbox.addWidget(btnQuit)

window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())
