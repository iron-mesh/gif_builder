import enum

from PySide2.QtCore import QCoreApplication

LOGGING_DISABLED = True

VERSION = "1.1.0"
COMPATIBLE_VERSION_LIST = ["1.0.0", "1.1.0"]

@enum.unique
class Modes (enum.IntEnum):
    FILEPATH = 0
    DIRPATH = 1
    EXEFILE = 2
    SAVE_IMAGE = 3
    SOUND = 4

@enum.unique
class MediaType:
    VIDEO = 0
    IMAGE = 1

@enum.unique
class WorkingState (enum.IntEnum):
    EDITING = 0
    PROCESSING = 1
    PROCESSING_FINISHED = 2

URL_SUPPPROJECT = {0:"https://ironmesh.ru/en/other/support-projects", 1:"https://ironmesh.ru/ru/other/support-projects"}

#translatable stings

#filters for file dialog
LC_IMAGEFILE_FILTER = "(*.png *.jpg *.tif *.bmp *.tga)"
LC_IMAGEFILE_FILTER_TITLE = QCoreApplication.translate("filter", "Images")
LC_EXE_FILTER = "(*.exe)"
LC_EXE_FILTER_TITLE = QCoreApplication.translate("filter", "Application")
LC_VIDEOFILE_FILTER = "(*.mp4 *.avi *.mov)"
LC_VIDEOFILE_FILTER_TITLE = QCoreApplication.translate("filter", "Video")
LC_SAVE_ANIMATION_FILTER = "(*.gif)"
LC_SAVE_ANIMATION_FILTER_TITLE = QCoreApplication.translate("filter", "Animation")
LC_PROJECTFILE_FILTER = "(*.gbp)"
LC_PROJECTFILE_FILTER_TITLE = QCoreApplication.translate("filter", "GIFBuilder Project")
LC_SOUND_FILTER = "(*.wav)"
LC_SOUND_FILTER_TITLE = QCoreApplication.translate("filter", "Sound")

#filedialog titles
LC_SELECT_DIR_TITLE = QCoreApplication.translate("file_dialog", "Select Directory")
LC_SELECT_FILE_TITLE = QCoreApplication.translate("file_dialog", "Select File")
LC_SELECT_EXEC_FILE_TITLE = QCoreApplication.translate("file_dialog", "Select Execution File")
LC_SELECT_IMAGESEQ_FILE_TITLE = QCoreApplication.translate("file_dialog", "Select Image Sequence")
LC_SELECT_VIDEO_FILE_TITLE = QCoreApplication.translate("file_dialog", "Select Video File")
LC_SAVE_ANIMATION_FILE_TITLE = QCoreApplication.translate("file_dialog", "Save Animation")
LC_SAVE_PROJECT_FILE_TITLE = QCoreApplication.translate("file_dialog", "Save Project")
LC_SAVEAS_PROJECT_FILE_TITLE = QCoreApplication.translate("file_dialog", "Save Project As")
LC_OPEN_PROJECT_FILE_TITLE = QCoreApplication.translate("file_dialog", "Open Project")
LC_OPEN_SOUND_TITLE = QCoreApplication.translate("file_dialog", "Select Sound File")



#translatable stings of GUI titles
LC_FRAMERATE = QCoreApplication.translate("interface", "Framerate")
LC_WIDTH = QCoreApplication.translate("interface", "Width")
LC_HEIGHT = QCoreApplication.translate("interface", "Height")
LC_FRAMECOUNT = QCoreApplication.translate("interface", "Frame count")
LC_MEDIATYPE = QCoreApplication.translate("interface", "Media type")
LC_FRAMESIZE = QCoreApplication.translate("interface", "Frame size")
LC_VIDEO = QCoreApplication.translate("interface", "Video")
LC_IMGSEQ = QCoreApplication.translate("interface", "Image Sequence")
LC_IMPORTERR = QCoreApplication.translate("interface", "Importing Error")
LC_EXPORTFILEPATH = QCoreApplication.translate("interface", "Select exporting file")
LC_ADDNEWTASK = QCoreApplication.translate("interface", "Add New Task")
LC_EDITTASK = QCoreApplication.translate("interface", "Edit Task")
LC_ERROR = QCoreApplication.translate("interface", "Error")
LC_CONFIRMATION = QCoreApplication.translate("interface", "Confirmation")
LC_WARNING = QCoreApplication.translate("interface", "Warning!")
LC_STOP = QCoreApplication.translate("interface", "Stop")
LC_BACK = QCoreApplication.translate("interface", "Back")
LC_CONVERT = QCoreApplication.translate("interface", "Convert")
LC_TWQM_EDIT= QCoreApplication.translate("interface", "Edit")
LC_TWQM_DELETE= QCoreApplication.translate("interface", "Delete")
LC_TWQM_DUPLICATE = QCoreApplication.translate("interface", "Duplicate")
LC_TWQM_EXPORTDIR = QCoreApplication.translate("interface", "Export Directory")
LC_TWQM_SOURCEDIR = QCoreApplication.translate("interface", "Source Directory")
LC_TWQM_DEACTIVATEALL = QCoreApplication.translate("interface", "Deactivate All")
LC_TWQM_ACTIVATEALL = QCoreApplication.translate("interface", "Activate All")
LC_TWQM_ACTIVITY = QCoreApplication.translate("interface", "Activity")

#translatable stings of tableview header

LC_HEADERACTIVE = QCoreApplication.translate("interface", "Active")
LC_HEADERSOURCEFILE = QCoreApplication.translate("interface", "Source File")
LC_HEADEREXPORTFILE = QCoreApplication.translate("interface", "Exporting File")
LC_HEADERSTARTFRAME = QCoreApplication.translate("interface", "Start Frame")
LC_HEADERENDFRAME = QCoreApplication.translate("interface", "End Frame")
LC_HEADERFRAMERATE = QCoreApplication.translate("interface", "Framerate")
LC_HEADERSCALE = QCoreApplication.translate("interface", "Scale")
LC_HEADERLOOP = QCoreApplication.translate("interface", "Loop Animation")

#messages
LC_MSG_NOTCOMPITABLE = QCoreApplication.translate("messages", "Version of project file isn't compatible! \n Project was created in version:")
LC_MSG_DELETEALL = QCoreApplication.translate("messages", "All tasks will be deleted. Are you sure?")
LC_MSG_NEWPROJECT = QCoreApplication.translate("messages", "Do you want to create new project?")
LC_MSG_URLOPENERROR = QCoreApplication.translate("messages", "Cannot open link: ")
LC_MSG_EXT_NOT_EQUAL = QCoreApplication.translate("messages", "File formats must be the same")
LC_MSG_EXIT_SAVE_QUESTION = QCoreApplication.translate("messages", "Do you want to save current project?")
LC_MSG_FFMPEG_PATH_NOT_CORRECT = QCoreApplication.translate("messages", "FFmpeg path is not correct or undefined!")
LC_MSG_SOUND_ISNT_SELECTED = QCoreApplication.translate("messages", "Sound file isn't selected. Go to Setting to select it.")