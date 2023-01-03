# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_edit_taskTcqHrh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ..InputPath.GBInputPath import QInputPath
from ..InputPath.GBInputSourceFilePathes import QInputSourceFilePathes


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(475, 698)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.isfp_import_media = QInputSourceFilePathes(Dialog)
        self.isfp_import_media.setObjectName(u"isfp_import_media")
        self.isfp_import_media.setMinimumSize(QSize(439, 74))

        self.verticalLayout.addWidget(self.isfp_import_media)

        self.ip_export_file = QInputPath(Dialog)
        self.ip_export_file.setObjectName(u"ip_export_file")

        self.verticalLayout.addWidget(self.ip_export_file)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_framerate = QLabel(Dialog)
        self.lb_framerate.setObjectName(u"lb_framerate")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_framerate.sizePolicy().hasHeightForWidth())
        self.lb_framerate.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.lb_framerate.setFont(font)
        self.lb_framerate.setLayoutDirection(Qt.LeftToRight)
        self.lb_framerate.setFrameShape(QFrame.NoFrame)
        self.lb_framerate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_framerate, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.sb_framerate = QSpinBox(Dialog)
        self.sb_framerate.setObjectName(u"sb_framerate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sb_framerate.sizePolicy().hasHeightForWidth())
        self.sb_framerate.setSizePolicy(sizePolicy1)
        self.sb_framerate.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setPointSize(11)
        self.sb_framerate.setFont(font1)
        self.sb_framerate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_framerate.setMinimum(1)
        self.sb_framerate.setMaximum(1000)

        self.gridLayout.addWidget(self.sb_framerate, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.sb_scale = QSpinBox(Dialog)
        self.sb_scale.setObjectName(u"sb_scale")
        sizePolicy1.setHeightForWidth(self.sb_scale.sizePolicy().hasHeightForWidth())
        self.sb_scale.setSizePolicy(sizePolicy1)
        self.sb_scale.setMinimumSize(QSize(100, 0))
        self.sb_scale.setFont(font1)
        self.sb_scale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_scale.setMinimum(5)
        self.sb_scale.setMaximum(100)
        self.sb_scale.setSingleStep(5)
        self.sb_scale.setValue(100)

        self.gridLayout.addWidget(self.sb_scale, 1, 2, 1, 1)

        self.lb_scale = QLabel(Dialog)
        self.lb_scale.setObjectName(u"lb_scale")
        sizePolicy.setHeightForWidth(self.lb_scale.sizePolicy().hasHeightForWidth())
        self.lb_scale.setSizePolicy(sizePolicy)
        self.lb_scale.setFont(font)
        self.lb_scale.setLayoutDirection(Qt.LeftToRight)
        self.lb_scale.setAutoFillBackground(False)
        self.lb_scale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_scale, 1, 0, 1, 1)

        self.lb_max_size_mb = QLabel(Dialog)
        self.lb_max_size_mb.setObjectName(u"lb_max_size_mb")
        sizePolicy.setHeightForWidth(self.lb_max_size_mb.sizePolicy().hasHeightForWidth())
        self.lb_max_size_mb.setSizePolicy(sizePolicy)
        self.lb_max_size_mb.setFont(font)
        self.lb_max_size_mb.setLayoutDirection(Qt.LeftToRight)
        self.lb_max_size_mb.setAutoFillBackground(False)
        self.lb_max_size_mb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_max_size_mb, 2, 0, 1, 1)

        self.max_size_dspinBox = QDoubleSpinBox(Dialog)
        self.max_size_dspinBox.setObjectName(u"max_size_dspinBox")
        self.max_size_dspinBox.setFont(font1)
        self.max_size_dspinBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.max_size_dspinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.max_size_dspinBox.setMaximum(99999999.989999994635582)
        self.max_size_dspinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.max_size_dspinBox, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.cb_loopanimation = QCheckBox(Dialog)
        self.cb_loopanimation.setObjectName(u"cb_loopanimation")
        self.cb_loopanimation.setFont(font)

        self.verticalLayout.addWidget(self.cb_loopanimation)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cb_dither_mode = QComboBox(Dialog)
        self.cb_dither_mode.addItem(u"bayer")
        self.cb_dither_mode.addItem(u"heckbert")
        self.cb_dither_mode.addItem(u"floyd_steinberg")
        self.cb_dither_mode.addItem(u"sierra2")
        self.cb_dither_mode.addItem(u"sierra2_4a")
        self.cb_dither_mode.setObjectName(u"cb_dither_mode")
        sizePolicy1.setHeightForWidth(self.cb_dither_mode.sizePolicy().hasHeightForWidth())
        self.cb_dither_mode.setSizePolicy(sizePolicy1)
        self.cb_dither_mode.setFont(font1)
        self.cb_dither_mode.setCurrentText(u"sierra2_4a")

        self.gridLayout_2.addWidget(self.cb_dither_mode, 1, 2, 1, 1)

        self.lb_framerate_2 = QLabel(Dialog)
        self.lb_framerate_2.setObjectName(u"lb_framerate_2")
        sizePolicy.setHeightForWidth(self.lb_framerate_2.sizePolicy().hasHeightForWidth())
        self.lb_framerate_2.setSizePolicy(sizePolicy)
        self.lb_framerate_2.setFont(font)
        self.lb_framerate_2.setLayoutDirection(Qt.LeftToRight)
        self.lb_framerate_2.setFrameShape(QFrame.NoFrame)
        self.lb_framerate_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_framerate_2, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.lb_framerate_3 = QLabel(Dialog)
        self.lb_framerate_3.setObjectName(u"lb_framerate_3")
        sizePolicy.setHeightForWidth(self.lb_framerate_3.sizePolicy().hasHeightForWidth())
        self.lb_framerate_3.setSizePolicy(sizePolicy)
        self.lb_framerate_3.setFont(font)
        self.lb_framerate_3.setLayoutDirection(Qt.LeftToRight)
        self.lb_framerate_3.setFrameShape(QFrame.NoFrame)
        self.lb_framerate_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_framerate_3, 1, 0, 1, 1)

        self.cb_diff_mode = QComboBox(Dialog)
        self.cb_diff_mode.addItem(u"none")
        self.cb_diff_mode.addItem(u"rectangle")
        self.cb_diff_mode.setObjectName(u"cb_diff_mode")
        sizePolicy1.setHeightForWidth(self.cb_diff_mode.sizePolicy().hasHeightForWidth())
        self.cb_diff_mode.setSizePolicy(sizePolicy1)
        self.cb_diff_mode.setFont(font1)
        self.cb_diff_mode.setCurrentText(u"none")

        self.gridLayout_2.addWidget(self.cb_diff_mode, 3, 2, 1, 1)

        self.lb_framerate_4 = QLabel(Dialog)
        self.lb_framerate_4.setObjectName(u"lb_framerate_4")
        sizePolicy.setHeightForWidth(self.lb_framerate_4.sizePolicy().hasHeightForWidth())
        self.lb_framerate_4.setSizePolicy(sizePolicy)
        self.lb_framerate_4.setFont(font)
        self.lb_framerate_4.setLayoutDirection(Qt.LeftToRight)
        self.lb_framerate_4.setFrameShape(QFrame.NoFrame)
        self.lb_framerate_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_framerate_4, 3, 0, 1, 1)

        self.sb_bayer_scale = QSpinBox(Dialog)
        self.sb_bayer_scale.setObjectName(u"sb_bayer_scale")
        self.sb_bayer_scale.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.sb_bayer_scale.sizePolicy().hasHeightForWidth())
        self.sb_bayer_scale.setSizePolicy(sizePolicy1)
        self.sb_bayer_scale.setMinimumSize(QSize(50, 0))
        self.sb_bayer_scale.setFont(font1)
        self.sb_bayer_scale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_bayer_scale.setMinimum(0)
        self.sb_bayer_scale.setMaximum(5)
        self.sb_bayer_scale.setSingleStep(1)
        self.sb_bayer_scale.setValue(2)

        self.gridLayout_2.addWidget(self.sb_bayer_scale, 2, 2, 1, 1)

        self.lb_bayer_scale = QLabel(Dialog)
        self.lb_bayer_scale.setObjectName(u"lb_bayer_scale")
        sizePolicy.setHeightForWidth(self.lb_bayer_scale.sizePolicy().hasHeightForWidth())
        self.lb_bayer_scale.setSizePolicy(sizePolicy)
        self.lb_bayer_scale.setFont(font)
        self.lb_bayer_scale.setLayoutDirection(Qt.LeftToRight)
        self.lb_bayer_scale.setAutoFillBackground(False)
        self.lb_bayer_scale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_bayer_scale, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.cb_stats_mode = QComboBox(Dialog)
        self.cb_stats_mode.addItem(u"full")
        self.cb_stats_mode.addItem(u"diff")
        self.cb_stats_mode.setObjectName(u"cb_stats_mode")
        sizePolicy1.setHeightForWidth(self.cb_stats_mode.sizePolicy().hasHeightForWidth())
        self.cb_stats_mode.setSizePolicy(sizePolicy1)
        self.cb_stats_mode.setFont(font1)
        self.cb_stats_mode.setEditable(False)
        self.cb_stats_mode.setCurrentText(u"full")

        self.gridLayout_2.addWidget(self.cb_stats_mode, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.btn_save_filter_setting = QPushButton(Dialog)
        self.btn_save_filter_setting.setObjectName(u"btn_save_filter_setting")
        self.btn_save_filter_setting.setFont(font1)

        self.verticalLayout.addWidget(self.btn_save_filter_setting)

        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 19))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(Dialog)
        self.btn_add.setObjectName(u"btn_add")
        font3 = QFont()
        font3.setPointSize(10)
        self.btn_add.setFont(font3)

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_addclose = QPushButton(Dialog)
        self.btn_addclose.setObjectName(u"btn_addclose")
        self.btn_addclose.setFont(font3)

        self.horizontalLayout.addWidget(self.btn_addclose)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font3)

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font3)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.sb_framerate, self.sb_scale)
        QWidget.setTabOrder(self.sb_scale, self.max_size_dspinBox)
        QWidget.setTabOrder(self.max_size_dspinBox, self.cb_loopanimation)
        QWidget.setTabOrder(self.cb_loopanimation, self.cb_stats_mode)
        QWidget.setTabOrder(self.cb_stats_mode, self.cb_dither_mode)
        QWidget.setTabOrder(self.cb_dither_mode, self.sb_bayer_scale)
        QWidget.setTabOrder(self.sb_bayer_scale, self.cb_diff_mode)
        QWidget.setTabOrder(self.cb_diff_mode, self.btn_save_filter_setting)
        QWidget.setTabOrder(self.btn_save_filter_setting, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.btn_addclose)
        QWidget.setTabOrder(self.btn_addclose, self.btn_cancel)

        self.retranslateUi(Dialog)
        self.btn_addclose.clicked.connect(Dialog.accept)
        self.btn_cancel.clicked.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.cb_dither_mode.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit Convert Task", None))
        self.lb_framerate.setText(QCoreApplication.translate("Dialog", u"Framerate", None))
        self.lb_scale.setText(QCoreApplication.translate("Dialog", u"Scale", None))
        self.lb_max_size_mb.setText(QCoreApplication.translate("Dialog", u"Max Size (Mbytes)", None))
