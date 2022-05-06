from PySide2.QtWidgets import QTableView, QMenu,QAction
from PySide2.QtCore import Signal
from PySide2.QtGui import QCursor
import logging, importlib
import include.GB_constants as GBC

logging.basicConfig(level=logging.DEBUG)
if(GBC.LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)

class GB_TableView(QTableView):
    edit_task_clicked = Signal()
    duplicate_task_clicked = Signal()
    exportdir_clicked = Signal()
    sourcedir_clicked = Signal()
    delete_task_clicked = Signal()

    def contextMenuEvent(self, event) -> None:
        if self.selectedIndexes():
            self.contextMenu = QMenu(self)
            edit_action = QAction(GBC.LC_TWQM_EDIT, self)
            dupli_action = QAction(GBC.LC_TWQM_DUPLICATE, self)
            exportdir_action = QAction(GBC.LC_TWQM_EXPORTDIR, self)
            sourcedir_action = QAction(GBC.LC_TWQM_SOURCEDIR, self)
            delete_action = QAction(GBC.LC_TWQM_DELETE, self)

            self.contextMenu.addAction(edit_action)
            # self.contextMenu.addAction(dupli_action)
            self.contextMenu.addAction(sourcedir_action)
            self.contextMenu.addAction(exportdir_action)
            self.contextMenu.addAction(delete_action)

            edit_action.triggered.connect(lambda: self.edit_task_clicked.emit())
            dupli_action.triggered.connect(lambda: self.duplicate_task_clicked.emit())
            exportdir_action.triggered.connect(lambda: self.exportdir_clicked.emit())
            sourcedir_action.triggered.connect(lambda: self.sourcedir_clicked.emit())
            delete_action.triggered.connect(lambda: self.delete_task_clicked.emit())

            self.contextMenu.popup(QCursor.pos())

            return True

    def retranslateUi(self):
        importlib.reload(GBC)