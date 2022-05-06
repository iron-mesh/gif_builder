import dataclasses
import logging
from dataclasses import dataclass

from .GB_constants import MediaType

logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)

@dataclass
class SettingsData:
    """ Class describes data structure of GIF builder settings"""
    language_index:int = 0
    ffmpeg_path:str = ""
    ffprobe_path:str = ""
    sound_path: str = ""
    exp_dir:str = ""
    def_framerate:int = 24

@dataclass
class MediaFileData:
    """ Class describes data structure of media file information"""
    framerate:int = 0
    width: int = 0
    height: int = 0
    frame_count: int = 0
    type:int = MediaType.VIDEO

    def __str__(self) -> str:
        return f" framerate: {self.framerate} \n width: {self.width} \n height: {self.height} \n frame_count: {self.frame_count} \n type: {self.type} "



@dataclass
class ImportedMediaData:
    """ Class describes data structure of imported media video or image sequence"""
    media_file_par:MediaFileData = MediaFileData()
    start_frame:int = 1
    end_frame: int = 1
    videofile_path:str = ""
    imgseq_pathes: list = dataclasses.field(default_factory=list)

@dataclass
class TaskHandlerResponse:
    """ Class describes data structure of task handler signal"""
    current: int = 0
    remain: int = 0
    finished: int = 0
    model_row:int = 0
    is_successful:bool = False



if __name__ == "__main__":
    s = SettingsData()
    logging.debug(s)