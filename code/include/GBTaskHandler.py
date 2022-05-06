import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from os.path import *
from .GB_types import *
from .GB_constants import *
from math import *
import subprocess, re, logging, shutil, os, time

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)


class TaskHandler(QThread):
    task_changed = Signal(TaskHandlerResponse, bool) #2th arg: True - task started,  False - task finished

    def __init__(self, parent):
        super(TaskHandler, self).__init__(parent)
        self._parent = parent
        self._temperal_dir:str = ""
        self.running:bool = True
        self._temperal_dir: str = ""
        self._palette_path: str = ""

    def run(self) -> None:
        model:QStandardItemModel = self._parent._task_list_model
        response = TaskHandlerResponse()
        response.current = 0
        response.finished = 0
        response.remain = 0


        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        for r in range(model.rowCount()):
            if(model.item(r, 0).checkState() == Qt.Checked):
                response.remain += 1

        for row in range(model.rowCount()):
            if not self.running: break
            if (model.item(row, 0).checkState() == Qt.Unchecked): continue
            response.model_row = row
            response.current += 1
            logging.debug(">>>>task started>>>>")
            self.task_changed.emit(response, True)
            #time.sleep(3)

            try:
                if not self._is_valid_task(row): raise Exception("task isn't valid").with_traceback()
                # pass 1 palette creation

                # pass 2 exporting
                with subprocess.Popen(self._generate_command(row), stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=startupinfo) as pr:
                    data, err = pr.communicate(timeout=600)
                    # logging.debug(f"data: {data}")
                    logging.debug(f"pass 2 error: {err}")
                    if err: raise Exception("FFmpeg Error").with_traceback()
            except Exception as msg:
                logging.debug(f"Thread message:{msg}")
                response.is_successful = False
            else:
                response.is_successful = True

            response.finished += 1
            response.remain -= 1
            #time.sleep(3)
            logging.debug(">>>>task finished>>>>")
            self.task_changed.emit(response, False)
            time.sleep(2)
            if self._temperal_dir and exists(self._temperal_dir):
                shutil.rmtree(self._temperal_dir)


    def _is_valid_task(self, row:int)->bool:
        model: QStandardItemModel = self._parent._task_list_model
        input_path = model.item(row, 1).text()
        export_path = model.item(row, 2).text()
        return (input_path and export_path)


    def _get_imgseq_mask(self, row:int)->tuple:
        """Return tuple: (<image mask for ffmpeg>, <index of first image>),
        if error is occured return None"""
        model: QStandardItemModel = self._parent._task_list_model
        imglist:list = model.item(row, 1).data(role = Qt.UserRole).imgseq_pathes
        first_element:int = int(model.item(row, 3).text()) - 1
        last_element:int = int(model.item(row, 4).text()) - 1
        first_image_index:int = 0
        extention: str = splitext(imglist[first_element])[1]
        export_dir: str = dirname(imglist[first_element])
        regex_template_str_stage1:str = r"^(\D+)(\d+)$"
        regex_template_stage1 = re.compile(regex_template_str_stage1)
        match_stage1:re.Match = regex_template_stage1.search(splitext(basename(imglist[first_element]))[0])
        if (match_stage1 is None): return None
        logging.debug(f"match_stage1.groups: {match_stage1.groups()}")
        num_count:int = len(match_stage1.group(2))
        if num_count > 9: return None
        first_image_index = int(match_stage1.group(2))
        regex_template_str_stage2 = f"^{match_stage1.group(1)}[0-9]" + '{' + str(num_count) + '}$'
        regex_template_stage2 = re.compile(regex_template_str_stage2)
        for img in imglist[first_element: last_element + 1]:
            if(not regex_template_stage2.match(splitext(basename(img))[0])): return None
        return f"{export_dir}/{match_stage1.group(1)}%0{num_count}d{extention}", first_image_index


    def _generate_commands(self, row:int)->tuple:
        """Generates commands for ffmpeg ->(<palette creation>, <gif creation>)"""
        model:QStandardItemModel = self._parent._task_list_model
        imp_media_data:ImportedMediaData = model.item(row, 1).data(role=Qt.UserRole)
        mode:int = imp_media_data.media_file_par.type
        first_frame: int = int(model.item(row, 3).text()) - 1
        last_frame: int = int(model.item(row, 4).text()) - 1
        command:list[str] = [self._parent.settings.ffmpeg_path, "-y", "-loglevel", "error"]
        command_palette:list[str] = [self._parent.settings.ffmpeg_path, "-y", "-loglevel", "error"]
        if (mode == MediaType.VIDEO):
            command.append("-i")
            command_palette.append("-i")
            command.append(imp_media_data.videofile_path)
            command_palette.append(imp_media_data.videofile_path)
            # if (first_frame > 0):
            #     command.append("-start_number")
            #     command.append(str(first_frame))
            # if (last_frame - first_frame + 1) < imp_media_data.media_file_par.frame_count:
            #     command.append("-frames:v")
            #     command.append(str(last_frame - first_frame + 1))
            if int(model.item(row, 5).text()) != imp_media_data.media_file_par.framerate:
                command.append("-r")
                command.append(model.item(row, 5).text())
        else:
            command.append("-f")
            command.append("image2")
            command.append("-framerate")
            command.append(model.item(row, 5).text())
            inputfile_mask = self._get_imgseq_mask(row)
            if(inputfile_mask is not None):
                command.append("-start_number")
                command.append(str(inputfile_mask[1]))
                command.append("-i")
                command.append(inputfile_mask[0])
            else:
                command.append("-i")
                command.append(self._copy_images_to_temperal(row)[0])
            if (inputfile_mask is not None) and ((last_frame - first_frame + 1) < imp_media_data.media_file_par.frame_count):
                command.append("-frames:v")
                command.append(str(last_frame - first_frame + 1))
        vfilter_list = []
        if (mode == MediaType.VIDEO) and (first_frame > 0 or ((last_frame - first_frame + 1) < imp_media_data.media_file_par.frame_count)):
            vfilter_list.append(f"select = 'between(n, {first_frame}, {last_frame})'")
            # command.append("-vsync")
            # command.append("0")
        scale: int = int(model.item(row, 6).text())
        if(scale < 100):
            original_width = imp_media_data.media_file_par.width
            original_height = imp_media_data.media_file_par.height
            vfilter_list.append(f"scale={trunc(original_width * scale / 100)}:{trunc(original_height * scale / 100)}")
        if vfilter_list:
            command.append("-vf")
            command.append(", ".join(vfilter_list))
        if model.item(row, 7).checkState() == Qt.Unchecked:
            command.append("-loop")
            command.append("-1")
        command.append(model.item(row, 2).text())
        logging.debug(command)
        return command


    def _copy_images_to_temperal(self, row:int) -> tuple:
        """Copy files into temperal directory and
        Return tuple(<input files mask for ffmpeg>, <temperal directory>"""
        logging.debug("in _copy_images_to_temperal")
        model: QStandardItemModel = self._parent._task_list_model
        imglist: list = model.item(row, 1).data(role=Qt.UserRole).imgseq_pathes
        first_element: int = int(model.item(row, 3).text()) - 1
        last_element: int = int(model.item(row, 4).text()) - 1
        export_dir:str = dirname(model.item(row, 2).text())
        temperal_dir:str = export_dir + r"/gif_builder_temp"
        if exists(temperal_dir):
            shutil.rmtree(temperal_dir)
        extention:str = splitext(imglist[first_element])[1]
        img_index:int = 0
        os.makedirs(temperal_dir)
        for img in imglist[first_element: last_element + 1]:
            shutil.copy(img, f"{temperal_dir}/img_{img_index}{extention}", follow_symlinks=True)
            img_index += 1
        self._temperal_dir = temperal_dir
        return (f"{temperal_dir}/img_%d{extention}", temperal_dir)







