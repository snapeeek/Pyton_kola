from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from helper import StyledItemDelegate


class Module(QDialog):
    changed = pyqtSignal(str)

    @property
    def color(self):
        return str(self.combo.currentText())

    @color.setter
    def color(self, new_color):
        self.combo.setCurrentText(new_color)

    def closeEvent(self, event):
        event.ignore()

    def help(self):
        self.changed.emit(self.combo.currentText())

    def __init__(self, parent=None, title=""):
        super(Module, self).__init__(parent)
        main_layout = QVBoxLayout(self)
        colors = ['red', 'yellow', 'green', 'blue']
        self.combo = QComboBox()
        self.combo.addItems(colors)
        self.combo.setCurrentText('green')
        self.combo.setItemDelegate(StyledItemDelegate())
        self.combo.currentTextChanged.connect(self.help)

        main_layout.addWidget(self.combo)
        self.setWindowTitle('Ustaw kolor okna głównego')
        self.resize(350, 100)
        self.show()
