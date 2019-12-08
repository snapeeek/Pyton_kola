from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from module import Module
from module2 import KoloDialog

class Dialog(QMainWindow):
    fileName = ""

    def __init__(self):
        super(Dialog, self).__init__()
        self.dialog = Module(self)
        self.currentColor = 'green'
        self.color = QColor(0, 255, 0, 255)
        self.bigWidget = QWidget()
        self.color_menu = QAction("Kolor okna głównego", self)
        self.outside_circle =100
        self.inside_circle = 50
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialogi')
        self.setGeometry(400, 400, 800, 400)
        grid = QGridLayout()
        self.setWindowIcon(QIcon('happyface.jpg'))
        self.setCentralWidget(self.bigWidget)
        palette = QPalette()
        palette.setColor(QPalette.Window, self.color)
        self.setPalette(palette)
        self.dialog.hide()
        self.dialog.changed.connect(self.changed_color)

        self.color_menu.setCheckable(True)
        self.color_menu.triggered.connect(self.toggle_dialog)

        circle_set = QAction("Ustawienia koła", self)
        circle_set.triggered.connect(self.get_sth)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&Dialog')
        file_menu.addAction(self.color_menu)
        file_menu.addAction(circle_set)

        self.bigWidget.setLayout(grid)

        self.show()

    def get_sth(self):
        popout = KoloDialog()
        popout.setModal(True)
        popout.setGeometry(400,400,550,300)
        popout.setWindowTitle("Ustawianie Kola")
        popout.setup_values(self.outside_circle,self.inside_circle)
        result = popout.exec()
        ret = popout.get_result()
        self.outside_circle = int(ret[0])
        self.inside_circle = int(ret[1])

        qp = QPainter()
        qp.begin(self)
        self.draw_ellipses(qp)
        qp.end()

    def toggle_dialog(self):  # funkcja obsługi elementu menu /pokaż – schowaj dialog
        if self.color_menu.isChecked():
            self.dialog.show()
            self.dialog.color = self.currentColor
        else:
            self.dialog.hide()

    def changed_color(self, color):
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
        self.draw_ellipses(qp)
        qp.end()

    def draw_ellipses(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(112, 112, 112, 255))

        main_size = self.bigWidget.frameSize()
        point = QPoint(int(main_size.width() / 2),int(main_size.height() / 2))
        qp.drawEllipse(point, self.outside_circle, self.outside_circle)

        qp.setBrush(self.color)
        qp.drawEllipse(point, self.inside_circle, self.inside_circle)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    dial = Dialog()
    sys.exit(app.exec())