
from .GB_types import *
import os.path
from dataclasses import dataclass, field

@dataclass
class ImportedMediaContainer:
    """Class describes data structure of imported media video or image sequence replacement of ImportedMediaData"""
    media_file_par:MediaFileParameters = MediaFileParameters()
    start_frame: int = 1
    end_frame: int = 1
    videofile_path: str = ""
    img_name_list:list[tuple] = field(default_factory=list)
    img_dir_list:list[str] = field(default_factory=list)


    def load_imported_media_data(self, data:ImportedMediaData) -> None:
        """Loads data from obsolete ImportedMediaData """
        self.media_file_par = data.media_file_par
        self.start_frame = data.start_frame
        self.end_frame = data.end_frame
        self.videofile_path = data.videofile_path
        self.import_images(data.imgseq_pathes)

    def import_images(self, img_seg:list) ->None:
        """Recieves list of file addresses and packs them into class"""
        if img_seg:
            for if_name in img_seg:
                dir_name = os.path.dirname(if_name)
                file_name = os.path.basename(if_name)
                if dir_name not in self.img_dir_list:
                    self.img_dir_list.append(dir_name)
                self.img_name_list.append((self.img_dir_list.index(dir_name), file_name))

    def get_img_list(self):
        """ Return gen function of list of full pathes of source images"""
        for dir_index, fname in self.img_name_list:
            yield os.path.join(self.img_dir_list[dir_index], fname)


