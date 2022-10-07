# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowOpAgkT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ..InputPath.GBInputPath import QInputPath
from ..GB_TableView import GB_TableView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1159, 758)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        MainWindow.setIconSize(QSize(128, 128))
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.new_button = QPushButton(self.centralwidget)
        self.new_button.setObjectName(u"new_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_button.sizePolicy().hasHeightForWidth())
        self.new_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.new_button.setFont(font)
        self.new_button.setToolTipDuration(-1)
        self.new_button.setStyleSheet(u"padding:5px 5px 5px 5px;\n"
"")
        self.new_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.new_button)

        self.open_button = QPushButton(self.centralwidget)
        self.open_button.setObjectName(u"open_button")
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setFont(font)
        self.open_button.setStyleSheet(u"padding:5px 5px 5px 5px;")
        self.open_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.open_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet(u"padding:5px 5px 5px 5px;")
        self.save_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.save_button)

        self.saveAs_button = QPushButton(self.centralwidget)
        self.saveAs_button.setObjectName(u"saveAs_button")
        sizePolicy.setHeightForWidth(self.saveAs_button.sizePolicy().hasHeightForWidth())
        self.saveAs_button.setSizePolicy(sizePolicy)
        self.saveAs_button.setFont(font)
        self.saveAs_button.setStyleSheet(u"padding:5px 5px 5px 5px;")
        self.saveAs_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.saveAs_button)

        self.verticalSpacer = QSpacerItem(13, 47, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.close_settings_button = QPushButton(self.centralwidget)
        self.close_settings_button.setObjectName(u"close_settings_button")
        sizePolicy.setHeightForWidth(self.close_settings_button.sizePolicy().hasHeightForWidth())
        self.close_settings_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.close_settings_button.setFont(font1)
#if QT_CONFIG(accessibility)
        self.close_settings_button.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.close_settings_button.setStyleSheet(u"color:white;\n"
"background-color: red")
        self.close_settings_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.close_settings_button.setText(u"\u00d7")

        self.verticalLayout.addWidget(self.close_settings_button)

        self.settings_button = QPushButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(u"padding:5px 5px 5px 5px;")
        self.settings_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.verticalLayout.addWidget(self.settings_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.tasks_page = QWidget()
        self.tasks_page.setObjectName(u"tasks_page")
        self.tasks_page.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.verticalLayout_4 = QVBoxLayout(self.tasks_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.status_stack = QStackedWidget(self.tasks_page)
        self.status_stack.setObjectName(u"status_stack")
        self.status_stack.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.status_stack.sizePolicy().hasHeightForWidth())
        self.status_stack.setSizePolicy(sizePolicy2)
        self.status_stack.setMinimumSize(QSize(0, 0))
        self.status_stack.setLayoutDirection(Qt.LeftToRight)
        self.status_stack.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.status_stack.setFrameShape(QFrame.NoFrame)
        self.status_stack.setFrameShadow(QFrame.Plain)
        self.status_stack.setLineWidth(0)
        self.converting_page = QWidget()
        self.converting_page.setObjectName(u"converting_page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.converting_page.sizePolicy().hasHeightForWidth())
        self.converting_page.setSizePolicy(sizePolicy3)
        self.verticalLayout_7 = QVBoxLayout(self.converting_page)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 3)
        self.convert_status_label_2 = QLabel(self.converting_page)
        self.convert_status_label_2.setObjectName(u"convert_status_label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.convert_status_label_2.sizePolicy().hasHeightForWidth())
        self.convert_status_label_2.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamily(u"Lucida Console")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.convert_status_label_2.setFont(font2)
        self.convert_status_label_2.setLayoutDirection(Qt.LeftToRight)
        self.convert_status_label_2.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.convert_status_label_2.setMargin(0)

        self.verticalLayout_7.addWidget(self.convert_status_label_2)

        self.line_4 = QFrame(self.converting_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.remain_task_label = QLabel(self.converting_page)
        self.remain_task_label.setObjectName(u"remain_task_label")
        sizePolicy4.setHeightForWidth(self.remain_task_label.sizePolicy().hasHeightForWidth())
        self.remain_task_label.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily(u"Lucida Console")
        font3.setPointSize(12)
        self.remain_task_label.setFont(font3)
        self.remain_task_label.setLayoutDirection(Qt.LeftToRight)
        self.remain_task_label.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.remain_task_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.remain_task_label.setMargin(0)

        self.gridLayout_2.addWidget(self.remain_task_label, 0, 2, 1, 1)

        self.remain_tasks_lcd = QLCDNumber(self.converting_page)
        self.remain_tasks_lcd.setObjectName(u"remain_tasks_lcd")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.remain_tasks_lcd.sizePolicy().hasHeightForWidth())
        self.remain_tasks_lcd.setSizePolicy(sizePolicy5)
        self.remain_tasks_lcd.setMinimumSize(QSize(90, 35))
        font4 = QFont()
        font4.setFamily(u"MS UI Gothic")
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setWeight(50)
        self.remain_tasks_lcd.setFont(font4)
        self.remain_tasks_lcd.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(accessibility)
        self.remain_tasks_lcd.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.remain_tasks_lcd.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.remain_tasks_lcd.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.remain_tasks_lcd.setFrameShape(QFrame.Box)
        self.remain_tasks_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.remain_tasks_lcd.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.remain_tasks_lcd, 1, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(17, 27, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.finished_tasks_lcd = QLCDNumber(self.converting_page)
        self.finished_tasks_lcd.setObjectName(u"finished_tasks_lcd")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.finished_tasks_lcd.sizePolicy().hasHeightForWidth())
        self.finished_tasks_lcd.setSizePolicy(sizePolicy6)
        self.finished_tasks_lcd.setMinimumSize(QSize(90, 35))
        self.finished_tasks_lcd.setFont(font4)
        self.finished_tasks_lcd.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(accessibility)
        self.finished_tasks_lcd.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.finished_tasks_lcd.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.finished_tasks_lcd.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.finished_tasks_lcd.setFrameShape(QFrame.Box)
        self.finished_tasks_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.finished_tasks_lcd.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.finished_tasks_lcd, 1, 4, 1, 1)

        self.current_task_lcd = QLCDNumber(self.converting_page)
        self.current_task_lcd.setObjectName(u"current_task_lcd")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.current_task_lcd.sizePolicy().hasHeightForWidth())
        self.current_task_lcd.setSizePolicy(sizePolicy7)
        self.current_task_lcd.setMinimumSize(QSize(90, 35))
        self.current_task_lcd.setFont(font4)
        self.current_task_lcd.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(accessibility)
        self.current_task_lcd.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.current_task_lcd.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.current_task_lcd.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.current_task_lcd.setFrameShape(QFrame.Box)
        self.current_task_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.current_task_lcd.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.current_task_lcd, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(17, 27, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.finished_task_label = QLabel(self.converting_page)
        self.finished_task_label.setObjectName(u"finished_task_label")
        sizePolicy4.setHeightForWidth(self.finished_task_label.sizePolicy().hasHeightForWidth())
        self.finished_task_label.setSizePolicy(sizePolicy4)
        self.finished_task_label.setFont(font3)
        self.finished_task_label.setLayoutDirection(Qt.LeftToRight)
        self.finished_task_label.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.finished_task_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.finished_task_label.setMargin(0)

        self.gridLayout_2.addWidget(self.finished_task_label, 0, 4, 1, 1)

        self.current_task_label = QLabel(self.converting_page)
        self.current_task_label.setObjectName(u"current_task_label")
        self.current_task_label.setFont(font3)
        self.current_task_label.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.current_task_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.current_task_label, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.progressBar = QProgressBar(self.converting_page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.progressBar.setFont(font5)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.progressBar.setValue(91)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.progressBar.setFormat(u"current_task")

        self.verticalLayout_7.addWidget(self.progressBar)

        self.status_stack.addWidget(self.converting_page)
        self.tasks_page1 = QWidget()
        self.tasks_page1.setObjectName(u"tasks_page1")
        sizePolicy7.setHeightForWidth(self.tasks_page1.sizePolicy().hasHeightForWidth())
        self.tasks_page1.setSizePolicy(sizePolicy7)
        self.tasks_page1.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout_6 = QVBoxLayout(self.tasks_page1)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 5, -1, 3)
        self.tasks_status_label = QLabel(self.tasks_page1)
        self.tasks_status_label.setObjectName(u"tasks_status_label")
        sizePolicy7.setHeightForWidth(self.tasks_status_label.sizePolicy().hasHeightForWidth())
        self.tasks_status_label.setSizePolicy(sizePolicy7)
        font6 = QFont()
        font6.setFamily(u"Lucida Console")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        font6.setKerning(True)
        self.tasks_status_label.setFont(font6)
        self.tasks_status_label.setLayoutDirection(Qt.LeftToRight)
        self.tasks_status_label.setMargin(0)

        self.verticalLayout_6.addWidget(self.tasks_status_label)

        self.line_3 = QFrame(self.tasks_page1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(1)
        self.active_tasks_lcd = QLCDNumber(self.tasks_page1)
        self.active_tasks_lcd.setObjectName(u"active_tasks_lcd")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.active_tasks_lcd.sizePolicy().hasHeightForWidth())
        self.active_tasks_lcd.setSizePolicy(sizePolicy8)
        self.active_tasks_lcd.setMinimumSize(QSize(90, 35))
        font7 = QFont()
        font7.setFamily(u"MS UI Gothic")
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setWeight(50)
        self.active_tasks_lcd.setFont(font7)
#if QT_CONFIG(accessibility)
        self.active_tasks_lcd.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.active_tasks_lcd.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.active_tasks_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.active_tasks_lcd.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.active_tasks_lcd, 1, 0, 1, 1)

        self.totally_tasks_lcd = QLCDNumber(self.tasks_page1)
        self.totally_tasks_lcd.setObjectName(u"totally_tasks_lcd")
        sizePolicy5.setHeightForWidth(self.totally_tasks_lcd.sizePolicy().hasHeightForWidth())
        self.totally_tasks_lcd.setSizePolicy(sizePolicy5)
        self.totally_tasks_lcd.setMinimumSize(QSize(90, 35))
        self.totally_tasks_lcd.setFont(font4)
        self.totally_tasks_lcd.setCursor(QCursor(Qt.ArrowCursor))
#if QT_CONFIG(accessibility)
        self.totally_tasks_lcd.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.totally_tasks_lcd.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.totally_tasks_lcd.setFrameShape(QFrame.Box)
        self.totally_tasks_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.totally_tasks_lcd.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.totally_tasks_lcd, 1, 2, 1, 1)

        self.active_tasks_label = QLabel(self.tasks_page1)
        self.active_tasks_label.setObjectName(u"active_tasks_label")
        sizePolicy3.setHeightForWidth(self.active_tasks_label.sizePolicy().hasHeightForWidth())
        self.active_tasks_label.setSizePolicy(sizePolicy3)
        font8 = QFont()
        font8.setFamily(u"Lucida Console")
        font8.setPointSize(12)
        font8.setKerning(True)
        self.active_tasks_label.setFont(font8)
        self.active_tasks_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.active_tasks_label, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(17, 27, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.totally_tasks_label = QLabel(self.tasks_page1)
        self.totally_tasks_label.setObjectName(u"totally_tasks_label")
        sizePolicy3.setHeightForWidth(self.totally_tasks_label.sizePolicy().hasHeightForWidth())
        self.totally_tasks_label.setSizePolicy(sizePolicy3)
        self.totally_tasks_label.setFont(font8)
        self.totally_tasks_label.setLayoutDirection(Qt.LeftToRight)
        self.totally_tasks_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totally_tasks_label.setMargin(0)

        self.gridLayout.addWidget(self.totally_tasks_label, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(438, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.status_stack.addWidget(self.tasks_page1)

        self.verticalLayout_4.addWidget(self.status_stack)

        self.tableView = GB_TableView(self.tasks_page)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy9)
        self.tableView.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableView.setLayoutDirection(Qt.LeftToRight)
        self.tableView.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.tableView.setShowGrid(False)

        self.verticalLayout_4.addWidget(self.tableView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.moveup_button = QPushButton(self.tasks_page)
        self.moveup_button.setObjectName(u"moveup_button")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.moveup_button.sizePolicy().hasHeightForWidth())
        self.moveup_button.setSizePolicy(sizePolicy10)
        self.moveup_button.setMinimumSize(QSize(0, 0))
        font9 = QFont()
        font9.setPointSize(10)
        self.moveup_button.setFont(font9)
        self.moveup_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout_5.addWidget(self.moveup_button)

        self.movedown_button = QPushButton(self.tasks_page)
        self.movedown_button.setObjectName(u"movedown_button")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.movedown_button.sizePolicy().hasHeightForWidth())
        self.movedown_button.setSizePolicy(sizePolicy11)
        self.movedown_button.setFont(font9)
        self.movedown_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout_5.addWidget(self.movedown_button)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.add_item_button = QPushButton(self.tasks_page)
        self.add_item_button.setObjectName(u"add_item_button")
        sizePolicy11.setHeightForWidth(self.add_item_button.sizePolicy().hasHeightForWidth())
        self.add_item_button.setSizePolicy(sizePolicy11)
        self.add_item_button.setFont(font9)
        self.add_item_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout_5.addWidget(self.add_item_button)

        self.edit_item_button = QPushButton(self.tasks_page)
        self.edit_item_button.setObjectName(u"edit_item_button")
        sizePolicy11.setHeightForWidth(self.edit_item_button.sizePolicy().hasHeightForWidth())
        self.edit_item_button.setSizePolicy(sizePolicy11)
        self.edit_item_button.setFont(font9)
        self.edit_item_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout_5.addWidget(self.edit_item_button)

        self.delete_item_button = QPushButton(self.tasks_page)
        self.delete_item_button.setObjectName(u"delete_item_button")
        sizePolicy11.setHeightForWidth(self.delete_item_button.sizePolicy().hasHeightForWidth())
        self.delete_item_button.setSizePolicy(sizePolicy11)
        self.delete_item_button.setFont(font9)
        self.delete_item_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout_5.addWidget(self.delete_item_button)

        self.deleteall_item_button = QPushButton(self.tasks_page)
        self.deleteall_item_button.setObjectName(u"deleteall_item_button")
        sizePolicy11.setHeightForWidth(self.deleteall_item_button.sizePolicy().hasHeightForWidth())
        self.deleteall_item_button.setSizePolicy(sizePolicy11)
        self.deleteall_item_button.setFont(font9)
        self.deleteall_item_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout_5.addWidget(self.deleteall_item_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.line_6 = QFrame(self.tasks_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.soound_alert_checkBox = QCheckBox(self.tasks_page)
        self.soound_alert_checkBox.setObjectName(u"soound_alert_checkBox")
        sizePolicy10.setHeightForWidth(self.soound_alert_checkBox.sizePolicy().hasHeightForWidth())
        self.soound_alert_checkBox.setSizePolicy(sizePolicy10)
        self.soound_alert_checkBox.setFont(font9)
        self.soound_alert_checkBox.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout.addWidget(self.soound_alert_checkBox)

        self.win_notification_checkBox = QCheckBox(self.tasks_page)
        self.win_notification_checkBox.setObjectName(u"win_notification_checkBox")
        sizePolicy10.setHeightForWidth(self.win_notification_checkBox.sizePolicy().hasHeightForWidth())
        self.win_notification_checkBox.setSizePolicy(sizePolicy10)
        self.win_notification_checkBox.setFont(font9)
        self.win_notification_checkBox.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.win_notification_checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.win_notification_checkBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.after_convert_label = QLabel(self.tasks_page)
        self.after_convert_label.setObjectName(u"after_convert_label")
        sizePolicy12 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.after_convert_label.sizePolicy().hasHeightForWidth())
        self.after_convert_label.setSizePolicy(sizePolicy12)
        self.after_convert_label.setFont(font9)
        self.after_convert_label.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout.addWidget(self.after_convert_label)

        self.after_converting_combobox = QComboBox(self.tasks_page)
        self.after_converting_combobox.addItem("")
        self.after_converting_combobox.addItem("")
        self.after_converting_combobox.addItem("")
        self.after_converting_combobox.setObjectName(u"after_converting_combobox")
        sizePolicy10.setHeightForWidth(self.after_converting_combobox.sizePolicy().hasHeightForWidth())
        self.after_converting_combobox.setSizePolicy(sizePolicy10)
        self.after_converting_combobox.setMinimumSize(QSize(120, 0))
        self.after_converting_combobox.setFont(font9)
        self.after_converting_combobox.setLayoutDirection(Qt.LeftToRight)
        self.after_converting_combobox.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))

        self.horizontalLayout.addWidget(self.after_converting_combobox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.start_button = QPushButton(self.tasks_page)
        self.start_button.setObjectName(u"start_button")
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QSize(180, 30))
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        font10.setStrikeOut(False)
        self.start_button.setFont(font10)
        self.start_button.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.start_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.start_button.setFlat(False)

        self.horizontalLayout.addWidget(self.start_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.tasks_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.horizontalLayout_4 = QHBoxLayout(self.setting_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.settings_scrollArea = QScrollArea(self.setting_page)
        self.settings_scrollArea.setObjectName(u"settings_scrollArea")
        self.settings_scrollArea.setStyleSheet(u"")
        self.settings_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1027, 665))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cb_language = QComboBox(self.scrollAreaWidgetContents)
        self.cb_language.addItem("")
        self.cb_language.addItem("")
        self.cb_language.setObjectName(u"cb_language")
        sizePolicy10.setHeightForWidth(self.cb_language.sizePolicy().hasHeightForWidth())
        self.cb_language.setSizePolicy(sizePolicy10)
        self.cb_language.setFont(font)
