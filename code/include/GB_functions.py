import json
import re
import subprocess, os, logging



from .GB_types import *
from .GB_constants import *
from types import ModuleType
from PySide2.QtWidgets import QMessageBox


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




if __name__ == "__main__":
    pass

