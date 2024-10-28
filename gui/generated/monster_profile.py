# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monster_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Monster_Profile(object):
    def setupUi(self, Monster_Profile):
        if not Monster_Profile.objectName():
            Monster_Profile.setObjectName(u"Monster_Profile")
        Monster_Profile.resize(299, 179)
        self.horizontalLayout_5 = QHBoxLayout(Monster_Profile)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(Monster_Profile)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(30, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QSize(0, 30))
        self.checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setText(u"")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.horizontalLayout_3.addWidget(self.checkBox)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 70))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.monster_icon_label = QLabel(self.frame_5)
        self.monster_icon_label.setObjectName(u"monster_icon_label")
        self.monster_icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.monster_icon_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(30, 0))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.horizontalLayout_4.setStretch(0, 8)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 8)

        self.horizontalLayout_6.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_8)

        self.bottom_color_frame = QFrame(self.frame_6)
        self.bottom_color_frame.setObjectName(u"bottom_color_frame")
        self.bottom_color_frame.setMinimumSize(QSize(200, 30))
        self.bottom_color_frame.setMaximumSize(QSize(16777215, 30))
        self.bottom_color_frame.setStyleSheet(u"background-color: rgb(29, 33, 38);")
        self.bottom_color_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.bottom_color_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottom_color_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.monster_name_label = QLabel(self.bottom_color_frame)
        self.monster_name_label.setObjectName(u"monster_name_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.monster_name_label.sizePolicy().hasHeightForWidth())
        self.monster_name_label.setSizePolicy(sizePolicy1)
        self.monster_name_label.setMinimumSize(QSize(0, 30))
        self.monster_name_label.setMaximumSize(QSize(16777215, 30))
        self.monster_name_label.setStyleSheet(u"")
        self.monster_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.monster_name_label)


        self.verticalLayout.addWidget(self.bottom_color_frame)

        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_4 = QFrame(Monster_Profile)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.configure_monster_btn = QPushButton(self.frame_4)
        self.configure_monster_btn.setObjectName(u"configure_monster_btn")
        self.configure_monster_btn.setMinimumSize(QSize(30, 30))
        self.configure_monster_btn.setMaximumSize(QSize(16777215, 16777215))
        self.configure_monster_btn.setStyleSheet(u"border: none;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.configure_monster_btn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.configure_monster_btn)

        self.delete_monster_btn = QPushButton(self.frame_4)
        self.delete_monster_btn.setObjectName(u"delete_monster_btn")
        self.delete_monster_btn.setMinimumSize(QSize(0, 0))
        self.delete_monster_btn.setMaximumSize(QSize(45, 45))
        self.delete_monster_btn.setStyleSheet(u"border: none;")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_monster_btn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.delete_monster_btn)


        self.horizontalLayout_5.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(Monster_Profile)

        QMetaObject.connectSlotsByName(Monster_Profile)
    # setupUi

    def retranslateUi(self, Monster_Profile):
        Monster_Profile.setWindowTitle(QCoreApplication.translate("Monster_Profile", u"Form", None))
        self.monster_icon_label.setText("")
        self.monster_name_label.setText(QCoreApplication.translate("Monster_Profile", u"Boss Name", None))
        self.configure_monster_btn.setText("")
        self.delete_monster_btn.setText("")
    # retranslateUi

