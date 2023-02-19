import sys

from PyQt6 import QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    profile = QWebEngineProfile().defaultProfile()
    profile.setHttpUserAgent(
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    )
    web = QWebEngineView()
    page = QWebEnginePage(profile, web)

    web.setPage(page)
    web.load(QUrl("https://esia.gosuslugi.ru/login/"))
    # web.load(QUrl("https://www.zdrav29.ru/"))
    web.show()
    web.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
    sys.exit(app.exec())
