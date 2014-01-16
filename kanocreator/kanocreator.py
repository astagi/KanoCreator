import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import qmlRegisterType
from PyQt5.QtQuick import QQuickView
from command import Command

def main():
    app = QApplication(sys.argv)

    qmlRegisterType(Command, 'Command', 1, 0, 'Command')

    view = QQuickView()
    view.setSource(QUrl("qml/main.qml"))
    view.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
