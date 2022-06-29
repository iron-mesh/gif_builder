import sys
from os.path import *

from PySide2 import QtCore
from PySide2.QtWidgets import *

from ..import GB_constants as GBC
from ..GB_functions import *
from ..GUI.ui_input_source_file_pathes import Ui_Form

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)

class QInputSourceFilePathes(QWidget):
    """ Class provides element of UI to input path(es) to video or image sequence"""
    path_changed = QtCore.Signal()

    def __init__(self, parent):
        super().__init__()
        self._imp_media = ImportedMediaData()
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._ui.btn_import_video_file.clicked.connect(self._on_press_video_import)
        self._ui.btn_import_img_seq.clicked.connect(self._on_press_imgseq_import)
        self._ui.sb_start_frame.valueChanged.connect(self._on_update_spinboxes)
        self._ui.sb_end_frame.valueChanged.connect(self._on_update_spinboxes)


    @QtCore.Slot()
    def _on_press_video_import(self)->None:
        prev_path = self._imp_media.videofile_path
        self._imp_media.videofile_path = QFileDialog.getOpenFileName(None, GBC.LC_SELECT_VIDEO_FILE_TITLE, "", f"{GBC.LC_VIDEOFILE_FILTER_TITLE} {GBC.LC_VIDEOFILE_FILTER}")[0]
        self._imp_media.media_file_par.type = MediaType.VIDEO
        self._display_media_par(reset_framerange = True)
        if(prev_path != self._imp_media.videofile_path): self.path_changed.emit()


    @QtCore.Slot()
    def _on_press_imgseq_import(self)->None:
        prev_pathes = self._imp_media.imgseq_pathes if len(self._imp_media.imgseq_pathes) else [""]
        image_list = QFileDialog.getOpenFileNames(None, GBC.LC_SELECT_IMAGESEQ_FILE_TITLE, "", f"{GBC.LC_IMAGEFILE_FILTER_TITLE} {GBC.LC_IMAGEFILE_FILTER}")[0]
        if image_list:
            if(not self._is_fileformat_identical(image_list)):
                self._ui.te_import_info.setText(f" <p style=\"color:red\">{GBC.LC_IMPORTERR}: {GBC.LC_MSG_EXT_NOT_EQUAL}</p>")
                return
            self._imp_media.media_file_par.type = MediaType.IMAGE
            self._imp_media.imgseq_pathes = image_list
            self._display_media_par(reset_framerange = True)
            if (prev_pathes[0] != self._imp_media.imgseq_pathes[0]):self.path_changed.emit()

    def _display_media_par(self, reset_framerange: bool = False)->None:
        """  display media source parameters
        update_framerange = True:  method inserts framerange from source """
        im = self._imp_media
        mfp = self._imp_media.media_file_par
        logging.debug("im.media_file_par is mfp"if im.media_file_par is mfp else "im.media_file_par is NOT mfp")

        if(not im.videofile_path and mfp.type == MediaType.VIDEO) or (not im.imgseq_pathes and mfp.type == MediaType.IMAGE):
            return
        try:
            file_path:str = im.videofile_path if (mfp.type == MediaType.VIDEO) else im.imgseq_pathes[0]
            mfp = get_media_parameters(self._app_settings.ffprobe_path, file_path, mfp.type)
            logging.debug(f"mfp = {mfp}")
        except Exception as msg:
            logging.debug("error: " + msg.__str__())
            self._ui.te_import_info.setText(f" <p style=\"color:red\">{GBC.LC_IMPORTERR}</p>")
            return

        if (mfp.type == MediaType.IMAGE):
            mfp.frame_count = len(im.imgseq_pathes)

        type_str:str = LC_VIDEO if (mfp.type == MediaType.VIDEO) else GBC.LC_IMGSEQ
        if(mfp.type == MediaType.VIDEO):
            result = f"{im.videofile_path}\n{GBC.LC_MEDIATYPE}: {type_str}\n{GBC.LC_FRAMESIZE}:\n  {GBC.LC_WIDTH}: {mfp.width} \n  {GBC.LC_HEIGHT}: {mfp.height}\n{GBC.LC_FRAMERATE}: {mfp.framerate}\n{GBC.LC_FRAMECOUNT}: {mfp.frame_count} "
        else:
            result = f"{im.imgseq_pathes[0]}\n{GBC.LC_MEDIATYPE}: {type_str}\n{GBC.LC_FRAMESIZE}:\n  {GBC.LC_WIDTH}: {mfp.width} \n  {GBC.LC_HEIGHT}: {mfp.height}\n{GBC.LC_FRAMECOUNT}: {mfp.frame_count} "

        self._ui.te_import_info.setText(result)
        self._ui.sb_start_frame.setEnabled(True)
        self._ui.sb_end_frame.setEnabled(True)
        self._ui.sb_start_frame.setMaximum(mfp.frame_count)
        self._ui.sb_end_frame.setMaximum(mfp.frame_count)
        self._ui.sb_start_frame.setValue(1)
        self._ui.sb_end_frame.setValue(mfp.frame_count)
        self._ui.sb_start_frame.setMinimum(1)
        self._ui.sb_end_frame.setMinimum(1)
        self._imp_media.media_file_par = mfp

        if(not reset_framerange):
            start_f = im.start_frame
            end_f = im.end_frame

            sb_start_f = self._ui.sb_start_frame.value()
            sb_end_f = self._ui.sb_end_frame.value()

            if(start_f > sb_start_f and start_f < sb_end_f): self._ui.sb_start_frame.setValue(start_f)
            if (end_f > sb_start_f and end_f < sb_end_f): self._ui.sb_end_frame.setValue(end_f)

    def get_data(self)->ImportedMediaData:
        self._imp_media.start_frame = self._ui.sb_start_frame.value()
        self._imp_media.end_frame = self._ui.sb_end_frame.value()
        return self._imp_media

    def set_data(self, data:ImportedMediaData)->None:
        self._imp_media = data
        self._display_media_par()


    @QtCore.Slot()
    def _on_update_spinboxes(self):
        self._ui.sb_start_frame.setMaximum(self._ui.sb_end_frame.value())
        self._ui.sb_end_frame.setMinimum(self._ui.sb_start_frame.value())
        return self._imp_media

    def link_appsettings(self, app_settings: SettingsData):
        self._app_settings = app_settings

    def _is_fileformat_identical(self, ilist:list)->bool:
        extention = splitext(ilist[0])[1]
        logging.debug(f" File extention: {extention}")
        for p in ilist:
            if extention != splitext(p)[1]: return False
        return True




if __name__ == "__main__":
    print("GBInputSourceFilePathes.py test")
    app = QApplication(sys.argv)
    settings = SettingsData()
    settings.ffprobe_path = r"D:\Soft\ffmpeg-N-104359-g9b445663a5-win64-lgpl\bin\ffprobe.exe"
    window = QWidget()
    window.setWindowTitle("GBInputSourceFilePathes.py test")
    layout = QVBoxLayout(window)
    layout.addWidget(QLabel("Select Something"))
    input= QInputSourceFilePathes()
    input.path_changed.connect(lambda: print("path changed"))
    input.link_appsettings(settings)
    layout.addWidget(input)
    btn = QPushButton("Extract")
    btn.clicked.connect(lambda: logging.debug(input.get_data()))
    layout.addWidget(btn)
    window.resize(700, 300)
    window.show()
    sys.exit(app.exec_())




