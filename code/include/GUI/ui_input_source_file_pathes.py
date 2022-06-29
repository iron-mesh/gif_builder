# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_source_file_pathesnRLpvG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(549, 238)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_import_video_file = QPushButton(Form)
        self.btn_import_video_file.setObjectName(u"btn_import_video_file")
        self.btn_import_video_file.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_import_video_file.setFont(font)

        self.horizontalLayout.addWidget(self.btn_import_video_file)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.btn_import_img_seq = QPushButton(Form)
        self.btn_import_img_seq.setObjectName(u"btn_import_img_seq")
        self.btn_import_img_seq.setMinimumSize(QSize(200, 0))
        self.btn_import_img_seq.setFont(font)

        self.horizontalLayout.addWidget(self.btn_import_img_seq)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.te_import_info = QTextEdit(Form)
        self.te_import_info.setObjectName(u"te_import_info")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_import_info.sizePolicy().hasHeightForWidth())
        self.te_import_info.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.te_import_info.setFont(font1)
        self.te_import_info.setReadOnly(True)

        self.verticalLayout.addWidget(self.te_import_info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.sb_start_frame = QSpinBox(Form)
        self.sb_start_frame.setObjectName(u"sb_start_frame")
        self.sb_start_frame.setEnabled(False)
        self.sb_start_frame.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.sb_start_frame.setFont(font2)
        self.sb_start_frame.setLayoutDirection(Qt.LeftToRight)
        self.sb_start_frame.setAutoFillBackground(False)
        self.sb_start_frame.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_start_frame.setReadOnly(False)
        self.sb_start_frame.setMinimum(1)
        self.sb_start_frame.setMaximum(1)

        self.verticalLayout_2.addWidget(self.sb_start_frame)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.sb_end_frame = QSpinBox(Form)
        self.sb_end_frame.setObjectName(u"sb_end_frame")
        self.sb_end_frame.setEnabled(False)
        self.sb_end_frame.setMinimumSize(QSize(150, 0))
        self.sb_end_frame.setFont(font2)
        self.sb_end_frame.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_end_frame.setReadOnly(False)
        self.sb_end_frame.setMinimum(1)
        self.sb_end_frame.setMaximum(1)

        self.verticalLayout_4.addWidget(self.sb_end_frame)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_import_video_file.setText(QCoreApplication.translate("Form", u"Import Video File", None))
        self.btn_import_img_seq.setText(QCoreApplication.translate("Form", u"Import Image Sequence", None))
        self.te_import_info.setDocumentTitle("")
        self.te_import_info.setPlaceholderText(QCoreApplication.translate("Form", u"Information about imported files", None))
        self.label.setText(QCoreApplication.translate("Form", u"Start Frame", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"End Frame", None))
    # retranslateUi

