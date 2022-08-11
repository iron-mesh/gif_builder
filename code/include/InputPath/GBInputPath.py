import logging
import sys, os

from PySide2 import QtCore
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QFileDialog, QApplication, QVBoxLayout, QLabel

from .. import GB_constants as GBC

logging.basicConfig(level=logging.DEBUG)
if(GBC.LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)

class QInputPath(QWidget):
    """ Class provides element of UI to input path to file or directory"""
    path_changed = QtCore.Signal(str)

    def __init__(self, path = "", mode:int = GBC.Modes.DIRPATH):
        super().__init__()
        self._mode = mode
        self.line_edit = QLineEdit(path)
        self.line_edit.setFont(QFont('Arial', 11))
        self.button = QPushButton()
        self.button_del = QPushButton()
        icon = QIcon()
        icon.addFile(os.path.join(".", r"resources/icons/open_folder.png"), QtCore.QSize(), QIcon.Normal, QIcon.Off)
        icon_del = QIcon()
        icon_del.addFile(os.path.join(".", r"resources/icons/delete.png"), QtCore.QSize(), QIcon.Normal, QIcon.Off)
        self.button.setIcon(icon)
        self.button_del.setIcon(icon_del)
        self.button.clicked.connect(self._on_selectpath_button)
        self.button_del.clicked.connect(self._on_delete_button)

        layout = QHBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.button_del)

    def _on_selectpath_button(self):
        buf_path = self.get_path()
        logging.debug("buf path: {0}".format(buf_path))
        if (self._mode == GBC.Modes.DIRPATH):
            path:str = QFileDialog.getExistingDirectory(None, GBC.LC_SELECT_DIR_TITLE, self.get_path(), QFileDialog.ShowDirsOnly)
        elif (self._mode == GBC.Modes.FILEPATH):
            path:str = QFileDialog.getOpenFileName(None, GBC.LC_SELECT_FILE_TITLE, self.get_path(), f"{GBC.LC_IMAGEFILE_FILTER_TITLE} {GBC.LC_IMAGEFILE_FILTER}") [0]
        elif (self._mode == GBC.Modes.EXEFILE):
            if (sys.platform == "win32"):
                path:str = QFileDialog.getOpenFileName(None, GBC.LC_SELECT_EXEC_FILE_TITLE, self.get_path(), f"{GBC.LC_EXE_FILTER_TITLE} {GBC.LC_EXE_FILTER}")[0]
            else:
                path: str = QFileDialog.getOpenFileName(None, GBC.LC_SELECT_EXEC_FILE_TITLE, self.get_path() )[0]
        elif (self._mode == GBC.Modes.SAVE_IMAGE):
            path:str = QFileDialog.getSaveFileName(None, GBC.LC_SAVE_ANIMATION_FILE_TITLE, self.get_path(), f"{GBC.LC_SAVE_ANIMATION_FILTER_TITLE} {GBC.LC_SAVE_ANIMATION_FILTER}")[0]
        elif (self._mode == GBC.Modes.SOUND):
            path: str = QFileDialog.getOpenFileName(None, GBC.LC_OPEN_SOUND_TITLE, self.get_path(), f"{GBC.LC_SOUND_FILTER_TITLE} {GBC.LC_SOUND_FILTER}")[0]

        if(path != buf_path and path):
            logging.debug(f"current path: {path}")
            self.set_path(path)
            self.path_changed.emit(path)

    def _on_delete_button(self):
        self.line_edit.clear()

    def set_mode(self, mode:int) -> None:
        self._mode:int = mode
        if mode == GBC.Modes.SAVE_IMAGE:
            self.button_del.setVisible(False)
        else:
            self.button_del.setVisible(True)

    def get_mode(self) -> int:
        return self._mode

    def get_path(self)->str:
        return self.line_edit.text()

    def set_path(self, path:str)->None:
        self.line_edit.setText(path)

    def set_placeholder_text(self, text:str)->None:
        self.line_edit.setPlaceholderText(text)







