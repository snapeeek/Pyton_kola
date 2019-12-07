from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from module import Module


class Dialog(QMainWindow):
    fileName = ""

    def __init__(self):
        super(Dialog, self).__init__()
        self.big_widget = QWidget()
        self.color = QColor(0, 255, 0, 255)
        self.current_color = 'green'
        self.dialog = Module(self)
        self.color_menu = QAction("Kolor okna głównego", self)
        self.color_menu.setCheckable(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dialogi')
        self.setGeometry(400, 400, 800, 400)
        grid = QGridLayout()
        
        self.setWindowIcon(QIcon('happyface.jpg'))
        self.setCentralWidget(self.big_widget)
        
        palette = QPalette()
        palette.setColor(QPalette.Window, self.color)
       
        self.setPalette(palette)
        
        self.dialog.hide()
        self.dialog.changed.connect(self.changed_color)

        self.color_menu.triggered.connect(self.toggle_title_dialog)

        circle_set = QAction("Ustawienia koła", self)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&Dialog')
        file_menu.addAction(self.color_menu)
        file_menu.addAction(circle_set)

        self.big_widget.setLayout(grid)

        self.show()

    def toggle_title_dialog(self):  # funkcja obsługi elementu menu /pokaż – schowaj dialog
        if self.color_menu.isChecked():
            self.dialog.show()
            self.dialog.color = self.current_color
        else:            
            self.dialog.hide()

    def changed_color(self, color):
        if color == 'green':
            self.color = QColor(0, 255, 0, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.current_color = 'green'
            self.setPalette(palette)
        elif color == 'red':
            self.color = QColor(255, 0, 0, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.current_color = 'red'
            self.setPalette(palette)
        elif color == 'blue':
            self.color = QColor(0, 0, 255, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.current_color = 'blue'
            self.setPalette(palette)
        else:
            self.color = QColor(255, 255, 0, 255)
            palette = QPalette()
            palette.setColor(QPalette.Window, self.color)
            self.current_color = 'green'
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

        main_size = self.big_widget.frameSize()
        main_height = main_size.height()
        main_width = main_size.width()
        point = QPoint(main_width / 2, main_height / 2)
        qp.drawEllipse(point, 100, 100)

        qp.setBrush(self.color)
        qp.drawEllipse(point, 50, 50)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    dial = Dialog()
    sys.exit(app.exec())