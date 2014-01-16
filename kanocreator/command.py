from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import *
from PyQt5.QtQuick import QQuickView

class Command(QObject):

    outputReady = pyqtSignal(str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._command = ''
        self._process = None

    @pyqtProperty('QString')
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command

    @pyqtSlot(result=str)
    def execute(self):
        self._process = QProcess(self)
        self._process.start(self._command)
        self._process.waitForReadyRead(-1)
        output = self._process.readAllStandardOutput()
        return str(output)

    @pyqtSlot()
    def executeAsync(self):
        self._process = QProcess(self)
        self._process.finished.connect(self.readStdOutput)
        self._process.start(self._command)

    @pyqtSlot()
    def readStdOutput(self):
        output = self._process.readAllStandardOutput()
        self.outputReady.emit(str(output))
