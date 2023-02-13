from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QBoxLayout
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("First app on PyQt")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Hello World!</center>")
btnQuit = QtWidgets.QPushButton("&Close window")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())
