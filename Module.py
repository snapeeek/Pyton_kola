from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from Helper import StyledItemDelegate

class Module(QDialog):
    changed = pyqtSignal(str)

    @property
    def color(self):
        return str(self.combo.currentText())

    # właśwość text – wpisany tytuł
    @color.setter
    def color(self, newColor):
        self.combo.setCurrentText(newColor)

    def closeEvent(self, event):   #zablokowanie możliwości zamkniecia
        event.ignore()

    def help(self):
        self.changed.emit(self.combo.currentText())

    def __init__(self, parent=None, title=""):
        super(Module, self).__init__(parent)
        mainLayout = QVBoxLayout(self)
        kolory = ['red', 'yellow', 'green', 'blue']
        self.combo = QComboBox()
        self.combo.addItems(kolory)
        self.combo.setCurrentText('green')
        self.combo.setItemDelegate(StyledItemDelegate())
        self.combo.currentTextChanged.connect(self.help)
        # self.combo.setModel(model)

        mainLayout.addWidget(self.combo)
        self.setWindowTitle('Ustaw kolor okna głównego')
        self.resize(350, 100)
        self.show()