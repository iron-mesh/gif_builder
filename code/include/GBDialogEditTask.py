import sys

import PySide2.QtWidgets as wgts
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QDialog, QWidget, QApplication

from .GB_constants import *
from .GB_types import *
from .GUI.ui_dialog_edit_task import Ui_Dialog
from dataclasses import replace

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)


class GBDialogEditTask(QDialog):
    """ Class provides element of UI to input path(es) to video or image sequence"""

    def __init__(self, parent, app_set:SettingsData):
        super().__init__()
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        if parent.windowIcon():
            self.setWindowIcon(parent.windowIcon())
        self._ui.ip_export_file.set_mode(Modes.SAVE_IMAGE)
        self._ui.ip_export_file.set_placeholder_text(LC_EXPORTFILEPATH)
        self._ui.isfp_import_media.link_appsettings(app_set)
        self._ui.isfp_import_media.path_changed.connect(self._on_path_changed)
        self._ui.cb_dither_mode.currentIndexChanged.connect(self._on_dither_changed)

    def import_data(self, i_list:list[QModelIndex])->None:
        """recieves list of indexes and puts values to form"""
        im_media:ImportedMediaData = i_list[1].data(role = Qt.UserRole)
        filter_options:FilterOptions = i_list[2].data(role = Qt.UserRole)
        im_media.start_frame = int(i_list[3].data())
        im_media.end_frame = int(i_list[4].data())

        self._ui.isfp_import_media.set_data(im_media)
        self._ui.ip_export_file.set_path(i_list[2].data())
        self._ui.sb_framerate.setValue(int(i_list[5].data()))
        self._ui.sb_scale.setValue(int(i_list[6].data()))
        logging.debug(i_list[7].data(role = Qt.CheckStateRole))
        if(i_list[7].data(role = Qt.CheckStateRole) == Qt.Checked):
            self._ui.cb_loopanimation.setChecked(True)
        self._ui.cb_stats_mode.setCurrentText(filter_options.stats_mode)
        self._ui.cb_dither_mode.setCurrentText(filter_options.dither_mode)
        self._ui.sb_bayer_scale.setValue(filter_options.bayer_scale)
        self._ui.cb_diff_mode.setCurrentText(filter_options.diff_mode)


    def update_data(self, i_list:list[QModelIndex])->None:
        """receives list of indexes and updates its info from form"""
        model:QStandardItemModel = i_list[0].model()
        imd = self._ui.isfp_import_media.get_data()
        if (imd.media_file_par.type == MediaType.VIDEO):
            model.setData(i_list[1], imd.videofile_path)
        else:
            model.setData(i_list[1], imd.imgseq_pathes[0])
        model.setData(i_list[1], imd, role=Qt.UserRole)
        model.setData(i_list[2], self._ui.ip_export_file.get_path())
        filter_options: FilterOptions = i_list[2].data(role=Qt.UserRole)
        filter_options.stats_mode = self._ui.cb_stats_mode.currentText()
        filter_options.dither_mode = self._ui.cb_dither_mode.currentText()
        filter_options.bayer_scale = self._ui.sb_bayer_scale.value()
        filter_options.diff_mode = self._ui.cb_diff_mode.currentText()
        model.setData(i_list[2], filter_options, role=Qt.UserRole)
        model.setData(i_list[3], str(imd.start_frame))
        model.setData(i_list[4], str(imd.end_frame))
        model.setData(i_list[5], str(self._ui.sb_framerate.value()))
        model.setData(i_list[6], str(self._ui.sb_scale.value()))
        model.setData(i_list[7], self._ui.cb_loopanimation.checkState(), role = Qt.CheckStateRole)

    def get_data(self)->list:
        """return list of QStandardItem"""
        res = []
        for i in range(8):
            res.append(QStandardItem())
        imd = self._ui.isfp_import_media.get_data()
        res[0].setData(Qt.Checked, role = Qt.CheckStateRole)
        if (imd.media_file_par.type == MediaType.VIDEO):
            res[1].setText(imd.videofile_path)
        else:
            res[1].setText(imd.imgseq_pathes[0])
        res[1].setEditable(False)
        res[2].setText(self._ui.ip_export_file.get_path())
        filter_options: FilterOptions = FilterOptions()
        filter_options.stats_mode = self._ui.cb_stats_mode.currentText()
        filter_options.dither_mode = self._ui.cb_dither_mode.currentText()
        filter_options.bayer_scale = self._ui.sb_bayer_scale.value()
        filter_options.diff_mode = self._ui.cb_diff_mode.currentText()
        res[2].setData(filter_options, role=Qt.UserRole)
        res[3].setText(str(imd.start_frame))
        res[4].setText(str(imd.end_frame))
        res[5].setText(str(self._ui.sb_framerate.value()))
        res[6].setText(str(self._ui.sb_scale.value()))
        res[7].setData(self._ui.cb_loopanimation.checkState(), role = Qt.CheckStateRole)

        res[0].setCheckable(True)
        res[7].setCheckable(True)
        res[1].setData(replace(imd), role = Qt.UserRole)

        for item in res:
            item.setTextAlignment(Qt.AlignCenter)

        return res

    @Slot()
    def _on_path_changed(self) -> None:
        mfp:MediaFileParameters = self._ui.isfp_import_media.get_data().media_file_par
        if ( mfp.type == MediaType.VIDEO):
            self._ui.sb_framerate.setValue(mfp.framerate)

    @Slot()
    def _on_dither_changed(self):
        if self._ui.cb_dither_mode.currentText() != "bayer":
            self._ui.sb_bayer_scale.setEnabled(False)
        else:
            self._ui.sb_bayer_scale.setEnabled(True)


if __name__ == "__main__":
    print("GBDialogEditTask test")
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GBDialogEditTask test")
    layout = wgts.QVBoxLayout(window)
    btn1 = wgts.QPushButton("Open dialog")
    btn2 = wgts.QPushButton("Resize")
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    window.resize(700, 300)
    window.show()
    dialog = GBDialogEditTask(SettingsData())
    btn1.clicked.connect(lambda: dialog.exec_())
    btn2.clicked.connect(lambda: dialog.resize(dialog.sizeHint()))
    sys.exit(app.exec_())




