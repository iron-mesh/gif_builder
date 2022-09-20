import json
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




if __name__ == "__main__":
    print("______get_media_parameters test _____")
    video_path = r"D:\MAIN\Art\Commercial Projects\25-03-22 Crypto Storage Case 3 (staff)\Export\animation\ ut  white -0001-0410.mp4"
    ffprobe_path = r"D:\Soft\ffmpeg-N-104359-g9b445663a5-win64-lgpl\bin\ffprobe.exe"
    ffmpeg_path = r"D:\Soft\ffmpeg-N-104359-g9b445663a5-win64-lgpl\bin\ffmpeg.exe"
    res = get_media_parameters(ffprobe_path, video_path, MediaType.VIDEO)
    print(res)
    print(f"{check_exefile.__name__} checking: {check_exefile(ffmpeg_path, 'ffmpeg')}")
