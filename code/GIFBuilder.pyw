# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import pickle, os, copy, winsound, importlib
import re
import sys
from include.ImportedMediaContainer import ImportedMediaContainer

import include.GB_constants as GBC

from PySide2.QtCore import *
from PySide2 import QtWidgets

import include.GBDialogEditTask as GBDET
from include.GB_delegates import *
from include.GB_types import *
from include.GBTaskHandler import *
from include.GB_RecentProjects import *
from include.GB_functions import *
from include.GUI.ui_main_window import Ui_MainWindow
from dataclasses import replace

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)


class GIFBuilder (QMainWindow):
    def __init__(self):
        logging.debug("GIFBuilder init")
        super(GIFBuilder, self).__init__()
        self._working_state = WorkingState.EDITING
        self._is_project_changed = False #flag of model changing status
        self._recent_proj = RecentProjects(self, False)
        self._recent_proj.link_callback(self._on_open_project)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # gui elements initialization
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.status_stack.setCurrentIndex(1)
        self.ui.inputpath_ffmpeg.set_mode(Modes.EXEFILE)
        self.ui.inputpath_ffprobe.set_mode(Modes.EXEFILE)
        self.ui.inputpath_export_dir.set_mode(Modes.DIRPATH)
        self.ui.inputpath_sound.set_mode(Modes.SOUND)
        self.ui.win_notification_checkBox.setVisible(False)
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        # buttons initialization
        self.ui.close_settings_button.setVisible(False)
        self.ui.settings_button.clicked.connect(lambda: self.on_show_settings(True))
        self.ui.close_settings_button.clicked.connect(lambda: self.on_show_settings(False))
        self.ui.close_settings_button.clicked.connect(self.save_settings)
        self.ui.add_item_button.clicked.connect(self._on_add_item)
        self.ui.edit_item_button.clicked.connect(self._on_edit_item)
        self.ui.delete_item_button.clicked.connect(self._on_delete_item)
        self.ui.deleteall_item_button.clicked.connect(self._on_delete_all)
        self.ui.new_button.clicked.connect(self._on_new_project)
        self.ui.open_button.clicked.connect(self._on_open_project)
        self.ui.open_resent_button.clicked.connect(self._on_openrecent_project)
        self.ui.save_button.clicked.connect(self._on_save_project)
        self.ui.saveAs_button.clicked.connect(lambda :self._on_save_project(save_as=True))
        self.ui.support_button.clicked.connect(self._on_supp_proj)
        self.ui.author_btn.clicked.connect(self._on_author_btn)
        self.ui.moveup_button.clicked.connect(lambda :self._on_move_row(direction='U'))
        self.ui.movedown_button.clicked.connect(lambda :self._on_move_row(direction='D'))
        self.ui.start_button.clicked.connect(self._on_start_button)
        self.ui.manual_button.clicked.connect(self._on_open_manual)
        self.ui.dwnld_build_button.clicked.connect(self._on_download_btn)
        self.ui.find_ffmpeg_exe_button.clicked.connect(self.on_find_ffmpeg_files)
        self.ui.feedback_button.clicked.connect(self._on_feedback_btn)
        # other initialization
        self.load_settings()
        self._projfile_path:str = ""
        self.ui.soound_alert_checkBox.stateChanged.connect(self._on_soundalert_changed)
        icon = QIcon()
        icon.addFile("./resources/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        if(sys.platform != "win32"):
            self.ui.dwnld_build_button.setVisible(False)
        # data model and Tableview presentation initialization
        self.ui.tableView.edit_task_clicked.connect(self._on_edit_item)
        self.ui.tableView.duplicate_task_clicked.connect(self._on_dupli_task)
        self.ui.tableView.delete_task_clicked.connect(self._on_delete_item)
        self.ui.tableView.exportdir_clicked.connect(self._on_export_dir)
        self.ui.tableView.sourcedir_clicked.connect(self._on_source_dir)
        self.ui.tableView.change_activity_all_clicked.connect(self.set_activity_status_all_tasks)
        self._task_list_model:QStandardItemModel = QStandardItemModel()
        self.ui.tableView.setModel(self._task_list_model)
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tableView.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.retranslateUi()
        header = self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.tableView.setHorizontalHeader(header)
        header = self.ui.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.tableView.setHorizontalHeader(header)
        self.ui.tableView.setShowGrid(True)
        spinbox_delegate = GBSpinboxDelegate(self)
        checkbox_delegate = GBCheckboxDelegate(self)
        self.ui.tableView.setItemDelegateForColumn(0, checkbox_delegate)
        self.ui.tableView.setItemDelegateForColumn(3, spinbox_delegate)
        self.ui.tableView.setItemDelegateForColumn(4, spinbox_delegate)
        self.ui.tableView.setItemDelegateForColumn(5, spinbox_delegate)
        self.ui.tableView.setItemDelegateForColumn(6, spinbox_delegate)
        self.ui.tableView.setItemDelegateForColumn(7, checkbox_delegate)
        self.setAcceptDrops(1)


        # handlers binding
        self._task_list_model.itemChanged.connect(self._on_item_changed)
        self.ui.cb_language.currentIndexChanged.connect(self._lang_changed)


        # task handler declaration
        self._task_handler = TaskHandler(self)
        self._task_handler.task_changed.connect(self._on_taskhandler_response, Qt.QueuedConnection)
        self._task_handler.finished.connect(self._has_taskhandler_finished)
        #sound
        # self._sound_effect = QtMultimedia.QSoundEffect(self, QtMultimedia.QAudioDeviceInfo.defaultOutputDevice())
        # self._sound_effect.setVolume(1)
        # translator
        self._translator = QTranslator()
        self._translatorQt = QTranslator()
        self._lang_changed(self.settings.language_index)

    @Slot()
    def _lang_changed(self,index:int):
        if index == 1:
            self._translator.load("./resources/cgifbuilder_en-ru.qm")
            self._translatorQt.load("./resources/qtbase_ru.qm")
            app.installTranslator(self._translator)
            app.installTranslator(self._translatorQt)
        elif index == 0:
            app.removeTranslator(self._translator)
            app.removeTranslator(self._translatorQt)
        self.ui.retranslateUi(self)
        self.retranslateUi()

    @Slot()
    def _on_open_manual(self):
        file_list:list = os.listdir("./resources")
        cur_lang:str = self.ui.cb_language.currentText()
        manual_url:str = ""
        regex = re.compile(r".*" + cur_lang + r"\.pdf", re.IGNORECASE)
        for f in file_list:
            if regex.search(f):
                manual_url = os.path.abspath(r"./resources") + f"/{f}"
                os.startfile(manual_url)
                return


    @check_workingstate
    def on_show_settings(self, status:bool)->None:
        if status:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.close_settings_button.setVisible(True)
            self.ui.settings_button.setVisible(False)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.close_settings_button.setVisible(False)
            self.ui.settings_button.setVisible(True)

    def load_settings(self)->None:
        self.settings:SettingsData = SettingsData()
        try:
            with open(r"settings.cfg", "rb") as s_file:
                self.settings = s = pickle.load(s_file)
                self.ui.cb_language.setCurrentIndex(s.language_index)
                self.ui.inputpath_ffmpeg.set_path(s.ffmpeg_path)
                self.ui.inputpath_ffprobe.set_path(s.ffprobe_path)
                self.ui.inputpath_export_dir.set_path(s.exp_dir)
                self.ui.inputpath_sound.set_path(s.sound_path)
                self.ui.sb_default_framerate.setValue(s.def_framerate)
        except FileNotFoundError:
            self.save_settings()

    @Slot()
    def save_settings(self)->None:
        logging.debug("save settings")
        buf_setting = SettingsData()
        buf_setting.language_index = self.ui.cb_language.currentIndex()
        buf_setting.ffmpeg_path = self.ui.inputpath_ffmpeg.get_path()
        buf_setting.ffprobe_path = self.ui.inputpath_ffprobe.get_path()
        buf_setting.exp_dir = self.ui.inputpath_export_dir.get_path()
        buf_setting.sound_path = self.ui.inputpath_sound.get_path()
        buf_setting.def_framerate = self.ui.sb_default_framerate.value()

        if(pickle.dumps(buf_setting)!=pickle.dumps(self.settings)):
            logging.debug("Setting rewriting")
            self.settings = buf_setting
            with open(r"settings.cfg", "wb") as s_file:
                pickle.dump(buf_setting, s_file)
        self.settings = buf_setting

    @check_workingstate
    @check_ffprobe
    @Slot()
    def _on_add_item(self)->None:
        def add_row():
            self._task_list_model.appendRow(dialog.get_data())
            self._task_list_model.itemChanged.emit(QStandardItem())

        dialog = GBDET.GBDialogEditTask(self, self.settings)
        dialog.setWindowTitle(GBC.LC_ADDNEWTASK)
        dialog._ui.sb_framerate.setValue(self.settings.def_framerate)
        dialog._ui.btn_add.clicked.connect(add_row)
        dialog._ui.buttonBox.hide()
        if(self.settings.exp_dir):
            dialog._ui.ip_export_file.set_path(os.path.join(self.settings.exp_dir,"untitled.gif"))
        res = dialog.exec_()
        if(res == QDialog.Accepted):
            add_row()

    @check_workingstate
    @check_ffprobe
    @Slot()
    def _on_edit_item(self)->None:
        i_list = self.ui.tableView.selectedIndexes()
        if(not i_list): return
        dialog = GBDET.GBDialogEditTask(self, self.settings)
        dialog.setWindowTitle(GBC.LC_EDITTASK)
        dialog._ui.btn_add.hide()
        dialog._ui.btn_cancel.hide()
        dialog._ui.btn_addclose.hide()
        dialog.import_data(i_list)
        res = dialog.exec_()
        if (res == QDialog.Accepted):
            dialog.update_data(i_list)

    @check_workingstate
    @Slot()
    def _on_delete_item(self) -> None:
        i_list = self.ui.tableView.selectedIndexes()
        if (i_list):
            self._task_list_model.removeRow(i_list[0].row())
            self._task_list_model.itemChanged.emit(QStandardItem())

    @check_workingstate
    @Slot()
    def _on_delete_all(self) -> None:
        if (self._task_list_model.rowCount() == 0): return
        dialog = QMessageBox(QMessageBox.Question,
                                       GBC.LC_CONFIRMATION, GBC.LC_MSG_DELETEALL,
                                       buttons=QMessageBox.Ok |
                                               QMessageBox.Cancel, parent=self)
        result = dialog.exec_()
        if(result == QMessageBox.Ok):
            self._clear_model()
            self._task_list_model.itemChanged.emit(QStandardItem())

    @Slot(QStandardItem)
    def _on_item_changed(self, item:QStandardItem) -> None:
        self.ui.totally_tasks_lcd.display(self._task_list_model.rowCount())
        if(item.column() == 0 or item.column() == -1):
            count: int = 0
            for i in range(self._task_list_model.rowCount()):
                state = self._task_list_model.item(i, 0).checkState()
                if (state == Qt.Checked): count += 1
            self.ui.active_tasks_lcd.display(count)
        if not self._is_project_changed: self._is_project_changed = True


    @check_workingstate
    @Slot()
    def _on_new_project(self) -> None:
        logging.debug("_on_new_project")
        if (self._task_list_model.rowCount() == 0 and not self._projfile_path):
            QMessageBox.warning(self, GBC.LC_WARNING, GBC.LC_MSG_CLEARALREADY)
            return

        result = QMessageBox.question(self, GBC.LC_CONFIRMATION, GBC.LC_MSG_NEWPROJECT, QMessageBox.Ok, QMessageBox.Cancel)
        if(result == QMessageBox.Ok):
            self._projfile_path = ""
            self._clear_model()
            self._task_list_model.itemChanged.emit(QStandardItem())
            self._update_window_title()
            self._is_project_changed = False

    @check_workingstate
    @Slot()
    def _on_open_project(self, fpath:str = "") -> None:
        if not fpath:
            path:str = QFileDialog.getOpenFileName(None, GBC.LC_OPEN_PROJECT_FILE_TITLE, self._projfile_path, f"{GBC.LC_PROJECTFILE_FILTER_TITLE} {GBC.LC_PROJECTFILE_FILTER}")[0]
            if(not path): return
        else:
            if not os.path.exists(fpath):
                QMessageBox.warning(self, GBC.LC_ERROR, f"{GBC.LC_MSG_FILEISNTFOUND}:\n {fpath}")
                return
            path:str = fpath


        self._projfile_path = path
        self._clear_model()
        file = QFile(self._projfile_path)
        file.open(QIODevice.ReadOnly)
        input = QDataStream(file)
        version_of_saver = input.readString()
        logging.debug(f"version_of_saver: <b>{version_of_saver}</b>")
        if(version_of_saver not in COMPATIBLE_VERSION_LIST):
            QMessageBox.warning(self, GBC.LC_ERROR, f"{GBC.LC_MSG_NOTCOMPITABLE} {version_of_saver}")
            return

        item_list = []
        while(not input.atEnd()):
            for c in range(8):
                item = QStandardItem()
                item.read(input)
                if c == 1:
                    imc:ImportedMediaContainer = item.data(role=Qt.UserRole)
                    imd:ImportedMediaData = ImportedMediaData()
                    imd = imc.export_imported_media_data()
                    item.setData(imd, role=Qt.UserRole)
                item_list.append(item)
            self._task_list_model.appendRow(item_list)
            item_list.clear()
        file.close()
        self._task_list_model.itemChanged.emit(QStandardItem())
        self._update_window_title()
        self._is_project_changed = False
        self._recent_proj.add_path(self._projfile_path)

    @check_workingstate
    @Slot()
    def _on_openrecent_project(self) -> None:
        self._recent_proj.show_popup()

    @check_workingstate
    @Slot()
    def _on_save_project(self, save_as:bool = False) -> None:
        if(not self._projfile_path or save_as):
            self._projfile_path = QFileDialog.getSaveFileName(None, GBC.LC_SAVE_PROJECT_FILE_TITLE if not save_as else GBC.LC_SAVEAS_PROJECT_FILE_TITLE, self._projfile_path, f"{GBC.LC_PROJECTFILE_FILTER_TITLE} {GBC.LC_PROJECTFILE_FILTER}")[0]
        if(not self._projfile_path): return
        file = QFile(self._projfile_path)
        file.open(QIODevice.WriteOnly)
        output = QDataStream(file)
        output.writeString(VERSION)
        for r in range(self._task_list_model.rowCount()):
            for c in range(8):
                if c == 1:
                    item:QStandardItem = QStandardItem(self._task_list_model.item(r, c))
                    imd:ImportedMediaData = item.data(role = Qt.UserRole)
                    imc:ImportedMediaContainer = ImportedMediaContainer()
                    imc.load_imported_media_data(imd)
                    item.setData(imc, role=Qt.UserRole)
                    item.write(output)
                else:
                    self._task_list_model.item(r, c).write(output)
        file.close()
        self._update_window_title()
        self._is_project_changed = False
        self._recent_proj.add_path(self._projfile_path)

    def _clear_model(self):
       self._task_list_model.removeRows(0, self._task_list_model.rowCount())


    def _update_window_title(self):
        if (self._projfile_path):
            self.setWindowTitle(f"GIF Builder - {self._projfile_path}")
        else: self.setWindowTitle("GIF Builder")

    @Slot()
    def _on_supp_proj(self):
        if (self.settings.language_index == 1):
            url = QUrl(URL_SUPPPROJECT[1])
        else:
            url = QUrl(URL_SUPPPROJECT[0])
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, GBC.LC_WARNING, GBC.LC_MSG_URLOPENERROR + url.path())

    @Slot()
    def _on_feedback_btn(self):
        url = QUrl(f"{GBC.URL_FEEDBACK_EMAIL}?subject={GBC.LC_FEEDBACK_SUBJECT} {GBC.VERSION}")
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, GBC.LC_WARNING, GBC.LC_MSG_URLOPENERROR + url.path())

    @Slot()
    def _on_author_btn(self):
        url = QUrl(URL_AUTHOR_PAGE)
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, GBC.LC_WARNING, GBC.LC_MSG_URLOPENERROR + url.path())

    @Slot()
    def _on_download_btn(self):
        logging.debug("download")
        def open_url(link):
            def handler():
                url = QUrl(link)
                if not QDesktopServices.openUrl(url):
                    QMessageBox.warning(self, GBC.LC_WARNING, GBC.LC_MSG_URLOPENERROR + url.path())
            return handler

        dwnld_context_menu = QMenu(self)
        dwnld_context_menu.setStyleSheet("font-size:16px")
        links = GBC.WIN_DOWNLOAD_BUILDS_URL
        for i, l in enumerate(links):
            if "ffmpeg.org" in l['url']: dwnld_context_menu.addSeparator()
            dwnld_context_menu.addAction(l['title']).triggered.connect(open_url(l['url']))
        dwnld_context_menu.popup(QCursor.pos())


    @check_workingstate
    @Slot()
    def _on_move_row(self, direction ='U')->None:
        if not self.ui.tableView.selectedIndexes():return
        s_row:int = self.ui.tableView.selectedIndexes()[0].row()
        logging.debug(f"selected row: {s_row}")
        row_count:int = self._task_list_model.rowCount()
        if (s_row == 0 and direction == "U") or (s_row == row_count - 1 and direction == "D"): return
        taken_items = self._task_list_model.takeRow(s_row)
        if direction == 'U':
            logging.debug(f"move_up")
            self._task_list_model.insertRow(s_row - 1, taken_items)
            self.ui.tableView.selectRow(s_row - 1)
        else:
            logging.debug(f"move_down")
            self._task_list_model.insertRow(s_row + 1, taken_items)
            self.ui.tableView.selectRow(s_row + 1)

    @Slot()
    def _on_start_button(self) -> None:
        if (self._working_state == WorkingState.EDITING):
            logging.debug("Handling has been started")
            if not check_exefile(self.settings.ffmpeg_path, "ffmpeg"):
                QMessageBox.warning(self, GBC.LC_WARNING, GBC.LC_MSG_FFMPEG_PATH_NOT_CORRECT, QMessageBox.Ok, QMessageBox.Ok)
                return
            if (self._task_list_model.rowCount() == 0): return
            self.ui.start_button.setText(GBC.LC_STOP)
            self.ui.start_button.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(255, 255, 255)")
            self.ui.status_stack.setCurrentIndex(0)
            self.ui.tableView.setEnabled(False)
            self.ui.tableView.clearSelection()
            self._working_state = WorkingState.PROCESSING
            self._task_handler.is_running = True
            self._task_handler.start(priority=QThread.NormalPriority)
        elif (self._working_state == WorkingState.PROCESSING):
            logging.debug("stop thread")
            self._task_handler.is_running = False
        elif (self._working_state == WorkingState.PROCESSING_FINISHED):
            self.ui.start_button.setText(GBC.LC_CONVERT)
            self.ui.start_button.setStyleSheet("background-color: rgb(0, 255, 0); color: rgb(0, 0, 0)")
            self.ui.status_stack.setCurrentIndex(1)
            self._working_state = WorkingState.EDITING
            for r in range(self._task_list_model.rowCount()):
                for c in range(self._task_list_model.columnCount()):
                    self._task_list_model.item(r, c).setBackground(Qt.white)


    @Slot(TaskHandlerResponse, bool)
    def _on_taskhandler_response(self, response:TaskHandlerResponse, is_started:bool)->None:
        model = self._task_list_model
        logging.debug(f" in task response handler: {'begin' if is_started else 'end'}: {response}")
        if is_started:
            for col in range(model.columnCount()):
                model.item(response.model_row, col).setBackground(QBrush(QColor(73, 148, 252)))
            self.ui.tableView.scrollTo(model.index(response.model_row, 0), hint=QAbstractItemView.PositionAtCenter)
            if response.current == 1:
                self.ui.progressBar.setMinimum(0)
                self.ui.progressBar.setMaximum(response.remain)
        else:
            brush = QBrush(QColor(140, 255, 125) if response.is_successful else QColor(255, 129, 125))
            for col in range(model.columnCount()):
                model.item(response.model_row, col).setBackground(brush)
            self._task_handler.set_pause(False)

        self.ui.current_task_lcd.display(response.current)
        self.ui.remain_tasks_lcd.display(response.remain)
        self.ui.finished_tasks_lcd.display(response.finished)
        self.ui.progressBar.setFormat(model.item(response.model_row, 2).text())
        self.ui.progressBar.setValue(response.finished)


    def _has_taskhandler_finished(self):
        self._working_state = WorkingState.PROCESSING_FINISHED
        self.ui.start_button.setText(GBC.LC_BACK)
        self.ui.start_button.setStyleSheet("background-color: rgb(0, 0, 255); color: rgb(255, 255, 255)")
        self.ui.tableView.setEnabled(True)
        #play sound
        if self.ui.soound_alert_checkBox.checkState() and os.path.exists(self.settings.sound_path):
            winsound.PlaySound(self.settings.sound_path, winsound.SND_FILENAME)
            # fn = QUrl.fromLocalFile(self.settings.sound_path)
            # sound.setSource(fn)
            # sound.setLoopCount(1)
            # sound.play()

        if self.ui.after_converting_combobox.currentIndex() == 1: #power off
            os.system('shutdown -s')
        elif self.ui.after_converting_combobox.currentIndex() == 2: #restart
            os.system("shutdown /r /t  1")



    @Slot()
    def _on_export_dir(self):
        export_path:str = self.ui.tableView.selectedIndexes()[2].data()
        if (export_path):
            dir_path = os.path.dirname(export_path)
            if (os.path.exists(dir_path)):
                os.startfile(dir_path)

    def _on_source_dir(self):
        source_path:str = self.ui.tableView.selectedIndexes()[1].data()
        if (source_path):
            dir_path = os.path.dirname(source_path)
            if (os.path.exists(dir_path)):
                os.startfile(dir_path)

    @Slot()
    def _on_dupli_task(self):
        buffer = []
        selected_row:int = self.ui.tableView.selectedIndexes()[0].row()
        model:QStandardItemModel = self.ui.tableView.selectedIndexes()[0].model()
        for col in range(model.columnCount()):
            buffer.append(QStandardItem(model.item(selected_row, col)))
        for i in (1, 2):
            buffer[i].setData(
                replace(model.item(selected_row,i).data(role=Qt.UserRole)),
                role=Qt.UserRole)
        model.insertRow(selected_row + 1, buffer)
        self._task_list_model.itemChanged.emit(QStandardItem())

    @Slot(int)
    def _on_soundalert_changed(self, state):
        if state and not os.path.exists(self.settings.sound_path):
            self.ui.soound_alert_checkBox.setCheckState(Qt.Unchecked)
            QMessageBox.warning(self, LC_WARNING, LC_MSG_SOUND_ISNT_SELECTED, QMessageBox.Ok, QMessageBox.Ok)


    def closeEvent(self, e):
        self._recent_proj.save_list_to_hdd()
        if self._working_state != WorkingState.EDITING:
            e.ignore()
            return
        if not self._is_project_changed: return
        result = QMessageBox.question(self, GBC.LC_CONFIRMATION, GBC.LC_MSG_EXIT_SAVE_QUESTION,
                                      QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)

        if result == QMessageBox.No or result == QMessageBox.Yes:
            if result == QMessageBox.Yes:
                self._on_save_project()
            e.accept()
            QWidget.closeEvent(self, e)
        elif result == QMessageBox.Cancel:
            e.ignore()

    def retranslateUi(self):
        importlib.reload(GBC)
        importlib.reload(GBDET)
        self._task_list_model.setHorizontalHeaderLabels(
            [GBC.LC_HEADERACTIVE, GBC.LC_HEADERSOURCEFILE, GBC.LC_HEADEREXPORTFILE, GBC.LC_HEADERSTARTFRAME, GBC.LC_HEADERENDFRAME,
             GBC.LC_HEADERFRAMERATE, GBC.LC_HEADERSCALE, GBC.LC_HEADERLOOP])
        self.ui.version_label.setText(VERSION)
        self.ui.tableView.retranslateUi()
        self._update_window_title()

    @Slot(bool)
    def set_activity_status_all_tasks(self, status:bool):
        model = self._task_list_model
        for row in range(model.rowCount()):
            model.item(row, 0).setCheckState(Qt.Checked if status else Qt.Unchecked)

    @Slot()
    def on_find_ffmpeg_files(self):
        search_res:dict = {}
        ffmpeg_path:str = ""
        ffprobe_path: str = ""
        for stage in range(1,3):
            dir_pathes = []
            if stage == 1:
                dir_pathes = os.environ["PATH"].split(';')
            elif stage == 2:
                dir_pathes.append(QFileDialog.getExistingDirectory(self, GBC.LC_SELECT_DIR_TITLE, "/", QFileDialog.ShowDirsOnly))

            for path in dir_pathes:
                if (stage == 1) and ("ffmpeg" not in path): continue
                search_res = find_ffmpeg_files(path)
                ffmpeg_path = search_res["ffmpeg"] if search_res["ffmpeg"] else ffmpeg_path
                ffprobe_path = search_res["ffprobe"] if search_res["ffprobe"] else ffprobe_path

            if ffmpeg_path:
                self.ui.inputpath_ffmpeg.set_path(ffmpeg_path)
            if ffprobe_path:
                self.ui.inputpath_ffprobe.set_path(ffprobe_path)

            if (stage == 1) and (not ffmpeg_path or not ffprobe_path):
                dialog_res = QMessageBox.question(self, GBC.LC_DIAL_SELECT_ACTION, GBC.LC_MSG_SELECT_DIR_FFMPEG_SEARCH, QMessageBox.StandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No))
                logging.debug(dialog_res)
                if dialog_res == QMessageBox.StandardButton.No:
                    break
            else:
                break

    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.MoveAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            extension = ".gbp"
            if (os.path.splitext(file_path)[1] == extension):
                event.accept()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self._on_open_project(file_path)






app = QApplication(sys.argv)
app.setStyle("Fusion")
window = GIFBuilder()
window.show()
sys.exit(app.exec_())
