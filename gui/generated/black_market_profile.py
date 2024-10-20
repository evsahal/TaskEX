# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'black_market_profile.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_BlackMarket_Profile(object):
    def setupUi(self, BlackMarket_Profile):
        if not BlackMarket_Profile.objectName():
            BlackMarket_Profile.setObjectName(u"BlackMarket_Profile")
        BlackMarket_Profile.resize(329, 217)
        self.verticalLayout = QVBoxLayout(BlackMarket_Profile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(BlackMarket_Profile)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_lineEdit = QLineEdit(self.frame)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 45))

        self.horizontalLayout.addWidget(self.name_lineEdit)

        self.save_btn = QPushButton(self.frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(45, 45))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.save_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.save_btn)

        self.delete_btn = QPushButton(self.frame)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(45, 45))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_btn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(BlackMarket_Profile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 305, 89))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_frame = QFrame(self.scrollAreaWidgetContents)
        self.scroll_area_frame.setObjectName(u"scroll_area_frame")
        self.scroll_area_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.scroll_area_frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(BlackMarket_Profile)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rss_btn = QPushButton(self.frame_3)
        self.rss_btn.setObjectName(u"rss_btn")
        self.rss_btn.setMinimumSize(QSize(0, 45))
        self.rss_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.rss_btn)

        self.gold_btn = QPushButton(self.frame_3)
        self.gold_btn.setObjectName(u"gold_btn")
        self.gold_btn.setMinimumSize(QSize(0, 45))
        self.gold_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.gold_btn)

        self.gems_btn = QPushButton(self.frame_3)
        self.gems_btn.setObjectName(u"gems_btn")
        self.gems_btn.setMinimumSize(QSize(0, 45))
        self.gems_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.gems_btn)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(BlackMarket_Profile)

        QMetaObject.connectSlotsByName(BlackMarket_Profile)
    # setupUi

    def retranslateUi(self, BlackMarket_Profile):
        BlackMarket_Profile.setWindowTitle(QCoreApplication.translate("BlackMarket_Profile", u"Form", None))
        self.save_btn.setText("")
        self.delete_btn.setText("")
        self.rss_btn.setText(QCoreApplication.translate("BlackMarket_Profile", u"Resources", None))
        self.gold_btn.setText(QCoreApplication.translate("BlackMarket_Profile", u"Gold", None))
        self.gems_btn.setText(QCoreApplication.translate("BlackMarket_Profile", u"Gems", None))
    # retranslateUi

