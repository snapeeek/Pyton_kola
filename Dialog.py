from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Module import Module


class Dialog(QMainWindow):
    fileName = ""


    def __init__(self):
        super(Dialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialogi')
        self.setGeometry(400, 400, 800, 400)
        grid = QGridLayout()
        self.bigWidget = QWidget()
        self.setWindowIcon(QIcon('happyface.jpg'))
        self.setCentralWidget(self.bigWidget)
        self.color = QColor(0, 255, 0, 255)
        palette = QPalette()
        palette.setColor(QPalette.Window, self.color)
        self.currentColor = 'green'
        self.setPalette(palette)
        self.dialog = Module(self)
        self.dialog.hide()
        self.dialog.changed.connect(self.changedColor)
        

        #self.Dialog.changed.connect(self.changeTitle)

        self.colourMenu = QAction("Kolor okna głównego", self)
        self.colourMenu.setCheckable(True)
        self.colourMenu.triggered.connect(self.toggleTitleDialog)

        circleSet = QAction("Ustawienia koła", self)
        # circleSet.triggered.connect(self.openFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Dialog')
        fileMenu.addAction(self.colourMenu)
        fileMenu.addAction(circleSet)

        self.bigWidget.setLayout(grid)

        self.show()

    def toggleTitleDialog(self):  # funkcja obsługi elementu menu /pokaż – schowaj dialog
        if self.colourMenu.isChecked():
            self.dialog.show()
            self.dialog.color = self.currentColor
        else:            
            self.dialog.hide()

    def changedColor(self, color):
        if color == 'green':
            self.color = QColor(0, 255, 0, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.currentColor = 'green'
            self.setPalette(palette)
        elif color == 'red':
            self.color = QColor(255, 0, 0, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.currentColor = 'red'
            self.setPalette(palette)
        elif color == 'blue':
            self.color = QColor(0, 0, 255, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.currentColor = 'blue'
            self.setPalette(palette)
        else:
            self.color = QColor(255, 255, 0, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.currentColor = 'green'
            self.setPalette(palette)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawEllipses(qp)
        qp.end()

    def drawEllipses(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(112, 112, 112, 255))

        mainSize = self.bigWidget.frameSize()
        mainHeight = mainSize.height()
        mainWidth = mainSize.width()
        point = QPoint(mainWidth / 2, mainHeight / 2)
        qp.drawEllipse(point, 100, 100)

        qp.setBrush(self.color)
        qp.drawEllipse(point, 50, 50)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    dial = Dialog()
    sys.exit(app.exec())