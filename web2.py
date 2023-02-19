from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys

url = 'https://2ip.ru/'

app = QApplication(sys.argv)

browser = QWebEngineView()
# browser.settings()
browser.load(QUrl(url))
browser.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
browser.show()

sys.exit(app.exec())
