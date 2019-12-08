from PyQt5.QtCore import Qt, QRect, QPoint, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class KoloDialog(QDialog):
    zmiana = pyqtSignal(str)

    def __init__(self, parent=None):
        super(KoloDialog, self).__init__(parent)
        self.setGeometry(400, 300, 150, 150)
        self.outside_circle_beg = 0
        self.inside_circle_beg = 0
        # ten layout na cale okienko
        big_layout = QVBoxLayout()

        # widget na suwaki i podglad
        widget_grid = QWidget()
        grid_layout = QGridLayout()
        widget_grid.setLayout(grid_layout)
        widget_grid.setGeometry(150, 150, 150, 150)
        widget_grid.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        object_validate = QIntValidator(self)
        object_validate.setRange(0, 255)
        self.outside = QLabel()
        self.outside.setText("Na Zewnatrz")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(255)
        self.slider.setMinimum(0)
        self.slider.valueChanged.connect(self.slider1_change)
        self.line_edit = QLineEdit('0')
        self.line_edit.setValidator(object_validate)
        self.line_edit.textChanged.connect(self.line_edit1_change)

        self.inside = QLabel()
        self.inside.setText("Wewnatarz")
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMaximum(255)
        self.slider2.setMinimum(0)
        self.slider2.valueChanged.connect(self.slider2_change)
        self.line_edit2 = QLineEdit('0')
        self.line_edit2.setValidator(object_validate)
        self.line_edit2.textChanged.connect(self.line_edit2_change)

        # podglad
        self.color = QColor(240, 240, 240, 255)
        self.podglad = QLabel()
        self.podglad.setGeometry(400, 410, 412, 460)

        # dodawanie sliderow labeli pol edycyjnych i podgladu do grida
        grid_layout.addWidget(self.outside, 0, 0)
        grid_layout.addWidget(self.slider, 0, 1)
        grid_layout.addWidget(self.line_edit, 0, 2)
        grid_layout.addWidget(self.inside, 1, 0)
        grid_layout.addWidget(self.slider2, 1, 1)
        grid_layout.addWidget(self.line_edit2, 1, 2)
        grid_layout.addWidget(self.podglad, 0, 3)

        # przyciski do aktywacji
        button_widget = QWidget()
        button_layout = QHBoxLayout()
        self.ok = QPushButton()
        self.ok.setText("Ok")
        self.ok.pressed.connect(self.close)
        self.cancel = QPushButton()
        self.cancel.setText("Anuluj")
        self.cancel.pressed.connect(self.revert_changes)
        button_layout.addStretch(1)
        button_layout.addWidget(self.ok)
        button_layout.addWidget(self.cancel)
        button_widget.setLayout(button_layout)

        # dodawnie tych wudgetow z layoutami
        big_layout.addWidget(widget_grid)
        big_layout.addWidget(button_widget)
        self.setLayout(big_layout)
        self.setModal(True)
        self.show()

    def paintEvent(self, *args, **kwargs):
        qp = QPainter()
        qp.begin(self)
        self.draw_ellipses(qp)
        qp.end()
        
    def draw_ellipses(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(112, 112, 112, 255))

        main_size = self.podglad.rect()
        main_height = main_size.height()
        main_width = main_size.width()
        point = QPoint(int(main_width / 2) + 400, int(main_height / 2) + 70)

        qp.drawEllipse(point, int(self.slider.value() * 0.3), int(self.slider.value() * 0.3))
        qp.setBrush(self.color)
        qp.drawEllipse(point, int(self.slider2.value() * 0.3), int(self.slider2.value() * 0.3))

    def revert_changes(self):
        self.slider.setValue(self.outside_circle_beg)
        self.slider2.setValue(self.inside_circle_beg)
        self.close()

    def line_edit1_change(self, value):
        if not value:
            return
        self.slider.setValue(int(value))
        self.update()

    def slider1_change(self, value):
        self.line_edit.setText(str(value))
        self.update()

    def line_edit2_change(self, value):
        if not value:
            return
        self.slider2.setValue(int(value))

        self.update()
        
    def slider2_change(self, value):
        self.line_edit2.setText(str(value))

        self.update()
        
    def setup_values(self, outside_circle, inside_circle):
        if not outside_circle:
            return
        if not inside_circle:
            return
        self.outside_circle_beg = outside_circle
        self.inside_circle_beg = inside_circle
        self.slider.setValue(int(outside_circle))
        self.line_edit.setText(str(outside_circle))
        self.slider2.setValue(int(inside_circle))
        self.line_edit2.setText(str(inside_circle))
        qp = QPainter()
        qp.begin(self)
        self.draw_ellipses(qp)
        qp.end()

    def get_result(self):
        return [self.slider.value(), self.slider2.value()]