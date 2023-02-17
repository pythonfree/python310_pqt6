# Прохоренок Н.А., Дронов В.А. - Python 3 и PyQt 6. Разработка приложений - 2023
from PyQt6 import QtWidgets, QtCore
import sys
import time
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна по центру экрана")
window.resize(300, 100)
window.move(window.width() * -2, 0)

window.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)

window.show()
# time.sleep(3)
screen_size = window.screen().availableSize()
x = (screen_size.width() - window.width()) // 2
y = (screen_size.height() - window.height()) // 2
window.move(x, y)

if window.windowState() and QtCore.Qt.WindowState.WindowFullScreen:
    print("Полноэкранный режим")

sys.exit(app.exec())
