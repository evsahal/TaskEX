# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'black_market_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_BlackMarket_Profile(object):
    def setupUi(self, BlackMarket_Profile):
        if not BlackMarket_Profile.objectName():
            BlackMarket_Profile.setObjectName(u"BlackMarket_Profile")
        BlackMarket_Profile.resize(330, 235)
        BlackMarket_Profile.setMinimumSize(QSize(330, 0))
        BlackMarket_Profile.setMaximumSize(QSize(330, 16777215))
        BlackMarket_Profile.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(BlackMarket_Profile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(BlackMarket_Profile)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_4)
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


        self.verticalLayout_2.addWidget(self.frame)

        self.template_frame = QFrame(self.frame_4)
        self.template_frame.setObjectName(u"template_frame")
        self.template_frame.setStyleSheet(u"")
        self.template_frame.setFrameShape(QFrame.Shape.Box)
        self.template_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.template_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.template_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 282, 93))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_frame = QFrame(self.scrollAreaWidgetContents)
        self.scroll_area_frame.setObjectName(u"scroll_area_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area_frame.sizePolicy().hasHeightForWidth())
        self.scroll_area_frame.setSizePolicy(sizePolicy)
        self.scroll_area_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.scroll_area_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 12)
        self.add_template_btn = QPushButton(self.scroll_area_frame)
        self.add_template_btn.setObjectName(u"add_template_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_template_btn.sizePolicy().hasHeightForWidth())
        self.add_template_btn.setSizePolicy(sizePolicy1)
        self.add_template_btn.setMinimumSize(QSize(60, 60))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_template_btn.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.add_template_btn)


        self.horizontalLayout_4.addWidget(self.scroll_area_frame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.template_frame)

        self.purchase_button_frame = QFrame(self.frame_4)
        self.purchase_button_frame.setObjectName(u"purchase_button_frame")
        self.purchase_button_frame.setMinimumSize(QSize(0, 0))
        self.purchase_button_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.purchase_button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.purchase_button_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rss_btn = QPushButton(self.purchase_button_frame)
        self.rss_btn.setObjectName(u"rss_btn")
        self.rss_btn.setMinimumSize(QSize(90, 35))
        self.rss_btn.setCheckable(True)
        self.rss_btn.setChecked(False)

        self.horizontalLayout_3.addWidget(self.rss_btn)

        self.gold_btn = QPushButton(self.purchase_button_frame)
        self.gold_btn.setObjectName(u"gold_btn")
        self.gold_btn.setMinimumSize(QSize(80, 35))
        self.gold_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.gold_btn)

        self.gems_btn = QPushButton(self.purchase_button_frame)
        self.gems_btn.setObjectName(u"gems_btn")
        self.gems_btn.setMinimumSize(QSize(80, 35))
        self.gems_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.gems_btn)


        self.verticalLayout_2.addWidget(self.purchase_button_frame, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(BlackMarket_Profile)

        QMetaObject.connectSlotsByName(BlackMarket_Profile)
    # setupUi

    def retranslateUi(self, BlackMarket_Profile):
        BlackMarket_Profile.setWindowTitle(QCoreApplication.translate("BlackMarket_Profile", u"Form", None))
        self.name_lineEdit.setPlaceholderText(QCoreApplication.translate("BlackMarket_Profile", u"Item Name Here", None))
        self.save_btn.setText("")
        self.delete_btn.setText("")
        self.add_template_btn.setText("")
        self.rss_btn.setText(QCoreApplication.translate("BlackMarket_Profile", u"Resources", None))
        self.gold_btn.setText(QCoreApplication.translate("BlackMarket_Profile", u"Gold", None))
        self.gems_btn.setText(QCoreApplication.translate("BlackMarket_Profile", u"Gems", None))
    # retranslateUi