#if QT_CONFIG(accessibility)
        self.cb_language.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.cb_language.setCurrentText(u"English")
        self.cb_language.setPlaceholderText(u"")

        self.horizontalLayout_8.addWidget(self.cb_language)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.manual_button = QPushButton(self.scrollAreaWidgetContents)
        self.manual_button.setObjectName(u"manual_button")
        font11 = QFont()
        font11.setPointSize(11)
        self.manual_button.setFont(font11)
        self.manual_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.manual_button.setStyleSheet(u"QPushButton { color:rgb(85, 0, 255)}\n"
"\n"
":hover{\n"
"		color:blue;\n"
"		text-decoration: underline;\n"
"}")
        self.manual_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.manual_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.manual_button)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.inputpath_ffmpeg = QInputPath(self.scrollAreaWidgetContents)
        self.inputpath_ffmpeg.setObjectName(u"inputpath_ffmpeg")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.inputpath_ffmpeg.sizePolicy().hasHeightForWidth())
        self.inputpath_ffmpeg.setSizePolicy(sizePolicy13)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputpath_ffmpeg)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.inputpath_ffprobe = QInputPath(self.scrollAreaWidgetContents)
        self.inputpath_ffprobe.setObjectName(u"inputpath_ffprobe")
        sizePolicy13.setHeightForWidth(self.inputpath_ffprobe.sizePolicy().hasHeightForWidth())
        self.inputpath_ffprobe.setSizePolicy(sizePolicy13)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputpath_ffprobe)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.inputpath_export_dir = QInputPath(self.scrollAreaWidgetContents)
        self.inputpath_export_dir.setObjectName(u"inputpath_export_dir")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inputpath_export_dir)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.inputpath_sound = QInputPath(self.scrollAreaWidgetContents)
        self.inputpath_sound.setObjectName(u"inputpath_sound")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inputpath_sound)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.sb_default_framerate = QSpinBox(self.scrollAreaWidgetContents)
        self.sb_default_framerate.setObjectName(u"sb_default_framerate")
        sizePolicy10.setHeightForWidth(self.sb_default_framerate.sizePolicy().hasHeightForWidth())
        self.sb_default_framerate.setSizePolicy(sizePolicy10)
        self.sb_default_framerate.setMinimumSize(QSize(60, 0))
        self.sb_default_framerate.setFont(font)
