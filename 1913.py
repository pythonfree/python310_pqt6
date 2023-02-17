# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(
    "QGroupBox QLabel {color: blue;} QPushButton {font-style: italic}"
)
window = QtWidgets.QWidget()
window.setWindowTitle("Таблицы стилей")
window.setStyleSheet("QLabel#first {color: green;} QLabel:hover {color: red;}")
window.resize(200, 150)
lbl1 = QtWidgets.QLabel("Зеленый текст")
lbl1.setObjectName("first")
lbl2 = QtWidgets.QLabel("Полужирный текст")
lbl2.setStyleSheet("font-weight: bold")
lbl3 = QtWidgets.QLabel("Синий текст")
btn = QtWidgets.QPushButton("Курсивный текст")
box = QtWidgets.QGroupBox("Группа")
bbox = QtWidgets.QVBoxLayout()
bbox.addWidget(lbl3)
box.setLayout(bbox)
main_box = QtWidgets.QVBoxLayout()
main_box.addWidget(lbl1)
main_box.addWidget(lbl2)
main_box.addWidget(box)
main_box.addWidget(btn)
window.setLayout(main_box)
window.show()
sys.exit(app.exec())
