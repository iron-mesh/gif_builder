import logging
import sys

from PySide2 import QtCore
from PySide2.QtGui import QFont
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
        self.button = QPushButton("...")
        self.button.clicked.connect(self._on_press_button)

        layout = QHBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

    def _on_press_button(self):
        buf_path = self.get_path()
        logging.debug("buf path: {0}".format(buf_path))
        if (self._mode == GBC.Modes.DIRPATH):
            path:str = QFileDialog.getExistingDirectory(None, GBC.LC_SELECT_DIR_TITLE, self.get_path(), QFileDialog.ShowDirsOnly)
        elif (self._mode == GBC.Modes.FILEPATH):
            path:str = QFileDialog.getOpenFileName(None, GBC.LC_SELECT_FILE_TITLE, self.get_path(), f"{GBC.LC_IMAGEFILE_FILTER_TITLE} {GBC.LC_IMAGEFILE_FILTER}") [0]
        elif (self._mode == GBC.Modes.EXEFILE):
            path:str = QFileDialog.getOpenFileName(None, GBC.LC_SELECT_EXEC_FILE_TITLE, self.get_path(), f"{GBC.LC_EXE_FILTER_TITLE} {GBC.LC_EXE_FILTER}")[0]
        elif (self._mode == GBC.Modes.SAVE_IMAGE):
            path:str = QFileDialog.getSaveFileName(None, GBC.LC_SAVE_ANIMATION_FILE_TITLE, self.get_path(), f"{GBC.LC_SAVE_ANIMATION_FILTER_TITLE} {GBC.LC_SAVE_ANIMATION_FILTER}")[0]
        elif (self._mode == GBC.Modes.SOUND):
            path: str = QFileDialog.getOpenFileName(None, GBC.LC_OPEN_SOUND_TITLE, self.get_path(), f"{GBC.LC_SOUND_FILTER_TITLE} {GBC.LC_SOUND_FILTER}")[0]

        if(path != buf_path and path):
            logging.debug("current path: {0}".format(path))
            self.set_path(path)
            self.path_changed.emit(path)

    def set_mode(self, mode:int) -> None:
        self._mode:int = mode

    def get_mode(self) -> int:
        return self._mode

    def get_path(self)->str:
        return self.line_edit.text()

    def set_path(self, path:str)->None:
        self.line_edit.setText(path)

    def set_placeholder_text(self, text:str)->None:
        self.line_edit.setPlaceholderText(text)


if __name__ == "__main__":
    print("QInputPath test")
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QInputPath test")
    layout = QVBoxLayout(window)
    layout.addWidget(QLabel("Select Dir"))
    ip1 = QInputPath(mode = GBC.Modes.DIRPATH)
    ip1.path_changed.connect(lambda s: logging.debug("path changed: {0}".format(s)))
    layout.addWidget(ip1)
    layout.addWidget(QLabel("Select Exe file"))
    layout.addWidget(QInputPath(mode = GBC.Modes.EXEFILE))
    layout.addWidget(QLabel("Select image file"))
    layout.addWidget(QInputPath(mode=GBC.Modes.FILEPATH))
    layout.addWidget(QLabel("Save image"))
    layout.addWidget(QInputPath(mode=GBC.Modes.SAVE_IMAGE))
    window.resize(500, 300)
    window.show()
    sys.exit(app.exec_())