#if QT_CONFIG(accessibility)
        self.sb_default_framerate.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.sb_default_framerate.setMinimum(1)
        self.sb_default_framerate.setMaximum(1000)
        self.sb_default_framerate.setValue(24)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.sb_default_framerate)

        self.ffmep_utilities_layout = QHBoxLayout()
        self.ffmep_utilities_layout.setObjectName(u"ffmep_utilities_layout")
        self.find_ffmpeg_exe_button = QPushButton(self.scrollAreaWidgetContents)
        self.find_ffmpeg_exe_button.setObjectName(u"find_ffmpeg_exe_button")
        sizePolicy.setHeightForWidth(self.find_ffmpeg_exe_button.sizePolicy().hasHeightForWidth())
        self.find_ffmpeg_exe_button.setSizePolicy(sizePolicy)
        self.find_ffmpeg_exe_button.setFont(font11)
        self.find_ffmpeg_exe_button.setStyleSheet(u"padding:5px 15px 5px 15px;\n"
"")

        self.ffmep_utilities_layout.addWidget(self.find_ffmpeg_exe_button)

        self.dwnld_build_button = QPushButton(self.scrollAreaWidgetContents)
        self.dwnld_build_button.setObjectName(u"dwnld_build_button")
        self.dwnld_build_button.setFont(font11)
        self.dwnld_build_button.setStyleSheet(u"padding:5px 15px 5px 15px;\n"
"\n"
"")

        self.ffmep_utilities_layout.addWidget(self.dwnld_build_button)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.ffmep_utilities_layout.addItem(self.horizontalSpacer_14)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.ffmep_utilities_layout)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)


        self.verticalLayout_8.addLayout(self.formLayout)

        self.settings_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.settings_scrollArea)

        self.stackedWidget.addWidget(self.setting_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 7, -1, -1)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.author_btn = QPushButton(self.centralwidget)
        self.author_btn.setObjectName(u"author_btn")
        self.author_btn.setFont(font11)
        self.author_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.author_btn.setStyleSheet(u"QPushButton { color:rgb(85, 0, 255)}\n"
"\n"
":hover{\n"
"		color:blue;\n"
"		text-decoration: underline;\n"
"}")
        self.author_btn.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.author_btn.setText(u"By Balakirev Ivan")
