# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preset_configuration.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_PresetConfigDialog(object):
    def setupUi(self, PresetConfigDialog):
        if not PresetConfigDialog.objectName():
            PresetConfigDialog.setObjectName(u"PresetConfigDialog")
        PresetConfigDialog.resize(603, 731)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PresetConfigDialog.sizePolicy().hasHeightForWidth())
        PresetConfigDialog.setSizePolicy(sizePolicy)
        PresetConfigDialog.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0"
                        "px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel { font-size: 11px; color: rgb(113, 126, 149);  }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
""
                        "{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	s"
                        "election-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontr"
                        "ol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-rig"
                        "ht-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rg"
                        "b(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"Q"
                        "ComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    back"
                        "ground-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////"
                        "////////////////////\n"
"QListWidget */\n"
"QListWidget{\n"
"	border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* QTabBar */\n"
"QTabWidget::pane {\n"
"  border: 2px solid rgb(33, 37, 43);\n"
"  top:-1px; \n"
"  /*background: rgb(245, 245, 245);*/\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"    background-color: rgba(255, 255, 255, 40);\n"
"    min-width: 100px; \n"
"    min-height:22px;\n"
"    padding: 0px  2px; \n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    margin-left:2px;\n"
"    margin-right:2px;\n"
"}\n"
"QTabBar::tab:selected {  "
                        "\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 200);\n"
