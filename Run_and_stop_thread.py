from PyQt6 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.my_signal.emit("count = %s" % self.count)
            self.sleep(1)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Press key for running thread")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.btnStart = QtWidgets.QPushButton("Start thread")
        self.btnStop = QtWidgets.QPushButton("Stop thread")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.setLayout(self.vbox)
        self.my_thread = MyThread()
        self.btnStart.clicked.connect(self.on_start)
        self.btnStop.clicked.connect(self.on_stop)
        self.my_thread.my_signal.connect(self.on_change,
                                         QtCore.Qt.ConnectionType.QueuedConnection)

    def on_start(self):
        if not self.my_thread.isRunning():
            self.my_thread.start()

    def on_stop(self):
        self.my_thread.running = False

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        self.hide()
        self.my_thread.running = False
        self.my_thread.wait(5000)
        event.accept()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Start and stop thread")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec())
