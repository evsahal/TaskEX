# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instance_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_InstancePage(object):
    def setupUi(self, InstancePage):
        if not InstancePage.objectName():
            InstancePage.setObjectName(u"InstancePage")
        InstancePage.resize(1143, 836)
        InstancePage.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
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
"/*\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border: 1px solid rgb(255, 121, 198);\n"
""
                        "	 border-radius: 5px;\n"
"                              \n"
"                        }\n"
"QToolBox::tab:selected {\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"   background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left :10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QTimeEdit {\n"
"  background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left :10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox {\n"
"   background-color: rgba(40, 44, 52, 0.9);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left :10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
""
                        "	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49,"
                        " 60);\n"
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
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255)"
                        ";\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
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
"\n"
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
"QScrollB"
                        "ar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
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
"	border-rad"
                        "ius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
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
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 8"
                        "1);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"\n"
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
"\n"
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
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
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
"\n"
"QListWidget{\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QComman"
                        "dLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 2px solid rgb(33, 37, 43);\n"
"  top:-1px; \n"
"	left: 2px;\n"
"  background-color: rgba(40, 44, 52, 0.9);\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"	background-color: rgba(30, 35, 43, 0.9); \n"
"    min-width: 140px; \n"
"    min-height:28px;\n"
"    padding: 0px  0px; \n"
"	color: rgb(255, 121, 198);\n"
" 	border: 2px solid rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"	margin-left:2px;\n"
"    margin-right:2px;\n"
"}\n"
"QTabBar::tab:selected {  \n"
"    color: rgb(161, 110, 235);\n"
"    background-color: rgba(35, 40, 48, 0.9);\n"
"    margin-top: 0px;\n"
"}\n"
"QTabBar::tab:hover {  \n"
"	color: #aaa;\n"
"	background-color: rgb(40, 44, 52);\n"
"    margin-top: 0px;\n"
"}\n"
"\n"
"\n"
"QGroupBox { border: 1px solid  rgb(255, 121, 198); border-radius: 5px; marg"
                        "in-top: 0.5em; }\n"
"QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; }\n"
"QGroupBox::title { color: rgb(161, 110, 235); }\n"
"\n"
" QPushButton {\n"
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
"*/")
        self.verticalLayout = QVBoxLayout(InstancePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(InstancePage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.run_tab_ = QWidget()
        self.run_tab_.setObjectName(u"run_tab_")
        self.verticalLayout_2 = QVBoxLayout(self.run_tab_)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.run_main_frame = QFrame(self.run_tab_)
        self.run_main_frame.setObjectName(u"run_main_frame")
        self.run_main_frame.setStyleSheet(u"")
        self.run_main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.run_main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.run_main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.run_main_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(0,0,0);\n"
"font: 9pt \"Source Code Pro\";\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.textEdit)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.config_panel_gb = QGroupBox(self.run_main_frame)
        self.config_panel_gb.setObjectName(u"config_panel_gb")
        self.horizontalLayout_10 = QHBoxLayout(self.config_panel_gb)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(4, 4, 4, 4)

        self.gridLayout.addWidget(self.config_panel_gb, 0, 1, 2, 1)

        self.frame_3 = QFrame(self.run_main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_run_frame = QFrame(self.frame_3)
        self.top_run_frame.setObjectName(u"top_run_frame")
        self.top_run_frame.setStyleSheet(u"#top_run_frame{ border: 1px solid  rgb(255, 121, 198); border-radius: 5px; margin-top: 0.5em; }")
        self.top_run_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_run_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.top_run_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_10 = QFrame(self.top_run_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(7, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.frame_10)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(170, 45))

        self.horizontalLayout_8.addWidget(self.comboBox_2)

        self.emu_name_ = QLineEdit(self.frame_10)
        self.emu_name_.setObjectName(u"emu_name_")
        self.emu_name_.setMinimumSize(QSize(180, 45))
        self.emu_name_.setMaximumSize(QSize(200, 16777215))
        self.emu_name_.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.emu_name_)

        self.emu_port_ = QLineEdit(self.frame_10)
        self.emu_port_.setObjectName(u"emu_port_")
        self.emu_port_.setMinimumSize(QSize(0, 45))
        self.emu_port_.setMaximumSize(QSize(90, 16777215))
        self.emu_port_.setMaxLength(10)
        self.emu_port_.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.emu_port_)

        self.run_btn_ = QPushButton(self.frame_10)
        self.run_btn_.setObjectName(u"run_btn_")
        self.run_btn_.setMinimumSize(QSize(45, 45))
        self.run_btn_.setStyleSheet(u"background:transparent;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.run_btn_.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.run_btn_)


        self.horizontalLayout_6.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_11 = QFrame(self.top_run_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 7, 0)
        self.delete_instance_ = QPushButton(self.frame_11)
        self.delete_instance_.setObjectName(u"delete_instance_")
        self.delete_instance_.setMinimumSize(QSize(140, 45))
        self.delete_instance_.setStyleSheet(u"background:transparent;")

        self.horizontalLayout_9.addWidget(self.delete_instance_)


        self.horizontalLayout_6.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.top_run_frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_7 = QFrame(self.groupBox_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.preset_widget_ = QWidget(self.frame_9)
        self.preset_widget_.setObjectName(u"preset_widget_")
        self.horizontalLayout_7 = QHBoxLayout(self.preset_widget_)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.preset_combo_ = QComboBox(self.preset_widget_)
        self.preset_combo_.addItem("")
        self.preset_combo_.addItem("")
        self.preset_combo_.setObjectName(u"preset_combo_")
        self.preset_combo_.setMinimumSize(QSize(150, 45))
        self.preset_combo_.setMaximumSize(QSize(16777215, 45))
        self.preset_combo_.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout_7.addWidget(self.preset_combo_)

        self.preset_edit_btn_ = QPushButton(self.preset_widget_)
        self.preset_edit_btn_.setObjectName(u"preset_edit_btn_")
        self.preset_edit_btn_.setMinimumSize(QSize(45, 45))
        self.preset_edit_btn_.setMaximumSize(QSize(45, 45))
        self.preset_edit_btn_.setStyleSheet(u"background:transparent;")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.preset_edit_btn_.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.preset_edit_btn_)

        self.preset_delete_btn_ = QPushButton(self.preset_widget_)
        self.preset_delete_btn_.setObjectName(u"preset_delete_btn_")
        self.preset_delete_btn_.setMinimumSize(QSize(45, 45))
        self.preset_delete_btn_.setMaximumSize(QSize(45, 45))
        self.preset_delete_btn_.setStyleSheet(u"background:transparent;")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.preset_delete_btn_.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.preset_delete_btn_)

        self.preset_add_btn_ = QPushButton(self.preset_widget_)
        self.preset_add_btn_.setObjectName(u"preset_add_btn_")
        self.preset_add_btn_.setMinimumSize(QSize(45, 45))
        self.preset_add_btn_.setMaximumSize(QSize(45, 45))
        self.preset_add_btn_.setStyleSheet(u"background:transparent;")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.preset_add_btn_.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.preset_add_btn_)


        self.verticalLayout_9.addWidget(self.preset_widget_)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scheduler_table_ = QTableWidget(self.frame_5)
        if (self.scheduler_table_.columnCount() < 2):
            self.scheduler_table_.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.scheduler_table_.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.scheduler_table_.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.scheduler_table_.setObjectName(u"scheduler_table_")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduler_table_.sizePolicy().hasHeightForWidth())
        self.scheduler_table_.setSizePolicy(sizePolicy)
        self.scheduler_table_.setMouseTracking(False)
        self.scheduler_table_.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.scheduler_table_.setAcceptDrops(True)
        self.scheduler_table_.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scheduler_table_.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.scheduler_table_.setDragEnabled(True)
        self.scheduler_table_.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.scheduler_table_.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.scheduler_table_.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.scheduler_table_.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
        self.scheduler_table_.setShowGrid(True)
        self.scheduler_table_.setGridStyle(Qt.PenStyle.SolidLine)
        self.scheduler_table_.setCornerButtonEnabled(False)
        self.scheduler_table_.horizontalHeader().setMinimumSectionSize(45)
        self.scheduler_table_.horizontalHeader().setStretchLastSection(False)
        self.scheduler_table_.verticalHeader().setMinimumSectionSize(45)
        self.scheduler_table_.verticalHeader().setDefaultSectionSize(45)
        self.scheduler_table_.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_2.addWidget(self.scheduler_table_)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 3)

        self.horizontalLayout_5.addWidget(self.groupBox_3)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(self.groupBox_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, -1, 0)
        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.spinBox = QSpinBox(self.frame_15)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(120, 40))
        self.spinBox.setValue(5)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout_11.addWidget(self.frame_15, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_13)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_11.addWidget(self.checkBox)


        self.verticalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 5, 0, 0)
        self.timeEdit = QTimeEdit(self.frame_14)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(110, 40))
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)

        self.gridLayout_2.addWidget(self.timeEdit, 1, 3, 1, 1)

        self.timeEdit_2 = QTimeEdit(self.frame_14)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setMinimumSize(QSize(110, 40))
        self.timeEdit_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)

        self.gridLayout_2.addWidget(self.timeEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_11.addWidget(self.frame_12)


        self.verticalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 8)

        self.horizontalLayout_5.addWidget(self.frame_6)

        self.horizontalLayout_5.setStretch(0, 4)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 6)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 6)
        self.gridLayout.setColumnStretch(0, 6)
        self.gridLayout.setColumnStretch(1, 2)

        self.verticalLayout_2.addWidget(self.run_main_frame)

        self.tabWidget.addTab(self.run_tab_, "")
        self.general_tab_ = QWidget()
        self.general_tab_.setObjectName(u"general_tab_")
        self.tabWidget.addTab(self.general_tab_, "")
        self.join_rally_tab_ = QWidget()
        self.join_rally_tab_.setObjectName(u"join_rally_tab_")
        self.verticalLayout_12 = QVBoxLayout(self.join_rally_tab_)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_16 = QFrame(self.join_rally_tab_)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.skip_monsters_gb = QGroupBox(self.frame_16)
        self.skip_monsters_gb.setObjectName(u"skip_monsters_gb")
        self.horizontalLayout_12 = QHBoxLayout(self.skip_monsters_gb)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.jr_monster_list_scroll_area = QScrollArea(self.skip_monsters_gb)
        self.jr_monster_list_scroll_area.setObjectName(u"jr_monster_list_scroll_area")
        self.jr_monster_list_scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.jr_monster_list_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1067, 524))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.jr_monster_list1_frame_ = QFrame(self.scrollAreaWidgetContents)
        self.jr_monster_list1_frame_.setObjectName(u"jr_monster_list1_frame_")
        sizePolicy1.setHeightForWidth(self.jr_monster_list1_frame_.sizePolicy().hasHeightForWidth())
        self.jr_monster_list1_frame_.setSizePolicy(sizePolicy1)
        self.jr_monster_list1_frame_.setFrameShape(QFrame.Shape.NoFrame)
        self.jr_monster_list1_frame_.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_15.addWidget(self.jr_monster_list1_frame_, 0, Qt.AlignmentFlag.AlignTop)

        self.jr_monster_list2_frame_ = QFrame(self.scrollAreaWidgetContents)
        self.jr_monster_list2_frame_.setObjectName(u"jr_monster_list2_frame_")
        sizePolicy1.setHeightForWidth(self.jr_monster_list2_frame_.sizePolicy().hasHeightForWidth())
        self.jr_monster_list2_frame_.setSizePolicy(sizePolicy1)
        self.jr_monster_list2_frame_.setFrameShape(QFrame.Shape.NoFrame)
        self.jr_monster_list2_frame_.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_15.addWidget(self.jr_monster_list2_frame_)

        self.jr_monster_list_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_12.addWidget(self.jr_monster_list_scroll_area)


        self.verticalLayout_13.addWidget(self.skip_monsters_gb)


        self.verticalLayout_12.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.join_rally_tab_)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.frame_17)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_18 = QFrame(self.groupBox_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_748 = QFrame(self.frame_18)
        self.frame_748.setObjectName(u"frame_748")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_748.sizePolicy().hasHeightForWidth())
        self.frame_748.setSizePolicy(sizePolicy2)
        self.frame_748.setMaximumSize(QSize(16777215, 16777215))
        self.frame_748.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_748.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_748)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.widget_1082 = QWidget(self.frame_748)
        self.widget_1082.setObjectName(u"widget_1082")
        self.horizontalLayout_769 = QHBoxLayout(self.widget_1082)
        self.horizontalLayout_769.setSpacing(7)
        self.horizontalLayout_769.setObjectName(u"horizontalLayout_769")
        self.horizontalLayout_769.setContentsMargins(0, 0, 0, 0)
        self.label_234 = QLabel(self.widget_1082)
        self.label_234.setObjectName(u"label_234")

        self.horizontalLayout_769.addWidget(self.label_234, 0, Qt.AlignmentFlag.AlignLeft)

        self.jr_rotate_preset_settings_ = QPushButton(self.widget_1082)
        self.jr_rotate_preset_settings_.setObjectName(u"jr_rotate_preset_settings_")
        self.jr_rotate_preset_settings_.setMinimumSize(QSize(25, 25))
        self.jr_rotate_preset_settings_.setMaximumSize(QSize(25, 25))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.jr_rotate_preset_settings_.setIcon(icon4)
        self.jr_rotate_preset_settings_.setCheckable(False)

        self.horizontalLayout_769.addWidget(self.jr_rotate_preset_settings_)


        self.verticalLayout_39.addWidget(self.widget_1082)

        self.widget_1083 = QWidget(self.frame_748)
        self.widget_1083.setObjectName(u"widget_1083")
        self.widget_1083.setStyleSheet(u"QPushButton {\n"
"    background-color: #777;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #FF79C6;\n"
"}\n"
"")
        self.verticalLayout_1317 = QVBoxLayout(self.widget_1083)
        self.verticalLayout_1317.setObjectName(u"verticalLayout_1317")
        self.verticalLayout_1317.setContentsMargins(0, 0, 0, 0)
        self.widget_1084 = QWidget(self.widget_1083)
        self.widget_1084.setObjectName(u"widget_1084")
        self.horizontalLayout_770 = QHBoxLayout(self.widget_1084)
        self.horizontalLayout_770.setSpacing(7)
        self.horizontalLayout_770.setObjectName(u"horizontalLayout_770")
        self.horizontalLayout_770.setContentsMargins(0, 0, 0, 0)
        self.rotate_preset_one___ = QPushButton(self.widget_1084)
        self.rotate_preset_one___.setObjectName(u"rotate_preset_one___")
        self.rotate_preset_one___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_one___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_one___.setCheckable(True)

        self.horizontalLayout_770.addWidget(self.rotate_preset_one___)

        self.rotate_preset_two___ = QPushButton(self.widget_1084)
        self.rotate_preset_two___.setObjectName(u"rotate_preset_two___")
        self.rotate_preset_two___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_two___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_two___.setCheckable(True)

        self.horizontalLayout_770.addWidget(self.rotate_preset_two___)

        self.rotate_preset_three___ = QPushButton(self.widget_1084)
        self.rotate_preset_three___.setObjectName(u"rotate_preset_three___")
        self.rotate_preset_three___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_three___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_three___.setCheckable(True)

        self.horizontalLayout_770.addWidget(self.rotate_preset_three___)

        self.rotate_preset_four___ = QPushButton(self.widget_1084)
        self.rotate_preset_four___.setObjectName(u"rotate_preset_four___")
        self.rotate_preset_four___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_four___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_four___.setCheckable(True)

        self.horizontalLayout_770.addWidget(self.rotate_preset_four___)


        self.verticalLayout_1317.addWidget(self.widget_1084, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_1085 = QWidget(self.widget_1083)
        self.widget_1085.setObjectName(u"widget_1085")
        self.horizontalLayout_771 = QHBoxLayout(self.widget_1085)
        self.horizontalLayout_771.setSpacing(7)
        self.horizontalLayout_771.setObjectName(u"horizontalLayout_771")
        self.horizontalLayout_771.setContentsMargins(0, 0, 0, 0)
        self.rotate_preset_five___ = QPushButton(self.widget_1085)
        self.rotate_preset_five___.setObjectName(u"rotate_preset_five___")
        self.rotate_preset_five___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_five___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_five___.setCheckable(True)

        self.horizontalLayout_771.addWidget(self.rotate_preset_five___)

        self.rotate_preset_six___ = QPushButton(self.widget_1085)
        self.rotate_preset_six___.setObjectName(u"rotate_preset_six___")
        self.rotate_preset_six___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_six___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_six___.setCheckable(True)

        self.horizontalLayout_771.addWidget(self.rotate_preset_six___)

        self.rotate_preset_seven___ = QPushButton(self.widget_1085)
        self.rotate_preset_seven___.setObjectName(u"rotate_preset_seven___")
        self.rotate_preset_seven___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_seven___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_seven___.setCheckable(True)

        self.horizontalLayout_771.addWidget(self.rotate_preset_seven___)

        self.rotate_preset_eight___ = QPushButton(self.widget_1085)
        self.rotate_preset_eight___.setObjectName(u"rotate_preset_eight___")
        self.rotate_preset_eight___.setMinimumSize(QSize(25, 25))
        self.rotate_preset_eight___.setMaximumSize(QSize(25, 25))
        self.rotate_preset_eight___.setCheckable(True)

        self.horizontalLayout_771.addWidget(self.rotate_preset_eight___)


        self.verticalLayout_1317.addWidget(self.widget_1085, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_39.addWidget(self.widget_1083)


        self.gridLayout_3.addWidget(self.frame_748, 0, 0, 1, 1)

        self.frame_749 = QFrame(self.frame_18)
        self.frame_749.setObjectName(u"frame_749")
        self.frame_749.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_749.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_749)
        self.verticalLayout_40.setSpacing(7)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(11, 11, 11, 11)
        self.widget_36 = QWidget(self.frame_749)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_763 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_763.setObjectName(u"horizontalLayout_763")
        self.horizontalLayout_763.setContentsMargins(0, 0, 0, 0)
        self.auto_use_stamina___ = QCheckBox(self.widget_36)
        self.auto_use_stamina___.setObjectName(u"auto_use_stamina___")

        self.horizontalLayout_763.addWidget(self.auto_use_stamina___, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_40.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.frame_749)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_168 = QVBoxLayout(self.widget_37)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 7, 0, 0)
        self.auto_use_stamina_options___ = QComboBox(self.widget_37)
        self.auto_use_stamina_options___.addItem("")
        self.auto_use_stamina_options___.addItem("")
        self.auto_use_stamina_options___.setObjectName(u"auto_use_stamina_options___")

        self.verticalLayout_168.addWidget(self.auto_use_stamina_options___)


        self.verticalLayout_40.addWidget(self.widget_37)


        self.gridLayout_3.addWidget(self.frame_749, 0, 1, 1, 1)

        self.frame_750 = QFrame(self.frame_18)
        self.frame_750.setObjectName(u"frame_750")
        self.frame_750.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_750.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_1319 = QVBoxLayout(self.frame_750)
        self.verticalLayout_1319.setObjectName(u"verticalLayout_1319")
        self.widget_38 = QWidget(self.frame_750)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_1316 = QVBoxLayout(self.widget_38)
        self.verticalLayout_1316.setSpacing(7)
        self.verticalLayout_1316.setObjectName(u"verticalLayout_1316")
        self.verticalLayout_1316.setContentsMargins(0, 2, 0, 0)
        self.label_7 = QLabel(self.widget_38)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_1316.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_1319.addWidget(self.widget_38)

        self.widget_239 = QWidget(self.frame_750)
        self.widget_239.setObjectName(u"widget_239")
        self.verticalLayout_1318 = QVBoxLayout(self.widget_239)
        self.verticalLayout_1318.setObjectName(u"verticalLayout_1318")
        self.verticalLayout_1318.setContentsMargins(0, 8, 0, 3)
        self.jr_general_config_btn_ = QPushButton(self.widget_239)
        self.jr_general_config_btn_.setObjectName(u"jr_general_config_btn_")
        self.jr_general_config_btn_.setMinimumSize(QSize(0, 35))
        self.jr_general_config_btn_.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_1318.addWidget(self.jr_general_config_btn_)


        self.verticalLayout_1319.addWidget(self.widget_239)


        self.gridLayout_3.addWidget(self.frame_750, 0, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_18, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_14.addWidget(self.groupBox_6)


        self.verticalLayout_12.addWidget(self.frame_17)

        self.verticalLayout_12.setStretch(0, 10)
        self.verticalLayout_12.setStretch(1, 3)
        self.tabWidget.addTab(self.join_rally_tab_, "")
        self.monster_hunting_tab_ = QWidget()
        self.monster_hunting_tab_.setObjectName(u"monster_hunting_tab_")
        self.tabWidget.addTab(self.monster_hunting_tab_, "")
        self.resource_gathering_tab_ = QWidget()
        self.resource_gathering_tab_.setObjectName(u"resource_gathering_tab_")
        self.tabWidget.addTab(self.resource_gathering_tab_, "")
        self.world_map_scan_tab_ = QWidget()
        self.world_map_scan_tab_.setObjectName(u"world_map_scan_tab_")
        self.tabWidget.addTab(self.world_map_scan_tab_, "")
        self.troops_training_tab_ = QWidget()
        self.troops_training_tab_.setObjectName(u"troops_training_tab_")
        self.tabWidget.addTab(self.troops_training_tab_, "")
        self.black_market_tab_ = QWidget()
        self.black_market_tab_.setObjectName(u"black_market_tab_")
        self.tabWidget.addTab(self.black_market_tab_, "")
        self.patrol_tab_ = QWidget()
        self.patrol_tab_.setObjectName(u"patrol_tab_")
        self.tabWidget.addTab(self.patrol_tab_, "")
        self.more_activities_tab_ = QWidget()
        self.more_activities_tab_.setObjectName(u"more_activities_tab_")
        self.tabWidget.addTab(self.more_activities_tab_, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(InstancePage)

        self.tabWidget.setCurrentIndex(2)
        self.comboBox_2.setCurrentIndex(-1)
        self.preset_combo_.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(InstancePage)
    # setupUi

    def retranslateUi(self, InstancePage):
        InstancePage.setWindowTitle(QCoreApplication.translate("InstancePage", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("InstancePage", u"Console", None))
        self.config_panel_gb.setTitle(QCoreApplication.translate("InstancePage", u"Configuration Panel", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("InstancePage", u"Default", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Choose a Profile", None))
        self.emu_name_.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Emulator Name", None))
        self.emu_port_.setInputMask("")
        self.emu_port_.setText("")
        self.emu_port_.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Port No.", None))
        self.run_btn_.setText("")
        self.delete_instance_.setText(QCoreApplication.translate("InstancePage", u"Delete Instance", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("InstancePage", u"Scheduler", None))
        self.preset_combo_.setItemText(0, QCoreApplication.translate("InstancePage", u"Main Preset", None))
        self.preset_combo_.setItemText(1, QCoreApplication.translate("InstancePage", u"Alt Preset", None))

        self.preset_combo_.setCurrentText("")
        self.preset_combo_.setPlaceholderText(QCoreApplication.translate("InstancePage", u"Select Preset", None))
        self.preset_edit_btn_.setText("")
        self.preset_delete_btn_.setText("")
        self.preset_add_btn_.setText("")
        ___qtablewidgetitem = self.scheduler_table_.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InstancePage", u"Tasks", None));
        self.label.setText(QCoreApplication.translate("InstancePage", u"Scheduler Status", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("InstancePage", u"Game Settings", None))
        self.label_5.setText(QCoreApplication.translate("InstancePage", u"Kick & Reload", None))
        self.spinBox.setSuffix(QCoreApplication.translate("InstancePage", u"  Mins", None))
        self.checkBox.setText(QCoreApplication.translate("InstancePage", u"Add Break (Local Time)", None))
        self.label_3.setText(QCoreApplication.translate("InstancePage", u"Start Time", None))
        self.label_4.setText(QCoreApplication.translate("InstancePage", u"End Time", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("InstancePage", u"Profile Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.run_tab_), QCoreApplication.translate("InstancePage", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.general_tab_), QCoreApplication.translate("InstancePage", u"General", None))
        self.skip_monsters_gb.setTitle(QCoreApplication.translate("InstancePage", u"Skip Monsters", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("InstancePage", u"Join Settings", None))
        self.label_234.setText(QCoreApplication.translate("InstancePage", u"Preset Configuration", None))
#if QT_CONFIG(tooltip)
        self.jr_rotate_preset_settings_.setToolTip(QCoreApplication.translate("InstancePage", u"Preset Settings", None))
#endif // QT_CONFIG(tooltip)
        self.jr_rotate_preset_settings_.setText("")
#if QT_CONFIG(tooltip)
        self.rotate_preset_one___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 1", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_one___.setText(QCoreApplication.translate("InstancePage", u"1", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_two___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 2", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_two___.setText(QCoreApplication.translate("InstancePage", u"2", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_three___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 3", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_three___.setText(QCoreApplication.translate("InstancePage", u"3", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_four___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 4", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_four___.setText(QCoreApplication.translate("InstancePage", u"4", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_five___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 5", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_five___.setText(QCoreApplication.translate("InstancePage", u"5", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_six___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 6", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_six___.setText(QCoreApplication.translate("InstancePage", u"6", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_seven___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 7", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_seven___.setText(QCoreApplication.translate("InstancePage", u"7", None))
#if QT_CONFIG(tooltip)
        self.rotate_preset_eight___.setToolTip(QCoreApplication.translate("InstancePage", u"Use Preset 8", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_preset_eight___.setText(QCoreApplication.translate("InstancePage", u"8", None))
        self.auto_use_stamina___.setText(QCoreApplication.translate("InstancePage", u"Auto Use Stamina", None))
        self.auto_use_stamina_options___.setItemText(0, QCoreApplication.translate("InstancePage", u"Min Stamina", None))
        self.auto_use_stamina_options___.setItemText(1, QCoreApplication.translate("InstancePage", u"Max Stamina", None))

        self.label_7.setText(QCoreApplication.translate("InstancePage", u"Rally General Selection", None))
        self.jr_general_config_btn_.setText(QCoreApplication.translate("InstancePage", u"Configure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.join_rally_tab_), QCoreApplication.translate("InstancePage", u"Join Rally", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monster_hunting_tab_), QCoreApplication.translate("InstancePage", u"Monster Hunting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resource_gathering_tab_), QCoreApplication.translate("InstancePage", u"Resource Gathering", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.world_map_scan_tab_), QCoreApplication.translate("InstancePage", u"World Map Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.troops_training_tab_), QCoreApplication.translate("InstancePage", u"Troops Training", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.black_market_tab_), QCoreApplication.translate("InstancePage", u"Black Market", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patrol_tab_), QCoreApplication.translate("InstancePage", u"Patrol", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.more_activities_tab_), QCoreApplication.translate("InstancePage", u"More Activities", None))
    # retranslateUi