#if QT_CONFIG(shortcut)
        self.author_btn.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.author_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.author_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.feedback_button = QPushButton(self.centralwidget)
        self.feedback_button.setObjectName(u"feedback_button")
        self.feedback_button.setFont(font11)
        self.feedback_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.feedback_button.setStyleSheet(u"QPushButton { color:rgb(85, 0, 255)}\n"
"\n"
":hover{\n"
"		color:blue;\n"
"		text-decoration: underline;\n"
"}")
        self.feedback_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.feedback_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.feedback_button)

        self.horizontalSpacer_13 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.support_button = QPushButton(self.centralwidget)
        self.support_button.setObjectName(u"support_button")
        self.support_button.setFont(font11)
        self.support_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.support_button.setStyleSheet(u"QPushButton { color:rgb(85, 0, 255)}\n"
"\n"
":hover{\n"
"		color:blue;\n"
"		text-decoration: underline;\n"
"}")
        self.support_button.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.support_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.support_button)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.version_label = QLabel(self.centralwidget)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setFont(font9)
#if QT_CONFIG(tooltip)
        self.version_label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.version_label.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.version_label.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.version_label.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.version_label.setStyleSheet(u"color: rgb(182, 182, 182);")
        self.version_label.setTextFormat(Qt.PlainText)

        self.horizontalLayout_3.addWidget(self.version_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.new_button, self.open_button)
        QWidget.setTabOrder(self.open_button, self.save_button)
        QWidget.setTabOrder(self.save_button, self.saveAs_button)
        QWidget.setTabOrder(self.saveAs_button, self.close_settings_button)
        QWidget.setTabOrder(self.close_settings_button, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.tableView)
        QWidget.setTabOrder(self.tableView, self.moveup_button)
        QWidget.setTabOrder(self.moveup_button, self.movedown_button)
        QWidget.setTabOrder(self.movedown_button, self.add_item_button)
        QWidget.setTabOrder(self.add_item_button, self.edit_item_button)
        QWidget.setTabOrder(self.edit_item_button, self.delete_item_button)
        QWidget.setTabOrder(self.delete_item_button, self.deleteall_item_button)
        QWidget.setTabOrder(self.deleteall_item_button, self.soound_alert_checkBox)
        QWidget.setTabOrder(self.soound_alert_checkBox, self.win_notification_checkBox)
        QWidget.setTabOrder(self.win_notification_checkBox, self.after_converting_combobox)
        QWidget.setTabOrder(self.after_converting_combobox, self.start_button)
        QWidget.setTabOrder(self.start_button, self.sb_default_framerate)
        QWidget.setTabOrder(self.sb_default_framerate, self.settings_scrollArea)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.status_stack.setCurrentIndex(1)
        self.cb_language.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GIF Builder", None))
