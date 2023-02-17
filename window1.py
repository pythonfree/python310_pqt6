from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Заголовок окна")
window.resize(300, 50)
window.show()
print(window.width(), window.height())
print(window.frameSize().width(), window.frameSize().height())
print(window.screen().size().height(), window.screen().size().width())
print(window.screen().availableSize().height(), window.screen().availableSize().width())
sys.exit(app.exec())
