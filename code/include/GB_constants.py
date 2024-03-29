import enum

from PySide2.QtCore import QCoreApplication

LOGGING_DISABLED = True

VERSION = "1.3.0"
COMPATIBLE_VERSION_LIST = ["1.2.0a","1.2.0", "1.3.0dev", "1.3.0"]

WIN_DOWNLOAD_BUILDS_URL = [{'title':QCoreApplication.translate("interface", "Windows builds by BtbN"), 'url':"https://github.com/BtbN/FFmpeg-Builds/releases" },
                           {'title':QCoreApplication.translate("interface", "Windows builds from gyan.dev"), 'url':"https://www.gyan.dev/ffmpeg/builds/" },{'title':QCoreApplication.translate("interface", "Open the Official Site"), 'url':"https://ffmpeg.org/download.html" }]

@enum.unique
class Modes (enum.IntEnum):
    FILEPATH = 0
    DIRPATH = 1
    EXEFILE = 2
    SAVE_IMAGE = 3
    SOUND = 4

@enum.unique
class WorkingState (enum.IntEnum):
    EDITING = 0
    PROCESSING = 1
    PROCESSING_FINISHED = 2

URL_SUPPPROJECT = {0:"https://ironmesh.ru/en/other/support-projects", 1:"https://ironmesh.ru/ru/other/support-projects"}
URL_AUTHOR_PAGE = "https://ironmesh.ru/about"
URL_FEEDBACK_EMAIL = "mailto:feedback@ironmesh.ru"
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
LC_DIAL_SELECT_ACTION = QCoreApplication.translate("interface", "Select Action")
LC_FEEDBACK_SUBJECT = QCoreApplication.translate("interface", "Feedback about GIF Builder")
LC_NOTIFICATION = QCoreApplication.translate("interface", "Notification")

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
LC_MSG_FILEISNTFOUND = QCoreApplication.translate("messages", "This file hasn't been found")
LC_MSG_NOTFOUND = QCoreApplication.translate("messages", "not found")
LC_MSG_DELETEALL = QCoreApplication.translate("messages", "All tasks will be deleted. Are you sure?")
LC_MSG_NEWPROJECT = QCoreApplication.translate("messages", "Do you want to create new project? All data will be deleted.")
LC_MSG_URLOPENERROR = QCoreApplication.translate("messages", "Cannot open link: ")
LC_MSG_CLEARALREADY = QCoreApplication.translate("messages", "The project is clear already!")
LC_MSG_EXT_NOT_EQUAL = QCoreApplication.translate("messages", "File formats must be the same")
LC_MSG_EXIT_SAVE_QUESTION = QCoreApplication.translate("messages", "Do you want to save current project before exiting?")
LC_MSG_FFMPEG_PATH_NOT_CORRECT = QCoreApplication.translate("messages", "FFmpeg path is not correct or undefined!")
LC_MSG_FFPROBE_PATH_NOT_CORRECT = QCoreApplication.translate("messages", "FFprobe path is not correct or undefined!")
LC_MSG_SOUND_ISNT_SELECTED = QCoreApplication.translate("messages", "Sound file isn't selected. Go to Setting to select it.")
LC_MSG_SELECT_DIR_FFMPEG_SEARCH = QCoreApplication.translate("messages", "All or some files haven't  been found in the system. Do you want to choose a folder to search?")
LC_INVALID_FILE_TYPE = QCoreApplication.translate("messages", "Invalid file type")
LC_FILTER_SETTINGS_SAVED = QCoreApplication.translate("messages", "Filter setting has been saved")

IMG_EXTENSIONS = LC_IMAGEFILE_FILTER
VIDEO_EXTENSIONS = LC_VIDEOFILE_FILTER

for i in ['(', ')', '*']:
    IMG_EXTENSIONS = IMG_EXTENSIONS.replace(i, '')
    VIDEO_EXTENSIONS = VIDEO_EXTENSIONS.replace(i, '')

VIDEO_EXTENSIONS = VIDEO_EXTENSIONS.split(' ')
IMG_EXTENSIONS = IMG_EXTENSIONS.split(' ')