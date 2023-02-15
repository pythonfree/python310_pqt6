from PyQt6 import QtCore, QtWidgets

class MyThread(QtCore.QThread):
    x = 10
    mutex = QtCore.QMutex()
    def __init__(self, id, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id
    def run(self):
        self.change_x()
    def change_x(self):
        MyThread.mutex.lock()
        print("x = ", MyThread.x, " id = ", self.id)
        MyThread.x += 5
        self.sleep(3)
        print("x = ", MyThread.x, " id = ", self.id)
        MyThread.x += 34
        print("x = ", MyThread.x, " id = ", self.id)
        MyThread.mutex.unlock()
