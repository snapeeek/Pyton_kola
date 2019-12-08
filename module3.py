from PyQt5.QtCore import Qt, QRect, QPoint, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FaceDialog(QDialog):

    def __init__(self, parent=None):
        super(FaceDialog, self).__init__(parent)
        self.setGeometry(400, 300, 150, 150)
        self.setWindowTitle("Zmiana ikony")
        self.radio_buttons = QButtonGroup()
        self.progress = QProgressBar()
        self.progress.setOrientation(Qt.Vertical)
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        self.progress.setValue(50)
        # ten layout na cale okienko
        big_layout = QVBoxLayout()

        # widget na suwaki i podglad
        widget_grid = QWidget()
        grid_layout = QGridLayout()
        widget_grid.setLayout(grid_layout)
        widget_grid.setGeometry(150, 150, 150, 150)
        widget_grid.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        radio_button1 = QRadioButton("wesola")
        radio_button1.setChecked(True)
        radio_button2 = QRadioButton("normalna")
        radio_button3 = QRadioButton("smutna")
        self.radio_buttons.addButton(radio_button1, 1)
        self.radio_buttons.addButton(radio_button2, 2)
        self.radio_buttons.addButton(radio_button3, 3)

        button_widget1 = QGroupBox("Wybierz ikone")
        button_widget1_layout = QVBoxLayout()
        button_widget1_layout.addWidget(radio_button1)
        button_widget1_layout.addWidget(radio_button2)
        button_widget1_layout.addWidget(radio_button3)
        button_widget1.setLayout(button_widget1_layout)

        check_boxes = QButtonGroup()
        check_box1 = QCheckBox("wesola")
        check_box1.setChecked(True)
        check_box2 = QCheckBox("normalna")
        check_box2.setCheckable(False)
        check_box3 = QCheckBox("smutna")
        check_box3.setCheckable(False)
        check_boxes.addButton(check_box1)
        check_boxes.addButton(check_box2)
        check_boxes.addButton(check_box3)
        check_boxes.buttonToggled.connect(self.do_nothing)

        button_widget2 = QGroupBox("Wybierz ikone")
        button_widget2_layout = QVBoxLayout()
        button_widget2_layout.addWidget(check_box1)
        button_widget2_layout.addWidget(check_box2)
        button_widget2_layout.addWidget(check_box3)
        button_widget2.setLayout(button_widget2_layout)

        progress_label = QLabel("Poziom\nzadowolenia")
        help_widget = QWidget()
        help_widget_layout = QVBoxLayout()
        help_widget_layout.addWidget(self.progress)
        help_widget.setLayout(help_widget_layout)
        help_widget_layout.addWidget(progress_label)
        grid_layout.addWidget(button_widget1, 0, 0)
        grid_layout.addWidget(button_widget2, 1, 0)
        grid_layout.addWidget(help_widget, 1, 1)




        # dodawnie tych wudgetow z layoutami
        big_layout.addWidget(widget_grid)
        self.setLayout(big_layout)
        self.setModal(True)
        self.show()

    def do_nothing(self):
        print("Dupal")