"    margin-top: 0px;\n"
"}\n"
"QTabBar::tab:hover {  \n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"    margin-top: 0px;\n"
"}\n"
"\n"
"/* QGroupBox */\n"
"QGroupBox { border: 1px solid  rgb(255, 121, 198); border-radius: 5px; margin-top: 0.5em; }\n"
"QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }\n"
"QGroupBox::title { color: rgb(161, 110, 235); }\n"
"\n"
"\n"
"")
        PresetConfigDialog.setSizeGripEnabled(False)
        PresetConfigDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(PresetConfigDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(PresetConfigDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_12 = QVBoxLayout(self.widget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_11.addWidget(self.label_10)


        self.verticalLayout_12.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignTop)

        self.preset_frames = QWidget(PresetConfigDialog)
        self.preset_frames.setObjectName(u"preset_frames")
        self.gridLayout = QGridLayout(self.preset_frames)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.preset_frame_5 = QFrame(self.preset_frames)
        self.preset_frame_5.setObjectName(u"preset_frame_5")
        self.preset_frame_5.setStyleSheet(u"#preset_frame_5 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.preset_frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.preset_frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_7.addWidget(self.label_6)

        self.preset_5_option_1 = QCheckBox(self.preset_frame_5)
        self.preset_5_option_1.setObjectName(u"preset_5_option_1")
        self.preset_5_option_1.setProperty(u"id", 0)

        self.verticalLayout_7.addWidget(self.preset_5_option_1)

        self.preset_5_option_2 = QCheckBox(self.preset_frame_5)
        self.preset_5_option_2.setObjectName(u"preset_5_option_2")
        self.preset_5_option_2.setProperty(u"id", 0)

        self.verticalLayout_7.addWidget(self.preset_5_option_2)

        self.preset_5_option_3 = QCheckBox(self.preset_frame_5)
        self.preset_5_option_3.setObjectName(u"preset_5_option_3")
        self.preset_5_option_3.setProperty(u"id", 0)

        self.verticalLayout_7.addWidget(self.preset_5_option_3)


        self.gridLayout.addWidget(self.preset_frame_5, 2, 0, 1, 1)

        self.preset_frame_8 = QFrame(self.preset_frames)
        self.preset_frame_8.setObjectName(u"preset_frame_8")
        self.preset_frame_8.setStyleSheet(u"#preset_frame_8 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.preset_frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.preset_frame_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_10.addWidget(self.label_9)

        self.preset_8_option_1 = QCheckBox(self.preset_frame_8)
        self.preset_8_option_1.setObjectName(u"preset_8_option_1")
        self.preset_8_option_1.setProperty(u"id", 0)

        self.verticalLayout_10.addWidget(self.preset_8_option_1)

        self.preset_8_option_2 = QCheckBox(self.preset_frame_8)
        self.preset_8_option_2.setObjectName(u"preset_8_option_2")
        self.preset_8_option_2.setProperty(u"id", 0)

        self.verticalLayout_10.addWidget(self.preset_8_option_2)

        self.preset_8_option_3 = QCheckBox(self.preset_frame_8)
        self.preset_8_option_3.setObjectName(u"preset_8_option_3")
        self.preset_8_option_3.setProperty(u"id", 0)

        self.verticalLayout_10.addWidget(self.preset_8_option_3)


        self.gridLayout.addWidget(self.preset_frame_8, 3, 1, 1, 1)

        self.preset_frame_1 = QFrame(self.preset_frames)
        self.preset_frame_1.setObjectName(u"preset_frame_1")
        self.preset_frame_1.setStyleSheet(u"#preset_frame_1 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.preset_frame_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.preset_frame_1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_2.addWidget(self.label)

        self.preset_1_option_1 = QCheckBox(self.preset_frame_1)
        self.preset_1_option_1.setObjectName(u"preset_1_option_1")
        self.preset_1_option_1.setProperty(u"id", 0)

        self.verticalLayout_2.addWidget(self.preset_1_option_1)

        self.preset_1_option_2 = QCheckBox(self.preset_frame_1)
        self.preset_1_option_2.setObjectName(u"preset_1_option_2")
        self.preset_1_option_2.setProperty(u"id", 0)

        self.verticalLayout_2.addWidget(self.preset_1_option_2)

        self.preset_1_option_3 = QCheckBox(self.preset_frame_1)
        self.preset_1_option_3.setObjectName(u"preset_1_option_3")
        self.preset_1_option_3.setProperty(u"id", 0)

        self.verticalLayout_2.addWidget(self.preset_1_option_3)


        self.gridLayout.addWidget(self.preset_frame_1, 0, 0, 1, 1)

        self.preset_frame_4 = QFrame(self.preset_frames)
        self.preset_frame_4.setObjectName(u"preset_frame_4")
        self.preset_frame_4.setStyleSheet(u"#preset_frame_4 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.preset_frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.preset_frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_5.addWidget(self.label_4)

        self.preset_4_option_1 = QCheckBox(self.preset_frame_4)
        self.preset_4_option_1.setObjectName(u"preset_4_option_1")
        self.preset_4_option_1.setProperty(u"id", 0)

        self.verticalLayout_5.addWidget(self.preset_4_option_1)

        self.preset_4_option_2 = QCheckBox(self.preset_frame_4)
        self.preset_4_option_2.setObjectName(u"preset_4_option_2")
        self.preset_4_option_2.setProperty(u"id", 0)

        self.verticalLayout_5.addWidget(self.preset_4_option_2)

        self.preset_4_option_3 = QCheckBox(self.preset_frame_4)
        self.preset_4_option_3.setObjectName(u"preset_4_option_3")
        self.preset_4_option_3.setProperty(u"id", 0)

        self.verticalLayout_5.addWidget(self.preset_4_option_3)


        self.gridLayout.addWidget(self.preset_frame_4, 1, 1, 1, 1)

        self.preset_frame_6 = QFrame(self.preset_frames)
        self.preset_frame_6.setObjectName(u"preset_frame_6")
        self.preset_frame_6.setStyleSheet(u"#preset_frame_6 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.preset_frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.preset_frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_8.addWidget(self.label_7)

        self.preset_6_option_1 = QCheckBox(self.preset_frame_6)
        self.preset_6_option_1.setObjectName(u"preset_6_option_1")
        self.preset_6_option_1.setProperty(u"id", 0)

        self.verticalLayout_8.addWidget(self.preset_6_option_1)

        self.preset_6_option_2 = QCheckBox(self.preset_frame_6)
        self.preset_6_option_2.setObjectName(u"preset_6_option_2")
        self.preset_6_option_2.setProperty(u"id", 0)

        self.verticalLayout_8.addWidget(self.preset_6_option_2)

        self.preset_6_option_3 = QCheckBox(self.preset_frame_6)
        self.preset_6_option_3.setObjectName(u"preset_6_option_3")
        self.preset_6_option_3.setProperty(u"id", 0)

        self.verticalLayout_8.addWidget(self.preset_6_option_3)


        self.gridLayout.addWidget(self.preset_frame_6, 2, 1, 1, 1)

        self.preset_frame_3 = QFrame(self.preset_frames)
        self.preset_frame_3.setObjectName(u"preset_frame_3")
        self.preset_frame_3.setStyleSheet(u"#preset_frame_3 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.preset_frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.preset_frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.preset_3_option_1 = QCheckBox(self.preset_frame_3)
        self.preset_3_option_1.setObjectName(u"preset_3_option_1")
        self.preset_3_option_1.setProperty(u"id", 0)

        self.verticalLayout_4.addWidget(self.preset_3_option_1)

        self.preset_3_option_2 = QCheckBox(self.preset_frame_3)
        self.preset_3_option_2.setObjectName(u"preset_3_option_2")
        self.preset_3_option_2.setProperty(u"id", 0)

        self.verticalLayout_4.addWidget(self.preset_3_option_2)

        self.preset_3_option_3 = QCheckBox(self.preset_frame_3)
        self.preset_3_option_3.setObjectName(u"preset_3_option_3")
        self.preset_3_option_3.setProperty(u"id", 0)

        self.verticalLayout_4.addWidget(self.preset_3_option_3)


        self.gridLayout.addWidget(self.preset_frame_3, 1, 0, 1, 1)

        self.preset_frame_7 = QFrame(self.preset_frames)
        self.preset_frame_7.setObjectName(u"preset_frame_7")
        self.preset_frame_7.setStyleSheet(u"#preset_frame_7 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.preset_frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.preset_frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_9.addWidget(self.label_8)

        self.preset_7_option_1 = QCheckBox(self.preset_frame_7)
        self.preset_7_option_1.setObjectName(u"preset_7_option_1")
        self.preset_7_option_1.setProperty(u"id", 0)

        self.verticalLayout_9.addWidget(self.preset_7_option_1)

        self.preset_7_option_2 = QCheckBox(self.preset_frame_7)
        self.preset_7_option_2.setObjectName(u"preset_7_option_2")
        self.preset_7_option_2.setProperty(u"id", 0)

        self.verticalLayout_9.addWidget(self.preset_7_option_2)

        self.preset_7_option_3 = QCheckBox(self.preset_frame_7)
        self.preset_7_option_3.setObjectName(u"preset_7_option_3")
        self.preset_7_option_3.setProperty(u"id", 0)

        self.verticalLayout_9.addWidget(self.preset_7_option_3)


        self.gridLayout.addWidget(self.preset_frame_7, 3, 0, 1, 1)

        self.preset_frame_2 = QFrame(self.preset_frames)
        self.preset_frame_2.setObjectName(u"preset_frame_2")
        self.preset_frame_2.setStyleSheet(u"#preset_frame_2 { \n"
"	border: 1px solid  rgb(29, 33, 38); \n"
"}\n"
"")
        self.preset_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.preset_frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.preset_frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color: rgb(161, 110, 235);")

        self.verticalLayout_3.addWidget(self.label_2)

        self.preset_2_option_1 = QCheckBox(self.preset_frame_2)
        self.preset_2_option_1.setObjectName(u"preset_2_option_1")
        self.preset_2_option_1.setProperty(u"id", 0)

        self.verticalLayout_3.addWidget(self.preset_2_option_1)

        self.preset_2_option_2 = QCheckBox(self.preset_frame_2)
        self.preset_2_option_2.setObjectName(u"preset_2_option_2")
        self.preset_2_option_2.setProperty(u"id", 0)

        self.verticalLayout_3.addWidget(self.preset_2_option_2)

        self.preset_2_option_3 = QCheckBox(self.preset_frame_2)
        self.preset_2_option_3.setObjectName(u"preset_2_option_3")
        self.preset_2_option_3.setProperty(u"id", 0)

        self.verticalLayout_3.addWidget(self.preset_2_option_3)


        self.gridLayout.addWidget(self.preset_frame_2, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.preset_frames, 0, Qt.AlignmentFlag.AlignTop)

        self.frame = QFrame(PresetConfigDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)

        self.widget_4 = QWidget(PresetConfigDialog)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_preset_config = QPushButton(self.widget_4)
        self.cancel_preset_config.setObjectName(u"cancel_preset_config")
        self.cancel_preset_config.setMinimumSize(QSize(85, 30))

        self.horizontalLayout.addWidget(self.cancel_preset_config, 0, Qt.AlignmentFlag.AlignRight)

        self.save_preset_config = QPushButton(self.widget_4)
        self.save_preset_config.setObjectName(u"save_preset_config")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_preset_config.sizePolicy().hasHeightForWidth())
        self.save_preset_config.setSizePolicy(sizePolicy1)
        self.save_preset_config.setMinimumSize(QSize(85, 30))

        self.horizontalLayout.addWidget(self.save_preset_config, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(PresetConfigDialog)

        QMetaObject.connectSlotsByName(PresetConfigDialog)
    # setupUi

    def retranslateUi(self, PresetConfigDialog):
        PresetConfigDialog.setWindowTitle(QCoreApplication.translate("PresetConfigDialog", u"Dialog", None))
        self.label_10.setText(QCoreApplication.translate("PresetConfigDialog", u"Set up Presets", None))
        self.label_6.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 5", None))
        self.preset_5_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_5_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_5_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_9.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 8", None))
        self.preset_8_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_8_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_8_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 1", None))
        self.preset_1_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_1_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_1_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_4.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 4", None))
        self.preset_4_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_4_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_4_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_7.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 6", None))
        self.preset_6_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_6_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_6_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 3", None))
        self.preset_3_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_3_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_3_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_8.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 7", None))
        self.preset_7_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_7_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_7_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset 2", None))
        self.preset_2_option_1.setText(QCoreApplication.translate("PresetConfigDialog", u"Use Selected Generals", None))
        self.preset_2_option_2.setText(QCoreApplication.translate("PresetConfigDialog", u"Skip Preset with No General", None))
        self.preset_2_option_3.setText(QCoreApplication.translate("PresetConfigDialog", u"Reset to One Troop(Top Tier) ", None))
        self.label_5.setText(QCoreApplication.translate("PresetConfigDialog", u"Preset Configuration is bind to the Emulator Instance you are on!", None))
        self.cancel_preset_config.setText(QCoreApplication.translate("PresetConfigDialog", u"Cancel", None))
        self.save_preset_config.setText(QCoreApplication.translate("PresetConfigDialog", u"Save", None))
    # retranslateUi

