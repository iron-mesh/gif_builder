import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from os.path import *
from .GB_types import *
from .GB_constants import *
from math import *
import subprocess, re, logging, shutil, os

logging.basicConfig(level=logging.DEBUG)
if(LOGGING_DISABLED):
    logging.disable(logging.CRITICAL)


MAX_SCALE = 100
MIN_SCALE = 5
STEP = 5

class TaskHandler(QThread):
    task_changed = Signal(TaskHandlerResponse, bool) #2th arg: True - task started,  False - task finished

    def __init__(self, parent):
        super(TaskHandler, self).__init__(parent)
        self._parent = parent
        self._temperal_dir:str = ""
        self.is_running:bool = True
        self._paused: bool = False
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
            while(self._paused):
                pass
            if not self.is_running: break
            if (model.item(row, 0).checkState() == Qt.Unchecked): continue
            response.model_row = row
            response.current += 1
            logging.debug(">>>>task started>>>>")
            self.task_changed.emit(response, True)

            max_size_mb: float = float(model.item(row, 6).data(Qt.UserRole)) if model.item(row, 6).data(Qt.UserRole) else 0.0
            max_size_bytes: int = int(max_size_mb * 1024 ** 2)
            if (max_size_bytes > 0):
                export_file_path:str = model.item(row, 2).text()
                max_scale:int = MAX_SCALE
                min_scale: int = MIN_SCALE
                cur_scale:int = int(model.item(row, 6).text())
                modif_exp_path:bool = True
                exp_file_list:list = []
                stop_cycle:bool = False
            else:
                modif_exp_path:bool = False

            try:
                if not self._is_valid_task(row):
                    raise UserWarning("task isn't valid").with_traceback()
                cmd_palette, cmd = self._generate_commands(row, modif_exp_path)
                # pass 1 palette creation
                with subprocess.Popen(cmd_palette, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=startupinfo) as pr:
                    data, err = pr.communicate(timeout=600)
                    # logging.debug(f"data: {data}")
                    logging.debug(f"pass 1 error: {err}")
                    if err:
                        raise UserWarning("Palette creation, FFmpeg Error").with_traceback()
                # pass 2 exporting

                while 1:
                    # if cur_scale in [e[2] for e in exp_file_list]: continue
                    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=startupinfo) as pr:
                        data, err = pr.communicate(timeout=600)
                        # logging.debug(f"data: {data}")
                        logging.debug(f"pass 2 error: {err}")
                        if err:
                            raise UserWarning("Gif creation, FFmpeg Error").with_traceback()

                    if(max_size_bytes > 0): #execute if max size defined
                        real_fsize_bytes = os.stat(cmd[-1]).st_size
                        exp_file_list.append([cmd[-1], max_size_bytes - real_fsize_bytes, cur_scale])

                        if (real_fsize_bytes == max_size_bytes) or stop_cycle:
                            break

                        if (real_fsize_bytes > max_size_bytes):
                            if(cur_scale == min_scale):
                                break
                            max_scale = cur_scale
                        elif (real_fsize_bytes < max_size_bytes):
                            if (cur_scale == max_scale):
                                break
                            min_scale = cur_scale

                        if(max_scale - min_scale) > 5:
                            cur_scale = int((max_scale - min_scale) / 2 // 5 * 5) + min_scale
                        elif(real_fsize_bytes < max_size_bytes) and (max_scale - cur_scale == STEP):
                            cur_scale = max_scale
                            stop_cycle = True
                        elif (real_fsize_bytes < max_size_bytes) and (max_scale - cur_scale == STEP):
                            cur_scale = max_scale
                            stop_cycle = True
                        else:
                            break

                        model.item(row, 6).setText(str(cur_scale))
                        cmd = self._generate_commands(row, modif_exp_path)[1]

                    else: #execute if max size NOT defined
                        break

                if (max_size_bytes > 0):
                    logging.debug(f"Exported files: {exp_file_list}")
                    filtered_file_list = list(filter(lambda x: x[1]>=0, exp_file_list))
                    if filtered_file_list:
                        optimal_file = min(filtered_file_list, key=lambda x: x[1])[0]
                    else:
                        optimal_file = min(exp_file_list, key=lambda x: x[2])[0]
                    for el in exp_file_list:
                        if os.path.exists(el[0]):
                            if el[0] == optimal_file:
                                os.replace(optimal_file, export_file_path)
                            else:
                                os.remove(el[0])

                if os.path.exists(cmd_palette[-1]):
                    os.remove(cmd_palette[-1])

            except UserWarning as msg:
                logging.debug(f"Thread message: {msg}")
                response.is_successful = False
            else:
                response.is_successful = True

            response.finished += 1
            response.remain -= 1
            logging.debug(">>>>task finished>>>>")
            self.task_changed.emit(response, False)
            self.set_pause(True)
            if self._temperal_dir and exists(self._temperal_dir):
                shutil.rmtree(self._temperal_dir)


    def _is_valid_task(self, row:int)->bool:
        model: QStandardItemModel = self._parent._task_list_model
        input_path = model.item(row, 1).text()
        export_path = model.item(row, 2).text()
        return (input_path and export_path)


    def _get_imgseq_mask(self, row:int)->tuple:
        """Returns tuple: (<image mask for ffmpeg>, <index of first image>),
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


    def _generate_commands(self, row:int, add_suffix:bool = False)->tuple:
        """Generates commands for ffmpeg ->(<palette creation>, <gif creation>)"""
        model:QStandardItemModel = self._parent._task_list_model
        imp_media_data:ImportedMediaData = model.item(row, 1).data(role=Qt.UserRole)
        mode:int = imp_media_data.media_file_par.type
        first_frame: int = int(model.item(row, 3).text()) - 1
        last_frame: int = int(model.item(row, 4).text()) - 1
        self._palette_path = os.path.dirname(model.item(row, 2).text()) + r"/palette.png"
        command:list[str] = [self._parent.settings.ffmpeg_path, "-y", "-loglevel", "error"]
        command_palette:list[str] = [self._parent.settings.ffmpeg_path, "-y", "-loglevel", "error"]
        if (mode == MediaType.VIDEO):
            command.append("-i"); command_palette.append("-i")
            command.append(imp_media_data.videofile_path); command_palette.append(imp_media_data.videofile_path)
            command.append("-i") #palette
            command.append(self._palette_path)
            # if (first_frame > 0):
            #     command.append("-start_number")
            #     command.append(str(first_frame))
            # if (last_frame - first_frame + 1) < imp_media_data.media_file_par.frame_count:
            #     command.append("-frames:v")
            #     command.append(str(last_frame - first_frame + 1))
            if int(model.item(row, 5).text()) != imp_media_data.media_file_par.framerate: #video framerate
                command.append("-r")
                command.append(model.item(row, 5).text())
        else:
            command.append("-f"); command_palette.append("-f")
            command.append("image2"); command_palette.append("image2")
            command.append("-framerate")
            command.append(model.item(row, 5).text())
            inputfile_mask = self._get_imgseq_mask(row)
            if(inputfile_mask is not None):
                command.append("-start_number"); command_palette.append("-start_number")
                command.append(str(inputfile_mask[1])); command_palette.append(str(inputfile_mask[1]))
                command.append("-i"); command_palette.append("-i")
                command.append(inputfile_mask[0]); command_palette.append(inputfile_mask[0])
            else:
                command.append("-i"); command_palette.append("-i")
                temperal_images_dir:str = self._copy_images_to_temperal(row)[0]
                command.append(temperal_images_dir); command_palette.append(temperal_images_dir)
            command.append("-i")
            command.append(self._palette_path)
            if (inputfile_mask is not None):
                command.append("-frames:v"); command_palette.append("-frames:v")
                frame_count:str = str(last_frame - first_frame + 1)
                command.append(frame_count); command_palette.append(frame_count)
        vfilter_list = []
        if (mode == MediaType.VIDEO) and (first_frame > 0 or ((last_frame - first_frame + 1) < imp_media_data.media_file_par.frame_count)):
            vfilter_list.append(f"select = 'between(n, {first_frame}, {last_frame})'")
        scale: int = int(model.item(row, 6).text())
        if(scale < 100):
            original_width = imp_media_data.media_file_par.width
            original_height = imp_media_data.media_file_par.height
            vfilter_list.append(f"scale={trunc(original_width * scale / 100)}:{trunc(original_height * scale / 100)}:flags=lanczos")
        command_palette.append("-vf")
        logging.debug(self._join_args(vfilter_list, lst_char=', '))
        command_palette.append(self._join_args(vfilter_list, lst_char=', ') + self._get_filter_options(row, mode = "palettegen"))
        command.append("-lavfi")
        command.append(self._join_args(vfilter_list, lst_char=(' 'if scale<100 else ',')) + ("[x];[x][1:v]" if scale<100 else "") + self._get_filter_options(row, mode = "paletteuse"))
        if model.item(row, 7).checkState() == Qt.Unchecked:
            command.append("-loop")
            command.append("-1")

        # command.append("-vsync")
        # command.append("0")
        if add_suffix:
            path, ext = os.path.splitext(model.item(row, 2).text())
            scale = model.item(row, 6).text()
            modified_exp_path = path + '-' + scale + ext
            command.append(modified_exp_path)
        else:
            command.append(model.item(row, 2).text())
        command_palette.append(self._palette_path)

        logging.debug(f"pallete command: {command_palette}")
        logging.debug(f"command: {command}")

        return command_palette, command

    def _join_args(self, arg_list:list, lst_char:str="")->str:
        if arg_list:
            return ", ".join(arg_list) + lst_char
        else:
            return ""

    def _get_filter_options(self, row:int, mode:str):
        model: QStandardItemModel = self._parent._task_list_model
        filter_options:FilterOptions = model.item(row, 2).data(role = Qt.UserRole)
        if mode == "palettegen":
            return f"palettegen=stats_mode={filter_options.stats_mode}"
        elif mode == "paletteuse":
            bayer_scale:str = f":bayer_scale={filter_options.bayer_scale}" if filter_options.dither_mode == 'bayer' else ''
            return f"paletteuse=dither={filter_options.dither_mode}:diff_mode={filter_options.diff_mode}{bayer_scale}"

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

    def set_pause(self, status:bool):
        self._paused = status







