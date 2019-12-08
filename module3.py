from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class IconDialog(QDialog):

    def __init__(self, parent=None):
        super(IconDialog, self).__init__(parent)
        self.setGeometry(50,90,120,240)

        grid_layout = QGridLayout()
        self.beg_picture = ''

        #ikonka
        self.pictures = ['happyface.jpg', 'normal.png', 'sadface.jpg']
        self.picture = QLabel()
        self.picture.setFixedSize(90,90)
        self.picture.setPixmap(QPixmap(self.pictures[0]))
        self.actual_picture = self.pictures[0]

        button_widget = QWidget()
        button_layout = QVBoxLayout()
        self.ok = QPushButton()
        self.ok.setText("OK")
        self.ok.pressed.connect(self.close)
        self.cancel = QPushButton()
        self.cancel.setText("Cancel")
        self.cancel.pressed.connect(self.revert_changes)
        button_layout.addWidget(self.ok)
        button_layout.addWidget(self.cancel)
        button_layout.addStretch(1)
        button_widget.setLayout(button_layout)

        check_widget = QGroupBox()
        check_layout = QVBoxLayout()
        check_widget.setTitle("Wybierz ikone")
        self.happy_checkbox = QCheckBox()
        self.happy_checkbox.setText("happy")
        self.happy_checkbox.clicked.connect(self.ignore_check)
        self.normal_checkbox = QCheckBox()
        self.normal_checkbox.setText("normal")
        self.normal_checkbox.clicked.connect(self.ignore_check)
        self.sad_checkbox = QCheckBox()
        self.sad_checkbox.setText("sad")
        self.sad_checkbox.clicked.connect(self.ignore_check)
        check_layout.addWidget(self.happy_checkbox)
        check_layout.addWidget(self.normal_checkbox)
        check_layout.addWidget(self.sad_checkbox)
        check_widget.setLayout(check_layout)

        #wskaznik postepu
        progress_widget = QWidget()
        progress_layout = QVBoxLayout()
        self.progress = QProgressBar()
        self.progress.setOrientation(Qt.Vertical)
        self.progress.setValue(100)
        being_happy_label = QLabel()
        being_happy_label.setText("wskaznik\nzadowolenia")
        progress_layout.addWidget(self.progress)
        progress_layout.addWidget(being_happy_label)
        progress_widget.setLayout(progress_layout)

        # radiobuttony
        radio_widget = QGroupBox()
        radio_widget.setTitle("Wybierz ikone")
        radio_layout = QVBoxLayout()
        self.happy = QRadioButton()
        self.happy.setText("happy")
        self.happy.pressed.connect(self.set_happy)
        self.normal = QRadioButton()
        self.normal.setText("normal")
        self.normal.pressed.connect(self.set_normal)
        self.sad = QRadioButton()
        self.sad.setText("sad")
        self.sad.pressed.connect(self.set_sad)
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.happy)
        self.radio_group.addButton(self.normal)
        self.radio_group.addButton(self.sad)

        radio_layout.addWidget(self.happy)
        radio_layout.addWidget(self.normal)
        radio_layout.addWidget(self.sad)
        radio_widget.setLayout(radio_layout)

        grid_layout.addWidget(radio_widget, 0, 0)
        grid_layout.addWidget(self.picture, 0, 1)
        grid_layout.addWidget(button_widget, 0, 2)
        grid_layout.addWidget(check_widget, 1, 0)
        grid_layout.addWidget(progress_widget, 1, 1)
        self.setLayout(grid_layout)
        self.setModal(True)
        self.show()

    def revert_changes(self):
        self.actual_picture = self.beg_picture
        self.close()

    def set_icon(self, name):
        self.beg_picture = name
        if name == self.pictures[0]:
            self.actual_picture = name
            self.set_happy()
            self.happy.setChecked(True)
        elif name == self.pictures[1]:
            self.actual_picture = name
            self.set_normal()
            self.normal.setChecked(True)
        elif name == self.pictures[2]:
            self.actual_picture = name
            self.set_sad()
            self.sad.setChecked(True)
        else:
            print("error")

    def get_icon(self):
        return self.actual_picture

    def set_happy(self):
        self.clear()
        self.happy.setChecked(True)
        self.actual_picture = self.pictures[0]
        pix_map = QPixmap(self.actual_picture).scaled(90, 90, Qt.KeepAspectRatio)
        self.picture.setPixmap(pix_map)
        self.happy_checkbox.setChecked(True)
        self.progress.setValue(100)
    
    def set_normal(self):
        self.clear()
        self.normal.setChecked(True)
        self.actual_picture = self.pictures[1]
        pix_map = QPixmap(self.actual_picture).scaled(90, 90, Qt.KeepAspectRatio)
        self.picture.setPixmap(pix_map)
        self.normal_checkbox.setChecked(True)
        self.progress.setValue(50)

    def set_sad(self):
        self.clear()
        self.sad.setChecked(True)
        self.actual_picture = self.pictures[2]
        pix_map = QPixmap(self.actual_picture).scaled(90, 90, Qt.KeepAspectRatio)
        self.picture.setPixmap(pix_map)
        self.sad_checkbox.setChecked(True)
        self.progress.setValue(5)
    
    def clear(self):
        self.happy.setChecked(False)
        self.normal.setChecked(False)
        self.sad.setChecked(False)
        self.happy_checkbox.setChecked(False)
        self.normal_checkbox.setChecked(False)
        self.sad_checkbox.setChecked(False)
        self.progress.setValue(0)
    
    def ignore_check(self):
        self.happy_checkbox.setChecked(False)
        self.normal_checkbox.setChecked(False)
        self.sad_checkbox.setChecked(False)
        if self.actual_picture == self.pictures[0]:
            self.happy_checkbox.setChecked(True)
        elif self.actual_picture == self.pictures[1]:
            self.normal_checkbox.setChecked(True)
        else:
            self.sad_checkbox.setChecked(True)