#if QT_CONFIG(tooltip)
        self.max_size_dspinBox.setToolTip(QCoreApplication.translate("Dialog", u"Limits size of the result file by tweaking the image scale\n"
"0 - disabled ", None))
#endif // QT_CONFIG(tooltip)
        self.cb_loopanimation.setText(QCoreApplication.translate("Dialog", u"Loop Animation", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filter options", None))

#if QT_CONFIG(tooltip)
        self.cb_dither_mode.setToolTip(QCoreApplication.translate("Dialog", u"Select dithering mode", None))
#endif // QT_CONFIG(tooltip)
        self.lb_framerate_2.setText(QCoreApplication.translate("Dialog", u"Statistic mode", None))
        self.lb_framerate_3.setText(QCoreApplication.translate("Dialog", u"Dithering mode", None))

#if QT_CONFIG(tooltip)
        self.cb_diff_mode.setToolTip(QCoreApplication.translate("Dialog", u"Define the zone to process", None))
#endif // QT_CONFIG(tooltip)
        self.lb_framerate_4.setText(QCoreApplication.translate("Dialog", u"Zone to process", None))
        self.lb_bayer_scale.setText(QCoreApplication.translate("Dialog", u"Bayer scale", None))

#if QT_CONFIG(tooltip)
        self.cb_stats_mode.setToolTip(QCoreApplication.translate("Dialog", u"Set statistics mode of palette generator", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_save_filter_setting.setToolTip(QCoreApplication.translate("Dialog", u"Save the current filter settings on your computer", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_filter_setting.setText(QCoreApplication.translate("Dialog", u"Save Filter options as default", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.btn_addclose.setText(QCoreApplication.translate("Dialog", u"  Add and Close  ", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

