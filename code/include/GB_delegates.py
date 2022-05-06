
import logging
import sys

import PySide2.QtCore as Core
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .GB_constants import *

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)

class GBCheckboxDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QCheckBox(parent)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().itemFromIndex(index).checkState()
        if value == 2:
            editor.setChecked(True)
        else:
            editor.setChecked(False)

    def updateEditorGeometry(self, editor, options, index):
        editor.setGeometry(options.rect)

    def setModelData(self, editor, model, index):
        value = Core.Qt.Checked if editor.isChecked() else Core.Qt.Unchecked
        model.itemFromIndex(index).setCheckState(value)


class GBSpinboxDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QSpinBox(parent)
        editor.setFrame(False)
        model: QStandardItemModel = index.model()
        column: int = model.itemFromIndex(index).column()
        row: int = model.itemFromIndex(index).row()
        if (column == 3):
            editor.setMinimum(1)
            editor.setMaximum(int(model.item(row, 4).text()))
        elif (column == 4):
            logging.debug(f" framecount {model.item(row, 1).data(Qt.UserRole).media_file_par.frame_count}")
            editor.setMinimum(int(model.item(row, 3).text()))
            editor.setMaximum(int(model.item(row, 1).data(Qt.UserRole).media_file_par.frame_count))
        elif (column == 5):
            editor.setMinimum(1)
            editor.setMaximum(1000)
        elif (column == 6):
            editor.setMinimum(5)
            editor.setMaximum(100)
            editor.setSingleStep(5)
        return editor

    def setEditorData(self, editor:QSpinBox, index):
        value = int(index.model().data(index, role = Qt.EditRole))
        editor.setValue(value)

    def updateEditorGeometry(self, editor, options, index):
        editor.setGeometry(options.rect)

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, Qt.EditRole)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Delegate Test")
    layout = QVBoxLayout(window)
    tv = QTableView()
    stim = QStandardItemModel()
    for i in range(10):
        list = []
        for j in range(8):
            list.append(QStandardItem(str(j)))
        stim.appendRow(list)


    tv.setModel(stim)#
    spinbox = GBSpinboxDelegate()
    for i in range(3, 7):
        tv.setItemDelegateForColumn(i,spinbox)
    layout.addWidget(tv)
    window.show()
    sys.exit(app.exec_())