#if QT_CONFIG(tooltip)
        self.new_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Create new project</p><p><span style=\" font-weight:600;\">Ctrl+N</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.new_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.new_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.new_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.new_button.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.new_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.open_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Open existing project</p><p><span style=\" font-weight:600;\">Ctrl+O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.open_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.save_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Save current project</p><p><span style=\" font-weight:600;\">Ctrl+S</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.save_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.saveAs_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Save As current project</p><p><span style=\" font-weight:600;\">Ctrl+Shift+S</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saveAs_button.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(shortcut)
        self.saveAs_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.close_settings_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.close_settings_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.settings_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Open settings</p><p><span style=\" font-weight:600;\">Ctrl+Alt+S</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.settings_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.convert_status_label_2.setText(QCoreApplication.translate("MainWindow", u"Converting status", None))
        self.remain_task_label.setText(QCoreApplication.translate("MainWindow", u"Remain", None))
        self.finished_task_label.setText(QCoreApplication.translate("MainWindow", u"Finished", None))
        self.current_task_label.setText(QCoreApplication.translate("MainWindow", u"Current", None))
        self.tasks_status_label.setText(QCoreApplication.translate("MainWindow", u"Tasks status", None))
        self.active_tasks_label.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.totally_tasks_label.setText(QCoreApplication.translate("MainWindow", u"Totally", None))
