# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'general_profile.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from core.custom_widgets.GeneralNameLineEdit import GeneralNameLineEdit

class Ui_General_Profile(object):
    def setupUi(self, General_Profile):
        if not General_Profile.objectName():
            General_Profile.setObjectName(u"General_Profile")
        General_Profile.resize(255, 221)
        self.horizontalLayout = QHBoxLayout(General_Profile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(General_Profile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(180, 160))
        self.frame_3.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.general_icon_label = QLabel(self.frame_3)
        self.general_icon_label.setObjectName(u"general_icon_label")
        self.general_icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.general_icon_label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(180, 0))
        self.frame_4.setStyleSheet(u"background-color: rgb(29, 33, 38);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.edit_general = GeneralNameLineEdit(self.frame_4)
        self.edit_general.setObjectName(u"edit_general")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_general.sizePolicy().hasHeightForWidth())
        self.edit_general.setSizePolicy(sizePolicy)
        self.edit_general.setMinimumSize(QSize(0, 35))
        self.edit_general.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.edit_general.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.edit_general)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 2)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(General_Profile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.delete_general_btn = QPushButton(self.frame_2)
        self.delete_general_btn.setObjectName(u"delete_general_btn")
        self.delete_general_btn.setMaximumSize(QSize(45, 45))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_general_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.delete_general_btn)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(General_Profile)

        QMetaObject.connectSlotsByName(General_Profile)
    # setupUi

    def retranslateUi(self, General_Profile):
        General_Profile.setWindowTitle(QCoreApplication.translate("General_Profile", u"Form", None))
        self.general_icon_label.setText("")
        self.delete_general_btn.setText("")
    # retranslateUi

