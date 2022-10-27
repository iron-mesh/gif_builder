from .GB_types import *
import os.path, re
from dataclasses import dataclass, field

@dataclass
class ImportedMediaContainer:
    """Class describes data structure of imported media video or image sequence replacement of ImportedMediaData"""
    media_file_par:MediaFileParameters = MediaFileParameters()
    start_frame: int = 1
    end_frame: int = 1
    videofile_path: str = ""
    _dir_list:list[str] = field(default_factory=list)
    _img_list:list[dict] = field(default_factory=list)

    def load_imported_media_data(self, data:ImportedMediaData)->None:
        """Loads data from ImportedMediaData instance"""
        self.media_file_par = data.media_file_par
        self.start_frame = data.start_frame
        self.end_frame = data.end_frame
        self.videofile_path = data.videofile_path
        self.import_images(data.imgseq_pathes)

    def export_imported_media_data(self) -> ImportedMediaData:
        """Export data from this class to ImportedMediaData """
        imd = ImportedMediaData()
        imd.media_file_par = self.media_file_par
        imd.start_frame = self.start_frame
        imd.end_frame = self.end_frame
        imd.videofile_path = self.videofile_path
        imd.imgseq_pathes = self.get_img_list()
        return imd

    def import_images(self, img_seg:list)->None:
        """Recieves list of file addresses and packs them into the class (fields: _dir_list, img_list)  """

        def analize_num_str(s: str, reset=False) -> bool:
            """Checks string of number; returns False, if number sequence changes unlogically """
            if reset:  # start new seq
                analize_num_str.is_fixed_length = (s[0] == '0')
                analize_num_str.num_length = len(s)
            if not analize_num_str.is_fixed_length and (s[0] == '0'):
                analize_num_str.is_fixed_length = True
            if analize_num_str.is_fixed_length and analize_num_str.num_length != len(s):
                analize_num_str.is_fixed_length = False
                return False
            else:
                return True

        def get_dict_template():
            return {"manifest": "",
                   "dir_index": 0,
                   "mask":{"head":"", "tail":""},
                   "file_list":[],
                   "num_range":[]}

        def close_dict():
            """ Close the last dictionary in the list"""
            nonlocal range_record_started, mask_creating_failed, prev_num, analize_num_str, head, tail
            if not mask_creating_failed:
                self._img_list[-1]["num_range"][-1][1] = prev_num
                range_record_started = False
                del self._img_list[-1]["file_list"]
                self._img_list[-1]["mask"]['head'] = head
                self._img_list[-1]["mask"]['tail'] = tail
                if analize_num_str.is_fixed_length:
                    self._img_list[-1]["manifest"] = f"mask|fixed_length:{analize_num_str.num_length}"
                else:
                    self._img_list[-1]["manifest"] = f"mask|nonfixed_length"
            else:
                del self._img_list[-1]["mask"]
                del self._img_list[-1]["num_range"]
                self._img_list[-1]["manifest"] = "list"


        if not img_seg:
            return None

        seq_len:int = len(img_seg) #length of the input list
        img_list = self._img_list
        dir_list = self._dir_list
        init_dict:bool = True
        mask_creating_failed: bool = False
        range_record_started:bool = False

        prev_dir_name:str = ""
        prev_num:int = 0
        enum_direction:int = 0

        for i in range(seq_len): #pathes processing
            dir_name = os.path.dirname(img_seg[i])
            file_name = os.path.basename(img_seg[i])

            if prev_dir_name != dir_name:
                init_dict = True

            if init_dict: #init new dictionary (start)
                if len(img_list)>0:
                    close_dict()
                if dir_name not in dir_list: dir_list.append(dir_name)
                img_list.append(get_dict_template())
                img_list[-1]["dir_index"] = dir_list.index(dir_name)
                re_mask = re.compile(r"(\D*)(\d*)(\D*)")
                match_obj1 = re_mask.search(file_name)
                head, num_str, tail = match_obj1.groups()
                if not num_str:
                    mask_creating_failed = True
                else:
                    prev_num = int(num_str)
                enum_direction = 0
                analize_num_str(num_str, reset=True)
                init_dict = False #init new dictionary (end)

            if not mask_creating_failed:
                match_obj1 = re_mask.search(file_name)
                num_str = match_obj1.group(2)
                if not analize_num_str(num_str) or match_obj1.group(1) != head or match_obj1.group(3) != tail:
                    mask_creating_failed = True
                    range_record_started = False

                if range_record_started:
                    if not enum_direction:
                        enum_direction = 1 if (int(num_str) - prev_num) > 0 else -1
                    if (c_num := int(num_str)) - prev_num == enum_direction:
                        prev_num = c_num
                    else:
                        #close range and start new
                        img_list[-1]["num_range"][-1][1] = prev_num
                        prev_num = c_num
                        range_record_started = False

                if not range_record_started:
                    img_list[-1]["num_range"].append( [int(num_str), 0])
                    range_record_started = True

            img_list[-1]["file_list"].append(file_name)
            prev_dir_name = dir_name

        close_dict()

    def get_img_list_iterator(self)->str:
        """ Return gen function of list of full pathes of source images"""
        def my_range(a:int, b:int)-> int:
            step = 1 if (a < b) else -1
            counter:int = a
            while(1):
                yield counter
                if counter != b:
                    counter += step
                else:
                    break

        def convert_to_fl_num(n:int, length:int)->str:
            """Convert number to string of fixed length"""
            num_s = str(n)
            return f"{(length - len(num_s)) * '0'}{num_s}"

        dir_list:list = self._dir_list
        img_list:list = self._img_list

        for img in img_list:
            dict_type:str = img["manifest"].split('|')[0]
            mask_type:str = ""
            num_length:int = 0
            dir_name = dir_list[img["dir_index"]]

            if dict_type == "list":
                for file_name in img["file_list"]:
                    yield os.path.join(dir_name, file_name)

            elif dict_type == "mask":
                m = img["manifest"].split('|')[1].split(':')
                mask_type = m[0]
                num_length = int(m[1]) if mask_type == "fixed_length" else 0
                head = img["mask"]['head']
                tail = img["mask"]['tail']
                for el in img["num_range"]:
                    if mask_type == "nonfixed_length":
                        for i in my_range(el[0], el[1]):
                            yield os.path.join(dir_name, head + str(i) + tail)
                    else:
                        for i in my_range(el[0], el[1]):
                            yield os.path.join(dir_name, head + convert_to_fl_num(i, num_length) + tail)

    def get_img_list(self)->list:
        """ Return list of full pathes of source images"""
        return list(self.get_img_list_iterator())

    def get_img_by_index(self, index:int) -> str:
        """ Empty Block"""
        for i, el in enumerate(self.get_img_list_iterator()):
            if i == index: return el
        return ""



