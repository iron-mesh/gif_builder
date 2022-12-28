import json, re, subprocess, os, logging

from .GB_types import *
from .GB_constants import *
from types import ModuleType
from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QStandardItem
from PySide2.QtCore import Qt
from dataclasses import replace


from importlib import reload

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)

def rreload(module):
    """Recursively reload modules."""
    reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)


def get_media_parameters(ffprobe_path:str, file_path:str, media_type:MediaType)->MediaFileParameters:
    """ Returns parametres of mediafile"""
    cmd = [ffprobe_path, '-print_format', 'json', '-show_streams', '-count_frames', file_path]
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    res = subprocess.run(cmd, capture_output=True, startupinfo=startupinfo)
    json_val = json.loads(res.stdout)

    result = MediaFileParameters()
    result.width = int(json_val['streams'][0]['width'])
    result.height = int(json_val['streams'][0]['height'])

    if(media_type == MediaType.VIDEO):
        result.type = MediaType.VIDEO
        fr_str:str = (json_val['streams'][0]['avg_frame_rate'])
        result.framerate = int(fr_str.split('/')[0]) // int(fr_str.split('/')[1])
        result.frame_count = int(json_val['streams'][0]['nb_frames'])
    else:
        result.type = MediaType.IMAGE

    return result


def check_workingstate(f):
    def wrapper(self, *args, **kwargs):
        if (self._working_state == WorkingState.EDITING):
            f(self, *args, **kwargs)
        else:
            pass
    return wrapper

def check_ffprobe(f):
    def wrapper(self, *args, **kwargs):
        if (check_exefile(self.settings.ffprobe_path, "ffprobe")):
            f(self, *args, **kwargs)
        else:
            QMessageBox.warning(self, LC_WARNING, LC_MSG_FFPROBE_PATH_NOT_CORRECT, QMessageBox.Ok,
                                QMessageBox.Ok)
            return
    return wrapper

def check_exefile(path:str, match_str:str)->bool:
    if not os.path.exists(path): return False
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        with subprocess.Popen(path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=startupinfo) as process:
            data, err = process.communicate(timeout=60)
            if err.decode(encoding="utf-8").find(match_str) == -1: raise Exception(f"{match_str} check error").with_traceback()
    except:
        return False
    else:
        return True

def find_ffmpeg_files(dir:str)->dict:
    re_ffmpeg = re.compile(r"^.*ffmpeg.*exe$", flags=re.IGNORECASE)
    re_ffprobe = re.compile(r"^.*ffprobe.*exe$", flags=re.IGNORECASE)
    result = {"ffprobe":"", "ffmpeg":""}
    for dir_name, subdir_names, file_names in os.walk(dir):

        for f_name in file_names:
            if (re_ffmpeg.search(f_name)):
                path = os.path.join(dir_name, f_name)
                if check_exefile(path, "ffmpeg"):
                    result["ffmpeg"] = path

            if (re_ffprobe.search(f_name)):
                path = os.path.join(dir_name, f_name)
                if check_exefile(path, "ffprobe"):
                    result["ffprobe"] = path
    return result


def get_model_from_source(type:MediaType, source, settings:SettingsData,fname:str = "")->list[QStandardItem]:
    imd:ImportedMediaData = ImportedMediaData()
    imd.media_file_par = MediaFileParameters()
    mfd = imd.media_file_par
    mfd.type = type
    if(type == MediaType.VIDEO):
        imd.videofile_path = source
        mfd = get_media_parameters(settings.ffprobe_path, source, type)
        imd.end_frame = mfd.frame_count
    elif(type == MediaType.IMAGE):
        imd.imgseq_pathes = source
        mfd = get_media_parameters(settings.ffprobe_path, source[0], type)
        mfd.framerate = settings.def_framerate
        mfd.frame_count = len(source)
        imd.end_frame = mfd.frame_count
    imd.start_frame = 1

    res = list()
    for i in range(8):
        res.append(QStandardItem())

    res[0].setData(Qt.Checked, role=Qt.CheckStateRole)
    res[0].setCheckable(True)
    if (imd.media_file_par.type == MediaType.VIDEO):
        res[1].setText(imd.videofile_path)
    else:
        res[1].setText(imd.imgseq_pathes[0])
    res[1].setEditable(False)
    res[1].setData(replace(imd), role=Qt.UserRole)

    export_path:str = ""
    if(settings.exp_dir):
        file_name: str = os.path.basename(imd.videofile_path) if type == MediaType.VIDEO else os.path.basename(
            imd.imgseq_pathes[0])
        file_name = os.path.splitext(file_name)[0] if not fname else fname
        export_path = os.path.join(settings.exp_dir, file_name + '.gif')

    res[2].setText(export_path)
    filter_options: FilterOptions = FilterOptions()
    res[2].setData(filter_options, role=Qt.UserRole)
    res[3].setText(str(imd.start_frame))
    res[4].setText(str(imd.end_frame))
    res[5].setText(str(mfd.framerate))
    res[6].setText("100")
    res[7].setData(settings.looped_animation, role=Qt.CheckStateRole)
    res[7].setCheckable(True)

    for item in res:
        item.setTextAlignment(Qt.AlignCenter)

    return res




if __name__ == "__main__":
    pass