#if QT_CONFIG(statustip)
        self.tableView.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.moveup_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Move up selected element</p><p><span style=\" font-weight:600;\">PageUp</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.moveup_button.setText(QCoreApplication.translate("MainWindow", u"\u02c4", None))
#if QT_CONFIG(shortcut)
        self.moveup_button.setShortcut(QCoreApplication.translate("MainWindow", u"PgUp", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.movedown_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Move down selected element</p><p><span style=\" font-weight:600;\">PageDown</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.movedown_button.setText(QCoreApplication.translate("MainWindow", u"\u02c5", None))
#if QT_CONFIG(shortcut)
        self.movedown_button.setShortcut(QCoreApplication.translate("MainWindow", u"PgDown", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.add_item_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Add task</p><p><span style=\" font-weight:600;\">Ctrl+I</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_item_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(shortcut)
        self.add_item_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.edit_item_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Edit selected task</p><p><span style=\" font-weight:600;\">Ctrl+E</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.edit_item_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(shortcut)
        self.edit_item_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.delete_item_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Delete selected task</p><p><span style=\" font-weight:600;\">Del</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_item_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(shortcut)
        self.delete_item_button.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.deleteall_item_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Delete all tasks</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deleteall_item_button.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
#if QT_CONFIG(shortcut)
        self.deleteall_item_button.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.soound_alert_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sound alert after converting</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.soound_alert_checkBox.setText(QCoreApplication.translate("MainWindow", u"Sound Alert", None))
#if QT_CONFIG(tooltip)
        self.win_notification_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Send Windows notification after converting</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.win_notification_checkBox.setText(QCoreApplication.translate("MainWindow", u" Windows Notification", None))
        self.after_convert_label.setText(QCoreApplication.translate("MainWindow", u"After converting:", None))
        self.after_converting_combobox.setItemText(0, "")
        self.after_converting_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Power Off", None))
        self.after_converting_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Restart", None))

#if QT_CONFIG(tooltip)
        self.start_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Start converting</p><p><span style=\" font-weight:600;\">Ctrl+R</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
#if QT_CONFIG(shortcut)
        self.start_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.cb_language.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.cb_language.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))

#if QT_CONFIG(tooltip)
        self.manual_button.setToolTip(QCoreApplication.translate("MainWindow", u"Do you need help?", None))
#endif // QT_CONFIG(tooltip)
        self.manual_button.setText(QCoreApplication.translate("MainWindow", u"User Manual", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FFmpeg path", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"FFprobe path", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Default export directory", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sound Alert", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Default framerate", None))
#if QT_CONFIG(tooltip)
        self.find_ffmpeg_exe_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Try to find FFmpeg files</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.find_ffmpeg_exe_button.setText(QCoreApplication.translate("MainWindow", u"Find FFmpeg Files", None))
#if QT_CONFIG(tooltip)
        self.dwnld_build_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select a link to website to download FFmpeg builds </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dwnld_build_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"FFmpeg", None))
        self.feedback_button.setText(QCoreApplication.translate("MainWindow", u"Send Feedback", None))
        self.support_button.setText(QCoreApplication.translate("MainWindow", u"Support this Project", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"v 1.0.0", None))
    # retranslateUi

