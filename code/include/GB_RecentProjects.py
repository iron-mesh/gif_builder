import os.path

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from os.path import *
from .GB_types import *
from .GB_constants import *
from math import *
import logging

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)

max_length = 13
save_file_path = r"./resources/recent_projects.txt"

class RecentProjects:
    """Class for saving recent projects"""
    def __init__(self, parent:QMainWindow, load_list = False):
        super().__init__()
        self._parent = parent
        self._callback = None
        self._file_list:list[str] = []
        if load_list: self.load_list_from_hdd()
        if not os.path.exists(save_file_path):
            file = open(save_file_path, encoding="utf-8", mode="w")
            file.close()
        else:
            self.load_list_from_hdd()

    def link_callback(self, callback_func):
        self._callback = callback_func

    def load_list_from_hdd(self):
        logging.debug("Recent file reading")
        with open(save_file_path, encoding="utf-8", mode="r") as s_file:
            data = s_file.read()
            if data:
                self._file_list = data.split(";")

    def save_list_to_hdd(self):
        rewrite_file = False
        prev_list = []
        with open(save_file_path, encoding="utf-8", mode="r") as s_file:
            data = s_file.read()
            if data:
                prev_list = data.split(";")

        rewrite_file = self._file_list != prev_list

        if rewrite_file and self._file_list:
            with open(save_file_path, encoding="utf-8", mode="w") as s_file:
                logging.debug("Recent file writing")
                s_file.write(";".join(self._file_list))

    def show_popup(self):
        """Show popup menu with recent files"""
        def get_handler(path):
            return lambda :self._callback(path)

        list = self._file_list
        logging.debug(list)

        if list:
            recents_context_menu = QMenu(self._parent)
            recents_context_menu.setStyleSheet("font-size:16px")
            for i, e in enumerate(reversed(list)):
                is_found:bool = os.path.exists(e)
                title:str = f"{i + 1}. {os.path.basename(e)} {''if is_found else ('(' + LC_MSG_NOTFOUND + ')')}"
                action = QAction(title, self._parent)
                action.triggered.connect(get_handler(e))
                action.setStatusTip(e)
                action.setEnabled(is_found)
                recents_context_menu.addAction(action)

                #recents_context_menu.addAction(title).triggered.connect(get_handler(e))
            recents_context_menu.popup(QCursor.pos())


    def add_path(self, path):
        list = self._file_list
        if path in list:
            index = list.index(path)
            list.pop(index)
        else:
            if len(list) >= max_length:
                list.pop(0)
        list.append(path)



