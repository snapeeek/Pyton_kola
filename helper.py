from PyQt5 import QtCore, QtGui, QtWidgets


class StyledItemDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        QtWidgets.QStyledItemDelegate.__init__(self, parent=parent)

    def paint(self, painter, option, index):
        if index.row() == 0:
            painter.save()
            painter.fillRect(option.rect, QtGui.QBrush(QtCore.Qt.red))
            painter.restore()
        elif index.row() == 1:
            painter.save()
            painter.fillRect(option.rect, QtGui.QBrush(QtCore.Qt.yellow))
            painter.restore()
        elif index.row() == 2:
            painter.save()
            painter.fillRect(option.rect, QtGui.QBrush(QtCore.Qt.green))
            painter.restore()
        else:
            painter.save()
            painter.fillRect(option.rect, QtGui.QBrush(QtCore.Qt.blue))
            painter.restore()
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)