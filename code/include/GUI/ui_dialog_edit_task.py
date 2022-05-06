# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_edit_taskLWxovW.ui'
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
        Dialog.resize(475, 465)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.isfp_import_media = QInputSourceFilePathes()
        self.isfp_import_media.setObjectName(u"isfp_import_media")
        self.isfp_import_media.setMinimumSize(QSize(439, 74))

        self.verticalLayout.addWidget(self.isfp_import_media)

        self.ip_export_file = QInputPath(Dialog)
        self.ip_export_file.setObjectName(u"ip_export_file")

        self.verticalLayout.addWidget(self.ip_export_file)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sb_scale = QSpinBox(Dialog)
        self.sb_scale.setObjectName(u"sb_scale")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_scale.sizePolicy().hasHeightForWidth())
        self.sb_scale.setSizePolicy(sizePolicy)
        self.sb_scale.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(11)
        self.sb_scale.setFont(font)
        self.sb_scale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_scale.setMinimum(5)
        self.sb_scale.setMaximum(100)
        self.sb_scale.setSingleStep(5)
        self.sb_scale.setValue(100)

        self.gridLayout.addWidget(self.sb_scale, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.lb_scale = QLabel(Dialog)
        self.lb_scale.setObjectName(u"lb_scale")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_scale.sizePolicy().hasHeightForWidth())
        self.lb_scale.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.lb_scale.setFont(font1)
        self.lb_scale.setLayoutDirection(Qt.LeftToRight)
        self.lb_scale.setAutoFillBackground(False)
        self.lb_scale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_scale, 1, 0, 1, 1)

        self.sb_framerate = QSpinBox(Dialog)
        self.sb_framerate.setObjectName(u"sb_framerate")
        sizePolicy.setHeightForWidth(self.sb_framerate.sizePolicy().hasHeightForWidth())
        self.sb_framerate.setSizePolicy(sizePolicy)
        self.sb_framerate.setMinimumSize(QSize(100, 0))
        self.sb_framerate.setFont(font)
        self.sb_framerate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_framerate.setMinimum(1)
        self.sb_framerate.setMaximum(1000)

        self.gridLayout.addWidget(self.sb_framerate, 0, 2, 1, 1)

        self.lb_framerate = QLabel(Dialog)
        self.lb_framerate.setObjectName(u"lb_framerate")
        sizePolicy1.setHeightForWidth(self.lb_framerate.sizePolicy().hasHeightForWidth())
        self.lb_framerate.setSizePolicy(sizePolicy1)
        self.lb_framerate.setFont(font1)
        self.lb_framerate.setLayoutDirection(Qt.LeftToRight)
        self.lb_framerate.setFrameShape(QFrame.NoFrame)
        self.lb_framerate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lb_framerate, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.cb_loopanimation = QCheckBox(Dialog)
        self.cb_loopanimation.setObjectName(u"cb_loopanimation")
        self.cb_loopanimation.setFont(font1)

        self.verticalLayout.addWidget(self.cb_loopanimation)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(Dialog)
        self.btn_add.setObjectName(u"btn_add")
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_add.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_addclose = QPushButton(Dialog)
        self.btn_addclose.setObjectName(u"btn_addclose")
        self.btn_addclose.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_addclose)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font2)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.sb_framerate, self.sb_scale)
        QWidget.setTabOrder(self.sb_scale, self.cb_loopanimation)

        self.retranslateUi(Dialog)
        self.btn_addclose.clicked.connect(Dialog.accept)
        self.btn_cancel.clicked.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Edit Convert Task", None))
        self.lb_scale.setText(QCoreApplication.translate("Dialog", u"Scale", None))
        self.lb_framerate.setText(QCoreApplication.translate("Dialog", u"Framerate", None))
        self.cb_loopanimation.setText(QCoreApplication.translate("Dialog", u"Loop Animation", None))
        self.btn_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.btn_addclose.setText(QCoreApplication.translate("Dialog", u"  Add and Close  ", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

